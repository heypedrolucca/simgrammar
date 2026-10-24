# Teardown

*Game* · `teardown` · status: **sourced**

A heist and destruction game set in fully destructible voxel levels where the player plans a route by cutting, smashing, and driving through structures, then races a 60-second alarm timer to grab the targets.

| field | value |
|---|---|
| year | 2020 |
| year full release | 2022 |
| developer | Tuxedo Labs |
| platforms | PC, Console |
| subgenre | Physics sandbox |
| sim domain | Physical / mechanical |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Systemic |
| perspective | First-person |
| win structure | Campaign |
| failure model | Hard restart |
| narrative mode | Authored |
| multiplayer | Single-player, Co-op, Competitive |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

A heist and destruction game set in fully destructible voxel levels where the player plans a route by cutting, smashing, and driving through structures, then races a 60-second alarm timer to grab the targets.

## Core Loop

survey the level -> cut, blast, and ram a route through voxel structures -> stage vehicles and ramps -> trigger the alarm by taking a target -> grab the rest along the planned path before the timer ends

## Design Notes

Every object is made of small voxels with material types (wood, plaster, brick, metal, glass), and disconnected chunks become rigid bodies that fall, roll, and burn, so geometry is a resource the player spends. The design separates an unlimited planning phase from a timed execution phase: picking up a connected target starts a 60-second alarm, so the player engineers shortcuts with tools, explosives, and vehicles before the first grab. Materials resist tools differently, and fire spreads through wood, which turns construction knowledge into route planning.

## Relations

**uses**

- [Voxel destruction](../mechanic/voxel-destruction.md) (core): Levels are made of small voxels whose material sets which tools can break them; the sledgehammer breaks soft materials, the blowtorch cuts metal, and explosives remove volumes.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (core): Voxel chunks cut loose become dynamic bodies with mass that fall, roll, and crush; vehicles and cranes push and lift them.
- [Crisis countdown](../mechanic/crisis-countdown.md) (core): In most heists taking an alarmed target starts a 60-second timer to reach the getaway vehicle, so the route must be prepared during an unlimited setup phase.
- [Fire spread](../mechanic/fire-spread.md) (supporting): Fire spreads across wood and other flammables and can burn targets or open routes; burning structures weaken and fall.
- [Material interactions](../mechanic/material-interactions.md) (supporting): Materials respond differently to each tool and to fire; a fire extinguisher puts fires out.
- [Structural integrity](../mechanic/structural-integrity.md) (supporting): Sections cut off from all supports fall, so removing pillars can drop a floor.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): 40 campaign missions specify targets, optional targets, and conditions such as stealing, destroying, or collecting evidence.
- [Modding API](../mechanic/modding-api.md) (supporting): Lua scripting, a level editor, and Steam Workshop support custom levels, tools, and modes.

## Backlinks (computed)

**precedent for:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md)

## Sources

- [Teardown (video game)](../source/src-wikipedia-teardown.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
