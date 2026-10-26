#!/usr/bin/env python3
"""Check cited evidence against the live web. Needs network; never part of the build (I11).

  python scripts/check_sources.py --changed origin/main   PRs: records and sources this branch touched; fails on a
                                                          quote that is not in its source or a store id whose store
                                                          name does not match the game
  python scripts/check_sources.py --all                   scheduled: everything; reports and exits 0
  python scripts/check_sources.py --ids src-a,src-b --suggest-archive  look up a Wayback snapshot for sources without `archived`
  python scripts/check_sources.py --cache DIR             read and write fetched pages in DIR (offline reruns, tests)

What it checks:
  claim quotes   every claim (and technique key result) with a `quote` must contain that text in its first source,
                 fetched from `archived` when set, else from url / doi / arxiv. Text is compared after lowercasing,
                 unifying quotes and dashes, and collapsing whitespace, so typography does not cause false alarms.
  store ids      store_ids.steam resolves on the Steam store API to the game's name or an alias (similarity >= 0.85;
                 0.6-0.85 warns, below 0.6 fails); store_ids.wikidata likewise against the item's English label. IGDB needs an API key and is
                 checked for format only (schema).
  archives       with --suggest-archive, prints the closest existing Wayback snapshot for sources lacking `archived`.
Fetch failures (paywalls, bot walls, timeouts), quotes missing only from a DOI or arXiv abstract page, and store ids
that do not resolve are warnings, never failures: the reviewer checks those by hand. A quote missing from a page that
holds the full text (the archived snapshot, a plain url, arXiv HTML) fails.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, load_entities, load_registry  # noqa: E402

UA = "SimGrammar-source-check/1.1 (+https://github.com/yoheinakajima/simgrammar)"
QUOTES = {"\u2018": "'", "\u2019": "'", "\u201a": "'", "\u201b": "'", "\u201c": '"', "\u201d": '"', "\u201e": '"',
          "\u2013": "-", "\u2014": "-", "\u2212": "-", "\u00a0": " ", "\u00ad": "", "\u2026": "...",
          "\u2122": "", "\u00ae": "", "\u00a9": ""}


SEQUEL = re.compile(r"^[\s:,-]*(\d+|ii|iii|iv|v|vi|vii|viii|ix|x|xi|xii)\b")


class _Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "svg"):
            self.skip += 1
        elif tag in ("p", "br", "div", "li", "h1", "h2", "h3", "h4", "td", "tr", "section", "article"):
            self.parts.append(" ")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "svg") and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def normalize(text: str) -> str:
    text = html.unescape(text)
    for a, b in QUOTES.items():
        text = text.replace(a, b)
    text = unicodedata.normalize("NFKC", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def divergence(quote: str, text: str) -> str:
    """Where a quote stops matching: the longest prefix of the normalized quote found in the page, and what the page
    has after it. Tells a reviewer whether a word differs or the page is a different one altogether."""
    q = normalize(quote)
    lo, hi = 0, len(q)
    while lo < hi:  # longest prefix present
        mid = (lo + hi + 1) // 2
        if q[:mid] in text:
            lo = mid
        else:
            hi = mid - 1
    if lo < 12:
        return f"no part of the quote's opening is on the page ({len(text)} characters of text fetched; begins \"{text[:80]}\")"
    at = text.find(q[:lo]) + lo
    return f"matches for {lo} of {len(q)} characters, up to \"...{q[max(0, lo - 30):lo]}\"; the page continues \"{text[at:at + 40]}\""


def page_text(raw: str, content_type: str = "") -> str:
    if "html" in content_type or raw.lstrip()[:1] == "<":
        p = _Text()
        p.feed(raw)
        raw = " ".join(p.parts)
    return normalize(raw)


class Fetcher:
    def __init__(self, cache: Path | None):
        self.cache = cache
        self.tried, self.failed = 0, 0
        if cache:
            cache.mkdir(parents=True, exist_ok=True)

    def get(self, url: str) -> tuple[str | None, str, str]:
        """Return (text or None, content_type, error)."""
        key = hashlib.sha256(url.encode()).hexdigest()[:24]
        if self.cache and (self.cache / f"{key}.json").exists():
            c = json.loads((self.cache / f"{key}.json").read_text(encoding="utf-8"))
            return c["text"], c["type"], c.get("error", "")
        text, ctype, err = None, "", ""
        for attempt in range(2):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/json,text/plain,*/*"})
                with urllib.request.urlopen(req, timeout=25) as r:
                    ctype = r.headers.get("Content-Type", "")
                    if "pdf" in ctype:
                        return None, ctype, "pdf (check the quote by hand)"
                    text = r.read(6_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace")
                    err = ""
                    break
            except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
                err = f"{type(exc).__name__}: {exc}"[:200]
                time.sleep(2)
        self.tried += 1
        self.failed += text is None and not ctype
        if self.cache:
            (self.cache / f"{key}.json").write_text(json.dumps({"url": url, "text": text, "type": ctype, "error": err}), encoding="utf-8")
        return text, ctype, err


def candidates(src: dict) -> list[tuple[str, bool]]:
    """Pages to search for a quote, with whether each holds the full text. An archived snapshot and a plain url do;
    a DOI landing page or an arXiv abstract page usually does not, so arXiv's HTML full text is tried as well."""
    out = []
    if src.get("archived"):
        out.append((src["archived"], True))
    if src.get("url"):
        out.append((src["url"], "doi.org/" not in src["url"] and "arxiv.org/abs/" not in src["url"]))
    if src.get("arxiv"):
        out += [(f"https://arxiv.org/html/{src['arxiv']}", True), (f"https://arxiv.org/abs/{src['arxiv']}", False)]
    if src.get("doi"):
        out.append((f"https://doi.org/{src['doi']}", False))
    seen, uniq = set(), []
    for u, full in out:
        if u not in seen:
            seen.add(u)
            uniq.append((u, full))
    return uniq


