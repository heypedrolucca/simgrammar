"""Project the dataset into a static website (dist/web), styled with Register (web/register.css).

Pages:
  index.html                         the paper, rendered from report/src with interactive figures, and the grammar mosaic
  <type>/index.html                  one index per entity type: mechanics as icon tiles, games as parts boards, opportunities
                                     by horizon, each with its sortable table as the plain-text twin; techniques and sources a table
  <type>/<id>/index.html             one page per entity, with its icon, its parts board (games), the shorts that show it,
                                     and where the book and the shorts mention it
  book/index.html, book/<chapter>/   the book (book/src as rendered by this build), one chapter a page
  watch/index.html                   the published shorts (media/published.yaml)
  data/index.html                    downloads, provenance log, contract
  og/<type>/<id>.png, og/*.png       a link-preview image per page (scripts/og.py)
  paper.md, references.bib, manifest.json, figures/*.svg, llms.txt, CNAME, robots.txt, sitemap.xml, 404.html, assets/*

Everything here is a deterministic function of data/, report/, vocab/, schema/, book/, media/, and web/; icons come from
the build's dist/visual (ADR-0006). The video files are not: the Pages workflow fetches the ones media/published.yaml lists
from their GitHub release and checks each sha256. Pages work without JavaScript; assets/simgrammar.js only adds interaction.
"""
from __future__ import annotations

import html
import json
import re
from collections import defaultdict
from pathlib import Path

from markdown_it import MarkdownIt

from lib import ROOT, get_path, read_yaml, vocab_terms
from report_render import _decl_rows, _fmt, render

WEB_SRC = ROOT / "web"
NAV = [("paper", "Paper", ""), ("book", "Book", "book/"), ("game", "Games", "game/"), ("mechanic", "Mechanics", "mechanic/"), ("technique", "Techniques", "technique/"),
       ("opportunity", "Opportunities", "opportunity/"), ("watch", "Watch", "watch/"), ("source", "Sources", "source/"), ("data", "Data", "data/")]
FAVICON = "free-placement"   # the icon the browser tab shows
STATE = {"asserted": "optional", "sourced": "waiting", "verified": "done", "contested": "blocked"}
SKIP_FACTS = {"id", "type", "name", "aliases", "summary", "status", "provenance", "sources", "claims", "deprecated", "key_results", "falsifiable_signal",
              "assertions", "ratings", "store_ids", "archived"}
OUTCOME_STATE = {"confirmed": "done", "refuted": "stop", "ambiguous": "blocked", "withdrawn": "superseded"}
STORE_URL = {"steam": "https://store.steampowered.com/app/{}/", "igdb": "https://www.igdb.com/games/{}", "wikidata": "https://www.wikidata.org/wiki/{}"}
LONG = {"game": ["core_loop", "design_notes"], "mechanic": ["definition", "player_experience"], "technique": ["mechanism"],
        "opportunity": ["thesis", "design_sketch", "validation_experiment"], "source": ["notes"]}
LISTS = {"mechanic": ["design_levers", "failure_modes", "dynamics", "open_questions"], "technique": ["limitations"], "opportunity": ["key_risks"]}
VOCAB_COLUMNS = {"family": "mechanic_family", "family_a": "mechanic_family", "family_b": "mechanic_family", "subgenre": "subgenre",
                 "maturity": "technique_maturity", "category": "technique_category", "effect": "effect", "opportunity_type": "opportunity_type",
                 "horizon": "horizon", "kind": "source_kind"}


def esc(s) -> str:
    return html.escape("" if s is None else str(s), quote=True)


def host(url: str) -> str:
    m = re.match(r"https?://([^/]+)", url or "")
    return (m.group(1) if m else url).removeprefix("www.")


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


