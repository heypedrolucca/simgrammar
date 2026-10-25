"""Project the dataset into a static website (dist/web), styled with Register (web/register.css).

Pages:
  index.html                         the paper, rendered from report/src with interactive figures
  <type>/index.html                  one index per entity type (sortable table)
  <type>/<id>/index.html             one page per entity
  data/index.html                    downloads, provenance log, contract
  paper.md, references.bib, manifest.json, figures/*.svg, llms.txt, CNAME, 404.html, assets/*

Everything here is a deterministic function of data/, report/, vocab/, schema/, and web/.
Pages work without JavaScript; assets/simgrammar.js only adds interaction.
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
NAV = [("paper", "Paper", ""), ("game", "Games", "game/"), ("mechanic", "Mechanics", "mechanic/"), ("technique", "Techniques", "technique/"),
       ("opportunity", "Opportunities", "opportunity/"), ("source", "Sources", "source/"), ("data", "Data", "data/")]
STATE = {"asserted": "optional", "sourced": "waiting", "verified": "done", "contested": "blocked"}
SKIP_FACTS = {"id", "type", "name", "aliases", "summary", "status", "provenance", "sources", "claims", "deprecated", "key_results", "falsifiable_signal"}
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
    def __init__(self, ents, edges, analysis, vocabs, registry, schemas, ctx, manifest, meta):
        self.ents, self.edges, self.analysis, self.vocabs = ents, edges, analysis, vocabs
        self.registry, self.schemas, self.ctx, self.manifest, self.meta = registry, schemas, ctx, manifest, meta
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

    def gh(self, path):
        return f'{self.site["repo"]}/blob/main/{path}'

    def page(self, *, title, desc, body, depth, nav, path):
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
        return (f'<figure class="chart" id="fig-{name}"><div class="chart-head"><span><b>figure {n}</b></span><span>{esc(name)}</span></div>'
                f'<div class="chart-body">{svg}</div><figcaption class="chart-caption">{esc(f["caption"])} '
                f'<span class="run">source · dist/analysis/figures/{esc(name)}.svg · dataset {self.short}</span></figcaption></figure>')

    @staticmethod
    def fluid(svg):
        """Inline SVGs scale to the column: drop the fixed width and height the standalone file keeps."""
        return re.sub(r'^(<svg[^>]*?) width="\d+" height="\d+"', r"\1", svg, count=1).replace("max-width:100%;height:auto", "width:100%;max-width:none;height:auto", 1)

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
                f'<div class="chart-body">{self.fluid(v["svg"])}</div>{v.get("legend", "")}'
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
<p class="small faint">source · dist/analysis/stats.json · dataset {self.short} · every number on this page is rendered from the dataset at build time</p>"""
        main = f"""<div class="sidebar">
<aside class="hide-md"><nav class="toc sticky" aria-label="Contents"><span class="toc-head">contents</span>{tocs}</nav></aside>
<article class="prose" style="min-width:0">
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
                 f'<a href="{esc(self.gh("dist/wiki/" + t + "/" + e.id + ".md"))}">markdown</a><a href="{esc(self.gh("dist/entities/" + plural + ".json"))}">json</a></div>')
        head = (f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="{base}" data-internal>simgrammar</a></li><li><a href="../" data-internal>{esc(plural)}</a></li><li>{esc(e.id)}</li></ol></nav>'
                f'<div class="page-header"><p class="eyebrow">{" ".join(eyebrow)}</p><h1>{esc(d.get("name", e.id))}</h1>'
                + (f'<p class="dek">{esc(d["summary"])}</p>' if d.get("summary") else "") + meta + twins + "</div>")
        if d.get("deprecated"):
            head += (f'<div class="note" data-surface="open"><span class="label">deprecated</span><p>{esc(d["deprecated"].get("reason", ""))} '
                     f'Superseded by {self.link(d["deprecated"]["superseded_by"], base)}.</p></div>')
        main = []
        for f in LONG.get(t, []):
            if d.get(f):
                cls = ' class="mono"' if f == "core_loop" else ""
                main.append(self.section(f.replace("_", " "), f'<p{cls}>{esc(d[f])}</p>'))
        for f in LISTS.get(t, []):
            if d.get(f):
                main.append(self.section(f.replace("_", " "), "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in d[f]) + "</ul>"))
        if t == "opportunity" and d.get("falsifiable_signal"):
            fs = d["falsifiable_signal"]
            main.append(self.section("falsifiable prediction", f'<div class="register" data-kind="forecasts"><div class="row"><div class="id"><b>by {esc(fs["resolve_by"])}</b></div>'
                                     f'<div><h3>{esc(fs["prediction"])}</h3><p>{esc(fs["criteria"])}</p></div><div class="end"><span class="status" data-state="waiting">open</span></div></div></div>'))
        main.append(self.relations(e, base))
        claims = (d.get("key_results") or []) + (d.get("claims") or [])
        if claims:
            rows = []
            for i, c in enumerate(claims, start=1):
                srcs = ", ".join(self.link(s, base, s) for s in c.get("sources", []))
                disp = f'<p class="scope">disputed · {esc(c["disputes"])}</p>' if c.get("disputes") else ""
                rows.append(f'<div class="row"><div class="id">c{i:02d}<small>{esc(c.get("confidence", ""))}</small></div><div><p>{esc(c["text"])}</p>'
                            f'<p class="scope">{srcs}</p>{disp}</div></div>')
            main.append(self.section("claims", f'<div class="register" data-kind="claims">{"".join(rows)}</div>', f"{len(claims)} with sources"))
        if t == "source":
            loc = d.get("url") or (f"https://doi.org/{d['doi']}" if d.get("doi") else None) or (f"https://arxiv.org/abs/{d['arxiv']}" if d.get("arxiv") else None)
            cited = der.get("incoming", {}).get("cited_by", [])
            main.append(self.section("cited by", self.list_links(cited, base) if cited else '<p class="muted">Cited in the report text.</p>', f"{len(cited)} records"))
            if loc:
                main.insert(0, self.section("locator", f'<p><a href="{esc(loc)}">{esc(loc)}</a></p>'))
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
        return self.page(title=title, desc=desc, body=body, depth=2, nav=t, path=f"{t}/{e.id}/")

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
        out = []
        if rows:
            out.append(f'<h3>record</h3><dl class="receipt">{"".join(rows)}</dl>')
        if scores:
            sc = "".join(f"<dt>{esc(k.replace('_', ' '))}</dt><dd>{self.meter(v)}</dd>" for k, v in scores)
            out.append(f'<h3 style="margin-top:24px">scores</h3><dl class="receipt">{sc}</dl><p class="small faint">rubric anchors in vocab/rubrics.yaml · single model rater</p>')
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
            rows.append((ed.type, rank, f'<div class="row"><div class="id">{esc(et[ed.type]["label"].lower())}</div><div><h3>{self.link(ed.target, base)}</h3>{note}</div>'
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
            links = ", ".join(self.link(x, base) for x in ids)
            inc_rows.append(f'<div class="row"><div class="id">{esc(k.replace("_", " "))}</div><div><p style="color:var(--ink)">{links}</p></div>'
                            f'<div class="end">{len(ids)}</div></div>')
        if inc_rows:
            out.append(self.section("backlinks", f'<div class="register">{"".join(inc_rows)}</div>', "computed from other records"))
        return "".join(out)

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
            "game": "Every catalogued simulation game with its subgenre, cluster, and number of mechanics. Each page holds the decomposition, design notes, claims, and sources.",
            "mechanic": "Every mechanic, ordered by how many games use it. Scores are rubric anchors from 1 to 5; exposure is the maturity-weighted reach of the technique set.",
            "technique": "Every mathematical, AI, ML, and LLM technique in the set, with its maturity in games and what it does to reproducibility.",
            "opportunity": "Every design opportunity, ordered by priority (weighted geometric mean of impact, feasibility, and novelty). Each carries a dated, falsifiable prediction.",
            "source": "Every source cited by a record or by the paper, newest first.",
        }[t]
        body = (f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol><li><a href="../" data-internal>simgrammar</a></li><li>{esc(plural)}</li></ol></nav>'
                f'<div class="page-header"><p class="eyebrow"><span class="id">{esc(plural)}</span> <span>{len(rows)} records</span></p><h1>{esc(plural.capitalize())}</h1>'
                f'<p class="dek">{esc(intro)}</p><div class="twins"><b>this list as</b><a href="{esc(self.gh("dist/tables/" + plural + ".csv"))}">csv</a>'
                f'<a href="{esc(self.gh("dist/entities/" + plural + ".json"))}">json</a><a href="{esc(self.gh(self.registry["types"][t]["dir"]))}">yaml sources</a></div></div>'
                f'<div class="controls" data-filter-controls hidden><label class="field"><span>filter</span><input type="search" data-filter placeholder="type to filter {esc(plural)}"></label></div>'
                f'<div class="table-wrap"><table class="data" data-style="dense" data-sortable data-filterable><thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>')
        return self.page(title=f"{plural.capitalize()} · simgrammar", desc=intro, body=body, depth=1, nav=t, path=f"{t}/")

    # ------------------------------------------------------------------ data page
    def data_page(self):
        man = self.manifest
        files = [
            ("dist/tables/*.csv", "one flat table per entity type, edges.csv, game_mechanic_matrix.csv", "tree/main/dist/tables"),
            ("dist/entities/*.json", "full records with computed fields under _derived", "tree/main/dist/entities"),
            ("dist/graph/", "nodes.jsonl, edges.jsonl, cytoscape.json, graph.graphml", "tree/main/dist/graph"),
            ("dist/analysis/", "stats.json, every analysis table as csv, figures", "tree/main/dist/analysis"),
            ("dist/wiki/", "one markdown page per record and vocabulary, with backlinks", "tree/main/dist/wiki"),
            ("dist/paper/", "paper.md, references.bib, figures", "tree/main/dist/paper"),
            ("dist/manifest.json", "per-record and dataset sha256, schema and vocab hashes", "blob/main/dist/manifest.json"),
        ]
        frows = "".join(f'<div class="row"><div class="id">{esc(p)}</div><div><p style="color:var(--ink)">{esc(dsc)}</p></div>'
                        f'<div class="end"><a href="{esc(self.site["repo"] + "/" + href)}">open</a></div></div>' for p, dsc, href in files)
        cmds = [("git clone " + self.site["repo"], "get the repository"), ("pip install -r requirements.txt", "pinned dependencies"),
                ("make check", "validate every rule and confirm every projection is fresh"), ("python scripts/find.py production chain", "search before you create a record"),
                ("python scripts/new.py run my-run --kind catalog", "open a run before you edit data"), ("make build", "regenerate dist/, including this site"),
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
                + self.section("downloads", f'<div class="register" data-size="wide">{frows}</div>', "projections in dist/")
                + self.section("commands", f'<div class="register" data-kind="cmds">{crows}</div>', "from the repository root")
                + self.section("research log", f'<div class="register" data-kind="log" data-style="timeline">{rrows}</div>', f"{len(runs)} runs, newest first")
                + self.section("vocabularies", f'<div class="register" data-size="wide">{vrows}</div>', "closed; add terms through an ADR"))
        return self.page(title="Data · simgrammar", desc="Downloads, commands, research log, and vocabularies for the SimGrammar dataset.", body=body, depth=1, nav="data", path="data/")

    def llms_txt(self):
        m, man = self.meta, self.manifest
        lines = [f"# simgrammar · {m['title']}", "", f"> {m['subtitle']}. A versioned dataset of simulation game mechanics with provenance, and the paper projected from it.", "",
                 f"dataset sha256: {man['dataset_sha256']}", f"contract: {man['contract_version']} · paper v{m['version']} ({m['date']})", "",
                 "## Read", f"- {self.site['url']}paper.md: the paper as markdown", f"- {self.site['url']}references.bib: bibliography", f"- {self.site['url']}manifest.json: counts and hashes", "",
                 "## Data", f"- {self.site['repo']}/tree/main/dist/tables: csv per type, edges.csv, game_mechanic_matrix.csv",
                 f"- {self.site['repo']}/tree/main/dist/entities: full json records", f"- {self.site['repo']}/tree/main/dist/graph: jsonl, cytoscape, graphml", "",
                 "## Contribute", f"- {self.site['repo']}/blob/main/AGENTS.md: procedure for humans and agents", f"- {self.site['repo']}/blob/main/CONTRACT.md: invariants and validator rules", ""]
        return "\n".join(lines)

    def not_found(self):
        body = ('<div class="page-header"><p class="eyebrow"><span class="id">404</span></p><h1>No record at this address</h1>'
                '<p class="dek">Record ids never change once merged, so this address never held a page, or the record was deprecated before it was published.</p>'
                '<div class="actions"><a class="btn" href="/" data-internal>Back to the paper</a></div></div>')
        return self.page(title="Not found · simgrammar", desc="Page not found.", body=body, depth=0, nav="", path="404.html").replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/')


def build_web(ents, edges, analysis, vocabs, registry, schemas, ctx, manifest, meta, paper_md, references_bib, figure_svgs) -> dict[str, str]:
    w = Web(ents, edges, analysis, vocabs, registry, schemas, ctx, manifest, meta)
    outs = {}
    outs["web/index.html"] = w.paper()
    for t in w.types:
        outs[f"web/{t}/index.html"] = w.index(t)
        for e in sorted(ents.get(t, []), key=lambda e: e.id):
            outs[f"web/{t}/{e.id}/index.html"] = w.entity(e)
    outs["web/data/index.html"] = w.data_page()
    outs["web/404.html"] = w.not_found()
    outs["web/llms.txt"] = w.llms_txt()
    # the paper's entity links point into dist/wiki; on the site they point at the record pages
    outs["web/paper.md"] = re.sub(r"\]\(\.\./wiki/([a-z]+)/([a-z0-9-]+)\.md\)", lambda m: f"]({meta['site']['url']}{m.group(1)}/{m.group(2)}/)", paper_md)
    outs["web/references.bib"] = references_bib
    outs["web/manifest.json"] = json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    for name, svg in figure_svgs.items():
        outs[f"web/figures/{name}.svg"] = svg
    outs["web/CNAME"] = meta["site"]["domain"] + "\n"
    outs["web/.nojekyll"] = ""
    for f in ("register.css", "simgrammar.js"):
        outs[f"web/assets/{f}"] = (WEB_SRC / f).read_text(encoding="utf-8")
    return outs