def similar(a: str, b: str) -> float:
    """1.0 for the same name after normalization, else a character-sequence ratio (a sequel scores below 1)."""
    a, b = normalize(a), normalize(b)
    if a == b:
        return 1.0
    short, long_ = sorted((a, b), key=len)
    if long_.startswith(short) and SEQUEL.match(long_[len(short):]):
        return 0.5  # "Cities: Skylines" vs "Cities: Skylines II" is a different game
    return SequenceMatcher(None, a, b).ratio()


def judge(e, names, got, label, fails, warns) -> int:
    best = max(similar(n, got) for n in names)
    if best >= 0.85:
        return 1
    msg = (f"{e.id}: {label} is '{got}', not '{e.data.get('name')}' (similarity {best:.2f}). If this is a different game or edition, "
           "fix the id; only if the store lists this same game under another name, add that name to aliases")
    (fails if best < 0.6 else warns).append(msg)
    return 0


def changed_paths(base: str) -> set[str]:
    out = subprocess.run(["git", "diff", "--name-only", f"{base}...HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return {line.strip() for line in out.splitlines() if line.strip()}


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--changed", metavar="BASE")
    g.add_argument("--all", action="store_true")
    g.add_argument("--ids", metavar="ID,ID,...", help="only these record or source ids (comma-separated), e.g. the ids a task issue lists")
    ap.add_argument("--cache", type=Path)
    ap.add_argument("--suggest-archive", action="store_true")
    args = ap.parse_args()
    reg = load_registry()
    ents, _ = load_entities(reg)
    by_id = {e.id: e for t, lst in ents.items() if t != "run" for e in lst}
    scope = None
    if args.ids:
        scope = {x.strip() for x in args.ids.split(",") if x.strip()}
        unknown = sorted(scope - set(by_id))
        if unknown:
            raise SystemExit(f"unknown ids: {', '.join(unknown)}")
    if args.changed:
        paths = changed_paths(args.changed)
        scope = {e.id for e in by_id.values() if str(e.path.relative_to(ROOT)) in paths}
        # a changed source re-checks every claim that cites it
        scope |= {e.id for e in by_id.values() for c in (e.data.get("claims") or []) + (e.data.get("key_results") or []) if set(c.get("sources", [])) & scope}
    f = Fetcher(args.cache)
    fails, warns, oks = [], [], 0

    for e in sorted(by_id.values(), key=lambda e: e.id):
        if scope is not None and e.id not in scope:
            continue
        for kind in ("claims", "key_results"):
            for i, c in enumerate(e.data.get(kind) or []):
                q = c.get("quote")
                if not q:
                    continue
                src = by_id.get((c.get("sources") or [None])[0])
                urls = candidates(src.data) if src else []
                if not urls:
                    warns.append(f"{e.id} {kind}[{i}]: first source has no fetchable locator (ISBN only?); a reviewer checks the quote by hand")
                    continue
                found, fetched, landing_only, why = False, [], True, ""
                for url, is_full_text in urls:
                    text, ctype, err = f.get(url)
                    if text is None:
                        continue
                    fetched.append(url)
                    landing_only = landing_only and not is_full_text
                    body = page_text(text, ctype)
                    if normalize(q) in body:
                        found = True
                        break
                    why = why or divergence(q, body)
                if found:
                    oks += 1
                elif not fetched:
                    warns.append(f"{e.id} {kind}[{i}]: could not fetch {urls[0][0]}; a reviewer checks the quote by hand")
                elif landing_only:
                    warns.append(f"{e.id} {kind}[{i}]: quote not on the landing or abstract page {fetched[0]}; the full text may hold it, so a reviewer checks by hand")
                else:
                    fails.append(f"{e.id} {kind}[{i}]: quote not found in {', '.join(fetched)}: \"{q[:80]}\"; {why}")
        ids = e.data.get("store_ids") or {}
        names = [e.data.get("name", "")] + list(e.data.get("aliases") or [])
        if "steam" in ids:
            text, _, err = f.get(f"https://store.steampowered.com/api/appdetails?appids={ids['steam']}&filters=basic")
            try:
                got = json.loads(text)[str(ids["steam"])]["data"]["name"] if text else None
            except (KeyError, TypeError, ValueError):
                got = None
            if got is None:
                warns.append(f"{e.id}: Steam app {ids['steam']} did not resolve ({err or 'no data'})")
            else:
                oks += judge(e, names, got, f"Steam app {ids['steam']}", fails, warns)
        if "wikidata" in ids:
            text, _, err = f.get(f"https://www.wikidata.org/wiki/Special:EntityData/{ids['wikidata']}.json")
            try:
                got = json.loads(text)["entities"][ids["wikidata"]]["labels"]["en"]["value"] if text else None
            except (KeyError, TypeError, ValueError):
                got = None
            if got is None:
                warns.append(f"{e.id}: Wikidata {ids['wikidata']} did not resolve ({err or 'no English label'})")
            else:
                oks += judge(e, names, got, f"Wikidata {ids['wikidata']}", fails, warns)
        if args.suggest_archive and e.type == "source" and e.data.get("url") and not e.data.get("archived"):
            text, _, err = f.get("https://archive.org/wayback/available?url=" + urllib.parse.quote(e.data["url"], safe=""))
            try:
                snap = json.loads(text)["archived_snapshots"]["closest"]["url"] if text else None
            except (KeyError, TypeError, ValueError):
                snap = None
            # the API answers with http:// snapshot urls; the schema wants https://
            snap = snap.replace("http://", "https://", 1) if snap else None
            stamp = re.match(r"^https://web\.archive\.org/web/([0-9]{8})", snap or "")
            when = f" (snapshot {stamp.group(1)[:4]}-{stamp.group(1)[4:6]}-{stamp.group(1)[6:]}, accessed {e.data.get('accessed', '?')})" if stamp else ""
            print(f"ARCHIVE {e.id}: " + (f"archived: {snap}{when}" if snap else "no snapshot; save one at https://web.archive.org/save/" + e.data["url"]))

    for w in warns:
        print("WARN", w)
    for x in fails:
        print("FAIL", x)
    print(f"\n{oks} checked OK, {len(warns)} warning(s), {len(fails)} failure(s).")
    if f.tried and f.failed == f.tried:
        print(f"NOTHING CHECKED: all {f.tried} fetches failed (no network, or a proxy refused them). This result verifies nothing; "
              "the `sources` workflow on the pull request runs the real check.")
    sys.exit(1 if (fails and args.changed) else 0)


if __name__ == "__main__":
    main()
