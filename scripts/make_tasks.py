#!/usr/bin/env python3
"""Generate contributor task batches from the dataset's gaps (tasks/*.md briefs). Not part of the build.

  python scripts/make_tasks.py                 print every task as markdown
  python scripts/make_tasks.py --json          the same as JSON (used by .github/workflows/tasks.yml to open issues)
  python scripts/make_tasks.py --brief store-ids --limit 3

Each task has a stable key (brief plus a hash of its record ids), so reopening the workflow never duplicates an issue.
Batch sizes keep every task inside the PR limits (E039).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, is_wiki_source, load_calibration, load_entities, load_registry, read_yaml  # noqa: E402

REPO = "https://github.com/yoheinakajima/simgrammar"
BRIEFS = {
    "archive-sources": ("maintenance", 25, "Archive {n} sources on the Wayback Machine"),
    "source-claims": ("maintenance", 8, "Add verbatim quotes to the claims of {n} records"),
    "store-ids": ("catalog", 10, "Add store ids to {n} games"),
    "catalog-game": ("catalog", 3, "Catalogue {n} candidate games"),
    "verify-record": ("verification", 6, "Verify {n} sourced records (independent operator)"),
    "rate-scores": ("verification", 10, "Rate the scores of {n} mechanics (calibrated, independent operator)"),
    "resolve-prediction": ("verification", 1, "Resolve an overdue prediction"),
}
DONE = {
    "archive-sources": "every listed source you could archive has an `archived` snapshot of its own url (E034) and names your run in `provenance.reviewed`; any you could not are named in your run's `method`; `make check` and `make pr-check` are green",
    "source-claims": "every claim on the listed records has a verbatim `quote` and `locator` from its first source, or is named in your run's `method` with the reason; the `sources` workflow finds each quote or flags it for review; `make check` and `make pr-check` are green",
    "store-ids": "each listed game has every store id you could confirm (games without one are named in your run's `method`), the `sources` workflow resolves them to the right game, `make check` and `make pr-check` are green",
    "catalog-game": "each candidate is catalogued to the depth of data/games/rimworld.yaml, or declined in your run's notes with the admission test it fails; every new claim carries a quote",
    "verify-record": "each record is `verified` or `contested` (with a `disputes` claim), your run is independent of the creating run (E035), `make check` is green",
    "rate-scores": "your run carries a passing calibration (E036), each listed mechanic has your rating per scale with a rationale, the original score is recorded, stored values are lower medians (E037)",
    "resolve-prediction": "the prediction has a `resolution` with evidence from a run independent of its creator (E035, E038)",
}


def batches(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]


def task(brief, ids, paths, notes=""):
    kind, _, title = BRIEFS[brief]
    key = f"{brief}:{hashlib.sha256(','.join(ids).encode()).hexdigest()[:10]}"
    lines = [f"<!-- task-key: {key} -->", f"**Brief:** [tasks/{brief}.md]({REPO}/blob/main/tasks/{brief}.md) · **Run kind:** `{kind}`", "", "**Sources**" if brief == "archive-sources" else "**Records**", ""]
    lines += [f"- `{i}` ({p})" for i, p in zip(ids, paths)]
    if brief in ("archive-sources", "source-claims", "store-ids"):
        flag = " --suggest-archive" if brief == "archive-sources" else ""
        lines += ["", "**Check these with:** `python scripts/check_sources.py --ids " + ",".join(ids) + flag + "`"]
    lines += ["", f"**Done when:** {DONE[brief]}."]
    if notes:
        lines += ["", f"**Notes:** {notes}"]
    lines += ["", "Claim it by commenting `claiming`. One issue, one run, one pull request that links this issue (CONTRIBUTING.md)."]
    return {"key": key, "brief": brief, "title": title.format(n=len(ids)), "records": ids, "body": "\n".join(lines)}


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def build_tasks(today: dt.date, exclude: set[str] | None = None) -> list[dict]:
    """exclude holds "<brief>:<id>" (already in a task issue for that brief) and "path:<file>" (touched by an open PR)."""
    exclude = exclude or set()
    reg = load_registry()
    ents, _ = load_entities(reg)
    rel = lambda e: str(e.path.relative_to(ROOT))  # noqa: E731
    pr_paths = {x[5:] for x in exclude if x.startswith("path:")}

    def keep(brief, items, ident=lambda e: e.id, path=None):
        path = path or (lambda e: rel(e))
        return [e for e in items if f"{brief}:{ident(e)}" not in exclude and path(e) not in pr_paths]
    by_id = {e.id: e for t, lst in ents.items() if t != "run" for e in lst}
    out = []
    srcs = sorted((s for s in ents["source"] if s.data.get("url") and not s.data.get("archived")), key=lambda s: (is_wiki_source(s.data), s.id))
    srcs = keep("archive-sources", srcs)
    for b in batches(srcs, BRIEFS["archive-sources"][1]):
        out.append(task("archive-sources", [s.id for s in b], [rel(s) for s in b], "Primary sources come first; wikis last."))
    order = {"technique": 0, "game": 1, "mechanic": 2, "opportunity": 3}
    unq = sorted((e for t in order for e in ents.get(t, []) if any(not c.get("quote") for c in (e.data.get("claims") or []) + (e.data.get("key_results") or []))),
                 key=lambda e: (order[e.type], e.id))
    unq = keep("source-claims", unq)
    for b in batches(unq, BRIEFS["source-claims"][1]):
        out.append(task("source-claims", [e.id for e in b], [rel(e) for e in b]))
    steam = sorted((g for g in ents["game"] if not g.data.get("store_ids") and "pc" in (g.data.get("platforms") or []) and (g.data.get("year") or 0) >= 2003),
                   key=lambda g: (-(g.data.get("influence") or 0), g.id))
    steam = keep("store-ids", steam)
    for b in batches(steam, BRIEFS["store-ids"][1]):
        out.append(task("store-ids", [g.id for g in b], [rel(g) for g in b], "PC games released since Steam opened, most influential first."))
    cands = (read_yaml(ROOT / "tasks" / "candidates.yaml") or {}).get("candidates") or []
    names = {(e.data.get("name") or "").lower() for e in ents["game"]} | {a.lower() for e in ents["game"] for a in e.data.get("aliases") or []}
    open_c = [c for c in cands if c["name"].lower() not in names]
    open_c = keep("catalog-game", open_c, ident=lambda c: c["name"], path=lambda c: f"data/games/{slug(c['name'])}.yaml")
    for b in batches(open_c, BRIEFS["catalog-game"][1]):
        out.append(task("catalog-game", [c["name"] for c in b], [c["why"] for c in b], "Candidates from tasks/candidates.yaml; apply the inclusion test before cataloguing."))
    ver = sorted((e for t in ("technique", "game", "mechanic") for e in ents.get(t, []) if e.data.get("status") == "sourced"
                  and any(not is_wiki_source(by_id[s].data) for s in e.data.get("sources") or [] if s in by_id)), key=lambda e: (order[e.type], e.id))
    ver = keep("verify-record", ver)
    for b in batches(ver, BRIEFS["verify-record"][1]):
        out.append(task("verify-record", [e.id for e in b], [rel(e) for e in b], "Needs an operator other than the record's creator (most records were created by yoheinakajima's runs)."))
    cal = set(((load_calibration(reg) or {}).get("mechanics") or {}))
    mech = sorted((m for m in ents["mechanic"] if m.id not in cal and not m.data.get("deprecated")), key=lambda m: m.id)
    mech = keep("rate-scores", mech)
    for b in batches(mech, BRIEFS["rate-scores"][1]):
        out.append(task("rate-scores", [m.id for m in b], [rel(m) for m in b], "Calibrate first (tasks/rate-scores.md); calibration-set mechanics are excluded."))
    for o in keep("resolve-prediction", sorted(ents["opportunity"], key=lambda e: e.id)):
        sig = o.data.get("falsifiable_signal") or {}
        rb = str(sig.get("resolve_by", "9999"))
        if not sig.get("resolution") and rb < today.isoformat()[: len(rb)]:
            out.append(task("resolve-prediction", [o.id], [rel(o)], f"Resolve-by date {rb} has passed (W106)."))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--brief", choices=sorted(BRIEFS))
    ap.add_argument("--limit", type=int, default=0, help="at most this many tasks per brief")
    ap.add_argument("--exclude", type=Path, help="file of lines '<brief>:<id>' (records already in a task issue) and "
                                                  "'path:<file>' (files touched by open PRs); those records get no new task")
    args = ap.parse_args()
    exclude = {ln.strip() for ln in args.exclude.read_text(encoding="utf-8").splitlines() if ln.strip()} if args.exclude else set()
    tasks = build_tasks(dt.date.today(), exclude)
    if args.brief:
        tasks = [t for t in tasks if t["brief"] == args.brief]
    if args.limit:
        seen = {}
        tasks = [t for t in tasks if seen.setdefault(t["brief"], 0) < args.limit and not seen.__setitem__(t["brief"], seen[t["brief"]] + 1)]
    if args.json:
        print(json.dumps(tasks, indent=2, ensure_ascii=False))
    else:
        for t in tasks:
            print(f"## {t['title']}  [{t['key']}]\n\n{t['body']}\n")
        counts = {}
        for t in tasks:
            counts[t["brief"]] = counts.get(t["brief"], 0) + 1
        print("# totals:", ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))


if __name__ == "__main__":
    main()
