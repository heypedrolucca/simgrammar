# SimGrammar

An open, machine-readable atlas of simulation game mechanics: which games use which rule-systems, how each mechanic works and fails, which math/AI/ML/LLM results change what those mechanics can be, and where the design opportunities are.

The repository is the research. The report, wiki, tables, graph, and site are projections of the same YAML files, rebuilt and checked on every commit, so they cannot disagree with each other.

<!-- BEGIN GENERATED: stats -->
| Entity type | Count | Sourced or verified |
|---|---:|---:|
| games | 174 | 172 |
| mechanics | 199 | 171 |
| techniques | 45 | 45 |
| opportunities | 43 | 0 |
| sources | 643 | 643 |
| runs (provenance log) | 26 | n/a |

Typed edges: **4114** · game→mechanic uses: **1823** · games span **1968–2026**.
<!-- END GENERATED: stats -->

## Read it

| You want | Open |
|---|---|
| The report (paper form) | [`dist/paper/paper.md`](dist/paper/paper.md) · BibTeX: [`dist/paper/references.bib`](dist/paper/references.bib) |
| A wiki you can click through | [`dist/wiki/index.md`](dist/wiki/index.md) |
| Sortable / filterable tables | [`dist/tables/`](dist/tables/) (games, mechanics, techniques, opportunities, sources, edges, game×mechanic matrix) |
| A graph | [`dist/graph/`](dist/graph/) (`nodes.jsonl`/`edges.jsonl`, Cytoscape JSON, GraphML for Gephi) |
| Analysis outputs | [`dist/analysis/`](dist/analysis/) (stats, co-occurrence, white space, clusters, exposure, figures) |
| An interactive explorer | [`site/index.html`](site/index.html) (serve the repo root; reads `dist/site/data.json`) |
| SQL | `make sqlite` → `dist/simgrammar.sqlite` |
| Integrity certificate | [`dist/manifest.json`](dist/manifest.json): per-entity and dataset SHA-256 |

## Contribute

```bash
pip install -r requirements.txt
make hooks       # optional pre-commit check
make check       # validate + verify projections are fresh
```

1. Read [`CONTRACT.md`](CONTRACT.md) (invariants and enforced rules) and [`AGENTS.md`](AGENTS.md) (procedure; written for AI agents, works for humans).
2. Open a run: `python scripts/new.py run <slug> --kind catalog --actor human --operator <you> --purpose "..."`.
3. Search first: `python scripts/find.py "<concept>"`.
4. Scaffold: `python scripts/new.py mechanic <id> --run <run-id>`, fill every field, cite sources.
5. `make build && make check`, commit, open a PR.

The quickest high-value contribution is sourcing an entity from the verification queue: [`dist/analysis/verification-queue.csv`](dist/analysis/verification-queue.csv).

## Layout

```
CONTRACT.md      invariants, change classes, generated rule table
AGENTS.md        step-by-step procedure for agents and humans
schema/          JSON Schemas (closed) + registry.yaml (types, dirs, contract version)
vocab/           closed vocabularies, edge types, anchored rubrics
data/            canonical entities, one YAML file each
log/runs/        append-only provenance records
decisions/       ADRs for vocab, rubric, schema, and rule changes
report/src/      report prose with {{tokens}}, [[links]], [@citations]
report/          tables.yaml (declarative table views), analysis.yaml (analysis parameters), meta.yaml
scripts/         validate.py, build.py, analyze.py, new.py, find.py
dist/            generated projections (committed; CI fails if stale)
site/            static explorer over dist/site/data.json
```

## Design lineage

Two ideas carried over from earlier projects:

- **The log is the source; views are projections** (ActiveGraph). Canonical facts live in small typed records with provenance; every table, graph, and paper is a replayable projection, and the build is deterministic so drift is a diff.
- **Provenance-first knowledge with explicit epistemic status** (Epistemedia). Every entity carries `asserted / sourced / verified / contested`, verification requires an independent run, and the manifest's hashes let anyone certify which dataset version a claim came from.

## License

Code: Apache-2.0. Data, vocabularies, and report text: CC BY 4.0. See [`LICENSE`](LICENSE).
