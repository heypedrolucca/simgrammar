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
| Edge | Owner → Target | Inverse (computed) | Symmetric | Meaning |
|---|---|---|---|---|
| `uses` | game → mechanic | `used_by` | no | A game uses a mechanic. Attributes role (mechanic_role) and note. |
| `influenced_by` | game → game | `influenced` | no | A game's design draws on an earlier game. |
| `requires` | mechanic → mechanic | `required_by` | no | A mechanic cannot function without another mechanic. |
| `specializes` | mechanic → mechanic | `generalizes` | no | A mechanic is a narrower form of a parent mechanic. |
| `synergy` | mechanic → mechanic | `synergy` | yes | Two mechanics amplify each other's dynamics when combined. |
| `tension` | mechanic → mechanic | `tension` | yes | Two mechanics pull design in opposite directions; combining them needs a resolution. |
| `affects` | technique → mechanic | `affected_by` | no | A technique changes a mechanic. Attributes effect (effect vocab) and note. |
| `builds_on` | technique → technique | `built_upon_by` | no | A technique depends on or extends an earlier technique. |
| `deployed_in` | technique → game | `deploys` | no | A technique is used in a specific game, shipped or prototype. |
| `involves` | opportunity → mechanic | `involved_in` | no | An opportunity reworks or combines a mechanic. |
| `applies` | opportunity → technique | `applied_in` | no | An opportunity depends on a technique. |
| `precedent` | opportunity → game | `precedent_for` | no | A game partially demonstrates an opportunity. |
| `cites` | any → source | `cited_by` | no | An entity or claim relies on a source. |
<!-- END GENERATED: edge-types -->

## 5. Enforced rules

Run `make check`. Every finding names a rule code; `--json` gives machine-readable output with a fix hint.

<!-- BEGIN GENERATED: rules -->
| Rule | Name | Check | Fix |
|---|---|---|---|
| E001 | yaml-parse | Every data file parses as YAML and contains exactly one mapping. | Fix YAML syntax; one entity per file. |
| E002 | file-location | File stem equals `id`; file lives in the directory registered for its `type`. | Rename the file or move it; never change an id after merge (see E003). |
| E003 | id-unique | Entity ids are kebab-case and globally unique across all entity types. | Pick a distinct id. Search first with `python scripts/find.py <term>`. |
| E004 | schema | Entity validates against its JSON Schema (no extra fields, required fields present, lengths and types). | Match schema/<type>.schema.json. Unknown fields are never allowed; propose schema changes in the run's `proposals`. |
| E005 | vocab | Every `x-vocab` field uses a term defined in vocab/<name>.yaml. | Use an existing term. To add one, open an ADR (decisions/) and add it in the same PR. |
| E006 | ref-missing | Every reference (`x-edge`, `x-ref`) resolves to an existing entity or run. | Create the target first or fix the id. |
| E007 | ref-type | Edge targets have the type declared in vocab/edge_types.yaml, and the edge is stored on its declared owner type. | Store the edge on the owner side only; inverses are computed. |
| E008 | self-edge | No entity has an edge to itself. | Remove the self-reference. |
| E009 | duplicate-edge | The same (source, type, target) appears at most once. | Merge duplicate entries. |
| E010 | symmetric-owner | Symmetric edges (synergy, tension) are stored once, on the entity whose id sorts first. | Move the edge to the lexicographically smaller id and delete the mirror. |
| E011 | orphan-source | Every source is cited by at least one entity, claim, or report citation. | Cite it or delete it. |
| E012 | evidence | `sourced`/`verified` entities cite sources; `verified` has a reviewed run distinct from `created`; techniques always cite sources. | Add sources or lower status to `asserted`. |
| E013 | provenance | `provenance.created` and every `reviewed` run exist in log/runs/. | Create the run file with `python scripts/new.py run <slug>`. |
| E014 | deprecated-target | No edge points at a deprecated entity; `superseded_by` targets are live. | Repoint edges to the successor. |
| E015 | acyclic | `requires`, `specializes`, `builds_on`, and `influenced_by` graphs are acyclic. | Break the cycle; one direction is wrong. |
| E016 | game-mechanics | Each game has >=1 core mechanic, every core mechanic has a `note`, and no mechanic is listed twice. | Mark the identity-defining mechanics core and describe how the game implements them. |
| E017 | mechanic-grounding | Every mechanic with maturity classic/established is used by >=2 games; every mechanic is used by >=1 game unless maturity is experimental. | Tag the games that use it, lower maturity, or deprecate it into a broader mechanic. |
| E018 | rubric | Ordinal fields name a rubric scale that exists, and values are anchor levels of that scale. | Score against the anchors in vocab/rubrics.yaml. |
| E019 | report-token | Every `{{...}}` token in report/src resolves (count, stat, table, figure). | Use a defined token; tables live in report/tables.yaml, stats in scripts/analyze.py. |
| E020 | report-link | Every `[[id]]` link and `[@src-id]` citation in report/src resolves. | Fix the id or create the entity. |
| E021 | report-literal-stat | Report prose states no literal dataset counts (e.g. '142 games'); counts must come from tokens. | Replace the number with a token such as `{{count:game}}`. |
| E022 | vocab-integrity | Vocab files have unique term ids, a definition per term; edge_types declare owner, target, inverse, symmetric. | Repair the vocab file. |
| E023 | dist-fresh | dist/ and GENERATED blocks equal a fresh build (`python scripts/build.py --check`). | Run `make build` and commit the result. Never hand-edit dist/ or GENERATED blocks. |
| E024 | dates | `year_full_release` >= `year`; technique years and source dates are not in the future. | Correct the dates. |
| E025 | influence-order | A game's `influenced_by` targets were released in or before its year. | Reverse or remove the edge. |
| E026 | contested | `contested` entities carry at least one claim with `disputes` filled. | Record the dispute and its source. |
| E027 | placeholder | No string anywhere in data/ or log/ contains the scaffold placeholder `TODO`. | Fill every field `scripts/new.py` scaffolded. |
| E028 | contract-version | The version in CONTRACT.md's header equals `contract_version` in schema/registry.yaml, and every schema `$id` carries that version. | Bump all three together. |
| E029 | report-assertion | Every `{{assert:<stat> <op> <value>}}` in report/src holds. Assertions pin interpretive prose (rankings, signs, orderings) to the data it describes. | The data changed under the prose: rewrite the sentence next to the assertion, then update the assertion. |
| W101 | unused-vocab | Vocab terms not used by any entity (warning). | Fine early on; prune or document before 2.0. |
| W102 | verification-queue | Count of `asserted` entities awaiting sources (info). | Pick one from dist/analysis/verification_queue.csv and source it. |
<!-- END GENERATED: rules -->

