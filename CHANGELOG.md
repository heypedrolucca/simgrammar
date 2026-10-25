# Changelog

Contract, schema, vocabulary, and rubric changes. Data changes are tracked by run records in `log/runs/` and by git history.

## 1.0 (2026-10-23)

- Initial contract (CONTRACT.md), schemas for game, mechanic, technique, opportunity, source, run.
- Closed vocabularies in `vocab/`, edge types with single owners, anchored rubrics and composites.
- Validator rules E001-E031, W101-W104; deterministic build with projections to tables, graph, wiki, paper, and site.
- ADR-0001: repository architecture.
- ADR-0002 (pre-release hardening after an independent drift test): run `kind` with E031 (only taxonomy runs create mechanics; only verification runs verify), report assertions E029, style lint E030, broader literal-count lint E021 with citation exemption, placeholder lint across vocab and report prose, required GENERATED blocks, future-date checks for games and full source dates, run contract version check, W103 thin decompositions, source id pattern in schema, CODEOWNERS for contract surfaces.
- ADR-0003 (pre-release, after an independent content review): inverse-prevalence weighting and k=16 for game clustering, time-and-pacing excluded from white space, `field.` and `rank.` references in report assertions, schema rule that determinism-breaking techniques list determinism as a risk (`risks` up to six), W104 maturity-dates warning, prediction criteria with a post-2026-10-24 window and objective thresholds.

## 1.0 additions (2026-10-25)

- Website projection `dist/web/` (scripts/web.py), published by `.github/workflows/pages.yml`; styled with Register (vendored `web/register.css`, contract `web/DESIGN.md`).
- `{{viz:<name>}}` report token for interactive figures from scripts/viz.py (E019 covers unknown names); figures render as static SVG in paper.md.
- Dependencies pinned in requirements.txt; CI runs Python 3.13.
