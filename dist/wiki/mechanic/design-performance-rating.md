# Design performance rating

*Mechanic* · `design-performance-rating` · status: **sourced**

Player-built designs are run or analyzed and scored on simulated metrics such as ride excitement, bridge stress, or cost and cycles.

| field | value |
|---|---|
| aliases | ride ratings, solution metrics, stress test |
| family | Space & construction |
| substrate | Continuous physics, Rule system |
| math basis | Optimization, Classical mechanics |
| feedback | Balancing (negative) |
| player interface | Placement, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md) |
| earliest year *(computed)* | 1999 |
| prevalence *(computed)* | 8 |
| prevalence share *(computed)* | 0.046 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 3 |
| technique exposure *(computed)* | 0.438 |

## Definition

The player builds a design (a coaster track, a bridge, a machine program), the game runs or analyzes it, and a metric vector is computed from what happened. Metrics gate success, set income, or rank the design. In RollerCoaster Tycoon 2, as documented by OpenRCT2, a test run yields excitement, intensity, and nausea from peak positive, negative, and lateral g, number of drops, highest drop, inversions, and nearby scenery; excitement stops rising after 9 drops and 6 inversions, is cut 25% when intensity exceeds 10 with further cuts at 11, 12, 13.2, and 14.5, and is halved when lateral g exceeds 3.1. Poly Bridge drives vehicles over a bridge and shows member stress under a budget. SpaceChem scores solutions on cycles, reactors, and instructions, and Opus Magnum on cost, cycles, and area. State: the design and its last metric vector; update: re-evaluate on test or edit.

## Player Experience

Build, test, read the numbers, revise. Players learn the hidden physics through the scores, enjoy beating a threshold, and then chase better tradeoffs between metrics that pull against each other.

## Design Levers

- which metrics exist and how many are orthogonal
- formula shape, caps, and penalties, such as excitement penalties for excessive intensity
- hard pass or fail thresholds versus continuous scores
- when evaluation runs: an explicit test run, continuous re-evaluation, or end of level
- how much of each metric's derivation the game exposes
- comparison against other players' results

## Failure Modes

- Players optimize the formula instead of the fantasy, producing designs that score well but look absurd.
- A single scalar score collapses the design space onto one optimum.
- Opaque formulas require community reverse engineering; RollerCoaster Tycoon 2's rating rules are documented in detail only through the OpenRCT2 project.
- Scores that contradict intuition (a ride that looks thrilling rates low) make the simulation feel arbitrary.

## Dynamics

- Designs converge on formula sweet spots, such as stopping at the drop and inversion caps that end excitement gains.
- Multiple competing metrics produce distinct design schools, such as cheap versus fast solutions in Zachtronics games.
- When ratings set prices or demand, design quality couples directly to the economy.

## Open Questions

- Can a learned critic rate open-ended designs on qualities like elegance or thrill that hand formulas miss, without becoming a new exploit target?
- Does showing per-term contributions to a score widen or narrow the range of designs players explore?

## Relations

**synergy**

- [Modular assembly](../mechanic/modular-assembly.md): Rating the assembled design closes the build-test loop.
- [Structural integrity](../mechanic/structural-integrity.md): Stress and load ratings turn structural rules into a score (Poly Bridge).

## Backlinks (computed)

**affected by:** [Differentiable simulation](../technique/differentiable-simulation.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md), [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md)

**involved in:** [Automated mechanic discovery](../opportunity/mechanic-discovery-search.md), [Specification programming games](../opportunity/specification-programming-games.md)

**required by:** [Comparative histograms](../mechanic/comparative-histograms.md)

**used by:** [Motorsport Manager](../game/motorsport-manager.md), [Opus Magnum](../game/opus-magnum.md), [PC Building Simulator](../game/pc-building-simulator.md), [Planet Coaster](../game/planet-coaster.md), [Poly Bridge](../game/poly-bridge.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [SpaceChem](../game/spacechem.md), [The Farmer Was Replaced](../game/the-farmer-was-replaced.md)

## Sources

- [Ride rating calculation](../source/src-openrct2-2026-ride-rating-calculation.md)
- [SpaceChem](../source/src-wikipedia-spacechem.md)
- [Opus Magnum](../source/src-wikipedia-opus-magnum.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