## 6. Vocabularies

<!-- BEGIN GENERATED: vocab-index -->
| Vocabulary | Terms | Description |
|---|---:|---|
| [`actor`](vocab/actor.yaml) | 3 | Who performed a research run. |
| [`agency_model`](vocab/agency_model.yaml) | 11 | How player intent reaches the simulation. A game may use several. |
| [`agent_count_order`](vocab/agent_count_order.yaml) | 7 | Order of magnitude of individually simulated agents in typical play. Aggregate populations shown as a number but simulated as stocks count as `aggregate`. |
| [`confidence`](vocab/confidence.yaml) | 3 | Confidence in a specific claim. |
| [`determinism_impact`](vocab/determinism_impact.yaml) | 3 | Effect on reproducibility, replays, lockstep multiplayer, and save integrity when used at runtime. |
| [`edge_types`](vocab/edge_types.yaml) | 13 | Every typed relation in the graph. Each edge is stored exactly once, on the `owner` side named here. Inverses are computed by the build and never stored. Symmetric edges are stored on the entity whose id sorts first. |
| [`effect`](vocab/effect.yaml) | 7 | How a technique changes a mechanic (attribute of the technique→mechanic `affects` edge). |
| [`failure_model`](vocab/failure_model.yaml) | 5 | What happens when the system goes wrong. |
| [`feedback`](vocab/feedback.yaml) | 4 | Dominant feedback loop polarity the mechanic creates in play. |
| [`fidelity`](vocab/fidelity.yaml) | 5 | How closely the model tracks real-world causal structure. Independent of graphics. |
| [`horizon`](vocab/horizon.yaml) | 4 | Expected time until meaningful use in shipped simulation games, as judged at the entity's last review date. |
| [`math_basis`](vocab/math_basis.yaml) | 24 | Formal mathematical model a mechanic instantiates, explicitly or implicitly. Used to connect mechanics to research literature. |
| [`maturity`](vocab/maturity.yaml) | 4 | Adoption maturity of a mechanic across shipped games. |
| [`mechanic_family`](vocab/mechanic_family.yaml) | 21 | Primary functional family of a mechanic. Exactly one per mechanic. Assign by the state the mechanic owns, not by the genre it appears in. |
| [`mechanic_role`](vocab/mechanic_role.yaml) | 2 | Role a mechanic plays in a specific game (attribute of the game→mechanic `uses` edge). |
| [`modding`](vocab/modding.yaml) | 4 | Depth of player modification supported or widely practiced. |
| [`multiplayer`](vocab/multiplayer.yaml) | 5 | Supported social play modes. |
| [`narrative_mode`](vocab/narrative_mode.yaml) | 5 | Where story comes from. |
| [`opportunity_type`](vocab/opportunity_type.yaml) | 8 | Kind of opportunity. |
| [`perspective`](vocab/perspective.yaml) | 7 | Primary camera or presentation. |
| [`platform`](vocab/platform.yaml) | 8 | Platform families a game shipped on at any point. |
| [`player_interface`](vocab/player_interface.yaml) | 9 | How the player touches this mechanic. |
| [`player_role`](vocab/player_role.yaml) | 13 | The fiction-level role the player occupies relative to the simulation. |
| [`production_tier`](vocab/production_tier.yaml) | 5 | Production context at release. |
| [`risk`](vocab/risk.yaml) | 11 | Primary risks of using a technique in simulation games. |
| [`runtime`](vocab/runtime.yaml) | 5 | Where in the lifecycle the technique runs. |
| [`sim_domain`](vocab/sim_domain.yaml) | 15 | Real-world domain the simulation models. One to three per game. |
| [`sim_scale`](vocab/sim_scale.yaml) | 10 | Spatial or organizational scale of the primary simulated unit of play. |
| [`source_kind`](vocab/source_kind.yaml) | 11 | Type of cited source. |
| [`status`](vocab/status.yaml) | 4 | Epistemic status of an entity. Ordered from weakest to strongest support. Status is a claim about evidence, never about importance. |
| [`subgenre`](vocab/subgenre.yaml) | 31 | Design lineage a game belongs to. One primary per game, optional secondaries. Lineage, not marketing label. |
| [`substrate`](vocab/substrate.yaml) | 10 | Computational representation the mechanic is usually implemented on. A mechanic may have several. |
| [`technique_category`](vocab/technique_category.yaml) | 17 | Research area of a technique or breakthrough. |
| [`technique_maturity`](vocab/technique_maturity.yaml) | 4 | Deployment maturity of a technique in games specifically (not in general AI). |
| [`time_model`](vocab/time_model.yaml) | 6 | Dominant relation between simulation time and player time. |
| [`win_structure`](vocab/win_structure.yaml) | 7 | How play is bounded and evaluated. |
<!-- END GENERATED: vocab-index -->

