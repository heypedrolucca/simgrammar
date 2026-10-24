#!/usr/bin/env python3
"""Search ids, names, aliases, and summaries before creating anything (prevents duplicates).

  python scripts/find.py "needs decay"
  python scripts/find.py traffic --type mechanic
"""
from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import load_entities  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--list", metavar="TYPE", help="print a compact index of every entity of TYPE (id | group | summary)")
    ap.add_argument("--type")
    ap.add_argument("-n", type=int, default=15)
    args = ap.parse_args()
    if args.list:
        ents, _ = load_entities()
        grp = {"game": "subgenre", "mechanic": "family", "technique": "category", "opportunity": "opportunity_type", "source": "kind"}.get(args.list, "type")
        for e in sorted(ents.get(args.list, []), key=lambda e: e.id):
            extra = f" ({e.data.get('year')})" if args.list in ("game", "technique") else ""
            print(f"{e.id}{extra} | {e.data.get(grp)} | {e.data.get('summary')}")
        return
    q = args.query.lower()
    qtok = set(q.replace("-", " ").split())
    ents, _ = load_entities()
    scored = []
    for t, lst in ents.items():
        if t == "run" or (args.type and t != args.type):
            continue
        for e in lst:
            hay = " ".join([e.id.replace("-", " "), str(e.data.get("name", "")), " ".join(e.data.get("aliases", []) or []),
                            str(e.data.get("summary", "")), str(e.data.get("definition", "")), str(e.data.get("design_notes", ""))]).lower()
            s = difflib.SequenceMatcher(None, q, e.id.replace("-", " ")).ratio()
            s += difflib.SequenceMatcher(None, q, str(e.data.get("name", "")).lower()).ratio()
            s += 0.6 * len(qtok & set(hay.replace("-", " ").split())) / max(len(qtok), 1)
            if q in hay:
                s += 1
            scored.append((s, t, e.id, e.data.get("name", ""), e.data.get("summary", "")))
    scored.sort(key=lambda x: -x[0])
    if not scored or scored[0][0] < 1.3:
        print("No strong match (best score below 1.3). Scores near 1.0 are string similarity only; read the candidates before assuming a duplicate.")
    for s, t, i, n, summ in scored[: args.n]:
        print(f"{s:4.2f}  {t:<11} {i:<40} {n}  —  {str(summ)[:90]}")


if __name__ == "__main__":
    main()
