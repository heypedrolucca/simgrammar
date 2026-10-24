# Adjacency scoring

*Mechanic* · `adjacency-scoring` · status: **asserted**

A placement's value is computed from a table of bonuses and penalties for the placements around it.

| field | value |
|---|---|
| aliases | adjacency bonus, neighbor bonus, synergy radius |
| family | Space & construction |
| substrate | Cellular grid, Rule system |
| math basis | Optimization, Combinatorics |
| feedback | Reinforcing (positive) |
| player interface | Placement |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| requires | [Building placement](../mechanic/free-placement.md) |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [M.U.L.E.](../game/mule.md) |
| earliest year *(computed)* | 1983 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each placeable type has a table of signed effects from neighbor types within a footprint, ring, or radius. When an object is placed (and in some games when a neighbor later changes), its value is recomputed as a base plus the sum of qualifying neighbor contributions, sometimes capped or with diminishing returns. The value feeds score, production yield, or desirability. Islanders (2019) previews the points a building will earn from nearby buildings before it is placed, and points unlock new building packs. Civilization VI (2016) gives districts adjacency yields from neighboring terrain and districts, such as science for a Campus next to mountains and gold for a Commercial Hub next to a river. Tile-laying builders such as Dorfromantik score matching edges between neighboring tiles. The state is the placement map plus the effect table; the update is a local sum.

## Player Experience

Every placement is a small search problem with a visible answer. Players hover candidates to read preview numbers, reserve tiles for pieces they expect later, and feel clever when one placement lights up several neighbors. Penalties make them keep nuisances apart, so layouts acquire districts and buffers.

## Design Levers

- neighborhood shape: touching tiles, ring, or radius, and whether diagonals count
- size and asymmetry of the effect table, including negative pairs that force separation
- stacking rule for multiple neighbors: linear, capped, or diminishing
- whether values freeze at placement or recompute when neighbors change later
- how much of the calculation the preview shows before commitment

## Failure Modes

- Once players find the best repeating cluster, every settlement uses the same stamp and the spatial puzzle ends.
- Positive-only tables make maximum density always optimal, removing any reason to spread out.
- Hidden or partly shown effect tables push players to wikis and calculators to plan placements.
- Retroactive recomputation changes the value of old placements in ways players did not intend and cannot trace.

## Dynamics

- Clusters of mutually reinforcing types form districts, and nuisance types get pushed to edges or buffers.
- Scarce space turns adjacency into a packing problem in which early placements constrain later ones.
- When adjacency feeds unlocks or income, early good clusters compound into a lead.

## Open Questions

- Can a learned model of layout quality replace hand-written pairwise tables while staying predictable enough to plan against?
- What table size and asymmetry keep a solved cluster template from appearing within a few hours of play?

## Relations

**requires**

- [Building placement](../mechanic/free-placement.md)

## Backlinks (computed)

**involved in:** [Learned build assist for cities](../opportunity/learned-build-assist.md), [Placement that tells stories](../opportunity/placement-that-tells-stories.md)

**used by:** [Anno 117: Pax Romana](../game/anno-117.md), [Islanders](../game/islanders.md), [M.U.L.E.](../game/mule.md), [The Farmer Was Replaced](../game/the-farmer-was-replaced.md)

---
Provenance: created in run `2026-10-24-taxonomy-m4`.
