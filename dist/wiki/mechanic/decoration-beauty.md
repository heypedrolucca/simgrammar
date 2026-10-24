# Decoration and beauty

*Mechanic* · `decoration-beauty` · status: **sourced**

Decorative objects and scenery carry beauty values that are aggregated over tiles, rooms, or radii and feed agent mood or ratings.

| field | value |
|---|---|
| aliases | beauty score, scenery rating, environment score |
| family | Space & construction |
| substrate | Cellular grid, Aggregate stocks |
| math basis | Optimization, Utility / decision theory |
| feedback | Reinforcing (positive) |
| player interface | Placement, Observation only |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Caesar III](../game/caesar-3.md) |
| earliest year *(computed)* | 1998 |
| prevalence *(computed)* | 11 |
| prevalence share *(computed)* | 0.063 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 3 |
| technique exposure *(computed)* | 1.375 |

## Definition

Each decorative object, floor, or surface has a beauty value, and dirt, corpses, and filth are negative. The game aggregates values over a radius or a room and samples the result for agents or attractions. In RimWorld a room's beauty is total beauty divided by a weighted size (the size if above 40 tiles, otherwise 20 plus half the size), graded from hideous (below -3.5) to unbelievably beautiful (100 or more), and combined with wealth, space, and cleanliness into impressiveness that sets mood thoughts; colonists also get mood from the beauty around them. In RollerCoaster Tycoon 2, as documented by OpenRCT2, scenery within 5 tiles of a ride's station adds 0.05 excitement per item up to 47 items. The Sims 4 rates rooms by an environment score from decor. Inputs are placed objects; outputs are mood, ratings, or prices.

## Player Experience

Cosmetic choices get a mechanical payoff, so players dress up rooms and paths and watch moods or ride ratings rise. The tension is between beautiful and efficient: every statue costs resources and floor space that production could use.

## Design Levers

- beauty value and cost of each object, and negative values for filth and industry
- aggregation rule: per tile, per radius, per room, with or without size normalization
- caps or diminishing returns on how much decoration counts
- which systems consume beauty: mood, ratings, prices, or visitor choice
- per-agent taste variation by trait or culture

## Failure Modes

- One object with the best beauty per cost dominates, so players spam it regardless of how the space looks.
- Proximity rules that count only a hot spot, such as scenery near a ride station in RollerCoaster Tycoon 2, reward decorating one spot and ignoring the rest of the ride.
- Beauty values that disagree with the art (an ugly-looking object rated beautiful) break trust in the system.
- If the score is hidden, decoration reads as optional and the mechanic goes unused.

## Dynamics

- Traffic creates filth that lowers beauty, which creates cleaning jobs that compete for labor.
- In RimWorld, decoration raises colony wealth, and wealth raises raid points, so beauty carries a security cost.
- Prosperity funds decoration, and decoration raises mood or ratings and so prosperity, a slow upgrade treadmill.

## Open Questions

- Can a vision model score the composition of a space instead of summing per-object beauty values, and would players accept its judgment?
- Does generated decor reduce the asset cost enough to make beauty a deep system rather than a spam target?

## Relations

**synergy**

- [Room recognition](../mechanic/room-recognition.md): Room quality depends on furnishings and beauty, rewarding interior design.

## Backlinks (computed)

**affected by:** [3D Gaussian Splatting](../technique/gaussian-splatting.md), [Neural rendering in the graphics pipeline](../technique/neural-rendering-shaders.md), [Text- and image-to-3D asset generation](../technique/text-to-3d-assets.md)

**involved in:** [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

**used by:** [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Caesar III](../game/caesar-3.md), [Farthest Frontier](../game/farthest-frontier.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Planet Coaster](../game/planet-coaster.md), [RimWorld](../game/rimworld.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [The Sims](../game/the-sims.md), [Two Point Hospital](../game/two-point-hospital.md), [Valheim](../game/valheim.md), [Zoo Tycoon](../game/zoo-tycoon.md)

## Sources

- [Room](../source/src-rimworldwiki-2026-room.md)
- [Ride rating calculation](../source/src-openrct2-2026-ride-rating-calculation.md)
- [Raid points](../source/src-rimworldwiki-2026-raid-points.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
