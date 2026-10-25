"""Checks that need the analysis: report prose (E019-E021, E029), entity assertions (E032), cluster k drift (W107).

Called by validate.py once data is valid.
"""
from __future__ import annotations

from lib import ROOT, extract_edges, load_entities, load_registry, load_schemas, load_vocabs
import analyze
from report_render import Context, evaluate_assertion, literal_stats, render


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
    for t, lst in ents.items():
        if t == "run":
            continue
        for e in lst:
            for i, expr in enumerate(e.data.get("assertions") or []):
                status, msg = evaluate_assertion(expr, analysis, ctx.by_id)
                if status != "ok":
                    F.add("E032", e.path, f"assertion '{expr}' {'is malformed' if status == 'malformed' else 'failed'}: {msg}; the entity's text no longer matches the data", f"assertions/{i}")
    st = analysis["stats"]
    if st.get("cluster_k_drift"):
        F.add("W107", ROOT / "report" / "analysis.yaml", f"the stability rule now clearly favours k={st['cluster_rule_k']} over the configured k={st['cluster_k']} (beyond the {st.get('cluster_drift_tolerance')} tolerance)", "clustering.k")
