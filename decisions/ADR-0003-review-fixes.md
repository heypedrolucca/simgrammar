# ADR-0003: Changes after an independent content review

- Status: accepted
- Date: 2026-10-24
- Contract version: 1.0 (pre-release; no published data depended on the earlier rules)

## Context

An independent reviewer read the report against the dataset and found four classes of problem the validator did not catch.

1. **Coding gaps.** Parallel catalog agents tagged distinctive mechanics and skipped ubiquitous ones (pause controls, placement, tech trees). Prevalence, clusters, and white space were computed on incomplete decompositions.
2. **Ubiquity effects.** Once the gaps were filled, unweighted Jaccard clustering merged most of the catalog into one cluster joined by pause controls and placement, and the white-space table ranked pairs that include a pacing control first.
3. **Prose that contradicted entity fields.** The report called techniques determinism-breaking that the data scores `mitigable`, said design automation runs offline when several techniques run at play time, and said nothing touching state had shipped while shipped techniques carry `replaces-substrate` edges.
4. **Unfalsifiable predictions.** Criteria used "major", "popular", "peer studio", and store rankings, had no start date (so pre-existing features could resolve them), and one prediction was already true.

## Decision

1. **Clustering** weights each mechanic by inverse prevalence, `log(N / prevalence)` (`report/analysis.yaml: clustering.idf`), with k raised to 16, the smallest k that separates the zoning and production-chain city-builder lineages. Cluster members are listed by centrality, and report tables cap long link lists.
2. **White space** excludes the time-and-pacing family (`whitespace.exclude_families`), since pacing controls are fixed by the time model rather than a design gap.
3. **Assertions** can reference stored fields (`field.<id>.<path>`) and table ranks (`rank.<table>.<id>[.<id>]`) as well as stats and derived fields, so prose about technique maturity, determinism, rankings, and white-space pairs fails the build (E029) when the data changes under it.
4. **Schema:** a technique whose `determinism_impact` is `breaks` must list `determinism` among its `risks`; `risks` allows six entries.
5. **W104** warns when mechanic maturity disagrees with catalog dates (`classic` without a use 20+ years before the newest game, `emerging` with a use more than 10 years before it, `experimental` used by three or more games).
6. **Predictions** count only features first shipped after 2026-10-24, in titles above stated Steam review thresholds or with a console release, confirmed by developer material.

## Consequences

Cluster labels, white-space pairs, and several stats changed; the report sections that interpret them were rewritten and pinned with assertions. Rubric scores remain single-rater judgments by one model, which the report now states wherever it reports correlations among scores.
