"""Token, link, and citation rendering for report/src and wiki pages.

Syntax (documented in AGENTS.md):
  {{count:<type>}}            number of live entities of a type (game, mechanic, technique, opportunity, source)
  {{count:edge:<edge_type>}}  number of edges of a type
  {{stat:<name>}}             named statistic from scripts/analyze.py
  {{table:<name>}}            table from report/tables.yaml or scripts/analyze.py
  {{figure:<name>}}           SVG figure from scripts/analyze.py
  {{vocab:<vocab>:<term>}}    a vocab term's label
  [[id]] / [[id|text]]        link to an entity
  [@src-id] / [@src-a; @src-b] citation
"""
from __future__ import annotations

import re
from collections import Counter

from lib import ROOT, get_path, read_yaml, vocab_terms

TOKEN_RE = re.compile(r"\{\{([a-z_]+):([^}]+)\}\}")
LINK_RE = re.compile(r"\[\[([a-z0-9-]+)(?:\|([^\]]+))?\]\]")
CITE_RE = re.compile(r"\[(@src-[a-z0-9-]+(?:\s*;\s*@src-[a-z0-9-]+)*)\]")
LITERAL_STAT_RE = re.compile(
    r"\b\d{2,}(?:,\d{3})*\s+(?:simulation\s+|sim\s+|distinct\s+|unique\s+)?(games|titles|mechanics|techniques|opportunities|sources|edges|entities|pairs|clusters|predictions)\b",
    re.I,
)


class Context:
    def __init__(self, ents, edges, analysis, vocabs, registry):
        self.ents = ents
        self.edges = edges
        self.analysis = analysis
        self.vocabs = vocabs
        self.registry = registry
        self.by_id = {e.id: e for t, lst in ents.items() if t != "run" for e in lst}
        self.edge_counts = Counter(e.type for e in edges)
        spec = read_yaml(ROOT / "report" / "tables.yaml") or {}
        self.decl_tables = {t["name"]: t for t in spec.get("tables", [])}
        self.citations: list[str] = []

    def link_target(self, eid: str, mode: str) -> str:
        e = self.by_id[eid]
        if mode == "wiki":
            return f"../{e.type}/{eid}.md"
        if mode == "site":
            return f"#/{e.type}/{eid}"
        return f"../wiki/{e.type}/{eid}.md"

    def label(self, eid: str) -> str:
        e = self.by_id.get(eid)
        return e.data.get("name", eid) if e else eid


def _fmt(v):
    if isinstance(v, float):
        s = f"{v:.3f}".rstrip("0").rstrip(".")
        return s
    if isinstance(v, list):
        return ", ".join(_fmt(x) for x in v)
    if v is None:
        return ""
    return str(v)


def _decl_rows(ctx: Context, spec: dict):
    ents = [e for e in ctx.ents.get(spec["entity"], []) if not e.data.get("deprecated")]
    rows = []
    for e in ents:
        rec = dict(e.data)
        rec["_derived"] = ctx.analysis["derived"].get(e.id, {})
        ok = True
        for k, v in (spec.get("filter") or {}).items():
            got = get_path(rec, k)
            allowed = v if isinstance(v, list) else [v]
            if isinstance(got, list):
                if not set(got) & set(allowed):
                    ok = False
            elif got not in allowed:
                ok = False
        if ok:
            rows.append(rec)
    for key in reversed(spec.get("sort") or ["id"]):
        rev = key.startswith("-")
        k = key.lstrip("-")
        rows.sort(key=lambda r: (get_path(r, k) is None, get_path(r, k) if get_path(r, k) is not None else 0), reverse=rev)
    if spec.get("limit"):
        rows = rows[: spec["limit"]]
    return rows


