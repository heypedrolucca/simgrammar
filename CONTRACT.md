# SimGrammar Contract

**Version 1.0** · Applies to everything under `data/`, `vocab/`, `schema/`, `log/`, `report/`.

This file defines what the repository guarantees. Code in `scripts/` enforces it; the rule table below is generated from `scripts/rules.py`, so the documented rules and the enforced rules are the same list. If this file and the code disagree, the code is the bug.

## 1. What this repository is

A versioned, machine-readable research graph of simulation game design:

- **games**: simulation games, each decomposed into the mechanics it uses
- **mechanics**: atomic rule-systems, each analyzed on its own
- **techniques**: math, AI, ML, and LLM results that change what mechanics can be
- **opportunities**: falsifiable design bets that combine mechanics and techniques
- **sources**: everything cited
- **runs**: append-only provenance records of who changed what, how

Every other artifact (tables, graph files, wiki, paper, site) is a projection built from those files.

## 2. Invariants

**I1. One source of truth.** Canonical state is `data/**/*.yaml`, `vocab/*.yaml`, `schema/*`, `log/runs/*.yaml`, and `report/src/*.md`. `dist/` and every `<!-- BEGIN GENERATED -->` block are projections. Never edit them by hand; CI rebuilds and fails on any difference (E023).

**I2. One entity, one file, one id.** File stem equals `id`. Ids are kebab-case and unique across all types (sources use the `src-` prefix). An id never changes after merge. To rename or merge, set `deprecated: {superseded_by, reason}` on the old entity and repoint edges (E014).

**I3. Closed schemas.** Every schema sets `additionalProperties: false`. A new field is a schema change (§4).

**I4. Closed vocabularies.** Every categorical field draws from `vocab/<name>.yaml`. A new term is a vocab change (§4). There are no free-form tags.

**I5. Anchored scores.** Every ordinal field names a scale in `vocab/rubrics.yaml` and is scored by matching anchor text. Between anchors, take the lower. Changing an anchor re-scores the dataset silently, so it is a contract change.

**I6. Edges live in one place.** Each edge type has one owner type (table below). Inverses are computed and never stored. Symmetric edges (`synergy`, `tension`) are stored only on the entity whose id sorts first (E007, E010).

**I7. Derived values are never stored.** Counts, prevalence, earliest appearance, clusters, exposure, priority, and backlinks are computed by `scripts/analyze.py`. A stored copy would drift; the schema has no field for them.

**I8. Status is a claim about evidence.** `asserted` means unsourced. `sourced` requires citations. `verified` requires a second run, distinct from the creating run, listed in `provenance.reviewed`. No one verifies their own work. Techniques always cite (E012).

**I9. Provenance is append-only.** Every entity names the run that created it. Run files are never rewritten after merge except for typos. Git history plus run records reconstruct how every fact entered the graph.

**I10. Prose cannot outrun data.** Report text gets dataset numbers only through tokens (`{{count:game}}`, `{{stat:...}}`, `{{table:...}}`). Literal counts fail E021. Every `[[id]]` link and `[@src-...]` citation must resolve.

**I11. Builds are deterministic.** Same inputs, byte-identical outputs. No timestamps, no unordered iteration, no network calls in the build.

**I12. Admission tests are part of the contract.**

- *Game*: a released or publicly demonstrated work whose core loop is driven by a model of some system (§AGENTS.md "Game inclusion test"). Works included only for specific mechanics set `boundary_case: true`.
- *Mechanic*: passes all four: (1) **nameable**: designers would recognize it across games; (2) **atomic**: owns one kind of state and one update rule; if it decomposes into two mechanics that each appear without the other, split it; (3) **tunable**: has at least two levers; (4) **removable**: a game could drop it and keep running. Combinations of mechanics are opportunities or game features, not mechanics.
- *Technique*: a dated, citable result (paper, release, shipped system) that changes what at least one mechanic can be. Vendor marketing alone is not sufficient.
- *Opportunity*: names at least one mechanic, has a validation experiment, and a falsifiable signal with a resolve-by date.

**I13. Disagreement is data.** A disputed fact becomes `status: contested` with a claim whose `disputes` field cites the opposing source (E026). Do not overwrite another contributor's sourced claim without recording the dispute.

## 3. Change classes

| Class | Examples | Requires |
|---|---|---|
| Data | add or edit games, mechanics, techniques, opportunities, sources | run record, `make check` green |
| Prose | report/src edits | `make check` green (tokens, links, literal-count lint) |
| Vocabulary | add, rename, or redefine a term | ADR in `decisions/`, migrate affected entities in the same PR |
| Rubric | change an anchor or composite weight | ADR, contract minor bump, note in CHANGELOG of which scores to revisit |
| Schema | add or change a field or edge type | ADR, contract minor bump (breaking: major), `schema/registry.yaml` `contract_version` bump, migration script if data changes |
| Rule | add or change a validator rule | ADR, edit `scripts/rules.py` and its implementation together |

Contract version lives in `schema/registry.yaml` and in the header of this file; CI fails if they disagree.

## 4. Edge types

<!-- BEGIN GENERATED: edge-types -->
<!-- END GENERATED: edge-types -->

## 5. Enforced rules

Run `make check`. Every finding names a rule code; `--json` gives machine-readable output with a fix hint.

<!-- BEGIN GENERATED: rules -->
<!-- END GENERATED: rules -->

## 6. Vocabularies

<!-- BEGIN GENERATED: vocab-index -->
<!-- END GENERATED: vocab-index -->

## 7. Rubric scales

<!-- BEGIN GENERATED: rubric-index -->
<!-- END GENERATED: rubric-index -->
