"""Deterministic analysis over the entity graph.

compute() returns:
  derived: {entity_id: {field: value}}      -> attached to entities as `_derived` in projections
  stats:   {name: number|string}            -> {{stat:name}} tokens
  tables:  {name: {"columns": [...], "rows": [...], "description": str}}  -> {{table:name}}
  figures: {name: {"svg": str, "caption": str}}  -> {{figure:name}}
Never stores anything back into data/. Same inputs -> byte-identical outputs.
"""
from __future__ import annotations

import math
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import squareform
from scipy.stats import spearmanr

from lib import ROOT, read_yaml, vocab_terms

MATURITY_ORDER = ["research", "prototype", "shipped-niche", "shipped-mainstream"]


def _r(x, n=3):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return None
    return round(float(x), n)


def compute(ents: dict, edges: list, vocabs: dict) -> dict:
    cfg = read_yaml(ROOT / "report" / "analysis.yaml")
    rub = vocabs["rubrics"]
    live = {t: [e for e in lst if not e.data.get("deprecated")] for t, lst in ents.items() if t != "run"}
    by_id = {e.id: e for lst in live.values() for e in lst}
    games = sorted(live.get("game", []), key=lambda e: e.id)
    mechs = sorted(live.get("mechanic", []), key=lambda e: e.id)
    techs = sorted(live.get("technique", []), key=lambda e: e.id)
    opps = sorted(live.get("opportunity", []), key=lambda e: e.id)
    fam_terms = vocab_terms(vocabs, "mechanic_family")
    sub_terms = vocab_terms(vocabs, "subgenre")
    derived: dict[str, dict] = defaultdict(dict)
    stats: dict[str, object] = {}
    tables: dict[str, dict] = {}
    figures: dict[str, dict] = {}

    # ---------------- inverse edges (computed, never stored)
    inverse = vocab_terms(vocabs, "edge_types")
    incoming: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    outgoing: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    for ed in edges:
        if ed.source not in by_id or ed.target not in by_id:
            continue
        et = inverse[ed.type]
        outgoing[ed.source][ed.type].append(ed.target)
        inv = et["inverse"]
        if et.get("symmetric"):
            outgoing[ed.target][ed.type].append(ed.source)
        else:
            incoming[ed.target][inv].append(ed.source)
    for eid in by_id:
        if incoming.get(eid):
            derived[eid]["incoming"] = {k: sorted(set(v)) for k, v in sorted(incoming[eid].items())}

    # ---------------- game x mechanic
    N = len(games)
    gm: dict[str, dict[str, str]] = {g.id: {m["id"]: m["role"] for m in g.data.get("mechanics", []) if m["id"] in by_id} for g in games}
    mech_games: dict[str, list[str]] = defaultdict(list)
    for gid, ms in gm.items():
        for mid in ms:
            mech_games[mid].append(gid)
    year = {g.id: g.data.get("year") for g in games}

    for g in games:
        ms = gm[g.id]
        fam = Counter(by_id[m].data.get("family") for m in ms)
        derived[g.id].update({
            "mechanic_count": len(ms),
            "core_count": sum(1 for r in ms.values() if r == "core"),
            "family_profile": dict(sorted(fam.items())),
        })

    for m in mechs:
        gl = sorted(mech_games.get(m.id, []), key=lambda gid: (year.get(gid) or 9999, gid))
        core = [gid for gid in gl if gm[gid][m.id] == "core"]
        derived[m.id].update({
            "prevalence": len(gl),
            "prevalence_share": _r(len(gl) / N) if N else 0,
            "core_count": len(core),
            "earliest_year": year.get(gl[0]) if gl else None,
            "earliest_game": gl[0] if gl else None,
            "subgenre_spread": len({by_id[g].data.get("subgenre") for g in gl}),
        })

    # ---------------- technique exposure per mechanic
    comp = rub["composites"]["technique_exposure"]
    exposure = defaultdict(float)
    tech_on_mech = defaultdict(list)
    for t in techs:
        mw = comp["maturity_weights"][t.data.get("maturity")]
        for a in t.data.get("affects", []):
            if a["id"] in by_id:
                exposure[a["id"]] += mw * comp["effect_weights"][a["effect"]]
                tech_on_mech[a["id"]].append(t.id)
        fams = Counter(by_id[a["id"]].data.get("family") for a in t.data.get("affects", []) if a["id"] in by_id)
        derived[t.id].update({
            "affects_count": len(t.data.get("affects", [])),
            "families_affected": dict(sorted(fams.items())),
        })
    for m in mechs:
        derived[m.id]["technique_exposure"] = _r(exposure.get(m.id, 0.0))
        derived[m.id]["technique_count"] = len(set(tech_on_mech.get(m.id, [])))

    # ---------------- opportunity priority
    w = rub["composites"]["opportunity_priority"]["weights"]
    for o in opps:
        d = o.data
        pr = (d["impact"] ** w["w_impact"]) * (d["feasibility"] ** w["w_feasibility"]) * (d["novelty"] ** w["w_novelty"])
        derived[o.id]["priority"] = _r(pr)

    # ---------------- stats: counts
    for t, lst in live.items():
        stats[f"n_{t}"] = len(lst)
    stats["n_edges"] = len(edges)
    stats["n_uses_edges"] = sum(len(v) for v in gm.values())
    mc = [derived[g.id]["mechanic_count"] for g in games] or [0]
    stats["mean_mechanics_per_game"] = _r(float(np.mean(mc)), 1)
    stats["median_mechanics_per_game"] = _r(float(np.median(mc)), 1)
    yrs = [y for y in year.values() if isinstance(y, int)]
    stats["year_min"] = min(yrs) if yrs else None
    stats["year_max"] = max(yrs) if yrs else None
    stats["n_boundary_cases"] = sum(1 for g in games if g.data.get("boundary_case"))
    stats["n_sourced_or_verified"] = sum(1 for lst in live.values() for e in lst if e.data.get("status") in ("sourced", "verified"))
    stats["n_asserted"] = sum(1 for lst in live.values() for e in lst if e.data.get("status") == "asserted")
    stats["n_families"] = len({m.data.get("family") for m in mechs})
    stats["n_subgenres"] = len({g.data.get("subgenre") for g in games})
    if mechs:
        top = max(mechs, key=lambda m: (derived[m.id]["prevalence"], m.id))
        stats["most_prevalent_mechanic"] = top.data["name"]
        stats["most_prevalent_mechanic_share_pct"] = _r(100 * derived[top.id]["prevalence"] / max(N, 1), 0)
        stats["n_mechanics_single_game"] = sum(1 for m in mechs if derived[m.id]["prevalence"] == 1)
        stats["n_mechanics_unused"] = sum(1 for m in mechs if derived[m.id]["prevalence"] == 0)

    # ---------------- correlations across mechanics (Spearman)
    def corr(a, b):
        xs = [m.data[a] for m in mechs]
        ys = [m.data[b] for m in mechs]
        if len(set(xs)) < 2 or len(set(ys)) < 2:
            return None, None
        r, p = spearmanr(xs, ys)
        return _r(r, 2), p

    for a, b in [("legibility", "emergence_potential"), ("authoring_cost", "ai_leverage"), ("legibility", "compute_cost"),
                 ("emergence_potential", "tuning_difficulty"), ("legibility", "ai_leverage")]:
        r, p = corr(a, b)
        stats[f"rho_{a}_{b}"] = r
        stats[f"p_{a}_{b}"] = ("<0.001" if p is not None and p < 0.001 else (_r(p, 3) if p is not None else None))
    if mechs and techs:
        xs = [m.data["ai_leverage"] for m in mechs]
        ys = [derived[m.id]["technique_exposure"] for m in mechs]
        if len(set(ys)) > 1:
            r, _ = spearmanr(xs, ys)
            stats["rho_ai_leverage_exposure"] = _r(r, 2)

    # ---------------- co-occurrence
    mids = [m.id for m in mechs if derived[m.id]["prevalence"] > 0]
    sets = {gid: set(ms) for gid, ms in gm.items()}
    pair_count = Counter()
    for gid, s in sets.items():
        for a, b in combinations(sorted(s), 2):
            pair_count[(a, b)] += 1
    prev = {m: derived[m]["prevalence"] for m in mids}
    tension_pairs = {tuple(sorted((ed.source, ed.target))) for ed in edges if ed.type == "tension"}
    rows = []
    for (a, b), c in pair_count.items():
        if c < cfg["cooccurrence"]["min_support"]:
            continue
        lift = c * N / (prev[a] * prev[b])
        rows.append({"mechanic_a": a, "mechanic_b": b, "games": c, "lift": _r(lift, 2),
                     "jaccard": _r(c / (prev[a] + prev[b] - c), 3)})
    rows.sort(key=lambda r: (-r["lift"], -r["games"], r["mechanic_a"], r["mechanic_b"]))
    tables["cooccurrence-top"] = {"description": f"Mechanic pairs ranked by lift (observed / expected co-occurrence across games), support >= {cfg['cooccurrence']['min_support']} games.",
                                  "columns": ["mechanic_a", "mechanic_b", "games", "lift", "jaccard"], "rows": rows[: cfg["cooccurrence"]["top_n"]], "link_columns": ["mechanic_a", "mechanic_b"]}
    tables["cooccurrence-all"] = {"description": "All pairs meeting support.", "columns": ["mechanic_a", "mechanic_b", "games", "lift", "jaccard"], "rows": rows, "link_columns": ["mechanic_a", "mechanic_b"]}
    stats["n_cooccurring_pairs"] = len(pair_count)
    stats["n_possible_pairs"] = len(mids) * (len(mids) - 1) // 2
    stats["pair_coverage_pct"] = _r(100 * len(pair_count) / max(stats["n_possible_pairs"], 1), 1)

    # ---------------- white space: common mechanics that rarely meet
    ws = cfg["whitespace"]
    thr = ws["min_prevalence_share"] * N
    common = [m for m in mids if prev[m] >= thr]
    wrows = []
    for a, b in combinations(sorted(common), 2):
        if ws["exclude_same_family"] and by_id[a].data["family"] == by_id[b].data["family"]:
            continue
        if (a, b) in tension_pairs:
            continue
        obs = pair_count.get((a, b), 0)
        if obs > ws["max_observed"]:
            continue
        expected = prev[a] * prev[b] / N
        wrows.append({"mechanic_a": a, "mechanic_b": b, "family_a": by_id[a].data["family"], "family_b": by_id[b].data["family"],
                      "observed": obs, "expected": _r(expected, 2), "gap": _r(expected - obs, 2)})
    wrows.sort(key=lambda r: (-r["gap"], r["mechanic_a"], r["mechanic_b"]))
    tables["whitespace"] = {"description": f"Pairs of common mechanics (each in >= {int(ws['min_prevalence_share']*100)}% of games, different families, not marked as tension) that co-occur at most {ws['max_observed']} time(s). Gap = expected - observed co-occurrence under independence.",
                            "columns": ["mechanic_a", "mechanic_b", "family_a", "family_b", "observed", "expected", "gap"], "rows": wrows[: ws["top_n"]], "link_columns": ["mechanic_a", "mechanic_b"]}
    stats["n_whitespace_pairs"] = len(wrows)
    stats["n_common_mechanics"] = len(common)

    # ---------------- clustering games by weighted mechanic sets (weighted Jaccard)
    cl = cfg["clustering"]
    if N >= cl["k"] and mids:
        idx = {m: i for i, m in enumerate(mids)}
        X = np.zeros((N, len(mids)))
        for gi, g in enumerate(games):
            for mid, role in gm[g.id].items():
                if mid in idx:
                    X[gi, idx[mid]] = cl["core_weight"] if role == "core" else 1.0
        D = np.zeros((N, N))
        for i in range(N):
            for j in range(i + 1, N):
                mn = np.minimum(X[i], X[j]).sum()
                mx = np.maximum(X[i], X[j]).sum()
                d = 1 - (mn / mx if mx else 0)
                D[i, j] = D[j, i] = d
        Z = linkage(squareform(D, checks=False), method="average")
        labels = fcluster(Z, t=cl["k"], criterion="maxclust")
        clusters = defaultdict(list)
        for g, lab in zip(games, labels):
            clusters[int(lab)].append(g)
        crow = []
        ordered = sorted(clusters.values(), key=lambda gs: (-len(gs), min(x.id for x in gs)))
        for ci, members in enumerate(ordered, start=1):
            cnt = Counter(mid for g in members for mid in gm[g.id])
            scored = []
            for mid, c in cnt.items():
                share_in = c / len(members)
                share_all = prev[mid] / N
                scored.append((share_in * math.log((share_in + 1e-9) / (share_all + 1e-9) + 1), mid))
            scored.sort(key=lambda x: (-x[0], x[1]))
            topm = [mid for _, mid in scored[: cl["top_mechanics_per_cluster"]]]
            subs = Counter(g.data.get("subgenre") for g in members).most_common(2)
            label = " + ".join(by_id[m].data["name"] for m in topm[:2])
            for g in members:
                derived[g.id]["cluster"] = f"C{ci:02d}"
            crow.append({"cluster": f"C{ci:02d}", "label": label, "size": len(members),
                         "dominant_subgenres": ", ".join(f"{sub_terms.get(s, {}).get('label', s)} ({n})" for s, n in subs),
                         "signature_mechanics": topm,
                         "members": sorted([g.id for g in members])})
        tables["game-clusters"] = {"description": f"Games clustered by weighted Jaccard similarity of mechanic sets (average linkage, k={cl['k']}, core weight {cl['core_weight']}). Signature mechanics maximize within-cluster share x log-lift.",
                                   "columns": ["cluster", "label", "size", "dominant_subgenres", "signature_mechanics", "members"], "rows": crow,
                                   "link_columns": ["signature_mechanics", "members"]}
        # how often clusters cut across subgenres
        cross = sum(1 for r in crow if len(set(by_id[g].data.get("subgenre") for g in r["members"])) > 1)
        stats["n_clusters"] = len(crow)
        stats["n_clusters_cross_subgenre"] = cross

    # ---------------- family x subgenre
    fam_ids = list(fam_terms)
    subs_used = sorted({g.data.get("subgenre") for g in games}, key=lambda s: list(sub_terms).index(s) if s in sub_terms else 999)
    mat = {s: Counter() for s in subs_used}
    for g in games:
        for mid in gm[g.id]:
            mat[g.data["subgenre"]][by_id[mid].data["family"]] += 1
    frows = []
    for s in subs_used:
        tot = sum(mat[s].values()) or 1
        row = {"subgenre": s, "games": sum(1 for g in games if g.data["subgenre"] == s)}
        for f in fam_ids:
            row[f] = _r(mat[s][f] / tot, 2)
        frows.append(row)
    tables["family-by-subgenre"] = {"description": "Share of each subgenre's mechanic uses falling in each mechanic family (rows sum to 1).",
                                    "columns": ["subgenre", "games"] + fam_ids, "rows": frows}

    # ---------------- family summaries
    famrows = []
    for f in fam_ids:
        ms = [m for m in mechs if m.data["family"] == f]
        if not ms:
            continue
        famrows.append({
            "family": f,
            "mechanics": len(ms),
            "uses": sum(derived[m.id]["prevalence"] for m in ms),
            "mean_legibility": _r(np.mean([m.data["legibility"] for m in ms]), 2),
            "mean_emergence": _r(np.mean([m.data["emergence_potential"] for m in ms]), 2),
            "mean_authoring_cost": _r(np.mean([m.data["authoring_cost"] for m in ms]), 2),
            "mean_ai_leverage": _r(np.mean([m.data["ai_leverage"] for m in ms]), 2),
            "technique_exposure": _r(sum(derived[m.id]["technique_exposure"] for m in ms), 2),
        })
    famrows.sort(key=lambda r: (-r["technique_exposure"], r["family"]))
    tables["family-summary"] = {"description": "Per mechanic family: size, total game uses, mean rubric scores, and summed technique exposure (maturity x effect weights from vocab/rubrics.yaml).",
                                "columns": ["family", "mechanics", "uses", "mean_legibility", "mean_emergence", "mean_authoring_cost", "mean_ai_leverage", "technique_exposure"], "rows": famrows}
    if famrows and famrows[0]["technique_exposure"] > 0:
        stats["top_exposed_family"] = fam_terms[famrows[0]["family"]]["label"]
        stats["least_exposed_family"] = fam_terms[famrows[-1]["family"]]["label"]

    # ---------------- AI leverage gap: high judged leverage but low current technique exposure
    gap_rows = []
    if techs:
        max_exp = max(derived[m.id]["technique_exposure"] for m in mechs) or 1
        for m in mechs:
            gap_rows.append({"mechanic": m.id, "family": m.data["family"], "ai_leverage": m.data["ai_leverage"],
                             "technique_exposure": derived[m.id]["technique_exposure"], "prevalence": derived[m.id]["prevalence"],
                             "gap": _r(m.data["ai_leverage"] / 5 - derived[m.id]["technique_exposure"] / max_exp, 3)})
        gap_rows.sort(key=lambda r: (-r["gap"], -r["prevalence"], r["mechanic"]))
    tables["leverage-gap"] = {"description": "Mechanics where expert-judged AI leverage outruns the techniques currently linked to them (normalized). High gap = under-researched opportunity or missing technique links.",
                              "columns": ["mechanic", "family", "ai_leverage", "technique_exposure", "prevalence", "gap"], "rows": gap_rows[:25], "link_columns": ["mechanic"]}
    exp_rows = sorted(({"mechanic": m.id, "family": m.data["family"], "technique_exposure": derived[m.id]["technique_exposure"],
                        "technique_count": derived[m.id]["technique_count"], "prevalence": derived[m.id]["prevalence"]} for m in mechs),
                      key=lambda r: (-r["technique_exposure"], -r["prevalence"], r["mechanic"]))
    tables["most-exposed-mechanics"] = {"description": "Mechanics most affected by the technique set.", "columns": ["mechanic", "family", "technique_exposure", "technique_count", "prevalence"],
                                        "rows": exp_rows[:25], "link_columns": ["mechanic"]}

    # ---------------- technique x family matrix
    trows = []
    for t in techs:
        row = {"technique": t.id, "category": t.data["category"], "maturity": t.data["maturity"], "trl": t.data["trl"], "horizon": t.data["horizon"]}
        fp = derived[t.id]["families_affected"]
        row["families"] = ", ".join(f"{fam_terms[f]['label']} ({n})" for f, n in sorted(fp.items(), key=lambda x: (-x[1], x[0])))
        trows.append(row)
    trows.sort(key=lambda r: (-MATURITY_ORDER.index(r["maturity"]), -r["trl"], r["technique"]))
    tables["technique-landscape"] = {"description": "Techniques ordered by game-deployment maturity and TRL, with mechanic families they affect.",
                                     "columns": ["technique", "category", "maturity", "trl", "horizon", "families"], "rows": trows, "link_columns": ["technique"]}
    zero = [m for m in mechs if derived[m.id]["technique_exposure"] == 0]
    stats["n_mechanics_zero_exposure"] = len(zero)
    total_uses = sum(derived[m.id]["prevalence"] for m in mechs) or 1
    stats["pct_uses_on_zero_exposure"] = _r(100 * sum(derived[m.id]["prevalence"] for m in zero) / total_uses, 0)
    top10 = sorted(mechs, key=lambda m: (-derived[m.id]["prevalence"], m.id))[:10]
    stats["n_top10_prevalent_zero_exposure"] = sum(1 for m in top10 if derived[m.id]["technique_exposure"] == 0)
    early = [derived[m.id]["earliest_year"] for m in mechs if derived[m.id]["earliest_year"]]
    stats["pct_mechanics_seen_by_2000"] = _r(100 * sum(1 for y in early if y <= 2000) / max(len(early), 1), 0)
    eff = Counter(a["effect"] for t in techs for a in t.data.get("affects", []))
    for k in vocab_terms(vocabs, "effect"):
        stats[f"n_effect_{k.replace('-', '_')}"] = eff.get(k, 0)
    tables["effect-distribution"] = {"description": "How techniques change mechanics, by effect type.", "columns": ["effect", "edges"],
                                     "rows": [{"effect": k, "edges": v} for k, v in sorted(eff.items(), key=lambda x: (-x[1], x[0]))]}
    if eff:
        stats["top_effect"] = vocab_terms(vocabs, "effect")[eff.most_common(1)[0][0]]["label"]
        stats["rarest_effect"] = vocab_terms(vocabs, "effect")[min(eff.items(), key=lambda x: (x[1], x[0]))[0]]["label"]
        stats["n_affects_edges"] = sum(eff.values())
    mat_counts = Counter(t.data["maturity"] for t in techs)
    for k in MATURITY_ORDER:
        stats[f"n_technique_{k.replace('-', '_')}"] = mat_counts.get(k, 0)
    det = Counter(t.data["determinism_impact"] for t in techs)
    stats["n_technique_breaks_determinism"] = det.get("breaks", 0)

    # ---------------- opportunities ranked
    orows = sorted(({"opportunity": o.id, "type": o.data["opportunity_type"], "priority": derived[o.id]["priority"], "impact": o.data["impact"],
                     "feasibility": o.data["feasibility"], "novelty": o.data["novelty"], "horizon": o.data["horizon"]} for o in opps),
                   key=lambda r: (-r["priority"], r["opportunity"]))
    tables["opportunities-ranked"] = {"description": "Opportunities by composite priority (weighted geometric mean of impact, feasibility, novelty; weights in vocab/rubrics.yaml).",
                                      "columns": ["opportunity", "type", "priority", "impact", "feasibility", "novelty", "horizon"], "rows": orows, "link_columns": ["opportunity"]}
    if orows:
        stats["top_opportunity"] = by_id[orows[0]["opportunity"]].data["name"]
    stats["n_predictions"] = len(opps)
    res = sorted(o.data["falsifiable_signal"]["resolve_by"] for o in opps)
    stats["first_prediction_resolves"] = res[0] if res else None

    # ---------------- adoption over time
    by_decade = Counter()
    for m in mechs:
        y = derived[m.id]["earliest_year"]
        if y:
            by_decade[f"{(y // 10) * 10}s"] += 1
    tables["mechanic-origins-by-decade"] = {"description": "Mechanics by decade of earliest appearance in the dataset (a lower bound on true origin; dataset is a sample).",
                                            "columns": ["decade", "mechanics"], "rows": [{"decade": k, "mechanics": v} for k, v in sorted(by_decade.items())]}
    games_by_decade = Counter(f"{(y // 10) * 10}s" for y in yrs)
    tables["games-by-decade"] = {"description": "Games in the dataset by decade of first release.", "columns": ["decade", "games"],
                                 "rows": [{"decade": k, "games": v} for k, v in sorted(games_by_decade.items())]}

    # ---------------- verification queue
    q = []
    for t in ("technique", "game", "mechanic", "opportunity"):
        for e in sorted(live.get(t, []), key=lambda e: e.id):
            if e.data.get("status") == "asserted":
                q.append({"type": t, "id": e.id, "name": e.data.get("name")})
    tables["verification-queue"] = {"description": "Asserted entities awaiting sources, in triage order.", "columns": ["type", "id", "name"], "rows": q}

    # ---------------- figures
    figures.update(_figures(mechs, derived, fam_terms, famrows, by_id, games, year))
    return {"derived": {k: dict(sorted(v.items())) for k, v in sorted(derived.items())}, "stats": dict(sorted(stats.items())),
            "tables": tables, "figures": figures}


