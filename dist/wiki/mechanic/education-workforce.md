# Education and workforce

*Mechanic* · `education-workforce` · status: **sourced**

Education levels gate job types, and schooling converts the labor pool into higher levels over time.

| field | value |
|---|---|
| aliases | education levels, schooling, skilled labor pool |
| family | Population & lineage |
| substrate | Aggregate stocks, Agent-based |
| math basis | System dynamics / ODEs, Population dynamics |
| feedback | Balancing (negative) |
| player interface | Placement, Parameter, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Cities: Skylines](../game/cities-skylines.md) |
| earliest year *(computed)* | 2015 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns an education level per citizen or the population's distribution over levels, and school capacity and coverage. Each period, school-age or eligible citizens with access and seats advance a level after a study period; capacity and budget limit throughput, and aging and migration change the mix. Jobs and buildings require minimum levels, so the distribution decides which industries can be staffed. Cities: Skylines uses uneducated, educated, well educated, and highly educated, with elementary schools of 300, high schools of 1,000, and universities of 4,500 seats; jobs carry education requirements, higher building levels need more educated workers, and citizens take lower jobs when nothing else is open. Victoria 3 moves literacy toward education access and grants pops qualifications for professions each month. Inputs: seats, budget, age structure. Outputs: the qualified worker distribution that labor matching reads.

## Player Experience

The player invests now for a different city later: schools cost upkeep for years before industry can upgrade. Players watch over- and under-education and adjust capacity, policies, and job mix to avoid unemployable graduates or empty offices.

## Design Levers

- number of levels and job requirements per level
- school capacity, upkeep, and study duration
- who studies: age gates, coverage radius, cost to citizens
- whether over-educated citizens accept lower jobs
- side effects of education on crime, garbage, or consumption

## Failure Modes

- Over-education: when educated citizens fill matching jobs first, basic industry reports worker shortages while graduates compete for offices.
- Long study times hide the lag between investment and effect, so players misread cause and effect.
- Single-step jumps with large schools make education a one-time checkbox.

## Dynamics

- Education shifts the industry mix toward offices and high tech, changing pollution and land value.
- Generational lag: the education mix follows age structure, so baby booms create later waves of graduates.
- Mismatches between education and jobs produce unemployment and shortages simultaneously.

## Open Questions

- Can agent-level career choice and schooling decisions by learned agents replace fixed education ladders without losing planning legibility?
- Which matching rule between education and jobs avoids both over-education collapse and meaningless education?

## Relations

**synergy**

- [Labor market](../mechanic/labor-market.md): Education reshapes which jobs can be filled.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md): Children age into a workforce whose skills depend on schooling.

## Backlinks (computed)

**involved in:** [Factories with a living workforce](../opportunity/living-workforce-factories.md)

**used by:** [Cities: Skylines](../game/cities-skylines.md), [Tropico 6](../game/tropico-6.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Education](../source/src-paradoxwikis-2026-skylines-education.md)
- [Pops](../source/src-paradoxwikis-2026-vic3-pops.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
