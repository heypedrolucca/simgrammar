#!/usr/bin/env python3
"""Rater calibration for mechanic rubric scores (E036).

Before a run creates mechanics or adds mechanic `ratings`, its rater scores the frozen calibration set blind:

  python scripts/calibrate.py sheet > /tmp/sheet.yaml        # definitions and anchors, no stored scores
  (fill every null with an anchor level, reading only the sheet)
  python scripts/calibrate.py score /tmp/sheet.yaml           # agreement with the frozen set
  python scripts/calibrate.py score /tmp/sheet.yaml --write-run <run-id>   # record the scores in the run file

The run file keeps the raw scores, never the agreement numbers; the validator and the build compute agreement from
them, so a recorded calibration cannot drift from what it claims. Do the sheet before opening data/mechanics/: the
check is only as blind as the rater makes it.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import (  # noqa: E402
    CALIBRATION_SCALES,
    ROOT,
    calibration_agreement,
    dump_yaml,
    load_calibration,
    load_registry,
    load_vocabs,
    read_yaml,
)


def sheet() -> str:
    reg = load_registry()
    cal = load_calibration(reg)
    rub = load_vocabs()["rubrics"]["scales"]
    out = {
        "set": cal["id"],
        "instructions": ("Score each mechanic on each scale by matching the anchor text below; between two anchors take the lower. "
                         "Use only this sheet. Do not open data/mechanics/ or the website until you have scored every row."),
        "anchors": {s: {"question": rub[s]["question"], "levels": {int(k): v for k, v in rub[s]["levels"].items()}} for s in CALIBRATION_SCALES},
        "mechanics": {},
    }
    for mid in sorted(cal["mechanics"]):
        d = read_yaml(ROOT / "data" / "mechanics" / f"{mid}.yaml")
        out["mechanics"][mid] = {
            "name": d["name"], "summary": d["summary"], "definition": " ".join(d["definition"].split()),
            "player_experience": " ".join(d["player_experience"].split()), "design_levers": d.get("design_levers", []),
            "scores": {s: None for s in CALIBRATION_SCALES},
        }
    return dump_yaml(out)


def score(path: Path, write_run: str | None) -> int:
    reg = load_registry()
    cal = load_calibration(reg)
    filled = read_yaml(path)
    scores = {mid: {s: v for s, v in (row.get("scores") or {}).items() if v is not None} for mid, row in (filled.get("mechanics") or {}).items()}
    gold = cal["mechanics"]
    ag = calibration_agreement(gold, scores)
    thr = (reg.get("contribution") or {}).get("calibration_min_within_one", 0.8)
    print(f"set {cal['id']}: {ag['n']} scores, {ag['missing']} missing")
    print(f"exact {ag['exact']}  within-one {ag['within_one']}  quadratic kappa {ag['kappa_quadratic']}  (threshold within-one >= {thr})")
    for s in CALIBRATION_SCALES:
        one = calibration_agreement({m: {s: g[s]} for m, g in gold.items()}, scores)
        print(f"  {s:20s} exact {one['exact']}  within-one {one['within_one']}")
    ok = ag["within_one"] is not None and ag["within_one"] >= thr and not ag["missing"]
    print("PASS" if ok else "BELOW THRESHOLD: reread the anchors where you disagreed and recalibrate")
    block = {"calibration": {"set": cal["id"], "scores": {m: {s: scores.get(m, {}).get(s) for s in CALIBRATION_SCALES} for m in sorted(gold)}}}
    if write_run:
        rp = ROOT / "log" / "runs" / f"{write_run}.yaml"
        run = read_yaml(rp)
        if run.get("calibration"):
            raise SystemExit(f"{rp.relative_to(ROOT)} already has a calibration block")
        text = rp.read_text(encoding="utf-8").rstrip("\n") + "\n" + dump_yaml(block)
        rp.write_text(text, encoding="utf-8")
        print(f"wrote calibration to {rp.relative_to(ROOT)}")
    else:
        print("\n# paste into your run file:\n" + dump_yaml(block))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("sheet")
    sp = sub.add_parser("score")
    sp.add_argument("path", type=Path)
    sp.add_argument("--write-run", metavar="RUN_ID")
    args = ap.parse_args()
    if args.cmd == "sheet":
        sys.stdout.write(sheet())
    else:
        sys.exit(score(args.path, args.write_run))


if __name__ == "__main__":
    main()