# ======================================================================= SVG
_FONT = "font-family='Helvetica, Arial, sans-serif'"


def _svg(w, h, body):
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' width='{w}' height='{h}' {_FONT} font-size='11'>"
            f"<rect width='{w}' height='{h}' fill='#ffffff'/>{body}</svg>\n")


def _esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&#39;")


def _figures(mechs, derived, fam_terms, famrows, by_id, games, year):
    figs = {}
    if not mechs:
        return figs
    # 1. legibility vs emergence, bubble = prevalence (deterministic jitter from id hash)
    W, H, L, B = 560, 460, 60, 50
    body = []
    for v in range(1, 6):
        x = L + (v - 0.5) * (W - L - 20) / 5
        y = H - B - (v - 0.5) * (H - B - 20) / 5
        body.append(f"<line x1='{x:.1f}' y1='20' x2='{x:.1f}' y2='{H-B}' stroke='#eee'/>")
        body.append(f"<line x1='{L}' y1='{y:.1f}' x2='{W-20}' y2='{y:.1f}' stroke='#eee'/>")
        body.append(f"<text x='{x:.1f}' y='{H-B+16}' text-anchor='middle'>{v}</text>")
        body.append(f"<text x='{L-10}' y='{y+4:.1f}' text-anchor='end'>{v}</text>")
    maxp = max(derived[m.id]["prevalence"] for m in mechs) or 1
    for m in sorted(mechs, key=lambda m: -derived[m.id]["prevalence"]):
        h = int(__import__("hashlib").md5(m.id.encode()).hexdigest(), 16)
        jx = ((h % 1000) / 1000 - 0.5) * 0.7
        jy = (((h // 1000) % 1000) / 1000 - 0.5) * 0.7
        x = L + (m.data["legibility"] - 0.5 + jx) * (W - L - 20) / 5
        y = H - B - (m.data["emergence_potential"] - 0.5 + jy) * (H - B - 20) / 5
        r = 2.5 + 9 * math.sqrt(derived[m.id]["prevalence"] / maxp)
        body.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='{r:.1f}' fill='#2f5d8a' fill-opacity='0.35' stroke='#2f5d8a' stroke-width='0.6'><title>{_esc(m.data['name'])}</title></circle>")
    body.append(f"<text x='{(W+L)/2:.0f}' y='{H-12}' text-anchor='middle' font-size='12'>Legibility (1 opaque - 5 transparent)</text>")
    body.append(f"<text transform='translate(16,{(H-B)/2:.0f}) rotate(-90)' text-anchor='middle' font-size='12'>Emergence potential</text>")
    figs["legibility-vs-emergence"] = {"svg": _svg(W, H, "".join(body)),
                                       "caption": "Each mechanic placed by rubric legibility (x) and emergence potential (y); area ~ number of games using it. Jitter is deterministic."}

    # 2. technique exposure by family (horizontal bars)
    rows = [r for r in famrows if r["technique_exposure"] > 0]
    if rows:
        W, rowh, L = 620, 22, 190
        H = 30 + rowh * len(rows) + 30
        mx = max(r["technique_exposure"] for r in rows)
        body = []
        for i, r in enumerate(rows):
            y = 20 + i * rowh
            wbar = (W - L - 60) * r["technique_exposure"] / mx
            body.append(f"<text x='{L-8}' y='{y+14}' text-anchor='end'>{_esc(fam_terms[r['family']]['label'])}</text>")
            body.append(f"<rect x='{L}' y='{y+3}' width='{wbar:.1f}' height='{rowh-7}' fill='#2f5d8a'/>")
            body.append(f"<text x='{L+wbar+6:.1f}' y='{y+14}'>{r['technique_exposure']}</text>")
        body.append(f"<text x='{L}' y='{H-8}' font-size='11' fill='#555'>Summed technique exposure (maturity x effect weights)</text>")
        figs["exposure-by-family"] = {"svg": _svg(W, H, "".join(body)), "caption": "Where current techniques concentrate: summed exposure of each family's mechanics."}

    # 3. cumulative mechanics by earliest year
    ys = sorted(derived[m.id]["earliest_year"] for m in mechs if derived[m.id]["earliest_year"])
    if ys:
        W, H, L, B = 620, 300, 50, 40
        y0, y1 = ys[0], max(ys[-1], ys[0] + 1)
        n = len(ys)
        pts = []
        for i, y in enumerate(ys, start=1):
            x = L + (y - y0) / (y1 - y0) * (W - L - 20)
            yy = H - B - i / n * (H - B - 20)
            pts.append(f"{x:.1f},{yy:.1f}")
        body = [f"<polyline points='{' '.join(pts)}' fill='none' stroke='#2f5d8a' stroke-width='2'/>"]
        for dec in range((y0 // 10) * 10, y1 + 1, 10):
            if dec < y0:
                continue
            x = L + (dec - y0) / (y1 - y0) * (W - L - 20)
            body.append(f"<line x1='{x:.1f}' y1='20' x2='{x:.1f}' y2='{H-B}' stroke='#eee'/><text x='{x:.1f}' y='{H-B+16}' text-anchor='middle'>{dec}</text>")
        body.append(f"<text x='{L-8}' y='{H-B}' text-anchor='end'>0</text><text x='{L-8}' y='26' text-anchor='end'>{n}</text>")
        body.append(f"<text x='{(W+L)/2:.0f}' y='{H-6}' text-anchor='middle' font-size='12'>Year of earliest dataset game using the mechanic</text>")
        figs["mechanic-accumulation"] = {"svg": _svg(W, H, "".join(body)),
                                         "caption": "Cumulative count of mechanics by first appearance in the dataset. Steps mark the years a design vocabulary expanded."}
    return figs
