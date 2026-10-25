# AGENTS.md: operating procedure for AI agents (and humans who want zero surprises)

You are contributing to a research graph that many agents and people edit concurrently. Drift happens when contributors invent fields, terms, ids, or numbers. This file removes those choices. Follow it literally. When it is silent, choose the option that changes the fewest files and record your doubt as a `proposal` in your run file.

`CLAUDE.md`, `.cursorrules`, and any other agent entrypoint point here. `CONTRACT.md` is the law; this file is the procedure.

## 0. Before you touch anything

```bash
pip install -r requirements.txt
make check          # must be green before you start; if it is red, stop and report
```

Read, in order: `CONTRACT.md` §2 (invariants), the schema for every type you will edit (`schema/<type>.schema.json`), and the vocab files those schemas reference. Do not rely on memory of a previous version of this repo.

## 1. Open a run

Every change belongs to exactly one run.

```bash
python scripts/new.py run <slug> --kind <kind> --actor agent --operator <github-handle-of-accountable-human> \
  --model <model-id> --harness "<tool you run in>" --purpose "<one sentence>"
```

`--kind` says what the run may do: `taxonomy` (the only kind that may create mechanics), `catalog` (games), `technique`, `synthesis` (opportunities, report), `verification` (the only kind that may set `status: verified`), `maintenance`. The validator enforces this (E031).

Fill `method` (what you searched, read, or computed) and keep `proposals` for anything you wanted to do but this file does not allow. Every entity you create gets `provenance.created: <run-id>`. Every existing entity you re-check gets your run id appended to `provenance.reviewed`.

## 2. Search before you create

```bash
python scripts/find.py "<name or concept>"           # all types
python scripts/find.py "<concept>" --type mechanic
```

If something close exists, edit it instead of creating a near-duplicate. Duplicates are the most common drift.

## 3. Admission tests

### Game inclusion test
Include a work if all hold: (a) released commercially, freely, or as a public research demo; (b) its core loop is driven by a model of some system (economy, ecology, physics, society, bodies, machines) whose state evolves without the player scripting each change; (c) it contributes at least one mechanic usage not already well represented, or it is a lineage-defining title. A work that fails (b) but is included anyway for specific mechanics (a puzzle or toy whose rules matter to simulation design) sets `boundary_case: true`; say in `design_notes` which mechanics justify it.

If no subgenre or other vocab term fits, pick the closest term and file a `vocab-term` proposal. If no mechanic fits a rule-system the game clearly has, **do not force-fit** the nearest mechanic (a wrong tag distorts prevalence and clustering); leave it out, describe it in `design_notes`, and file a `new-mechanic` proposal.

### Mechanic admission test (all four must pass)
1. **Nameable**: a designer would recognize it in games other than the one you are looking at.
2. **Atomic**: owns one kind of state and one update rule. If it splits into two parts that each appear without the other in real games, create two mechanics.
3. **Tunable**: has at least two levers you can list in `design_levers`.
4. **Removable**: a game could drop it and still run.