class Web:
    def __init__(self, ents, edges, analysis, vocabs, registry, schemas, ctx, manifest, meta, built=None):
        self.ents, self.edges, self.analysis, self.vocabs = ents, edges, analysis, vocabs
        self.registry, self.schemas, self.ctx, self.manifest, self.meta = registry, schemas, ctx, manifest, meta
        self.built = built or {}
        self.icons = {k[len("visual/icons/"):-len("@4x.png")] for k in self.built if k.startswith("visual/icons/") and k.endswith("@4x.png") and ".accent@" not in k}
        self.by_id = ctx.by_id
        self.published = read_yaml(ROOT / "media" / "published.yaml") if (ROOT / "media" / "published.yaml").exists() else {}
        self.shorts, self.shorts_of = [], defaultdict(list)
        for sh in self.published.get("shorts", []):
            md = self.built.get(f"media/shorts/{sh['script']}", "")
            title = re.search(r"^# Short \d+\. (.*)$", md, re.M)
            unknown = [i for i in sh.get("shows", []) if i not in self.by_id]
            if not md or unknown:
                raise SystemExit(f"media/published.yaml: {sh['key']} names a script this build did not render or unknown records {unknown}")
            sh = {**sh, "n": int(sh["key"].rsplit("-", 1)[1]), "title": title.group(1) if title else sh["key"],
                  "voice": re.findall(r"^\*\*Voice\.\*\* (.*)$", md, re.M)}
            self.shorts.append(sh)
            for i in sh["shows"]:
                self.shorts_of[i].append(sh)
        self.chapters = sorted(k[len("book/"):-3] for k in self.built if re.fullmatch(r"book/\d\d-[a-z0-9-]+\.md", k))
        self.book_refs = self.find_book_refs()
        self.site = meta["site"]
        self.by_id = ctx.by_id
        self.derived = analysis["derived"]
        self.short = manifest["dataset_sha256"][:8]
        self.types = [t for t, s in registry["types"].items() if not s.get("meta")]
        self.props = {t: schemas[Path(registry["types"][t]["schema"]).name]["properties"] for t in self.types}
        self.edges_out = defaultdict(list)
        for ed in edges:
            self.edges_out[ed.source].append(ed)
        self.vt = {}
        self.runs = {e.id: e for e in ents.get("run", [])}

    # ------------------------------------------------------------------ helpers
    def term(self, vname, t):
        if vname not in self.vt:
            self.vt[vname] = vocab_terms(self.vocabs, vname)
        return self.vt[vname].get(str(t), {}).get("label", str(t))

    def vocab_of(self, t, field):
        p = self.props[t].get(field) or {}
        return p.get("x-vocab") or (p.get("items") or {}).get("x-vocab")

    def link(self, eid, base, text=None):
        e = self.by_id.get(eid)
        if not e:
            return esc(text or eid)
        return f'<a href="{base}{e.type}/{eid}/" data-internal>{esc(text or e.data.get("name", eid))}</a>'

    def icon_id(self, eid):
        """The icon that stands for a record: its own, else a technique's category icon (as the video frames resolve it)."""
        if eid in self.icons:
            return eid
        e = self.by_id.get(eid)
        if e and e.type == "technique" and e.data.get("category") in self.icons:
            return e.data["category"]
        return None

    def icon(self, eid, base, size=48, alt=""):
        """A dithered icon at 24, 48 or 96 css px, so each of its 48 dither pixels lands on whole device pixels."""
        i = self.icon_id(eid)
        return f'<img data-icon src="{base}assets/icons/{i}.png" width="{size}" height="{size}" alt="{esc(alt)}" loading="lazy">' if i else ""

    def chip(self, eid, base):
        e = self.by_id.get(eid)
        if not e:
            return f'<span class="chip">{esc(eid)}</span>'
        ic = self.icon(eid, base, 24)
        return (f'<a class="chip" data-style="{"icon" if ic else "name"}" href="{base}{e.type}/{eid}/" data-internal>'
                f'{ic}{esc(e.data.get("name", eid))}</a>')

    def chips(self, ids, base):
        return '<div class="cluster" data-gap="chips">' + "".join(self.chip(x, base) for x in ids) + "</div>"

    def gh(self, path):
        return f'{self.site["repo"]}/blob/main/{path}'

    @staticmethod
    def dl(path, base):
        """Generated projections are not committed; the Pages workflow publishes them under /dist/ beside the site."""
        return f"{base}dist/{path}"

    def page(self, *, title, desc, body, depth, nav, path, image="og/site.png"):
        base = "../" * depth
        fam = "".join(f'<li><a href="{esc(u)}">{esc(n)}</a></li>' for n, u in self.site.get("family", []))
        fam += f'<li><a href="{base or "./"}" aria-current="true" data-internal>simgrammar</a></li>'
        navh = "".join(f'<a href="{base}{href}"{" aria-current=" + chr(34) + "page" + chr(34) if key == nav else ""} data-internal>{label}</a>'
                       for key, label, href in NAV)
        url = self.site["url"] + path
        return f"""<!doctype html>
<html lang="en" data-theme="{esc(self.site.get('theme', 'neutral'))}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(self.site['url'] + image)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{base}assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&amp;family=IBM+Plex+Mono:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/register.css">
<link rel="alternate" type="text/markdown" href="{base}paper.md" title="The paper as markdown">
<script src="{base}assets/simgrammar.js" defer></script>
</head>
<body>
<a class="skip-link" href="#content">Skip to content</a>
<div class="family shell" aria-label="Site family"><ul>{fam}</ul><span>one dataset · paper, tables, graph, wiki</span></div>
<header class="topbar shell">
  <a class="brand" href="{base or './'}" data-internal>simgrammar <small>the grammar of simulation</small></a>
  <input type="checkbox" id="menu" class="menu-toggle"><label for="menu" class="menu-label">menu</label>
  <nav class="nav" aria-label="Primary">{navh}</nav>
  <nav class="nav-utility" aria-label="Utility"><a href="{esc(self.site['repo'])}">github</a><a href="{base}paper.md" data-internal>paper.md</a><a href="{base}#cite" data-internal>cite</a></nav>
</header>
<main id="content" class="shell">
{body}
<footer class="site-footer"><span>dataset {self.short} · contract {esc(self.manifest['contract_version'])} · paper v{esc(self.meta['version'])}</span><span>generated by scripts/build.py · built with register.css</span></footer>
</main>
</body>
</html>
"""

    # ------------------------------------------------------------------ tables
    def cell(self, col, v, base, link_cols, cap=None):
        if isinstance(v, list):
            if col in link_cols:
                shown = v[:cap] if cap else v
                more = len(v) - len(shown)
                return ", ".join(self.link(x, base) if x in self.by_id else esc(x) for x in shown) + (f", and {more} more" if more else "")
            return esc(", ".join(_fmt(x) for x in v))
        if col in link_cols and isinstance(v, str) and v in self.by_id:
            return self.link(v, base)
        if col in VOCAB_COLUMNS and isinstance(v, str):
            return esc(self.term(VOCAB_COLUMNS[col], v))
        return esc(_fmt(v))

    def table(self, columns, headers, rows, base, link_cols=(), caption=None, cap=None, name=None):
        th = "".join(f'<th{" class=" + chr(34) + "num" + chr(34) if self._numeric(rows, c) else ""}>{esc(h)}</th>' for c, h in zip(columns, headers))
        trs = []
        for r in rows:
            tds = []
            for c in columns:
                v = r.get(c) if isinstance(r, dict) else None
                cls = ' class="num"' if self._numeric(rows, c) else ""
                tds.append(f"<td{cls}>{self.cell(c, v, base, set(link_cols), cap)}</td>")
            trs.append("<tr>" + "".join(tds) + "</tr>")
        t = (f'<div class="table-wrap"><table class="data" data-style="dense" data-sortable{" data-name=" + chr(34) + esc(name) + chr(34) if name else ""}>'
             f"<thead><tr>{th}</tr></thead><tbody>{''.join(trs)}</tbody></table></div>")
        cap_html = f'<p class="small muted">{esc(caption)}</p>' if caption else ""
        if len(rows) > 40:
            return f'<details class="disclosure"><summary>table · {len(rows)} rows{" · " + esc(name) if name else ""}</summary>{t}{cap_html}</details>'
        return t + cap_html

    @staticmethod
    def _numeric(rows, c):
        vals = [r.get(c) for r in rows if isinstance(r, dict) and r.get(c) is not None]
        return bool(vals) and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in vals)

    def report_table(self, name, base):
        ctx = self.ctx
        if name in ctx.decl_tables:
            spec = ctx.decl_tables[name]
            if spec.get("kind") == "count-by":
                from collections import Counter
                c = Counter()
                for e in ctx.ents.get(spec["entity"], []):
                    if e.data.get("deprecated"):
                        continue
                    v = get_path(e.data, spec["field"])
                    for x in (v if isinstance(v, list) else [v]):
                        if x is not None:
                            c[x] += 1
                rows = [{"term": self.term(spec["vocab"], k) if spec.get("vocab") else k, "count": n} for k, n in sorted(c.items(), key=lambda x: (-x[1], str(x[0])))]
                return self.table(["term", "count"], [spec.get("label", spec["field"]), self.registry["types"][spec["entity"]]["plural"]], rows, base, name=name)
            cols = spec["columns"]
            paths = [c["path"] if isinstance(c, dict) else c for c in cols]
            heads = [c.get("label") if isinstance(c, dict) else c.split(".")[-1].replace("_", " ") for c in cols]
            ent_t = spec["entity"]
            rows = []
            for r in _decl_rows(ctx, spec):
                row = {}
                for p in paths:
                    v = get_path(r, p)
                    vn = self.vocab_of(ent_t, p) if "." not in p else None
                    if p == "name":
                        v = r["id"]
                    elif vn and v is not None:
                        v = [self.term(vn, x) for x in v] if isinstance(v, list) else self.term(vn, v)
                    row[p] = v
                rows.append(row)
            return self.table(paths, heads, rows, base, link_cols={"name"}, caption=spec.get("caption"), name=name)
        t = self.analysis["tables"].get(name)
        if t is None:
            return None
        return self.table(t["columns"], [c.replace("_", " ") for c in t["columns"]], t["rows"], base, link_cols=t.get("link_columns", []),
                          caption=t["description"], cap=t.get("max_links"), name=name)

    # ------------------------------------------------------------------ figures
    def figure_static(self, name, n):
        f = self.analysis["figures"][name]
        svg = re.sub(r"^<svg ([^>]*?)width='\d+' height='\d+' style=\"", "<svg class=\"plot\" \\1style=\"width:100%;max-width:none;height:auto;", f["svg"], count=1)
        svg = svg.replace("width:100%;max-width:none;", "width:100%;max-width:none;min-width:480px;", 1)
        title = {"legibility-vs-emergence": "Legibility against emergence potential", "exposure-by-family": "Technique exposure by family",
                 "mechanic-accumulation": "Mechanics by first appearance"}.get(name, name)
        return (f'<figure class="chart" id="fig-{name}"><div class="chart-head"><span><b>figure {n}</b> · {esc(title)}</span><span>{esc(name)}.svg</span></div>'
                f'<div class="chart-body"><div class="table-wrap" style="border-top:0">{svg}</div></div><figcaption class="chart-caption">{esc(f["caption"])} '
                f'<span class="run">source · dist/analysis/figures/{esc(name)}.svg · dataset {self.short}</span></figcaption></figure>')

    @staticmethod
    def fluid(svg):
        """Inline SVGs scale to the column: drop the fixed width and height the standalone file keeps."""
        return re.sub(r'^(<svg[^>]*?) width="\d+" height="\d+"', r"\1", svg, count=1).replace("max-width:100%;height:auto", "width:100%;max-width:none;height:auto", 1)

    def scroller(self, v):
        """On wide screens the figure fills the column. Below its minimum width it keeps readable text and scrolls
        sideways inside .table-wrap, the one scroll container Register allows."""
        svg = self.fluid(v["svg"]).replace("width:100%;max-width:none;", f"width:100%;max-width:none;min-width:{v.get('min_width', 0)}px;", 1)
        hint = '<p class="small faint show-sm">swipe sideways to see the whole figure; the table below holds every value</p>'
        wrap = f'<div class="table-wrap" style="border-top:0">{svg}</div>'
        if v.get("aside"):
            return f'<div class="split"><div style="min-width:0">{wrap}{hint}</div><div style="min-width:0">{v["aside"]}</div></div>'
        return wrap + hint

    def figure_viz(self, name, n, base):
        v = self.analysis["vizzes"][name]
        tw = v["twin"]
        if "table" in tw:
            twin = self.report_table(tw["table"], base) or ""
            nrows = len(self.analysis["tables"][tw["table"]]["rows"])
        else:
            twin = self.table(tw["columns"], [c.replace("_", " ") for c in tw["columns"]], tw["rows"], base, link_cols=tw.get("link_columns", []), cap=8)
            nrows = len(tw["rows"])
        if twin.startswith("<details"):
            twin = re.sub(r"^<details class=\"disclosure\"><summary>.*?</summary>", "", twin)[: -len("</details>")]
        return (f'<figure class="chart" id="fig-{name}" data-viz="{name}" aria-describedby="cap-{name}">'
                f'<div class="chart-head"><span><b>figure {n}</b> · {esc(v["title"])}</span><span>{esc(v["head"])}</span></div>'
                f'<div class="controls" data-viz-controls hidden>{v["controls"]}</div>'
                f'<div class="chart-body">{self.scroller(v)}</div>{v.get("legend", "")}'
                f'<p class="live" data-readout aria-live="polite" hidden></p>'
                f'<p class="chart-caption" id="cap-{name}">{esc(v["caption"])} <span class="run">source · {esc(v["source"])} · dataset {self.short}</span></p>'
                f'<details class="disclosure"><summary>plain-text twin · {nrows} rows</summary><p class="small muted">{esc(tw["note"])}</p>{twin}</details>'
                f'{v["data"]}</figure>')

    # ------------------------------------------------------------------ paper
    def paper(self):
        ctx = self.ctx
        ctx.web_base = ""
        ctx.citations = []
        md = MarkdownIt("commonmark", {"html": True}).enable("table")
        parts = []
        for p in sorted((ROOT / "report" / "src").glob("*.md")):
            txt, _ = render(p.read_text(encoding="utf-8"), ctx, "web")
            parts.append(md.render(txt))
        body = "\n".join(parts)
        toc = []

        def head(m):
            lvl, inner = m.group(1), m.group(2)
            plain = re.sub(r"<[^>]+>", "", inner)
            hid = slug(plain)
            if lvl == "2":
                toc.append((hid, plain))
                return f'<hr class="rule" data-style="wedge"><h2 id="{hid}">{inner}</h2>'
            return f'<h{lvl} id="{hid}">{inner}</h{lvl}>'
        body = re.sub(r"<h([23])>(.*?)</h\1>", head, body)
        counter = {"n": 0}

        def place(m):
            kind, name = m.group(1), m.group(2)
            if kind == "TABLE":
                return self.report_table(name, "") or ""
            counter["n"] += 1
            return self.figure_static(name, counter["n"]) if kind == "FIGURE" else self.figure_viz(name, counter["n"], "")
        body = body.replace("<table>", '<div class="table-wrap"><table class="data" data-style="dense">').replace("</table>", "</table></div>")
        body = re.sub(r"<!--(TABLE|FIGURE|VIZ):([a-z0-9-]+)-->", place, body)
        body = body.replace('<hr class="rule" data-style="wedge">', "", 1)
        # references
        refs = []
        for i, sid in enumerate(ctx.citations, start=1):
            s = self.by_id[sid].data
            au = ", ".join(s.get("authors", [])[:6]) + (" et al." if len(s.get("authors", [])) > 6 else "")
            loc = s.get("url") or (f"https://doi.org/{s['doi']}" if s.get("doi") else "") or (f"https://arxiv.org/abs/{s['arxiv']}" if s.get("arxiv") else "")
            refs.append(f'<div class="row" id="ref-{sid}"><div class="id" data-ref="{i}"></div><div><span class="who">{esc(au)}</span> ({esc(s["date"])}). '
                        f'<a href="source/{sid}/" data-internal>{esc(s["name"])}</a>. <span class="venue">{esc(s.get("venue", ""))}</span>'
                        f'<span class="ids">{f"<a href={chr(34)}{esc(loc)}{chr(34)}>{esc(host(loc))}</a>" if loc else ""}</span></div></div>')
        toc += [("references", "References"), ("cite", "Cite"), ("receipt", "Build receipt")]
        st = self.analysis["stats"]
        meta, man = self.meta, self.manifest
        counts = {t: sum(1 for e in self.ents.get(t, []) if not e.data.get("deprecated")) for t in self.types}
        numbers = [
            (f'{st["rho_legibility_emergence_potential"]}', "ρ legibility vs emergence", "§5.6"),
            (f'{st["pct_mechanics_seen_by_2000"]:.0f}%', "mechanics seen by 2000", "§5.2"),
            (f'{st["pct_uses_on_zero_exposure"]:.0f}%', "uses on mechanics no technique touches", "§8.2"),
            (f'{st["n_technique_runtime_breaks"]} of {st["n_technique_runtime"]}', "runtime techniques that break replay", "§6.4"),
        ]
        nums = "".join(f'<div class="number"><b>{esc(v)}</b><span>{esc(lab)}</span><small>{esc(src)}</small></div>' for v, lab, src in numbers)
        tocs = "".join(f'<a href="#{hid}" data-internal>{esc(t)}</a>' for hid, t in toc)
        authors = ", ".join(meta["authors"])
        bib = (f"@misc{{nakajima{meta['date'][:4]}grammar,\n  title = {{{meta['title']}: {meta['subtitle']}}},\n  author = {{Nakajima, Yohei and {{SimGrammar contributors}}}},\n"
               f"  year = {{{meta['date'][:4]}}},\n  version = {{{meta['version']}}},\n  url = {{{self.site['url']}}},\n  note = {{Dataset {self.short}; full sha256 in manifest.json}}\n}}")
        nruns = len(self.ents.get("run", []))
        header = f"""<div class="page-header corners">
  <p class="eyebrow"><span class="id">v{esc(meta['version'])}</span> <span>{esc(meta['date'])}</span> <span>dataset <b>{self.short}</b></span> <span>contract {esc(man['contract_version'])}</span></p>
  <h1>{esc(meta['title'])}</h1>
  <p class="dek">{esc(meta['subtitle'])}.</p>
  <div class="meta"><span><b>{esc(authors)}</b></span><span>{counts['game']} games</span><span>{counts['mechanic']} mechanics</span><span>{counts['technique']} techniques</span><span>{counts['opportunity']} opportunities</span><span>{counts['source']} sources</span><span>{man['edges']} typed edges</span><span>{nruns} research runs</span></div>
  <div class="actions"><a class="btn" href="#abstract" data-internal>Read the paper</a><a class="btn" data-style="ghost" href="data/" data-internal>Get the data</a><a class="btn" data-style="ghost" href="{esc(self.site['repo'])}">Contribute on GitHub</a></div>
  <div class="twins"><b>this paper as</b><a href="paper.md" data-internal>markdown</a><a href="references.bib" data-internal>bibtex</a><a href="manifest.json" data-internal>manifest json</a><a href="llms.txt" data-internal>llms.txt</a></div>
</div>
<div class="numbers">{nums}</div>
<p class="small faint">source · dist/analysis/stats.json · dataset {self.short} · every number on this page is rendered from the dataset at build time</p>
{self.mosaic("")}"""
        main = f"""<div class="sidebar">
<aside class="hide-md sticky"><nav class="toc" aria-label="Contents"><span class="toc-head">contents</span>{tocs}</nav></aside>
<article class="prose" style="min-width:0">
<details class="disclosure show-md" data-toc-mobile><summary>contents · {len(toc)} sections</summary><nav class="toc" aria-label="Contents">{tocs}</nav></details>
{body}
<section class="section" id="references"><div class="section-line"><h2>references <span>· {len(refs)} cited in the text</span></h2><a href="source/" data-internal>all {counts['source']} sources</a></div>
<div class="register" data-kind="refs">{''.join(refs)}</div></section>
<section class="section cite" id="cite"><div class="section-line"><h2>cite</h2><span>bibtex</span></div>
<div class="cite-line"><span class="chip">{esc(authors)}</span><span class="chip">{esc(meta['date'][:4])}</span><span class="chip">v{esc(meta['version'])}</span><span class="chip">dataset {self.short}</span></div>
<div class="prompt"><div class="copy-row"><span>bibtex</span><span>{esc(meta['title'].lower())} · v{esc(meta['version'])}</span></div><pre>{esc(bib)}</pre></div></section>
<section class="section" id="receipt"><div class="section-line"><h2>build receipt <span>· reproduce this page</span></h2><span>python scripts/build.py</span></div>
<dl class="receipt" data-size="wide"><dt>dataset</dt><dd><span class="hash" data-prefix="sha256:">{man['dataset_sha256']}</span></dd>
<dt>contract</dt><dd>{esc(man['contract_version'])} · <a href="{esc(self.gh('CONTRACT.md'))}">CONTRACT.md</a></dd>
<dt>entities</dt><dd>{', '.join(f'{n} {t}' for t, n in man['counts'].items())}</dd>
<dt>edges</dt><dd>{man['edges']}</dd>
<dt>generator</dt><dd>{esc(man['generator'])} · scripts/web.py · scripts/viz.py</dd>
<dt>check</dt><dd><code>make check</code> fails if any page differs from a fresh build</dd></dl>
<p><span class="endmark"></span></p></section>
</article></div>"""
        return self.page(title=f"{meta['title']} · simgrammar", desc=meta["subtitle"], body=header + main, depth=0, nav="paper", path="")

    # ------------------------------------------------------------------ shorts and the book
    @staticmethod
    def mmss(sec):
        sec = int(round(sec))
        return f"{sec // 60}:{sec % 60:02d}"

    def voice_html(self, line, base):
        """A narration line as html: its citations become links to the source pages, its record links to record pages."""
        t = esc(line)
        t = re.sub(r"\s*\[((?:\[\d+\]\(#ref-[a-z0-9-]+\)(?:,\s*)?)+)\]",
                   lambda m: "".join(f' <a href="{base}source/{sid}/" data-internal>[{n}]</a>' for n, sid in re.findall(r"\[(\d+)\]\(#ref-([a-z0-9-]+)\)", m.group(1))), t)
        t = re.sub(r"\[([^\]]+)\]\((?:\.\./)+wiki/(\w+)/([a-z0-9-]+)\.md\)", lambda m: f'<a href="{base}{m.group(2)}/{m.group(3)}/" data-internal>{m.group(1)}</a>', t)
        return t.replace("**", "").replace("*", "")

    def short_figure(self, sh, base, width=270):
        return (f'<figure class="image" data-ratio="9/16"><a class="frame" href="{base}media/shorts/{esc(sh["file"])}" data-play>'
                f'<img src="{base}media/shorts/{esc(sh["poster"])}" width="{width}" height="{round(width * 16 / 9)}" alt="Short {sh["n"]}: {esc(sh["title"])}, opening frame" loading="lazy">'
                f'<span class="plate" data-size="sm">play · {self.mmss(sh["seconds"])}</span></a>'
                f'<figcaption><span class="provenance">rendered · {esc(sh["file"])} · drawn from the dataset</span></figcaption></figure>')

    def watch_section(self, e, base):
        ss = self.shorts_of.get(e.id, [])
        if not ss:
            return ""
        blocks = "".join(
            f'<div class="split" data-style="watch">{self.short_figure(sh, base)}<div><p class="eyebrow"><span class="id">short {sh["n"]}</span> <span>{self.mmss(sh["seconds"])}</span></p>'
            f'<h3>{esc(sh["title"])}</h3><details class="disclosure" open><summary>transcript</summary>{"".join(f"<p>{self.voice_html(v, base)}</p>" for v in sh["voice"])}</details>'
            + (f'<p class="small faint">also on the pages for</p>{self.chips([i for i in sh["shows"] if i != e.id], base)}' if len(sh["shows"]) > 1 else "")
            + "</div></div>" for sh in ss)
        return self.section("watch", blocks, f'{len(ss)} short{"s" if len(ss) > 1 else ""} with this record on screen')

    def find_book_refs(self):
        """Where the book mentions a record: chapters that link it, and for mechanics, chapters that name it in the text
        (its name as a whole phrase, outside headings and source lists). The glossary and catalog name everything, so they are left out."""
        refs = defaultdict(list)
        mechs = [e for e in self.ents.get("mechanic", []) if not e.data.get("deprecated")]
        for stem in self.chapters:
            if not re.match(r"(0[1-9]|1[0-9])-", stem):
                continue
            md = self.built[f"book/{stem}.md"].split("\n## Sources")[0]
            title = re.search(r"^# (.*)$", md, re.M).group(1)
            linked = []
            for i in re.findall(r"\]\(\.\./wiki/\w+/([a-z0-9-]+)\.md\)", md):
                if i in self.by_id and i not in linked:
                    linked.append(i)
            plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", re.sub(r"^#.*$", "", md, flags=re.M)).lower()
            named = [e.id for e in mechs if e.id not in linked and re.search(r"\b" + re.escape(e.data["name"].lower()) + r"s?\b", plain)]
            for i in linked:
                refs[i].append((stem, title, "linked from the text"))
            for i in named:
                refs[i].append((stem, title, "named in the text"))
        return refs

    def appears_section(self, e, base):
        rows = [f'<div class="row"><div class="id">ch {int(stem[:2])}</div><div><h3><a href="{base}book/{stem}/" data-internal>{esc(title)}</a></h3><p>{esc(how)}</p></div>'
                f'<div class="end">book</div></div>' for stem, title, how in self.book_refs.get(e.id, [])]
        rows += [f'<div class="row"><div class="id">short {sh["n"]}</div><div><h3><a href="{base}watch/#{sh["key"]}" data-internal>{esc(sh["title"])}</a></h3>'
                 f'<p>{self.mmss(sh["seconds"])} · on screen in the short</p></div><div class="end">short</div></div>' for sh in self.shorts_of.get(e.id, [])]
        if not rows:
            return ""
        nb, ns = len(self.book_refs.get(e.id, [])), len(self.shorts_of.get(e.id, []))
        right = " · ".join(x for x in (f'{nb} chapter{"s" if nb != 1 else ""}' if nb else "", f'{ns} short{"s" if ns != 1 else ""}' if ns else "") if x)
        return self.section("appears in", f'<div class="register">{"".join(rows)}</div>', right)

    def families(self):
        """Mechanics by family, families with the most mechanics first, each family's mechanics most used first."""
        fam = defaultdict(list)
        for e in self.ents.get("mechanic", []):
            if not e.data.get("deprecated"):
                fam[e.data["family"]].append(e)
        for f in fam:
            fam[f].sort(key=lambda e: (-self.derived.get(e.id, {}).get("prevalence", 0), e.data["name"]))
        return sorted(fam.items(), key=lambda kv: (-len(kv[1]), kv[0]))

    def mosaic(self, base):
        """Every mechanic as its icon, one row per family: the grammar at a glance. Its twin lists the same names."""
        fams = self.families()
        n = sum(len(v) for _, v in fams)
        rows = "".join(
            f'<div class="row"><div class="id">{esc(self.term("mechanic_family", f).lower())} <b>{len(ms)}</b></div><div>'
            + "".join(f'<a href="{base}mechanic/{e.id}/" title="{esc(e.data["name"])} · {self.derived.get(e.id, {}).get("prevalence", 0)} games" data-internal>'
                      f'{self.icon(e.id, base, 24, e.data["name"])}</a>' for e in ms)
            + "</div></div>" for f, ms in fams)
        twin = "".join(f'<div class="row"><div class="id">{esc(self.term("mechanic_family", f).lower())}</div><div><p>'
                       + ", ".join(self.link(e.id, base) for e in ms) + "</p></div></div>" for f, ms in fams)
        return (f'<figure class="chart" id="grammar"><div class="chart-head"><span><b>the grammar</b> · {n} mechanics in {len(fams)} families, most used first</span>'
                f'<span>mechanics.json</span></div><div class="chart-body"><div class="register" data-kind="mosaic">{rows}</div></div>'
                f'<p class="chart-caption">Each icon is one mechanic; point at it for its name, or open it. '
                f'<span class="run">source · dist/entities/mechanics.json · dataset {self.short}</span></p>'
                f'<details class="disclosure"><summary>plain-text twin · {len(fams)} families</summary><div class="register" data-size="wide">{twin}</div></details></figure>')

    # ------------------------------------------------------------------ entity pages
    def meter(self, v, scale_max=5):
        if not isinstance(v, int):
            return esc(v)
        cells = "".join(f'<i data-state="{"done" if i < v else ""}"></i>' for i in range(scale_max))
        return f'<span class="meter" data-size="sm" role="img" aria-label="{v} of {scale_max}">{cells}</span> <span class="meter-label">{v} / {scale_max}</span>'

    def entity(self, e):
        t, d = e.type, e.data
        base = "../../"
        props = self.props[t]
        der = self.derived.get(e.id, {})
        plural = self.registry["types"][t]["plural"]
        st = d.get("status")
        eyebrow = [f'<span class="id">{esc(e.id)}</span>', f"<span>{esc(self.registry['types'][t]['label'].lower())}</span>"]
        if st:
            eyebrow.append(f'<span class="status" data-state="{STATE.get(st, "optional")}">{esc(st)}</span>')
        if d.get("deprecated"):
            eyebrow.append('<span class="status" data-state="superseded">deprecated</span>')
        meta = self.entity_meta(e)
        twins = (f'<div class="twins"><b>this record as</b><a href="{esc(self.gh(self.registry["types"][t]["dir"] + "/" + e.id + ".yaml"))}">yaml source</a>'
                 f'<a href="{esc(self.dl("wiki/" + t + "/" + e.id + ".md", base))}">markdown</a><a href="{esc(self.dl("entities/" + plural + ".json", base))}">json</a></div>')
        icon = self.icon(e.id, base, 96)
        head = (f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="{base}" data-internal>simgrammar</a></li><li><a href="../" data-internal>{esc(plural)}</a></li><li>{esc(e.id)}</li></ol></nav>'
                f'<div class="page-header"{" data-style=" + chr(34) + "icon" + chr(34) if icon else ""}>{icon}<p class="eyebrow">{" ".join(eyebrow)}</p><h1>{esc(d.get("name", e.id))}</h1>'
                + (f'<p class="dek">{esc(d["summary"])}</p>' if d.get("summary") else "") + meta + twins + "</div>")
        if d.get("deprecated"):
            head += (f'<div class="note" data-surface="open"><span class="label">deprecated</span><p>{esc(d["deprecated"].get("reason", ""))} '
                     f'Superseded by {self.link(d["deprecated"]["superseded_by"], base)}.</p></div>')
        main = ([self.parts_board(e, base)] if t == "game" else []) + [self.watch_section(e, base)]
        for f in LONG.get(t, []):
            if d.get(f):
                cls = ' class="mono"' if f == "core_loop" else ""
                main.append(self.section(f.replace("_", " "), f'<p{cls}>{esc(d[f])}</p>'))
        for f in LISTS.get(t, []):
            if d.get(f):
                main.append(self.section(f.replace("_", " "), "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in d[f]) + "</ul>"))
        if t == "opportunity" and d.get("falsifiable_signal"):
            fs = d["falsifiable_signal"]
            res = fs.get("resolution")
            outcome = res["outcome"] if res else "open"
            res_html = ""
            if res:
                ev = ", ".join(self.link(x, base, x) for x in res.get("evidence") or [])
                res_html = (f'<p class="scope">resolved {esc(res["date"])} in <a href="{esc(self.gh("log/runs/" + res["run"] + ".yaml"))}">{esc(res["run"])}</a>'
                            + (f" · evidence {ev}" if ev else "") + f'</p><p>{esc(res["note"])}</p>')
            main.append(self.section("falsifiable prediction", f'<div class="register" data-kind="forecasts"><div class="row"><div class="id"><b>by {esc(fs["resolve_by"])}</b></div>'
                                     f'<div><h3>{esc(fs["prediction"])}</h3><p>{esc(fs["criteria"])}</p>{res_html}</div>'
                                     f'<div class="end"><span class="status" data-state="{OUTCOME_STATE.get(outcome, "waiting")}">{esc(outcome)}</span></div></div></div>'))
        if d.get("assertions"):
            items = "".join(f"<li><code>{esc(x)}</code></li>" for x in d["assertions"])
            main.append(self.section("checks against the data", f'<p class="small muted">The text above states findings about this dataset. The build fails (E032) if any of these stops holding.</p><ul>{items}</ul>',
                                     f'{len(d["assertions"])} assertion{"s" if len(d["assertions"]) != 1 else ""}'))
        if d.get("ratings"):
            rrows = "".join(f'<div class="row"><div class="id">{esc(r["field"].replace("_", " "))}<small>{esc(r["value"])}</small></div><div><p>{esc(r["rationale"])}</p>'
                            f'<p class="scope"><a href="{esc(self.gh("log/runs/" + r["run"] + ".yaml"))}">{esc(r["run"])}</a></p></div></div>' for r in d["ratings"])
            main.append(self.section("ratings", f'<div class="register" data-kind="claims">{rrows}</div>', f'{len(d["ratings"])} from named runs; stored scores are their lower median'))
        main.append(self.appears_section(e, base))
        main.append(self.relations(e, base))
        claims = (d.get("key_results") or []) + (d.get("claims") or [])
        if claims:
            rows = []
            for i, c in enumerate(claims, start=1):
                srcs = ", ".join(self.link(s, base, s) for s in c.get("sources", []))
                disp = f'<p class="scope">disputed · {esc(c["disputes"])}</p>' if c.get("disputes") else ""
                quote = (f'<blockquote><p>{esc(c["quote"])}</p></blockquote>' + (f'<p class="scope">{esc(c["locator"])}</p>' if c.get("locator") else "")) if c.get("quote") else ""
                rows.append(f'<div class="row"><div class="id">c{i:02d}<small>{esc(c.get("confidence", ""))}</small></div><div><p>{esc(c["text"])}</p>'
                            f'{quote}<p class="scope">{srcs}</p>{disp}</div></div>')
            main.append(self.section("claims", f'<div class="register" data-kind="claims">{"".join(rows)}</div>', f"{len(claims)} with sources"))
        if t == "source":
            loc = d.get("url") or (f"https://doi.org/{d['doi']}" if d.get("doi") else None) or (f"https://arxiv.org/abs/{d['arxiv']}" if d.get("arxiv") else None)
            cited = der.get("incoming", {}).get("cited_by", [])
            main.append(self.section("cited by", self.list_links(cited, base) if cited else '<p class="muted">Cited in the report text.</p>', f"{len(cited)} records"))
            if loc:
                arch = f'<p class="scope">archived · <a href="{esc(d["archived"])}">wayback snapshot</a></p>' if d.get("archived") else ""
                main.insert(0, self.section("locator", f'<p><a href="{esc(loc)}">{esc(loc)}</a></p>{arch}'))
        if d.get("sources"):
            rows = []
            for sid in d["sources"]:
                s = self.by_id.get(sid)
                if not s:
                    continue
                sd = s.data
                rows.append(f'<div class="row"><div class="id"></div><div><span class="who">{esc(", ".join(sd.get("authors", [])[:3]))}</span> ({esc(sd.get("date"))}). '
                            f'{self.link(sid, base)}. <span class="venue">{esc(sd.get("venue", ""))}</span></div></div>')
            main.append(self.section("sources", f'<div class="register" data-kind="refs">{"".join(rows)}</div>', f"{len(rows)}"))
        main.append(self.provenance(d.get("provenance", {})))
        aside = self.facts(e)
        body = head + f'<div class="split"><div style="min-width:0">{"".join(m for m in main if m)}</div><aside class="aside" style="min-width:0">{aside}</aside></div>'
        title = f"{d.get('name', e.id)} · {self.registry['types'][t]['label'].lower()} · simgrammar"
        desc = d.get("summary") or d.get("notes") or d.get("name", e.id)
        return self.page(title=title, desc=desc, body=body, depth=2, nav=t, path=f"{t}/{e.id}/", image=f"og/{t}/{e.id}.png" if t != "source" else "og/site.png")

    def section(self, title, inner, right=""):
        return f'<section class="section"><div class="section-line"><h2>{esc(title)}</h2>{f"<span>{esc(right)}</span>" if right else ""}</div>{inner}</section>'

    def list_links(self, ids, base):
        return "<p>" + ", ".join(self.link(x, base) for x in ids) + "</p>"

    def entity_meta(self, e):
        d, der, t = e.data, self.derived.get(e.id, {}), e.type
        items = []
        if t == "game":
            items = [str(d.get("year", "")), d.get("developer", ""), self.term("subgenre", d.get("subgenre")), f"cluster {der.get('cluster', '').lower()}", f"{der.get('mechanic_count', 0)} mechanics"]
        elif t == "mechanic":
            items = [self.term("mechanic_family", d.get("family")), self.term("maturity", d.get("maturity")), f"used by {der.get('prevalence', 0)} games",
                     f"first seen {der.get('earliest_year')}" if der.get("earliest_year") else "", f"technique exposure {der.get('technique_exposure')}"]
        elif t == "technique":
            items = [self.term("technique_category", d.get("category")), str(d.get("year", "")), self.term("technique_maturity", d.get("maturity")),
                     f"determinism {self.term('determinism_impact', d.get('determinism_impact'))}", f"{der.get('affects_count', 0)} mechanics affected"]
        elif t == "opportunity":
            items = [self.term("opportunity_type", d.get("opportunity_type")), f"horizon {self.term('horizon', d.get('horizon'))}", f"priority {der.get('priority')}",
                     f"resolves by {d.get('falsifiable_signal', {}).get('resolve_by', '')}"]
        elif t == "source":
            items = [self.term("source_kind", d.get("kind")), d.get("venue", ""), str(d.get("date", "")), f"accessed {d.get('accessed', '')}"]
        return '<div class="meta">' + "".join(f"<span>{esc(x)}</span>" for x in items if x and x != "None") + "</div>"

    def facts(self, e):
        t, d, props = e.type, e.data, self.props[e.type]
        skip = SKIP_FACTS | set(LONG.get(t, [])) | set(LISTS.get(t, []))
        rows = []
        scores = []
        for k, p in props.items():
            if k in skip or d.get(k) in (None, [], ""):
                continue
            if p.get("x-edge") or (p.get("items") or {}).get("x-edge") or (p.get("items") or {}).get("type") == "object" or k in ("mechanics", "affects"):
                continue
            v = d[k]
            if p.get("x-rubric"):
                scores.append((k, v))
                continue
            vn = p.get("x-vocab") or (p.get("items") or {}).get("x-vocab")
            if vn:
                v = ", ".join(self.term(vn, x) for x in v) if isinstance(v, list) else self.term(vn, v)
            elif isinstance(v, list):
                v = ", ".join(str(x) for x in v)
            elif isinstance(v, bool):
                v = "yes" if v else "no"
            rows.append(f"<dt>{esc(k.replace('_', ' '))}</dt><dd>{esc(v)}</dd>")
        for store, sid in sorted((d.get("store_ids") or {}).items()):
            rows.append(f'<dt>{esc(store)}</dt><dd><a href="{esc(STORE_URL[store].format(sid))}">{esc(sid)}</a></dd>')
        out = []
        if rows:
            out.append(f'<h3>record</h3><dl class="receipt">{"".join(rows)}</dl>')
        if scores:
            sc = "".join(f"<dt>{esc(k.replace('_', ' '))}</dt><dd>{self.meter(v)}</dd>" for k, v in scores)
            note = "single model rater" if not d.get("ratings") else f"lower median of {len(d['ratings'])} ratings"
            out.append(f'<h3 style="margin-top:24px">scores</h3><dl class="receipt">{sc}</dl><p class="small faint">rubric anchors in vocab/rubrics.yaml · {note}</p>')
        der = {k: v for k, v in self.derived.get(e.id, {}).items() if isinstance(v, (int, float, str)) and v is not None}
        if der:
            dr = "".join(f"<dt>{esc(k.replace('_', ' '))}</dt><dd>{self.link(v, '../../') if isinstance(v, str) and v in self.by_id else esc(_fmt(v))}</dd>" for k, v in der.items())
            out.append(f'<h3 style="margin-top:24px">computed</h3><dl class="receipt">{dr}</dl><p class="small faint">derived by scripts/analyze.py, never stored</p>')
        return "".join(out)

    def relations(self, e, base):
        et = vocab_terms(self.vocabs, "edge_types")
        rows = []
        for ed in sorted(self.edges_out.get(e.id, []), key=lambda x: (x.type, x.target)):
            if ed.type == "cites" or ed.target not in self.by_id:
                continue
            a = ed.attr_dict()
            end = []
            if a.get("role"):
                end.append(a["role"])
            if a.get("effect"):
                end.append(self.term("effect", a["effect"]))
            note = f'<p>{esc(a["note"])}</p>' if a.get("note") else ""
            rank = 0 if a.get("role") == "core" else 1
            if e.type == "game" and ed.type == "uses":
                continue
            rows.append((ed.type, rank, f'<div class="row"><div class="id">{esc(et[ed.type]["label"].lower())}</div><div><h3>{self.icon(ed.target, base, 24)}{self.link(ed.target, base)}</h3>{note}</div>'
                         f'<div class="end">{esc(" · ".join(end))}</div></div>'))
        out = []
        if rows:
            rows.sort(key=lambda r: (r[0], r[1]))
            out.append(self.section("relations", f'<div class="register">{"".join(r[2] for r in rows)}</div>', f"{len(rows)} stored edges"))
        inc = self.derived.get(e.id, {}).get("incoming", {})
        inc_rows = []
        for k, ids in sorted(inc.items()):
            if k == "cited_by":
                continue
            inc_rows.append(f'<div class="row"><div class="id">{esc(k.replace("_", " "))}</div><div>{self.chips(ids, base)}</div>'
                            f'<div class="end">{len(ids)}</div></div>')
        if inc_rows:
            out.append(self.section("backlinks", f'<div class="register">{"".join(inc_rows)}</div>', "computed from other records"))
        return "".join(out)

    def parts_board(self, e, base):
        """A game's mechanics drawn as its parts, core first, each with the note on how this game does it. It replaces the
        game's `uses` rows in relations; the rows' text is all here, so the board is its own twin."""
        parts = []
        for ed in self.edges_out.get(e.id, []):
            if ed.type == "uses" and ed.target in self.by_id:
                a = ed.attr_dict()
                parts.append((0 if a.get("role") == "core" else 1, ed.target, a))
        parts.sort(key=lambda p: (p[0], self.by_id[p[1]].data["name"]))
        if not parts:
            return ""
        def tile(eid, a, size):
            fam = self.term("mechanic_family", self.by_id[eid].data["family"]).lower()
            note = f'<p>{esc(a["note"])}</p>' if a.get("note") else ""
            return f'<div class="row"><div class="id">{self.icon(eid, base, size)}</div><div><small>{esc(fam)}</small><h3>{self.link(eid, base)}</h3>{note}</div></div>'
        core = [p for p in parts if p[0] == 0]
        rest = [p for p in parts if p[0] != 0]
        inner = ""
        if core:
            inner += f'<p class="small faint">core · {len(core)}</p><div class="register" data-kind="board">{"".join(tile(i, a, 96) for _, i, a in core)}</div>'
        if rest:
            inner += f'<p class="small faint">supporting · {len(rest)}</p><div class="register" data-kind="board" data-size="sm">{"".join(tile(i, a, 48) for _, i, a in rest)}</div>'
        return self.section("parts", inner, f'{len(parts)} mechanics, as {e.data.get("name", e.id)} does them')

    def provenance(self, prov):
        rows = []
        for rid, kind in [(prov.get("created"), "created")] + [(r, "reviewed") for r in prov.get("reviewed", [])]:
            if not rid:
                continue
            r = self.runs.get(rid)
            date = r.data.get("date") if r else ""
            rows.append(f'<div class="row" data-state="done"><div class="id">{esc(date)}</div><span class="dot"></span><span class="kind">{esc(kind)}</span>'
                        f'<span class="what"><a href="{esc(self.gh("log/runs/" + rid + ".yaml"))}">{esc(rid)}</a></span><span class="src">{esc(r.data.get("kind", "") if r else "")}</span></div>')
        return self.section("provenance", f'<div class="register" data-kind="log" data-style="timeline">{"".join(rows)}</div>', "runs in log/runs")

    # ------------------------------------------------------------------ indexes
    def index(self, t):
        spec = {
            "game": (["name", "year", "subgenre", "_derived.cluster", "_derived.mechanic_count", "status"], ["name", "year", "subgenre", "cluster", "mechanics", "status"], ["name"]),
            "mechanic": (["name", "family", "_derived.prevalence", "_derived.earliest_year", "maturity", "legibility", "emergence_potential", "ai_leverage", "_derived.technique_exposure"],
                         ["name", "family", "games", "first seen", "maturity", "legibility", "emergence", "ai leverage", "exposure"], ["-_derived.prevalence", "name"]),
            "technique": (["name", "category", "year", "maturity", "determinism_impact", "_derived.affects_count"], ["name", "category", "year", "maturity", "determinism", "mechanics"], ["name"]),
            "opportunity": (["name", "opportunity_type", "horizon", "_derived.priority", "falsifiable_signal.resolve_by"], ["name", "type", "horizon", "priority", "resolves by"], ["-_derived.priority", "name"]),
            "source": (["name", "kind", "venue", "date"], ["name", "kind", "venue", "date"], ["-date", "name"]),
        }[t]
        cols, heads, sort = spec
        lst = [e for e in self.ents.get(t, []) if not e.data.get("deprecated")]
        recs = []
        for e in lst:
            r = dict(e.data)
            r["_derived"] = self.derived.get(e.id, {})
            recs.append(r)
        for key in reversed(sort):
            rev = key.startswith("-")
            k = key.lstrip("-")
            recs.sort(key=lambda r: (get_path(r, k) is None, str(get_path(r, k)) if not isinstance(get_path(r, k), (int, float)) else get_path(r, k)), reverse=rev)
        rows = []
        for r in recs:
            row = {}
            for c in cols:
                v = get_path(r, c)
                vn = self.vocab_of(t, c) if "." not in c else None
                if c == "name":
                    v = r["id"]
                elif vn and v is not None:
                    v = ", ".join(self.term(vn, x) for x in v) if isinstance(v, list) else self.term(vn, v)
                elif c == "_derived.cluster" and v:
                    v = v.lower()
                row[c] = v
            rows.append(row)
        base = "../"
        th = "".join(f'<th{" class=" + chr(34) + "num" + chr(34) if self._numeric(rows, c) else ""}>{esc(h)}</th>' for c, h in zip(cols, heads))
        trs = []
        for row in rows:
            tds = "".join(f'<td{" class=" + chr(34) + "num" + chr(34) if self._numeric(rows, c) else ""}>{self.link(row[c], base) if c == "name" else esc(_fmt(row[c]))}</td>' for c in cols)
            trs.append(f"<tr>{tds}</tr>")
        plural = self.registry["types"][t]["plural"]
        label = self.registry["types"][t]["label"]
        intro = {
            "game": "Each catalogued game drawn as the mechanics it is built from, core parts first. Each page holds the decomposition, design notes, claims, and sources.",
            "mechanic": "Every mechanic as its icon, grouped by family and ordered by how many games use it. The table below holds every score: rubric anchors from 1 to 5, "
                        "and exposure, the maturity-weighted reach of the technique set.",
            "technique": "Every mathematical, AI, ML, and LLM technique in the set, with its maturity in games and what it does to reproducibility.",
            "opportunity": "Every design opportunity on a board by horizon, highest impact first, with the mechanics it builds on, the techniques it uses, and the risks "
                           "those techniques carry. Each carries a dated, falsifiable prediction; the table orders them by priority.",
            "source": "Every source cited by a record or by the paper, newest first.",
        }[t]
        h1 = {"game": "Every game is a set of parts", "opportunity": "What could be built, and when"}.get(t, plural.capitalize())
        placeholder = {"game": "filter by game or by a part it has"}.get(t, f"type to filter {plural}")
        table = f'<div class="table-wrap"><table class="data" data-style="dense" data-sortable data-filterable><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>'
        visual = {"mechanic": self.mechanic_tiles, "game": self.game_parts, "opportunity": self.opportunity_board}.get(t)
        if visual:
            table = visual(lst, base) + f'<details class="disclosure"><summary>plain-text twin · {len(rows)} rows, sortable</summary>{table}</details>'
        body = (f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="../" data-internal>simgrammar</a></li><li>{esc(plural)}</li></ol></nav>'
                f'<div class="page-header"><p class="eyebrow"><span class="id">{esc(plural)}</span> <span>{len(rows)} records</span></p><h1>{esc(h1)}</h1>'
                f'<p class="dek">{esc(intro)}</p><div class="twins"><b>this list as</b><a href="{esc(self.dl("tables/" + plural + ".csv", "../"))}">csv</a>'
                f'<a href="{esc(self.dl("entities/" + plural + ".json", "../"))}">json</a><a href="{esc(self.gh(self.registry["types"][t]["dir"]))}">yaml sources</a></div></div>'
                f'<div class="controls" data-filter-controls hidden><label class="field"><span>filter</span><input type="search" data-filter placeholder="{esc(placeholder)}"></label>'
                + (self.segmented("group", "Group games", [("subgenre", "by subgenre"), ("decade", "by decade")]) if t == "game" else "")
                + f'</div>{table}')
        return self.page(title=f"{plural.capitalize()} · simgrammar", desc=intro, body=body, depth=1, nav=t, path=f"{t}/", image=f"og/{t}.png")

    @staticmethod
    def segmented(name, label, options):
        """A view switch for simgrammar.js; without script the first view shows and the switch stays hidden."""
        bs = "".join(f'<button type="button" data-value="{v}" aria-pressed="{"true" if i == 0 else "false"}">{esc(t)}</button>' for i, (v, t) in enumerate(options))
        return f'<div class="segmented" role="group" aria-label="{esc(label)}" data-views="{name}">{bs}</div>'

    def group(self, head, inner, right=""):
        """A filterable group on an index page: a section the filter hides when nothing in it matches."""
        return (f'<section class="section" data-group><div class="section-line"><h2>{head}</h2>{f"<span>{esc(right)}</span>" if right else ""}</div>'
                f'{inner}</section>')

    def mechanic_tiles(self, lst, base):
        top = max((self.derived.get(e.id, {}).get("prevalence", 0) for e in lst), default=1) or 1

        def tile(e):
            der = self.derived.get(e.id, {})
            n = der.get("prevalence", 0)
            q = " ".join([e.data["name"], e.id, *e.data.get("aliases", [])]).lower()
            return (f'<a class="row" href="{base}mechanic/{e.id}/" data-q="{esc(q)}" data-internal>{self.icon(e.id, base, 48)}<h3>{esc(e.data["name"])}</h3>'
                    f'<span class="end"><span>{n} games</span><span>{der.get("earliest_year") or ""}</span></span>'
                    f'<span class="pbar"><i style="--p:{100 * n / top:.1f}%"></i></span></a>')
        groups = "".join(
            self.group(f'{self.icon(f, base, 24)}{esc(self.term("mechanic_family", f))} <span>· {len(ms)} mechanics</span>',
                       f'<div class="register" data-kind="tiles">{"".join(tile(e) for e in ms)}</div>',
                       f'{sum(self.derived.get(e.id, {}).get("prevalence", 0) for e in ms)} uses across the catalog')
            for f, ms in self.families())
        return f'<div data-filter-scope>{groups}</div>'

    def game_parts(self, lst, base):
        mname = {e.id: e.data["name"] for e in self.ents.get("mechanic", [])}

        def row(e, sub):
            ms = sorted(e.data.get("mechanics", []), key=lambda m: (m.get("role") != "core", mname.get(m["id"], m["id"])))
            icons = "".join(f'<a href="{base}mechanic/{m["id"]}/" data-m="{m["id"]}" data-role="{esc(m.get("role", ""))}" '
                            f'title="{esc(mname.get(m["id"], m["id"]))} · {esc(m.get("role", ""))}" data-internal>{self.icon(m["id"], base, 24, mname.get(m["id"], m["id"]))}</a>'
                            for m in ms)
            q = " ".join([e.data["name"], e.id, self.term("subgenre", e.data.get("subgenre"))] + [mname.get(m["id"], "") for m in ms]).lower()
            label = f' <span>{esc(self.term("subgenre", e.data.get("subgenre")))}</span>' if sub else ""
            return (f'<div class="row" data-q="{esc(q)}"><div class="id">{esc(e.data.get("year", ""))}</div><h3>{self.link(e.id, base)}{label}</h3>'
                    f'<div class="cluster" data-gap="icons">{icons}</div><div class="end">{len(ms)}</div></div>')
        by_sub, by_dec = defaultdict(list), defaultdict(list)
        for e in lst:
            by_sub[e.data.get("subgenre")].append(e)
            by_dec[e.data.get("year", 0) // 10 * 10].append(e)
        order = lambda e: (e.data.get("year", 0), e.data["name"])
        subs = "".join(self.group(f'{self.icon(s, base, 24)}{esc(self.term("subgenre", s))} <span>· {len(gs)} games</span>',
                                  f'<div class="register" data-kind="parts">{"".join(row(e, False) for e in sorted(gs, key=order))}</div>')
                       for s, gs in sorted(by_sub.items(), key=lambda kv: (-len(kv[1]), str(kv[0]))))
        decs = "".join(self.group(f'{d}s <span>· {len(gs)} games</span>',
                                  f'<div class="register" data-kind="parts">{"".join(row(e, True) for e in sorted(gs, key=order))}</div>',
                                  f'{sum(len(e.data.get("mechanics", [])) for e in gs) / len(gs):.1f} parts a game')
                       for d, gs in sorted(by_dec.items()))
        legend = ('<div class="legend"><span><i></i>core part</span><span><i data-style="faint"></i>supporting part</span>'
                  '<span class="hide-sm">point at a part to light up every game that has it</span></div>')
        return (f'{legend}<div data-filter-scope data-parts-scope><div data-view="subgenre">{subs}</div>'
                f'<div data-view="decade" hidden>{decs}</div></div>')

    def opportunity_board(self, lst, base):
        risk_labels = {str(t["id"]): t.get("label", t["id"]) for t in self.vocabs["risk"]["terms"]}

        def icons(ids, label=None):
            return '<div class="cluster" data-gap="icons">' + "".join(
                f'<a href="{base}{self.by_id[i].type}/{i}/" title="{esc(self.by_id[i].data["name"])}" data-internal>{self.icon(i, base, 24, self.by_id[i].data["name"])}</a>'
                for i in ids if i in self.by_id) + "</div>"

        def card(e):
            d = e.data
            techs = [x for x in d.get("applies", []) if x in self.by_id]
            risks = sorted({r for x in techs for r in self.by_id[x].data.get("risks", [])})
            rk = '<div class="cluster" data-gap="icons">' + "".join(
                f'<span title="{esc(risk_labels.get(r, r))}">{self.icon("risk-" + r, base, 24, risk_labels.get(r, r))}</span>' for r in risks) + "</div>"
            q = " ".join([d["name"], e.id, d.get("summary", "")]).lower()
            dl = "".join(f"<dt>{k}</dt><dd>{self.meter(d.get(k))}</dd>" for k in ("impact", "feasibility", "novelty") if d.get(k) is not None)
            dl += f"<dt>builds on</dt><dd>{icons(d.get('involves', []))}</dd><dt>uses</dt><dd>{icons(techs)}</dd>"
            dl += f"<dt>risks</dt><dd>{rk}</dd>" if risks else ""
            return (f'<div class="row" data-q="{esc(q)}"><div class="id">{esc(self.term("opportunity_type", d.get("opportunity_type")).lower())}</div>'
                    f'<div><h3>{self.link(e.id, base)}</h3><p>{esc(d.get("summary", ""))}</p><dl class="receipt">{dl}</dl></div></div>')
        cols = []
        for h in ("now", "1-2y", "3-5y", "5y-plus"):
            ops = sorted((e for e in lst if e.data.get("horizon") == h), key=lambda e: (-(e.data.get("impact") or 0), -(e.data.get("feasibility") or 0), e.data["name"]))
            inner = "".join(card(e) for e in ops) or '<div class="row"><p>none yet</p></div>'
            cols.append(f'<section data-group><div class="section-line"><h2>{self.icon("horizon-" + h, base, 48)}{esc(self.term("horizon", h))} <span>· {len(ops)}</span></h2></div>'
                        f'<div class="register" data-kind="cards">{inner}</div></section>')
        legend = '<div class="legend">' + "".join(f'<span>{self.icon("risk-" + r, base, 24)}{esc(lbl)}</span>' for r, lbl in risk_labels.items()) + "</div>"
        return f'{legend}<div class="grid" data-cols="4" data-gap="board" data-filter-scope>{"".join(cols)}</div>'

    # ------------------------------------------------------------------ data page
    def data_page(self):
        man = self.manifest
        plurals = [self.registry["types"][t]["plural"] for t in self.registry["types"] if not self.registry["types"][t].get("meta")]
        files = [
            ("dist/simgrammar-dist.zip", "everything below in one archive (assembled by the Pages workflow)", [("zip", "simgrammar-dist.zip")]),
            ("dist/tables/", "one flat table per entity type, edges.csv, game_mechanic_matrix.csv",
             [(n, f"tables/{n}.csv") for n in plurals + ["edges", "game_mechanic_matrix"]]),
            ("dist/entities/", "full records with computed fields under _derived", [(n, f"entities/{n}.json") for n in plurals]),
            ("dist/graph/", "nodes, edges, Cytoscape, GraphML", [("nodes", "graph/nodes.jsonl"), ("edges", "graph/edges.jsonl"), ("cytoscape", "graph/cytoscape.json"), ("graphml", "graph/graph.graphml")]),
            ("dist/analysis/", "every statistic, and every analysis table as csv", [("stats", "analysis/stats.json"), ("clusters", "analysis/game-clusters.csv"), ("white space", "analysis/whitespace.csv"), ("verification queue", "analysis/verification-queue.csv")]),
            ("dist/wiki/", "one markdown page per record and vocabulary, with backlinks", [("index", "wiki/index.md")]),
            ("dist/paper/", "the paper as markdown with its bibliography", [("paper", "paper/paper.md"), ("bibtex", "paper/references.bib")]),
            ("dist/manifest.json", "per-record and dataset sha256, schema and vocab hashes", [("manifest", "manifest.json")]),
        ]
        def anchors(links):
            return " ".join(f'<a href="{esc(self.dl(h, "../"))}">{esc(n)}</a>' for n, h in links)
        frows = "".join(f'<div class="row"><div class="id">{esc(p)}</div><div><p style="color:var(--ink)">{esc(dsc)}</p></div>'
                        f'<div class="end">{anchors(links)}</div></div>' for p, dsc, links in files)
        cmds = [("git clone " + self.site["repo"], "get the repository"), ("pip install -r requirements.txt", "pinned dependencies"),
                ("make check", "validate every rule, every report and record assertion, and the generated docs"), ("python scripts/find.py production chain", "search before you create a record"),
                ("python scripts/new.py run my-run --kind catalog", "open a run before you edit data"), ("make build", "build dist/ locally, including this site; CI builds and publishes it"),
                ("make sqlite", "query everything with SQL")]
        crows = "".join(f'<div class="row"><div class="id"></div><div><code>{esc(c)}</code><span class="why">{esc(w)}</span></div></div>' for c, w in cmds)
        runs = sorted(self.ents.get("run", []), key=lambda r: (str(r.data.get("date")), r.id), reverse=True)
        rrows = "".join(f'<div class="row" data-state="done"><div class="id">{esc(r.data.get("date"))}</div><span class="dot"></span><span class="kind">{esc(r.data.get("kind"))}</span>'
                        f'<span class="what"><a href="{esc(self.gh("log/runs/" + r.id + ".yaml"))}">{esc(r.id)}</a> · {esc(r.data.get("purpose", "")[:140])}</span>'
                        f'<span class="src">{esc(r.data.get("actor", ""))}</span></div>' for r in runs)
        vrows = "".join(f'<div class="row"><div class="id">{esc(n)}</div><div><p>{esc((v.get("description") or "").strip())}</p></div><div class="end">{len(v.get("terms", []))} terms</div></div>'
                        for n, v in sorted(self.vocabs.items()) if n not in ("rubrics",))
        body = (f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="../" data-internal>simgrammar</a></li><li>data</li></ol></nav>'
                f'<div class="page-header"><p class="eyebrow"><span class="id">data</span> <span>dataset <b>{self.short}</b></span> <span>contract {esc(man["contract_version"])}</span></p>'
                f'<h1>Take the data, check it, add to it</h1><p class="dek">Every page on this site is generated from YAML records in the repository. '
                f'The same records project into tables, a graph, a wiki, the paper, and this site, and a validator keeps them consistent.</p>'
                f'<div class="twins"><b>start with</b><a href="{esc(self.gh("AGENTS.md"))}">AGENTS.md</a><a href="{esc(self.gh("CONTRACT.md"))}">CONTRACT.md</a><a href="../llms.txt" data-internal>llms.txt</a></div></div>'
                + self.section("downloads", f'<div class="register" data-size="wide">{frows}</div>', "generated projections, published beside this site")
                + self.section("commands", f'<div class="register" data-kind="cmds">{crows}</div>', "from the repository root")
                + self.section("research log", f'<div class="register" data-kind="log" data-style="timeline">{rrows}</div>', f"{len(runs)} runs, newest first")
                + self.section("vocabularies", f'<div class="register" data-size="wide">{vrows}</div>', "closed; add terms through an ADR"))
        return self.page(title="Data · simgrammar", desc="Downloads, commands, research log, and vocabularies for the SimGrammar dataset.", body=body, depth=1, nav="data", path="data/")

    # ------------------------------------------------------------------ watch and book pages
    def watch_page(self):
        base = "../"
        tiles, twin = [], []
        for sh in self.shorts:
            about = [i for i in sh["shows"] if self.by_id[i].type != "game"][:2] + [i for i in sh["shows"] if self.by_id[i].type == "game"][:2]
            tiles.append(f'<div class="row" id="{sh["key"]}">{self.short_figure(sh, base, 216)}<p class="eyebrow"><span class="id">short {sh["n"]}</span> '
                         f'<span>{self.mmss(sh["seconds"])}</span></p><h3>{esc(sh["title"])}</h3><p>{self.voice_html(sh["voice"][0], base) if sh["voice"] else ""}</p>'
                         f'{self.chips(about, base)}</div>')
            twin.append(f'<div class="row"><div class="id">short {sh["n"]}</div><div><h3>{esc(sh["title"])}</h3>'
                        + "".join(f"<p>{self.voice_html(v, base)}</p>" for v in sh["voice"]) + "</div></div>")
        n = len(self.shorts)
        body = (f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="../" data-internal>simgrammar</a></li><li>watch</li></ol></nav>'
                f'<div class="page-header"><p class="eyebrow"><span class="id">watch</span> <span>{n} shorts</span></p><h1>{n} findings, under a minute each</h1>'
                f'<p class="dek">Each short states one finding from the dataset in its first sentence, and every picture in it is drawn from the records. '
                f'Each also appears on the pages of the records it shows. The full episodes come later.</p></div>'
                + (f'<div class="register" data-kind="watch">{"".join(tiles)}</div>'
                   f'<details class="disclosure"><summary>plain-text twin · {n} transcripts</summary><div class="register">{"".join(twin)}</div></details>'
                   if n else '<p class="muted">No shorts are published yet.</p>'))
        return self.page(title="Watch · simgrammar", desc=f"{n} short videos, each stating one finding from the SimGrammar dataset.", body=body,
                         depth=1, nav="watch", path="watch/", image="og/watch.png")

    def book_md(self, stem):
        """A rendered chapter with its links pointed at the site: records, other chapters, and the paper's figures."""
        md = self.built[f"book/{stem}.md"]
        md = re.sub(r"\]\(\.\./wiki/(\w+)/([a-z0-9-]+)\.md\)", r"](../../\1/\2/)", md)
        md = re.sub(r"\]\((\d\d-[a-z0-9-]+)\.md\)", r"](../\1/)", md)
        return md.replace("](../paper/figures/", "](../../figures/")

    def book_toc(self, current, base):
        links = []
        for m in re.finditer(r"^(#+ .*|\d+\. \[.*?\]\((\d\d-[a-z0-9-]+)\.md\)|\[.*?\]\((\d\d-[a-z0-9-]+)\.md\)|- \[.*?\]\((\d\d-[a-z0-9-]+)\.md\))", self.built["book/00-contents.md"], re.M):
            line = m.group(1)
            stem = m.group(2) or m.group(3) or m.group(4)
            if line.startswith("## "):
                links.append(f'<span class="toc-head">{esc(line[3:].lower())}</span>')
            elif stem:
                label = re.search(r"\[(.*?)\]", line).group(1)
                num = re.match(r"(\d+)\. ", line)
                cur = ' aria-current="true"' if stem == current else ""
                links.append(f'<a href="{base}book/{stem}/"{cur} data-internal>{esc((num.group(1) + ". ") if num else "")}{esc(label)}</a>')
        return "".join(links)

    def book_chapter(self, stem):
        base = "../../"
        mdr = MarkdownIt("commonmark", {"html": True}).enable("table")
        body = mdr.render(self.book_md(stem))
        body = body.replace("<table>", '<div class="table-wrap"><table class="data" data-style="dense">').replace("</table>", "</table></div>")
        title = re.search(r"^# (.*)$", self.built[f"book/{stem}.md"], re.M).group(1)
        words = len(re.sub(r"<[^>]+>", " ", body.split('<h2>Sources</h2>')[0]).split())
        i = self.chapters.index(stem)
        prev_, next_ = (self.chapters[i - 1] if i > 1 else None), (self.chapters[i + 1] if i + 1 < len(self.chapters) else None)
        def name_of(st):
            return re.search(r"^# (.*)$", self.built[f"book/{st}.md"], re.M).group(1)
        pager = '<nav class="pagination" aria-label="Chapters">' + (f'<a href="../{prev_}/" data-internal>← {esc(name_of(prev_))}</a>' if prev_ else "") + \
                f'<a href="../" data-internal>contents</a>' + (f'<a href="../{next_}/" data-internal>{esc(name_of(next_))} →</a>' if next_ else "") + "</nav>"
        mechs = [i for i, rs in self.book_refs.items() if any(r[0] == stem for r in rs) and self.by_id[i].type == "mechanic"]
        others = [i for i, rs in self.book_refs.items() if any(r[0] == stem for r in rs) and self.by_id[i].type != "mechanic"]
        rel = ""
        if mechs:
            rel += self.section("mechanics in this chapter", self.chips(sorted(mechs, key=lambda x: self.by_id[x].data["name"]), base), f"{len(mechs)} linked or named")
        if others:
            rel += self.section("records linked from this chapter", self.chips(others, base), f"{len(others)}")
        toc = self.book_toc(stem, base)
        main = (f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="{base}" data-internal>simgrammar</a></li><li><a href="../" data-internal>book</a></li><li>{esc(stem)}</li></ol></nav>'
                f'<div class="sidebar"><aside class="hide-md sticky"><nav class="toc" aria-label="The book">{toc}</nav></aside>'
                f'<article class="prose" style="min-width:0"><details class="disclosure show-md"><summary>the book · contents</summary><nav class="toc" aria-label="The book">{toc}</nav></details>'
                f'<p class="eyebrow"><span class="id">{esc(stem)}</span> <span>{words:,} words</span> <span>about {max(1, round(words / 230))} min</span></p>'
                f'{body}{pager}{rel}</article></div>')
        return self.page(title=f"{title} · the book · simgrammar", desc=f"{title}, a chapter of The Grammar of Simulation, rendered from the dataset.",
                         body=main, depth=2, nav="book", path=f"book/{stem}/", image=f"og/book/{stem}.png")

    def book_index(self):
        base = "../"
        words = sum(len(re.sub(r"[#*\[\]()]", " ", self.built[f"book/{st}.md"].split("\n## Sources")[0]).split()) for st in self.chapters if st[:2] not in ("00", "90", "91"))
        rows = []
        for st in self.chapters:
            if st == "00-contents":
                continue
            title = re.search(r"^# (.*)$", self.built[f"book/{st}.md"], re.M).group(1)
            nref = sum(1 for rs in self.book_refs.values() for r in rs if r[0] == st)
            rows.append(f'<div class="row"><div class="id">{esc(st[:2])}</div><div><h3><a href="{st}/" data-internal>{esc(title)}</a></h3></div>'
                        f'<div class="end">{f"{nref} records" if nref else ""}</div></div>')
        body = (f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="../" data-internal>simgrammar</a></li><li>book</li></ol></nav>'
                f'<div class="page-header"><p class="eyebrow"><span class="id">book</span> <span>{sum(1 for st in self.chapters if re.match(r"(0[1-9]|1[0-9])-", st))} chapters, a preface, and back matter</span> <span>about {words // 1000}k words</span></p>'
                f'<h1>The Grammar of Simulation, as a book</h1><p class="dek">The paper\'s findings at book length: thirteen chapters in four parts, a glossary of every '
                f'mechanic, and the catalog of games. Like the paper, every number is rendered from the dataset when the site is built, and every sentence that '
                f'interprets one is checked against the data.</p></div><div class="register" data-size="wide">{"".join(rows)}</div>')
        return self.page(title="The book · simgrammar", desc="The Grammar of Simulation as a book, one chapter a page, rendered from the dataset.", body=body,
                         depth=1, nav="book", path="book/", image="og/book.png")

    def llms_txt(self):
        m, man = self.meta, self.manifest
        lines = [f"# simgrammar · {m['title']}", "", f"> {m['subtitle']}. A versioned dataset of simulation game mechanics with provenance, and the paper projected from it.", "",
                 f"dataset sha256: {man['dataset_sha256']}", f"contract: {man['contract_version']} · paper v{m['version']} ({m['date']})", "",
                 "## Read", f"- {self.site['url']}paper.md: the paper as markdown", f"- {self.site['url']}references.bib: bibliography", f"- {self.site['url']}manifest.json: counts and hashes",
                 f"- {self.site['url']}book/: the book, one chapter a page", f"- {self.site['url']}watch/: the published shorts, with transcripts", "",
                 "## Data", f"- {self.site['url']}dist/simgrammar-dist.zip: every projection in one archive",
                 f"- {self.site['url']}dist/tables/games.csv (and mechanics, techniques, opportunities, sources, edges, game_mechanic_matrix): csv tables",
                 f"- {self.site['url']}dist/entities/games.json (and the other types): full json records",
                 f"- {self.site['url']}dist/graph/nodes.jsonl, edges.jsonl: the graph", f"- {self.site['url']}data/: every download, the research log, the vocabularies", "",
                 "## Contribute", f"- {self.site['repo']}/blob/main/AGENTS.md: procedure for humans and agents", f"- {self.site['repo']}/blob/main/CONTRACT.md: invariants and validator rules", ""]
        return "\n".join(lines)

    def not_found(self):
        body = ('<div class="page-header"><p class="eyebrow"><span class="id">404</span></p><h1>No record at this address</h1>'
                '<p class="dek">Record ids never change once merged, so this address never held a page, or the record was deprecated before it was published.</p>'
                '<div class="actions"><a class="btn" href="/" data-internal>Back to the paper</a></div></div>')
        return self.page(title="Not found · simgrammar", desc="Page not found.", body=body, depth=0, nav="", path="404.html").replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/')


def favicon(png: bytes) -> bytes:
    """The 192 px icon raster sampled every fourth pixel: 48 px, one pixel per dither pixel."""
    import io
    from PIL import Image
    out = io.BytesIO()
    Image.open(io.BytesIO(png)).resize((48, 48), Image.NEAREST).save(out, format="PNG")
    return out.getvalue()


def build_web(ents, edges, analysis, vocabs, registry, schemas, ctx, manifest, meta, paper_md, references_bib, figure_svgs, built=None) -> dict[str, str | bytes]:
    w = Web(ents, edges, analysis, vocabs, registry, schemas, ctx, manifest, meta, built)
    outs = {}
    outs["web/index.html"] = w.paper()
    for t in w.types:
        outs[f"web/{t}/index.html"] = w.index(t)
        for e in sorted(ents.get(t, []), key=lambda e: e.id):
            outs[f"web/{t}/{e.id}/index.html"] = w.entity(e)
    outs["web/data/index.html"] = w.data_page()
    outs["web/watch/index.html"] = w.watch_page()
    if w.chapters:
        outs["web/book/index.html"] = w.book_index()
        for stem in w.chapters:
            if stem != "00-contents":
                outs[f"web/book/{stem}/index.html"] = w.book_chapter(stem)
    outs["web/404.html"] = w.not_found()
    outs["web/llms.txt"] = w.llms_txt()
    # the paper's entity links point into dist/wiki; on the site they point at the record pages
    outs["web/paper.md"] = re.sub(r"\]\(\.\./wiki/([a-z]+)/([a-z0-9-]+)\.md\)", lambda m: f"]({meta['site']['url']}{m.group(1)}/{m.group(2)}/)", paper_md)
    outs["web/references.bib"] = references_bib
    outs["web/manifest.json"] = json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    for name, svg in figure_svgs.items():
        outs[f"web/figures/{name}.svg"] = svg
    outs["web/CNAME"] = meta["site"]["domain"] + "\n"
    root = meta["site"]["url"]
    pages = sorted(k[len("web/"):-len("index.html")] for k in outs if k.startswith("web/") and k.endswith("index.html"))
    outs["web/sitemap.xml"] = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                               + "".join(f"  <url><loc>{esc(root + p)}</loc></url>\n" for p in pages) + "</urlset>\n")
    outs["web/robots.txt"] = f"User-agent: *\nAllow: /\nSitemap: {root}sitemap.xml\n"
    outs["web/.nojekyll"] = ""
    for f in ("register.css", "simgrammar.js"):
        outs[f"web/assets/{f}"] = (WEB_SRC / f).read_text(encoding="utf-8")
    for i in sorted(w.icons):
        outs[f"web/assets/icons/{i}.png"] = w.built[f"visual/icons/{i}@4x.png"]
    if FAVICON in w.icons:
        outs["web/assets/favicon.png"] = favicon(w.built[f"visual/icons/{FAVICON}@4x.png"])
    if w.icons:
        import og
        outs.update(og.images(w))
    return outs
