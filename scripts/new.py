#!/usr/bin/env python3
"""Scaffold a run record or an entity from its schema. Placeholders contain TODO and fail E027 until filled.

  python scripts/new.py run <slug> --actor agent --operator yoheinakajima --model claude-opus-5-5 --purpose "..."
  python scripts/new.py game <id> --run <run-id>
  python scripts/new.py mechanic <id> --run <run-id>
  python scripts/new.py technique|opportunity|source <id> --run <run-id>
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ID_RE, ROOT, dump_yaml, load_registry  # noqa: E402

TEMPLATES = {
    "game": {
        "name": "TODO", "summary": "TODO one sentence", "year": "TODO", "developer": "TODO", "platforms": ["pc"],
        "subgenre": "TODO", "sim_domain": ["TODO"], "player_role": "TODO", "agency_model": ["TODO"], "time_model": "TODO",
        "sim_scale": "TODO", "fidelity": "TODO", "perspective": "TODO", "win_structure": "TODO", "failure_model": "TODO",
        "narrative_mode": "TODO", "multiplayer": ["single"], "modding": "TODO", "production_tier": "TODO", "agent_count_order": "TODO",
        "emergence": "TODO", "influence": "TODO", "core_loop": "TODO a -> b -> c", "mechanics": [{"id": "TODO", "role": "core", "note": "TODO"}],
        "sources": [], "status": "asserted",
    },
    "mechanic": {
        "name": "TODO", "summary": "TODO one sentence", "family": "TODO", "substrate": ["TODO"], "definition": "TODO",
        "player_experience": "TODO", "design_levers": ["TODO", "TODO 2"], "failure_modes": ["TODO"], "dynamics": ["TODO"],
        "math_basis": ["TODO"], "feedback": "TODO", "player_interface": ["TODO"], "legibility": "TODO", "emergence_potential": "TODO",
        "authoring_cost": "TODO", "compute_cost": "TODO", "tuning_difficulty": "TODO", "ai_leverage": "TODO", "maturity": "TODO", "sources": [], "status": "asserted",
    },
    "technique": {
        "name": "TODO", "summary": "TODO one sentence", "category": "TODO", "year": "TODO", "mechanism": "TODO",
        "key_results": [{"text": "TODO", "sources": ["src-TODO"], "confidence": "medium"}], "maturity": "TODO", "trl": "TODO",
        "runtime": ["TODO"], "determinism_impact": "TODO", "horizon": "TODO", "risks": ["TODO"],
        "affects": [{"id": "TODO", "effect": "TODO", "note": "TODO"}], "limitations": ["TODO"], "sources": ["src-TODO"], "status": "sourced",
    },
    "opportunity": {
        "name": "TODO", "summary": "TODO one sentence", "opportunity_type": "TODO", "thesis": "TODO", "design_sketch": "TODO",
        "involves": ["TODO"], "applies": [], "precedent": [], "novelty": "TODO", "feasibility": "TODO", "impact": "TODO", "horizon": "TODO",
        "key_risks": ["TODO"], "validation_experiment": "TODO",
        "falsifiable_signal": {"prediction": "TODO", "resolve_by": "2028-12-31", "criteria": "TODO"}, "sources": [], "status": "asserted",
    },
    "source": {"name": "TODO", "kind": "TODO", "authors": [], "date": "TODO", "url": "https://TODO", "accessed": dt.date.today().isoformat()},
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("type")
    ap.add_argument("id")
    ap.add_argument("--run")
    ap.add_argument("--actor", default="agent")
    ap.add_argument("--operator", default="TODO")
    ap.add_argument("--model", default="")
    ap.add_argument("--harness", default="")
    ap.add_argument("--purpose", default="TODO")
    args = ap.parse_args()
    reg = load_registry()
    if args.type not in reg["types"]:
        raise SystemExit(f"unknown type {args.type}; one of {list(reg['types'])}")
    spec = reg["types"][args.type]
    if args.type == "run":
        rid = f"{dt.date.today().isoformat()}-{args.id}"
        data = {"id": rid, "type": "run", "date": dt.date.today().isoformat(), "actor": args.actor, "operator": args.operator}
        if args.model or args.harness:
            data["agent"] = {k: v for k, v in (("model", args.model), ("harness", args.harness)) if v}
        data.update({"purpose": args.purpose, "method": "TODO", "contract_version": reg["contract_version"], "proposals": []})
        eid = rid
    else:
        eid = args.id
        if args.type == "source" and not eid.startswith("src-"):
            raise SystemExit("source ids start with src-")
        if not ID_RE.match(eid):
            raise SystemExit("id must be kebab-case")
        if not args.run:
            raise SystemExit("--run <run-id> is required for entities")
        data = {"id": eid, "type": args.type, **TEMPLATES[args.type], "provenance": {"created": args.run}}
    path = ROOT / spec["dir"] / f"{eid}.yaml"
    if path.exists():
        raise SystemExit(f"{path.relative_to(ROOT)} already exists")
    path.write_text(dump_yaml(data), encoding="utf-8")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
