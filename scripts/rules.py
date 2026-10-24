"""Rule catalog. The single source of truth for what the validator enforces.

CONTRACT.md's rule table is generated from this dict by build.py, so the documented rules
and the enforced rules cannot drift apart. Adding a rule = add it here + implement it in
validate.py (or build.py for E023) + bump CONTRACT minor version.
"""

RULES: dict[str, dict[str, str]] = {
    "E001": {"name": "yaml-parse", "check": "Every data file parses as YAML and contains exactly one mapping.", "fix": "Fix YAML syntax; one entity per file."},
    "E002": {"name": "file-location", "check": "File stem equals `id`; file lives in the directory registered for its `type`.", "fix": "Rename the file or move it; never change an id after merge (see E003)."},
    "E003": {"name": "id-unique", "check": "Entity ids are kebab-case and globally unique across all entity types.", "fix": "Pick a distinct id. Search first with `python scripts/find.py <term>`."},
    "E004": {"name": "schema", "check": "Entity validates against its JSON Schema (no extra fields, required fields present, lengths and types).", "fix": "Match schema/<type>.schema.json. Unknown fields are never allowed; propose schema changes in the run's `proposals`."},
    "E005": {"name": "vocab", "check": "Every `x-vocab` field uses a term defined in vocab/<name>.yaml.", "fix": "Use an existing term. To add one, open an ADR (decisions/) and add it in the same PR."},
    "E006": {"name": "ref-missing", "check": "Every reference (`x-edge`, `x-ref`) resolves to an existing entity or run.", "fix": "Create the target first or fix the id."},
    "E007": {"name": "ref-type", "check": "Edge targets have the type declared in vocab/edge_types.yaml, and the edge is stored on its declared owner type.", "fix": "Point the edge at an entity of the declared target type, and store it only on the declared owner type (vocab/edge_types.yaml); inverses are computed."},
    "E008": {"name": "self-edge", "check": "No entity has an edge to itself.", "fix": "Remove the self-reference."},
    "E009": {"name": "duplicate-edge", "check": "The same (source, type, target) appears at most once.", "fix": "Merge duplicate entries."},
    "E010": {"name": "symmetric-owner", "check": "Symmetric edges (synergy, tension) are stored once, on the entity whose id sorts first.", "fix": "Move the edge to the lexicographically smaller id and delete the mirror."},
    "E011": {"name": "orphan-source", "check": "Every source is cited by at least one entity, claim, or report citation.", "fix": "Cite it or delete it."},
    "E012": {"name": "evidence", "check": "`sourced`/`verified` entities cite sources; `verified` has a reviewed run distinct from `created`; techniques always cite sources.", "fix": "Add sources or lower status to `asserted`."},
    "E013": {"name": "provenance", "check": "`provenance.created` and every `reviewed` run exist in log/runs/.", "fix": "Create the run file with `python scripts/new.py run <slug>`."},
    "E014": {"name": "deprecated-target", "check": "No edge points at a deprecated entity; `superseded_by` targets are live.", "fix": "Repoint edges to the successor."},
    "E015": {"name": "acyclic", "check": "`requires`, `specializes`, `builds_on`, and `influenced_by` graphs are acyclic.", "fix": "Break the cycle; one direction is wrong."},
    "E016": {"name": "game-mechanics", "check": "Each game has >=1 core mechanic, every core mechanic has a `note`, and no mechanic is listed twice.", "fix": "Mark the identity-defining mechanics core and describe how the game implements them."},
    "E017": {"name": "mechanic-grounding", "check": "Every mechanic with maturity classic/established is used by >=2 games; every mechanic is used by >=1 game unless maturity is experimental.", "fix": "Tag the games that use it, lower maturity, or deprecate it into a broader mechanic."},
    "E018": {"name": "rubric", "check": "Ordinal fields name a rubric scale that exists, and values are anchor levels of that scale.", "fix": "Score against the anchors in vocab/rubrics.yaml."},
    "E019": {"name": "report-token", "check": "Every `{{...}}` token in report/src resolves (count, stat, table, figure).", "fix": "Use a defined token; tables live in report/tables.yaml, stats in scripts/analyze.py."},
    "E020": {"name": "report-link", "check": "Every `[[id]]` link and `[@src-id]` citation in report/src resolves.", "fix": "Fix the id or create the entity."},
    "E021": {"name": "report-literal-stat", "check": "Report prose states no literal counts or percentages of dataset nouns (games, mechanics, techniques, uses, edges, sources...), allowing up to two words between number and noun, unless the same sentence carries a citation (an external figure).", "fix": "Replace the number with a token such as `{{count:game}}`."},
    "E030": {"name": "style", "check": "Names and summaries of non-source entities contain no em-dash, no markdown, and none of the banned hype words (revolutionary, groundbreaking, game-changing, unprecedented, cutting-edge, paradigm-shifting).", "fix": "Rewrite plainly: commas or parentheses for asides, no emphasis markup, specific words instead of hype."},
    "E031": {"name": "run-kind", "check": "Mechanics are created only by runs of kind `taxonomy` or `bootstrap`; status `verified` requires a `reviewed` run of kind `verification`, distinct from the creating run and dated on or after it.", "fix": "Record a new-mechanic proposal instead of creating one; to verify, open a verification run and re-check the entity against its sources."},
    "E022": {"name": "vocab-integrity", "check": "Vocab files have unique term ids, a definition per term; edge_types declare owner, target, inverse, symmetric.", "fix": "Repair the vocab file."},
    "E023": {"name": "dist-fresh", "check": "dist/ and GENERATED blocks equal a fresh build, and every required GENERATED block is present (enforced by `python scripts/build.py --check`, not by validate.py).", "fix": "Run `make build` and commit the result. Never hand-edit dist/ or GENERATED blocks."},
    "E024": {"name": "dates", "check": "`year_full_release` >= `year`; game years, technique years, and source dates (full date) are not in the future.", "fix": "Correct the dates."},
    "E025": {"name": "influence-order", "check": "A game's `influenced_by` targets were released in or before its year.", "fix": "Reverse or remove the edge."},
    "E026": {"name": "contested", "check": "`contested` entities carry at least one claim with `disputes` filled.", "fix": "Record the dispute and its source."},
    "E027": {"name": "placeholder", "check": "No string in data/, log/, vocab/, or report/src contains a placeholder (TODO, TBD, FIXME, any case).", "fix": "Fill every field `scripts/new.py` scaffolded."},
    "E028": {"name": "contract-version", "check": "The version in CONTRACT.md's header equals `contract_version` in schema/registry.yaml, every schema `$id` carries that version, and every run records that version.", "fix": "Bump all three together."},
    "E029": {"name": "report-assertion", "check": "Every `{{assert:<stat> <op> <value>}}` in report/src holds. Assertions pin interpretive prose (rankings, signs, orderings) to the data it describes.", "fix": "The data changed under the prose: rewrite the sentence next to the assertion, then update the assertion."},
    "W101": {"name": "unused-vocab", "check": "Vocab terms not used by any entity (warning).", "fix": "Fine early on; prune or document before 2.0."},
    "W103": {"name": "thin-decomposition", "check": "Games tagged with fewer than 5 mechanics (warning; AGENTS.md expects 6-14).", "fix": "Tag every clearly present mechanic, or record why the game is thin in design_notes."},
    "W102": {"name": "verification-queue", "check": "Count of `asserted` entities awaiting sources (info).", "fix": "Pick one from dist/analysis/verification-queue.csv and source it."},
}
