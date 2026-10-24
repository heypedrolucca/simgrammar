# The Farmer Was Replaced

*Game* · `the-farmer-was-replaced` · status: **sourced**

A programming game in which the player writes Python-like code for a farming drone on a grid farm, where every operation costs simulated ticks, and harvests crops to buy unlocks for language features, farm size, more drones, and new crops.

| field | value |
|---|---|
| year | 2023 |
| year full release | 2025 |
| developer | Timon Herzog |
| platforms | PC |
| subgenre | Programming sim |
| subgenre secondary | Farming sim |
| sim domain | Computational / abstract, Biological / ecological |
| player role | Programmer |
| agency model | Programmatic |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Abstract |
| perspective | Isometric |
| win structure | Completion |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 2 |
| influence | 1 |
| influenced by |  |
| cluster *(computed)* | C06 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 6 |

## Summary

A programming game in which the player writes Python-like code for a farming drone on a grid farm, where every operation costs simulated ticks, and harvests crops to buy unlocks for language features, farm size, more drones, and new crops.

## Core Loop

write a drone program -> execute it on the farm grid -> plant, water, and harvest crops -> spend harvests on unlocks -> new language features and crops change what code is worth writing -> optimize for speed and leaderboard times

## Design Notes

The Farmer Was Replaced teaches programming by making farm labor too slow to do any other way: the drone does nothing unless code tells it to, and the language itself is unlocked piecemeal (loops, variables, functions, lists, dictionaries) with farm expansion and new crops. Execution is metered in simulated ticks rather than real CPU: literals and assignment are free, arithmetic and getters cost 1 tick, and a successful move() costs 200, so optimization means reducing drone actions more than reducing statements. Crops add algorithmic puzzles: polyculture companions requested within three moves multiply yield, harvesting the sunflower with the most petals (out of at least ten) gives eight times the power that doubles drone speed, and mazes and dinosaurs need search-style code. Leaderboards run the player's program as fixed-start simulations totaling at least two hours and score the average time. Code lives in .py files that external editors can edit.

## Sources

- src-steam-2026-the-farmer-was-replaced
- src-gamesmarket-2025-the-farmer-was-replaced-1-0
- src-tfwrwiki-2026-operation-costs
- src-tfwrwiki-2026-leaderboard
- src-tfwrwiki-2026-polyculture
- src-tfwrwiki-2026-sunflowers
- src-tfwrwiki-2026-unlocks

## Relations

**uses**

- [Player programming](../mechanic/player-programming.md) (core): A Python-like language stored in .py files drives the drone; every operation has a tick cost (arithmetic 1, a successful move 200, a failed action 1) that scales with the speed factor, and Megafarm adds more drones.
- [Crop cultivation](../mechanic/crop-cultivation.md) (core): Grass, bushes, trees, carrots, pumpkins, cactus, and sunflowers are planted, grown, and harvested by the drone, with Watering and Fertilizer unlocks that act on growth.
- [Tech tree](../mechanic/tech-tree.md) (core): Harvested resources buy unlocks with prerequisites, including farm expansion, speed, loops, variables, functions, lists, dictionaries, polyculture, mazes, dinosaurs, and the leaderboard.
- [Adjacency scoring](../mechanic/adjacency-scoring.md) (supporting): Under polyculture, grass, bushes, trees, and carrots request a different companion plant on a tile within three moves, found with get_companion(); planting it multiplies yield, 5x before upgrades and doubling per upgrade.
- [Design performance rating](../mechanic/design-performance-rating.md) (supporting): Leaderboards run the player's program from fixed starts until a resource target is met, repeated to at least two hours, and score the average completion time.
- [Execution budget](../mechanic/execution-budget.md) (supporting): Every operation costs simulated ticks (arithmetic 1, a successful move() 200, a failed action 1), so optimizing means cutting drone actions more than statements.

## Backlinks (computed)

**precedent for:** [Specification programming games](../opportunity/specification-programming-games.md)

## Claims

- Early access began on 2023-02-10, and version 1.0 released on 2025-10-10 with multiple drones and a revamped tech tree, published by Metaroot. *(confidence: high)* [[46](../source/src-steam-2026-the-farmer-was-replaced.md), [47](../source/src-gamesmarket-2025-the-farmer-was-replaced-1-0.md)]

## Sources

- [The Farmer Was Replaced](../source/src-steam-2026-the-farmer-was-replaced.md)
- [Rows of corn, lines of code: Swiss automation game The Farmer Was Replaced launches 10 October](../source/src-gamesmarket-2025-the-farmer-was-replaced-1-0.md)
- [Operation Costs](../source/src-tfwrwiki-2026-operation-costs.md)
- [Leaderboard](../source/src-tfwrwiki-2026-leaderboard.md)
- [Polyculture](../source/src-tfwrwiki-2026-polyculture.md)
- [Sunflowers](../source/src-tfwrwiki-2026-sunflowers.md)
- [Unlocks](../source/src-tfwrwiki-2026-unlocks.md)

---
Provenance: created in run `2026-10-24-catalog-gh`.
