# Islanders

*Game* · `islanders` · status: **sourced**

A minimalist placement puzzle in which every building scores points from compatible and incompatible neighbors on a procedural island, and score thresholds unlock new building packs and new islands.

| field | value |
|---|---|
| year | 2019 |
| developer | Grizzly Games |
| platforms | PC, Console, Handheld, VR |
| subgenre | City builder |
| sim domain | Urban |
| player role | Planner / mayor |
| agency model | Zoning / placement |
| time model | Turn-based |
| sim scale | Settlement |
| fidelity | Abstract |
| perspective | Free 3D camera |
| win structure | Score / ranking |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 2 |
| boundary case | True |
| cluster *(computed)* | C11 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 4 |

## Summary

A minimalist placement puzzle in which every building scores points from compatible and incompatible neighbors on a procedural island, and score thresholds unlock new building packs and new islands.

## Core Loop

choose a building from the inventory -> preview its point value from neighbors and terrain -> place it permanently -> score thresholds restock and offer a choice of two packs -> fill the gauge to move to a new island

## Design Notes

Islanders reduces the city builder to its placement rule: no resources, traffic, citizens, or research, only point values from proximity to compatible structures and natural features and penalties for incompatible ones. Placements are permanent, so each choice consumes space, and the run ends when buildings or space run out before the next threshold. It is included as a boundary case for adjacency scoring, since nothing in the world evolves without the player.

## Relations

**uses**

- [Adjacency scoring](../mechanic/adjacency-scoring.md) (core): Each building scores points from nearby compatible buildings and natural features and loses points for incompatible ones; the preview shows the total before placing.
- [Building placement](../mechanic/free-placement.md) (core): Buildings are placed freely on the island and cannot be removed or built over.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (core): Reaching a point threshold restocks the inventory and offers a choice of two building packs; filling the gauge unlocks a new island.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Each island is procedurally generated.

## Backlinks (computed)

**precedent for:** [Placement that tells stories](../opportunity/placement-that-tells-stories.md), [Quality-diversity scenario libraries](../opportunity/qd-scenario-libraries.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

## Sources

- [Islanders (video game)](../source/src-wikipedia-islanders.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
