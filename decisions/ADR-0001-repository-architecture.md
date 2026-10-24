# ADR-0001: Repository architecture for zero-drift collaborative research

- Status: accepted
- Date: 2026-10-23
- Contract version: 1.0

## Context

The research spans a catalog of games, a taxonomy of mechanics, a technique landscape that changes monthly, and a long report. It must project into a wiki, graph, sortable tables, and an academic paper, and accept edits from many humans and agents without the projections or the taxonomy drifting.

Drift has four usual sources: (1) duplicated facts stored in two places, (2) open-ended fields and tags, (3) prose that restates numbers, and (4) contributors who each reinterpret categories.

## Decision

1. **Canonical state is one YAML file per entity**, validated by closed JSON Schemas. Merge conflicts stay local to one entity.
2. **Schemas carry semantics** via annotations: `x-vocab` (closed vocabulary), `x-edge` (typed reference), `x-ref` (non-graph reference), `x-rubric` (anchored scale). Validator and build read annotations generically, so adding a field with `x-edge` automatically puts it in the graph, wiki, and CSVs.
3. **Edges have exactly one owner**; inverses and all aggregates are computed. There is no field in which a derived value could be stored.
4. **Report prose uses tokens** for every dataset number, table, and figure; a lint rejects literal counts.
5. **Every projection is committed and byte-reproducible**; CI rebuilds and diffs (`build.py --check`).
6. **Provenance records (runs) are append-only** and every entity cites its creating run; `verified` requires a different run.
7. **Rule documentation is generated from the rule implementation** (`scripts/rules.py` → CONTRACT.md).
8. **Vocabulary, rubric, schema, and rule changes require an ADR** and a contract version bump where they alter meaning.

## Consequences

- Contributors cannot add a tag or a field casually; they file a proposal. This slows taxonomy growth on purpose.
- Committing `dist/` makes diffs larger but lets anyone consume projections without running Python and makes drift visible in review.
- The dataset hash in `dist/manifest.json` gives each published claim a version anchor.

## Alternatives considered

- **Single large YAML/CSV**: simpler, but every edit conflicts and partial validation is hard.
- **Graph database as source of truth**: better queries, worse diffs and review; projections cover the query need (`make sqlite`).
- **Free tags plus periodic cleanup**: proven to drift.
