## 2. Method

### 2.1 Unit of analysis: the mechanic

A **mechanic** here is a rule-system that passes four admission tests (CONTRACT.md, I12):

- **Nameable.** Designers would recognize it in games other than the one being examined.
- **Atomic.** It owns one kind of state and one update rule. If it splits into two parts that each appear without the other in shipped games, it is two mechanics.
- **Tunable.** It has at least two levers.
- **Removable.** A game could drop it and keep running.

The tests exclude two common confusions. Dynamics such as "cascading failure" or "death spiral" are outcomes of coupled mechanics, so they appear in mechanics' `dynamics` fields rather than as entities. Genre-level patterns such as "colony management" are combinations, so they appear as game decompositions or opportunities. The result sits between the MDA framework's *mechanics* layer and a designer's pattern language: concrete enough to implement, general enough to recur.

Each mechanic belongs to one of {{stat:n_families}} families, assigned by the state it owns rather than the genre it appears in: [[weather]] is environment, [[labor-market]] is economy, [[agent-inspection]] is information.

### 2.2 Corpus

The game catalog was built to cover every subgenre in the vocabulary, every lineage-defining title from the 1960s onward, recent releases through {{stat:year_max}}, research demonstrations that run as interactive simulations (such as [[generative-agents-smallville]] and [[project-sid]]), and works included for a single mechanic (marked `boundary_case`; {{stat:n_boundary_cases}} such works). The catalog is a purposive sample, not a census: prevalence figures describe this corpus, and the earliest-appearance year of a mechanic is a lower bound on its true origin.

### 2.3 Schema and scoring

Every categorical field draws from a closed vocabulary (`vocab/`), and every ordinal field names an anchored rubric (`vocab/rubrics.yaml`). Scorers match the anchor text and take the lower anchor when between two. This trades resolution for consistency across contributors: a 3 in legibility means "understood after deliberate attention and the game's info tools" whoever assigned it. Scores are expert judgments, recorded as such, and the rubric for each is reproduced in the wiki.

Relations are typed edges with one owner each (`vocab/edge_types.yaml`). Inverses (which games use a mechanic, which techniques affect it) and all aggregates (prevalence, earliest appearance, clusters, technique exposure, opportunity priority) are computed by the build and never stored, so they cannot drift from the edges they summarize.

### 2.4 Evidence

Each entity carries an epistemic status. `asserted` means written from domain knowledge without a citation; `sourced` means at least one cited source supports its factual fields; `verified` requires a second, independent run. Techniques must always cite. At this version, {{stat:n_sourced_or_verified}} entities are sourced or verified and {{stat:n_asserted}} remain asserted; the asserted ones form a public verification queue (`dist/analysis/verification-queue.csv`).

### 2.5 Production

The dataset was produced by parallel research runs, each recorded in `log/runs/` with its operator, model, method, and the proposals it could not act on. Runs partitioned work by file, not by topic, so no two runs edited the same entity. Taxonomy runs analyzed mechanics; catalog runs verified release facts against public sources and decomposed games; technique runs searched the 2019 to 2026 literature and developer announcements. A validator enforcing the rules in CONTRACT.md §5 gated every merge. The same procedure (AGENTS.md) is what a new contributor, human or agent, follows.

### 2.6 Limitations

- **Sampling.** Commercial, English-language, PC-centric titles are over-represented; mobile management games and non-Western simulation traditions are under-represented.
- **Scoring.** Rubric scores are single-rater judgments in this version. The `verified` status and the review field exist so a second rater can confirm or contest them.
- **Decomposition depth.** A game's mechanic list records what is present and meaningful, not a complete specification. Absence of an edge is weak evidence of absence.
- **Recency.** Technique maturity and horizon are judged as of the run date and age quickly; each technique records the sources the judgment rests on.
