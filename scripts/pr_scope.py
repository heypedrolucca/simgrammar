#!/usr/bin/env python3
"""Pull-request scope check (E039). CI runs it on pull requests; it is not part of `make check`.

  python scripts/pr_scope.py --base origin/main --labels "bulk,run-typo"

A data PR adds exactly one run file, every record it adds or changes names that run in its provenance, it changes
at most `contribution.max_records_per_pr` records and `max_sources_per_pr` sources (schema/registry.yaml), it never
deletes a merged record (deprecate instead), it never edits a merged run file, and every non-merge commit is signed
off (Developer Certificate of Origin). Maintainer labels lift the limits:
`bulk` the record and source caps, `run-typo` the run-file rule.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, load_registry, read_yaml  # noqa: E402
from rules import RULES  # noqa: E402


def changed_files(base: str) -> list[tuple[str, str]]:
    out = subprocess.run(["git", "diff", "--name-status", "--no-renames", f"{base}...HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    rows = []
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            rows.append((parts[0][0], parts[-1]))
    return rows


def unsigned_commits(base: str) -> list[str]:
    """Non-merge commits on this branch without a Developer Certificate of Origin sign-off (CONTRIBUTING.md)."""
    out = subprocess.run(["git", "log", "--no-merges", "--format=%H%x1f%s%x1f%B%x1e", f"{base}..HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    bad = []
    for rec in out.split("\x1e"):
        parts = rec.strip().split("\x1f")
        if len(parts) >= 3 and "Signed-off-by:" not in parts[2]:
            bad.append(f"{parts[0][:10]} {parts[1][:60]}")
    return bad


def check(rows: list[tuple[str, str]], labels: set[str], registry: dict) -> list[str]:
    contrib = registry.get("contribution") or {}
    dirs = {spec["dir"]: t for t, spec in registry["types"].items()}
    records, sources, runs_added, runs_touched = [], [], [], []
    for status, path in rows:
        if not path.endswith(".yaml"):
            continue
        d = str(Path(path).parent)
        t = dirs.get(d)
        if t is None:
            continue
        if t == "run":
            (runs_added if status == "A" else runs_touched).append((status, path))
        elif t == "source":
            sources.append((status, path))
        else:
            records.append((status, path))
    errs = []
    bulk = contrib.get("bulk_label", "bulk") in labels
    if not bulk and len(records) > contrib.get("max_records_per_pr", 10):
        errs.append(f"{len(records)} records changed; the limit is {contrib.get('max_records_per_pr', 10)} per PR. Split the work into several PRs (one run each).")
    if not bulk and len(sources) > contrib.get("max_sources_per_pr", 30):
        errs.append(f"{len(sources)} sources changed; the limit is {contrib.get('max_sources_per_pr', 30)} per PR.")
    if runs_touched and contrib.get("run_typo_label", "run-typo") not in labels:
        for status, path in runs_touched:
            errs.append(f"{path}: merged run files are append-only ({'deleted' if status == 'D' else 'modified'}); open a new run instead (I9).")
    for status, path in records:
        if status == "D":
            errs.append(f"{path}: a merged record was deleted; set `deprecated: {{superseded_by, reason}}` instead (I2).")
    if records or sources:
        if len(runs_added) != 1:
            errs.append(f"a PR that changes data adds exactly one run file under log/runs/; this one adds {len(runs_added)}.")
        else:
            rid = Path(runs_added[0][1]).stem
            for status, path in records + sources:
                if status == "D":
                    continue
                data = read_yaml(ROOT / path) or {}
                prov = data.get("provenance") or {}
                if prov.get("created") != rid and rid not in (prov.get("reviewed") or []):
                    errs.append(f"{path}: provenance names neither created nor reviewed by this PR's run '{rid}'.")
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--labels", default="", help="comma-separated PR labels")
    args = ap.parse_args()
    labels = {x.strip() for x in args.labels.split(",") if x.strip()}
    errs = check(changed_files(args.base), labels, load_registry())
    errs += [f"commit {c} is not signed off; amend with `git commit -s` (Developer Certificate of Origin, CONTRIBUTING.md)" for c in unsigned_commits(args.base)]
    for e in errs:
        print(f"E039 {RULES['E039']['name']}: {e}")
    print(f"\n{len(errs)} scope error(s).", "OK" if not errs else "FAILED")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