If a candidate fails, it is a game-specific feature (describe it in that game's `uses` note) or an opportunity. Agents doing game or technique work **may not create mechanics**; add a `new-mechanic` proposal to the run instead. Mechanic creation is reserved for runs of kind `taxonomy` (E031).

### Technique inclusion test
A dated, citable result (paper, preprint, model release, shipped system, or engine feature) that changes at least one mechanic, with `affects` edges that say how (`effect` vocab). Vendor marketing alone fails. `year` is the year of the key result. `maturity` and `trl` describe deployment **in games**, not in AI generally.

### Opportunity test
Names at least one mechanic in `involves`, has a `validation_experiment` a small team could run, and a `falsifiable_signal` with a `resolve_by` date and criteria a stranger could check.

## 4. Fields: how to fill them without drifting

| Situation | Rule |
|---|---|
| Categorical field | Use an existing term from the vocab file named in the schema (`x-vocab`). Missing term → proposal `vocab-term`, pick the closest existing term now. |
| Ordinal score | Read the anchors in `vocab/rubrics.yaml`. Pick the anchor whose text matches. Between two, take the lower. Never adjust a score to make a ranking come out a certain way. |
| `summary` | One sentence, no markdown, no hype adjectives (revolutionary, groundbreaking, game-changing), no em-dashes. |
| Long text | Specific and mechanical. Name the variables and the update rule. Cite numbers only if a source supports them. |
| Game `mechanics` | 6–14 entries typical; fewer than 5 raises W103. `core` only for mechanics whose removal changes the game's identity; every core entry needs a `note` saying how this game implements it. |
| `influenced_by` | Only documented or widely acknowledged lineage. Earlier games only (E025). |
| Mechanic relations | `requires` for hard dependencies; `specializes` for narrower forms; `synergy`/`tension` stored only on the id that sorts first alphabetically (E010). Never list games or techniques on a mechanic. |
| Technique `affects` | One entry per mechanic actually changed; `effect` from `vocab/effect.yaml`; note says what changes. |
| `deployed_in` | Only games in `data/games/` where the technique is used (shipped or public demo). |
| Dates | `YYYY`, `YYYY-MM`, or `YYYY-MM-DD` at the precision you know. |
| Derived numbers | Never store counts, prevalence, earliest year, priority, clusters, or backlinks. The build computes them. |

## 5. Evidence and status

- No source → `status: asserted`. That is fine; the verification queue exists for this.
- You cite a source that supports the factual fields → `status: sourced`.
- You re-check someone else's sourced entity against its sources in a run of kind `verification` → append your run to `provenance.reviewed` and set `verified`. Never verify an entity your own run created; a review by any other kind of run does not count (E031).
- A source contradicts a sourced entity → `status: contested`, add a claim with `disputes`, cite both sides. Do not silently overwrite.

### Sources
- Id: `src-<publisher-or-first-author-surname>-<year>-<short-slug>`, e.g. `src-park-2023-generative-agents`, `src-steam-2024-manor-lords`; Wikipedia articles use `src-wikipedia-<slug>` (no year). The schema enforces both forms (E004).
- Check `data/sources/` before creating; one file per work. If it exists, cite it.
- Prefer primary sources (paper, official blog, store page, developer postmortem) over aggregators. `accessed` is the date you read it.
- Every source must be cited by something (E011).

## 6. Writing the report

`report/src/*.md` is prose plus tokens. Rendered by `make build` into `dist/paper/paper.md` and the website (`dist/web/`, published at sim.yohei.me).

| Token | Renders |
|---|---|
| `{{count:game}}` (any type) | live entity count |
| `{{count:edge:uses}}` (any edge type) | edge count |
| `{{stat:<name>}}` | a statistic from `dist/analysis/stats.json` |
| `{{table:<name>}}` | a table from `report/tables.yaml` or `dist/analysis/*.csv` |
| `{{figure:<name>}}` | an SVG from `dist/analysis/figures/` |
| `{{viz:<name>}}` | an interactive figure from `scripts/viz.py`: a static SVG in `paper.md`, interactive on the website, always with a plain-text twin table |
| `{{vocab:<vocab>:<term>}}` | a vocab label |
| `{{assert:<ref> <op> <value\|ref>}}` | renders nothing; fails the build (E029) if false. Put one next to every sentence that interprets a ranking, sign, ordering, or grouping. `<ref>` is a stat (`rho_legibility_emergence_potential < 0`), an entity's derived field (`derived.rimworld.cluster == derived.the-sims.cluster`), a stored field (`field.genie-world-models.maturity == prototype`), or a row rank in a generated table (`rank.whitespace.lifecycle-aging.production-chain <= 10`; 9999 when absent) |
| `[[id]]`, `[[id\|text]]` | link to an entity |
| `[@src-id]`, `[@src-a; @src-b]` | numbered citation |

Never type a dataset count ("140 games") into prose (E021). When a sentence interprets data ("X is the most exposed family", "the correlation is negative"), pin it with an assertion so the build fails if a later data change makes the sentence false. If you need a new statistic, add it to `scripts/analyze.py` (deterministic) in the same PR. If you need a new table view, add it to `report/tables.yaml`.

### The website

`scripts/web.py` projects everything into `dist/web/`: the paper, one page per record, an index per type, and a data page. It uses Register (`web/register.css`, vendored; its contract is `web/DESIGN.md`). Follow that contract when you change a page template: no new stylesheet or classes, lowercase mono labels, one accent, every component with a plain-text twin, and every page complete without JavaScript (`web/simgrammar.js` only adds interaction). Figures are laid out in Python, deterministically; the script never lays anything out. The domain lives in `report/meta.yaml` (`site.domain`) and is written to `dist/web/CNAME`. `.github/workflows/pages.yml` publishes `dist/web/` on every push to `main`.

## 7. Never

- Edit `dist/` or anything between `<!-- BEGIN GENERATED -->` markers.
- Add a field, vocab term, edge type, or rubric anchor without an ADR (`decisions/`).
- Change or reuse an id. Delete a merged entity (deprecate it).
- Store an inverse edge or a derived number.
- Leave a placeholder (`TODO`, `TBD`, `FIXME`, any case) in data, runs, vocab, or report prose (E027).
- Work around a failing rule. If you believe a rule is wrong, stop, keep `make check` green, and file a `rule` proposal.

## 8. Finish

```bash
make build            # regenerate dist/ and GENERATED blocks from your edits
make check            # validate + build --check; must be green
git add -A && git commit -m "<type>(<scope>): <what> [run:<run-id>]"
```

Commit types: `data`, `taxonomy`, `vocab`, `schema`, `report`, `build`, `docs`. One run per PR. The PR template asks for the run id, the rule codes you hit, and your proposals. Changes under `vocab/`, `schema/`, `scripts/`, `CONTRACT.md`, and `AGENTS.md` need maintainer review (`.github/CODEOWNERS`) because the validator cannot judge whether a contract change is justified; it can only enforce the contract as written.

## 9. Parallel agents

When several agents work at once, partition by **files**, not topics: each agent owns a disjoint set of entity files and only reads others. Shared files (sources) are append-only: check existence immediately before writing; if a source id already exists, cite it rather than rewriting it. The orchestrator runs `make check` after merging and owns conflict resolution.