def table_md(ctx: Context, name: str, mode: str) -> str | None:
    if name in ctx.decl_tables:
        spec = ctx.decl_tables[name]
        if spec.get("kind") == "count-by":
            field = spec["field"]
            c = Counter()
            for e in ctx.ents.get(spec["entity"], []):
                if e.data.get("deprecated"):
                    continue
                v = get_path(e.data, field)
                for x in (v if isinstance(v, list) else [v]):
                    if x is not None:
                        c[x] += 1
            terms = vocab_terms(ctx.vocabs, spec.get("vocab", "")) if spec.get("vocab") else {}
            lines = [f"| {spec.get('label', field)} | {ctx.registry['types'][spec['entity']]['plural'].title()} |", "|---|---:|"]
            for k, n in sorted(c.items(), key=lambda x: (-x[1], str(x[0]))):
                lines.append(f"| {terms.get(str(k), {}).get('label', k)} | {n} |")
            return "\n".join(lines) + "\n"
        cols = spec["columns"]
        rows = _decl_rows(ctx, spec)
        headers = [c.get("label") if isinstance(c, dict) else c.split(".")[-1].replace("_", " ") for c in cols]
        paths = [c["path"] if isinstance(c, dict) else c for c in cols]
        lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in cols) + "|"]
        for r in rows:
            cells = []
            for p in paths:
                v = get_path(r, p)
                if p in ("name",):
                    cells.append(f"[{_fmt(v)}]({ctx.link_target(r['id'], mode)})")
                else:
                    cells.append(_cell_md(ctx, p, v, mode))
            lines.append("| " + " | ".join(cells) + " |")
        cap = f"\n*{spec['caption']}*\n" if spec.get("caption") else ""
        return "\n".join(lines) + "\n" + cap
    t = ctx.analysis["tables"].get(name)
    if t is None:
        return None
    link_cols = set(t.get("link_columns", []))
    lines = ["| " + " | ".join(c.replace("_", " ") for c in t["columns"]) + " |", "|" + "|".join("---" for _ in t["columns"]) + "|"]
    for r in t["rows"]:
        cells = []
        for c in t["columns"]:
            v = r.get(c)
            if c in link_cols:
                vals = v if isinstance(v, list) else [v]
                cells.append(", ".join(f"[{ctx.label(x)}]({ctx.link_target(x, mode)})" if x in ctx.by_id else _fmt(x) for x in vals))
            else:
                cells.append(_cell_md(ctx, c, v, mode))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + f"\n\n*{t['description']}*\n"


def _cell_md(ctx, path, v, mode):
    s = _fmt(v)
    return s.replace("|", "\\|").replace("\n", " ")


def render(text: str, ctx: Context, mode: str = "paper") -> tuple[str, list[tuple[str, str]]]:
    errors: list[tuple[str, str]] = []
    a = ctx.analysis

    def tok(m):
        kind, arg = m.group(1), m.group(2).strip()
        if kind == "count":
            if arg.startswith("edge:"):
                et = arg[5:]
                if et not in vocab_terms(ctx.vocabs, "edge_types"):
                    errors.append(("E019", f"unknown edge type in {m.group(0)}"))
                    return m.group(0)
                return str(ctx.edge_counts.get(et, 0))
            if arg not in ctx.registry["types"]:
                errors.append(("E019", f"unknown type in {m.group(0)}"))
                return m.group(0)
            return str(sum(1 for e in ctx.ents.get(arg, []) if not e.data.get("deprecated")))
        if kind == "stat":
            if arg not in a["stats"]:
                errors.append(("E019", f"unknown stat {m.group(0)}"))
                return m.group(0)
            return _fmt(a["stats"][arg])
        if kind == "table":
            md = table_md(ctx, arg, mode)
            if md is None:
                errors.append(("E019", f"unknown table {m.group(0)}"))
                return m.group(0)
            return "\n" + md
        if kind == "figure":
            f = a["figures"].get(arg)
            if f is None:
                errors.append(("E019", f"unknown figure {m.group(0)}"))
                return m.group(0)
            return f"\n![{f['caption']}](figures/{arg}.svg)\n\n*Figure: {f['caption']}*\n"
        if kind == "vocab":
            vname, _, term = arg.partition(":")
            t = vocab_terms(ctx.vocabs, vname).get(term)
            if not t:
                errors.append(("E019", f"unknown vocab term {m.group(0)}"))
                return m.group(0)
            return t["label"]
        errors.append(("E019", f"unknown token kind {m.group(0)}"))
        return m.group(0)

    def link(m):
        eid, txt = m.group(1), m.group(2)
        if eid not in ctx.by_id:
            errors.append(("E020", f"unresolved link [[{eid}]]"))
            return m.group(0)
        return f"[{txt or ctx.label(eid)}]({ctx.link_target(eid, mode)})"

    def cite(m):
        ids = [x.strip()[1:] for x in m.group(1).split(";")]
        parts = []
        for sid in ids:
            if sid not in ctx.by_id:
                errors.append(("E020", f"unresolved citation @{sid}"))
                parts.append(sid)
                continue
            if sid not in ctx.citations:
                ctx.citations.append(sid)
            n = ctx.citations.index(sid) + 1
            parts.append(f"[{n}](#ref-{sid})" if mode != "wiki" else f"[{n}](../source/{sid}.md)")
        return "[" + ", ".join(parts) + "]"

    out = TOKEN_RE.sub(tok, text)
    out = LINK_RE.sub(link, out)
    out = CITE_RE.sub(cite, out)
    return out, errors


def literal_stats(text: str) -> list[str]:
    hits = []
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        clean = TOKEN_RE.sub("", line)
        for m in LITERAL_STAT_RE.finditer(clean):
            hits.append(m.group(0))
    return hits
