# Caves of Qud

*Game* · `caves-of-qud` · status: **sourced**

A science-fantasy roguelike RPG with simulated factions, liquids, body parts, and procedurally generated histories, built partly with wave function collapse.

| field | value |
|---|---|
| year | 2015 |
| year full release | 2024 |
| developer | Freehold Games |
| platforms | PC |
| subgenre | Systemic RPG |
| sim domain | Social / interpersonal, Biological / ecological, Physical / mechanical |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Turn-based |
| sim scale | Individual |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Campaign |
| failure model | Permadeath |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 4 |
| influence | 2 |
| boundary case | True |
| core loop | explore generated and handmade zones -> fight, trade, and talk with faction members -> mutate and equip -> uncover generated history -> go deeper |
| cluster *(computed)* | C05 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 9 |

## Design Notes

A roguelike included for its simulation layers: faction reputation that every creature carries, liquids that mix and flow, body-part anatomy, and procedurally generated sultan histories that the world refers to. It is a frequently cited example of wave function collapse in a shipped game.

## Relations

**uses**

- [Reputation](../mechanic/reputation.md) (core): Every creature belongs to factions; the player's standing with each faction decides who attacks, trades, or talks.
- [Simulated history generation](../mechanic/history-generation.md) (core): Generated histories of past sultans are written into the world as lore, shrines, and quests.
- [Procedural terrain](../mechanic/procedural-terrain.md) (core): Zones mix handmade and procedural maps; some generators use wave function collapse.
- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (supporting)
- [Material interactions](../mechanic/material-interactions.md) (supporting)
- [Injury body model](../mechanic/injury-body-model.md) (supporting)
- [Permadeath](../mechanic/permadeath.md) (supporting)
- [Turn structure](../mechanic/turn-structure.md) (supporting)
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting)

## Backlinks (computed)

**deploys:** [Wave Function Collapse and constraint-based tile generation](../technique/wave-function-collapse.md)

## Claims

- Early access began 2015-07-15 and 1.0 released 2024-12-05, published by Kitfox Games. *(confidence: high)* [[12](../source/src-steam-2024-caves-of-qud.md)]
- Caves of Qud is among the shipped games listed as using wave function collapse. *(confidence: medium)* [[13](../source/src-gumin-2016-wavefunctioncollapse.md)]

## Sources

- [Caves of Qud](../source/src-steam-2024-caves-of-qud.md)
- [WaveFunctionCollapse](../source/src-gumin-2016-wavefunctioncollapse.md)

---
Provenance: created in run `2026-10-24-catalog-additions`.
