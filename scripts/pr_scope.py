#!/usr/bin/env python3
"""Pull-request scope check (E039). CI runs it on pull requests; it is not part of `make check`.

  python scripts/pr_scope.py --base origin/main --labels "bulk,run-typo"

A data PR adds exactly one run file (current contract version, dated within the last 30 days, operator = PR author),
every record it adds or changes names that run in its provenance without rewriting `created` or dropping `reviewed`
entries, new ratings come from that run, new claims carry a `quote`, it changes
at most `contribution.max_records_per_pr` records and `max_sources_per_pr` sources (schema/registry.yaml), it never
deletes a merged record (deprecate instead), it never edits a merged run file, and every non-merge commit is signed
off (Developer Certificate of Origin). Maintainer labels lift the limits:
`bulk` the record and source caps, `run-typo` the run-file rule.
"""
from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import ROOT, load_calibration, load_registry, read_yaml  # noqa: E402

RUN_MAX_AGE_DAYS = 30
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


def base_version(base: str, path: str):
    """The file as it was at the merge base, or None if it did not exist."""
    mb = subprocess.run(["git", "merge-base", base, "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip() or base
    r = subprocess.run(["git", "show", f"{mb}:{path}"], cwd=ROOT, capture_output=True, text=True)
    return yaml.safe_load(r.stdout) if r.returncode == 0 else None


def record_changes(path: str, old: dict | None, new: dict, rid: str) -> list[str]:
    """Rules that compare a changed record with its merged version."""
    errs = []
    if old:
        po, pn = old.get("provenance") or {}, new.get("provenance") or {}
        if po.get("created") != pn.get("created"):
            errs.append(f"{path}: provenance.created changed from '{po.get('created')}' to '{pn.get('created')}'; it records who made the record and never changes (I9).")
        lost = [x for x in po.get("reviewed") or [] if x not in (pn.get("reviewed") or [])]
        if lost:
            errs.append(f"{path}: provenance.reviewed lost {lost}; the list is append-only (I9).")
    created = (new.get("provenance") or {}).get("created")
    old_ratings = [r for r in (old or {}).get("ratings") or []]
    for r in new.get("ratings") or []:
        if r in old_ratings:
            continue
        if r.get("run") == rid:
            continue
        if r.get("run") == created and old is not None and r.get("value") == old.get(r.get("field")) and not any(o.get("run") == created and o.get("field") == r.get("field") for o in old_ratings):
            continue  # recording the original score as the creator's rating, unchanged
        errs.append(f"{path}: new rating of '{r.get('field')}' is attributed to run '{r.get('run')}'; a PR adds ratings only from its own run (or records the creator's original score unchanged).")
    old_claims = {c.get("text") for c in ((old or {}).get("claims") or []) + ((old or {}).get("key_results") or [])}
    for c in (new.get("claims") or []) + (new.get("key_results") or []):
        if c.get("text") not in old_claims and not c.get("quote"):
            errs.append(f"{path}: new claim has no `quote`; copy the passage from its first source that supports it (tasks/source-claims.md).")
    return errs


def run_checks(path: str, run: dict, registry: dict, author: str | None, today: dt.date) -> list[str]:
    errs = []
    cv = str(registry.get("contract_version"))
    if str(run.get("contract_version")) != cv:
        errs.append(f"{path}: a new run records the current contract version {cv}, not {run.get('contract_version')}.")
    try:
        d = dt.date.fromisoformat(str(run.get("date")))
        if d > today or (today - d).days > RUN_MAX_AGE_DAYS:
            errs.append(f"{path}: run date {d} must be within the last {RUN_MAX_AGE_DAYS} days.")
    except ValueError:
        errs.append(f"{path}: run date {run.get('date')} is not a date.")
    if author and str(run.get("operator", "")).strip().lower() != author.strip().lower():
        errs.append(f"{path}: operator '{run.get('operator')}' is not the PR author '{author}'; the operator is the accountable person who opens the PR.")
    cal = run.get("calibration")
    cur = load_calibration(registry) or {}
    if cal and str(cal.get("set")) != str(cur.get("id")):
        errs.append(f"{path}: a new calibration uses the current set '{cur.get('id')}', not '{cal.get('set')}'.")
    return errs


def check(rows: list[tuple[str, str]], labels: set[str], registry: dict, base: str | None = None, author: str | None = None,
          today: dt.date | None = None) -> list[str]:
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
            errs += run_checks(runs_added[0][1], read_yaml(ROOT / runs_added[0][1]) or {}, registry, author, today or dt.date.today())
            for status, path in records + sources:
                if status == "D":
                    continue
                data = read_yaml(ROOT / path) or {}
                prov = data.get("provenance") or {}
                if prov.get("created") != rid and rid not in (prov.get("reviewed") or []):
                    errs.append(f"{path}: provenance names neither created nor reviewed by this PR's run '{rid}'.")
                if base is not None:
                    errs += record_changes(path, base_version(base, path) if status != "A" else None, data, rid)
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--labels", default="", help="comma-separated PR labels")
    ap.add_argument("--author", default="", help="GitHub login of the PR author; the new run's operator must match")
    args = ap.parse_args()
    labels = {x.strip() for x in args.labels.split(",") if x.strip()}
    errs = check(changed_files(args.base), labels, load_registry(), base=args.base, author=args.author or None)
    errs += [f"commit {c} is not signed off; amend with `git commit -s` (Developer Certificate of Origin, CONTRIBUTING.md)" for c in unsigned_commits(args.base)]
    for e in errs:
        print(f"E039 {RULES['E039']['name']}: {e}")
    print(f"\n{len(errs)} scope error(s).", "OK" if not errs else "FAILED")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
