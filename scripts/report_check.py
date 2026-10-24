"""Report checks (E019-E021). Called by validate.py once data is valid."""
from __future__ import annotations

from lib import ROOT, extract_edges, load_entities, load_registry, load_schemas, load_vocabs
import analyze
from report_render import Context, literal_stats, render


def check(F) -> None:
    registry = load_registry()
    vocabs = load_vocabs()
    schemas = load_schemas()
    ents, _ = load_entities(registry)
    edges = [ed for t, lst in ents.items() if t != "run" for e in lst for ed in extract_edges(e, schemas, registry)]
    analysis = analyze.compute(ents, edges, vocabs)
    ctx = Context(ents, edges, analysis, vocabs, registry)
    for p in sorted((ROOT / "report" / "src").glob("*.md")):
        text = p.read_text(encoding="utf-8")
        _, errs = render(text, ctx, "paper")
        for rule, msg in errs:
            F.add(rule, p, msg)
        for hit in literal_stats(text):
            F.add("E021", p, f"literal dataset count '{hit}'")
