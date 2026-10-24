# Vocabulary: status

Epistemic status of an entity. Ordered from weakest to strongest support. Status is a claim about evidence, never about importance.

| id | label | definition |
|---|---|---|
| `asserted` | Asserted | Written from contributor or model knowledge with no cited source. Eligible for the verification queue. |
| `sourced` | Sourced | At least one cited source in `sources` supports the entity's factual fields (dates, names, results). |
| `verified` | Verified | Sourced, and a second run distinct from `provenance.created` re-checked the facts and is listed in `provenance.reviewed`. |
| `contested` | Contested | A contributor disputes a field. The dispute is recorded in `claims` with the opposing source. Projections flag the entity. |
