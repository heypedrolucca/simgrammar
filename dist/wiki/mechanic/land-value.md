# Land value

*Mechanic* · `land-value` · status: **sourced**

Each location's value is computed from nearby amenities, nuisances, and access, and it drives density and building upgrades.

| field | value |
|---|---|
| aliases | desirability, property value |
| family | Economy & finance |
| substrate | Cellular grid, Aggregate stocks |
| math basis | Cellular automata, System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Placement, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [SimCity](../game/simcity-1989.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a value per tile or block, recomputed periodically from distance to centers, nearby amenities and nature, and nuisances. In Micropolis, the open-source SimCity engine, each developed 2x2 block gets value = 4 x (34 - distance to the population-weighted center) + a bonus for nearby trees and water - pollution, minus 20 where crime exceeds 190, clamped to 1-250. The value then drives residential growth (value minus pollution, scaled and capped), picks which of four building quality tiers develops, raises tax revenue through the city average, and lowers crime, which is computed as 128 - land value + density - police coverage. SimCity 4 computes desirability separately for each wealth level, and Cities: Skylines levels up buildings partly on land value raised by services and parks and lowered by pollution and noise.

## Player Experience

Shaping neighborhoods. The player places parks, transit, and services to lift values, keeps factories away from homes, and watches shabby blocks turn into towers. Checking the land value overlay becomes a planning habit.

## Design Levers

- components of the value formula (center distance, amenities, terrain, pollution, crime, noise) and their weights
- radius and falloff of each amenity or nuisance
- smoothing and update frequency of the value field
- thresholds that map value to building tiers, density, or wealth class
- whether value feeds taxes, rents, or residents' wealth directly

## Failure Modes

- Stacking cheap amenities such as parks in one spot maxes value and becomes a dominant pattern.
- When the formula is visible only as an overlay color, players cannot tell which factor holds a block back.
- A strong distance-to-center term makes every city look the same: dense core, poor fringe.

## Dynamics

- Low value raises crime and crime lowers value, so neglected districts slide toward slums unless policing or amenities break the loop.
- Rising value upgrades buildings and density, which adds traffic and noise that cap further gains.
- Value-based tax revenue rewards beautification, coupling aesthetics to the budget.

## Open Questions

- Could a learned hedonic model trained on real property data give land values that feel like real cities, and would players accept its opacity?
- Can land value include speculation and expectations, not only current neighbors, without destabilizing growth?

## Relations

**synergy**

- [Zoning](../mechanic/zoning.md): Zones develop according to land value, so placement decisions compound over time.
- [Service coverage](../mechanic/service-coverage.md): Service coverage raises land value, rewarding complete coverage with density.
- [Pollution spread](../mechanic/pollution-spread.md): Pollution depresses land value, creating the industrial-residential separation puzzle.

## Backlinks (computed)

**involved in:** [Learned build assist for cities](../opportunity/learned-build-assist.md)

**used by:** [Cities: Skylines](../game/cities-skylines.md), [Cities: Skylines II](../game/cities-skylines-2.md), [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [SimCity 4](../game/simcity-4.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
