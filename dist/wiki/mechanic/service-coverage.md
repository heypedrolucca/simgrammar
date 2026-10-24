# Service coverage

*Mechanic* · `service-coverage` · status: **sourced**

Service buildings such as police, fire, clinics, and schools satisfy demand within a radius or network distance, up to a capacity.

| field | value |
|---|---|
| aliases | service radius, coverage areas, service catchment |
| family | Logistics & networks |
| substrate | Cellular grid, Network / graph |
| math basis | Graph search, Optimization |
| feedback | Balancing (negative) |
| player interface | Placement, Parameter, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [SimCity](../game/simcity-1989.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 10 |
| prevalence share *(computed)* | 0.057 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each service building writes an effect value onto a coverage map, within a radius, a network distance, or by dispatching vehicles. Covered cells or buildings read that value to reduce a risk or raise a satisfaction term. In Micropolis each fire or police station adds an effect equal to 1000 times funded over requested budget, halved if unpowered and halved again without road access, to an 8x8-tile block map; the map is smoothed three times, and the smoothed police map is subtracted from each cell's crime score and the smoothed fire map sets fire protection. SimCity 2000 shows coverage as a radius; Cities: Skylines uses network distance and dispatches service vehicles. Capacity limits how many buildings or residents one facility can serve. Inputs: service building locations, funding, power, access. Outputs: per-cell coverage values and the downstream risk or happiness change.

## Player Experience

Filling the map with circles. Players place services to cover populated areas, check overlays for gaps, and balance coverage against budget. Uncovered districts show up as fires, crime, or unhappy residents, so the overlay becomes a to-do list.

## Design Levers

- coverage shape: Euclidean radius, network distance, or vehicle dispatch
- capacity per building and falloff with distance
- funding and power effects on strength
- how coverage maps to outcomes such as crime, fire risk, health, or education
- overlap rules: additive, maximum, or diminishing

## Failure Modes

- Radius coverage that ignores the road network lets buildings across a river count as covered.
- Overlapping coverage with no capacity limit makes one building per district enough.
- Hidden funding multipliers make coverage seem to drop at random.

## Dynamics

- Coverage shapes city form, rewarding compact grids around service hubs.
- Budget cuts weaken coverage everywhere at once, causing simultaneous crises.
- Coupled with land value, coverage raises desirability, which raises density, which raises demand for more services.

## Open Questions

- Can facility-location solvers act as advisors that suggest placements without removing the planning decision?
- Does vehicle dispatch produce more interesting failures than radius coverage at equal legibility?

## Backlinks (computed)

**generalizes:** [Walker service delivery](../mechanic/walker-service-delivery.md)

**used by:** [Cities: Skylines](../game/cities-skylines.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Frostpunk](../game/frostpunk.md), [Railroad Tycoon](../game/railroad-tycoon.md), [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [SimCity (2013)](../game/simcity-2013.md), [SimCity 4](../game/simcity-4.md), [Surviving Mars](../game/surviving-mars.md), [Transport Tycoon](../game/transport-tycoon.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