## 7. Rubric scales

<!-- BEGIN GENERATED: rubric-index -->
| Scale | Applies to | Question |
|---|---|---|
| `emergence` | game | How much of play arises from system interaction rather than authored content? |
| `influence` | game | How strongly did this game shape later simulation design? |
| `legibility` | mechanic | How easily can a typical player form an accurate mental model of the mechanic from play? |
| `emergence_potential` | mechanic | How much unscripted variety does this mechanic generate when coupled with others? |
| `authoring_cost` | mechanic | Developer cost of the content this mechanic consumes (animations, writing, assets, tuning data), per unit of player-facing variety. |
| `compute_cost` | mechanic | Runtime compute at the scale the mechanic is typically used. |
| `tuning_difficulty` | mechanic | How hard is it to balance so the mechanic is neither trivial nor degenerate? |
| `ai_leverage` | mechanic | Expert judgment of how much 2024-2026 AI techniques could change this mechanic's design ceiling (cross-checked by `affects` edges in analysis). |
| `trl` | technique | Technology Readiness Level for use in simulation games (NASA scale adapted). |
| `novelty` | opportunity | How far from shipped practice is this? |
| `feasibility` | opportunity | Can a small team (5-15) ship it within 24 months using techniques at their current maturity? |
| `impact` | opportunity | If it works, how much does it change player experience or the market? |
<!-- END GENERATED: rubric-index -->
