# Besiege

*Game* · `besiege` · status: **sourced**

A physics construction game where the player builds medieval siege machines from blocks, wheels, and weapons, then drives them against castles and armies in objective levels or a sandbox.

| field | value |
|---|---|
| year | 2015 |
| year full release | 2020 |
| developer | Spiderling Studios |
| platforms | PC, Console, Handheld, Mobile |
| subgenre | Construction / engineering |
| subgenre secondary | Physics sandbox |
| sim domain | Physical / mechanical, Military / conflict |
| player role | Engineer / designer |
| agency model | Design then test, Direct avatar |
| time model | Run on demand |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Co-op, Competitive, Async / shared content |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C07 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

A physics construction game where the player builds medieval siege machines from blocks, wheels, and weapons, then drives them against castles and armies in objective levels or a sandbox.

## Core Loop

read the level objective -> attach blocks, wheels, hinges, and weapons to a starting block -> bind controls -> run the level and drive the machine -> watch it work, flip, or break apart -> revise the design

## Design Notes

Machines grow from a single starting block, and each attached block is a rigid body joined to its neighbor by a breakable joint; powered wheels, hinges, pistons, and springs are bound to player keys, so a machine is both a structure and a control scheme. Designs fail by tipping, tearing at weak joints, or setting themselves alight, which is much of the appeal. Logic blocks (timers, logic gates, sensors) added later let machines act without input, and the level editor and PC multiplayer turned designs into contests.

## Relations

**uses**

- [Modular assembly](../mechanic/modular-assembly.md) (core): Machines are built outward from a starting block using 70+ blocks such as wooden blocks, powered wheels, hinges, pistons, cannons, bombs, flamethrowers, and balloons; block placement sets mass distribution and what each key does.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (core): Each block is a physics body connected by joints that break under excess force, so machines buckle, tip, or tear apart while driving and fighting.
- [Scenario objectives](../mechanic/scenario-objectives.md) (core): 55 campaign levels across four islands set goals such as destroying buildings, defeating troops, or solving puzzles with magical artifacts.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (supporting): The player drives the finished machine in real time with keys bound to its powered parts.
- [Material interactions](../mechanic/material-interactions.md) (supporting): Fire spreads across wooden blocks and enemy buildings; bombs and cannons break blocks.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): Timers, logic gates, and proximity sensors simulate key presses so machines can automate sequences.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Machines and levels are shared on Steam Workshop.
- [Modding API](../mechanic/modding-api.md) (supporting): An in-game modloader supports community mods with new blocks and logic.

## Sources

- [Besiege (video game)](../source/src-wikipedia-besiege.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
