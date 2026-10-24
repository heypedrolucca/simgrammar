# Walker service delivery

*Mechanic* · `walker-service-delivery` · status: **sourced**

Services are delivered by agents walking routes from their building, so coverage depends on where walkers actually go.

| field | value |
|---|---|
| aliases | walkers, roaming walkers, service walkers |
| family | Logistics & networks |
| substrate | Agent-based, Cellular grid |
| math basis | Markov / stochastic processes, Graph search |
| feedback | Balancing (negative) |
| player interface | Placement, Observation only |
| legibility | 2 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| requires | [Road networks](../mechanic/road-network.md) |
| specializes | [Service coverage](../mechanic/service-coverage.md) |
| open questions | Would walkers with learned or goal-driven routes make coverage more legible or less? |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Caesar III](../game/caesar-3.md) |
| earliest year *(computed)* | 1998 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each service building periodically spawns a walker that follows roads; as it passes, it writes a coverage value to nearby houses, which decays over time until the next visit. In Caesar III, as reproduced by the Julius reimplementation, a roaming walker first heads for a road point about 8 tiles out in a cardinal direction that rotates with each spawn, then wanders, turning pseudo-randomly at intersections and ending its walk at dead ends. Culture, health, and religion walkers set a per-service house value to 96, which decays by 1 on each periodic update; prefects reset fire risk to zero and engineers reset collapse risk to zero. Pharaoh and Zeus keep the model, and Pharaoh added roadblocks that turn roaming walkers back; Augustus, a Julius fork, brings roadblocks to Caesar III. Inputs: building location, road network, random turns. Outputs: per-house coverage values that gate housing evolution and prevent fires or collapses.

## Player Experience

Designing for wanderers. Players build looping road blocks so walkers cover the right houses, use roadblocks where available, and watch for houses that a walker never reaches. Knowing that coverage depends on chance makes layout feel like guiding a crowd.

## Design Levers

- walker roaming range and spawn interval
- turn rule at intersections: random, biased, or destination-based
- coverage radius around the walker and decay rate on houses
- roadblocks or other routing controls
- number of walker types and services per type

## Failure Modes

- Randomness that leaves some houses uncovered causes devolve-evolve flicker.
- Walker logic that needs community analysis to understand frustrates players.
- Too many walker types multiply layout constraints until blocks become formulaic.

## Dynamics

- Standard block layouts (looped housing blocks with services inside) become community conventions.
- Coverage gaps produce local fires and collapses that spread.
- Road changes can suddenly strand houses by changing walker routes.

## Open Questions

- Would walkers with learned or goal-driven routes make coverage more legible or less?

## Relations

**requires**

- [Road networks](../mechanic/road-network.md)

**specializes**

- [Service coverage](../mechanic/service-coverage.md)

## Backlinks (computed)

**used by:** [Caesar III](../game/caesar-3.md), [Pharaoh](../game/pharaoh.md)

## Sources

- [Julius: an open source re-implementation of Caesar III](../source/src-bvschaik-2026-julius.md)
- [Caesar III](../source/src-wikipedia-caesar-iii.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
