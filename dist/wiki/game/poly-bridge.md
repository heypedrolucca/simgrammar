# Poly Bridge

*Game* · `poly-bridge` · status: **sourced**

A bridge-building puzzle game where the player places beams and roads from materials with different costs and strengths under a budget, then runs a physics test as vehicles cross.

| field | value |
|---|---|
| year | 2015 |
| year full release | 2016 |
| developer | Dry Cactus |
| platforms | PC, Mobile |
| subgenre | Construction / engineering |
| sim domain | Physical / mechanical |
| player role | Engineer / designer |
| agency model | Design then test |
| time model | Run on demand |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Async / shared content |
| modding | Content |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 7 |

## Summary

A bridge-building puzzle game where the player places beams and roads from materials with different costs and strengths under a budget, then runs a physics test as vehicles cross.

## Core Loop

read anchors, vehicles, and budget -> place beams and roads from materials -> run the simulation -> watch stress and failures -> trim cost or reinforce -> submit to leaderboard

## Design Notes

Bridges are trusses of joints and members in a side-view plane; each material (road, wood, steel, rope, cable, hydraulics) has its own cost, strength, and mass, and crossing vehicles load the structure until members exceed their limit and snap. The puzzle is minimizing cost under a level budget while keeping stress below breaking, and hydraulic phases tied to vehicle checkpoints let bridges move in sync with traffic. Failed runs are free to repeat, so the loop is fast iteration against a stress readout.

## Relations

**uses**

- [Structural integrity](../mechanic/structural-integrity.md) (core): Every member carries tension or compression shown as a stress color; a member past its material limit breaks and the load redistributes, often cascading into collapse.
- [Modular assembly](../mechanic/modular-assembly.md) (core): Bridges are built from road, wood, steel, rope, cable, and hydraulic members connected at joints; materials trade cost against strength and weight.
- [Design performance rating](../mechanic/design-performance-rating.md) (core): A level passes when its vehicles reach their flags; total material cost against the level budget is the measure of a good solution, and Steam leaderboards compare results.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (supporting): Cars, trucks, and other vehicles are physics bodies whose mass and speed load the bridge.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Levels fix anchor points, allowed materials, budget, and vehicle routes.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): A multi-phase hydraulics controller fires pistons when vehicles reach checkpoints.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Sandbox designs are published as Workshop levels, and test runs export as GIF replays.

## Backlinks (computed)

**precedent for:** [Quality-diversity scenario libraries](../opportunity/qd-scenario-libraries.md)

## Sources

- [Poly Bridge](../source/src-wikipedia-poly-bridge.md)
- [Poly Bridge on Steam](../source/src-steam-2026-poly-bridge.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
