# Changelog

Contract, schema, vocabulary, and rubric changes. Data changes are tracked by run records in `log/runs/` and by git history.

## 1.0 (2026-10-23)

- Initial contract (CONTRACT.md), schemas for game, mechanic, technique, opportunity, source, run.
- Closed vocabularies in `vocab/`, edge types with single owners, anchored rubrics and composites.
- Validator rules E001-E028, W101-W102; deterministic build with projections to tables, graph, wiki, paper, and site.
- ADR-0001: repository architecture.
- ADR-0002 (pre-release hardening after an independent drift test): run `kind` with E031 (only taxonomy runs create mechanics; only verification runs verify), report assertions E029, style lint E030, broader literal-count lint E021 with citation exemption, placeholder lint across vocab and report prose, required GENERATED blocks, future-date checks for games and full source dates, run contract version check, W103 thin decompositions, source id pattern in schema, CODEOWNERS for contract surfaces.
