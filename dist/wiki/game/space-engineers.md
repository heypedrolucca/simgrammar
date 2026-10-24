# Space Engineers

*Game* · `space-engineers` · status: **sourced**

A voxel sandbox where players mine asteroids and planets and build ships and stations block by block, with every block carrying mass, inertia, power needs, and damage under Newtonian physics.

| field | value |
|---|---|
| year | 2013 |
| year full release | 2019 |
| developer | Keen Software House |
| platforms | PC, Console |
| subgenre | Sandbox world |
| subgenre secondary | Construction / engineering, Space sim |
| sim domain | Physical / mechanical, Cosmic / space, Industrial / logistics |
| player role | Engineer / designer |
| agency model | Direct avatar, Programmatic |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Systemic |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player, Co-op, Competitive |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C07 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 14 |

## Summary

A voxel sandbox where players mine asteroids and planets and build ships and stations block by block, with every block carrying mass, inertia, power needs, and damage under Newtonian physics.

## Core Loop

mine ore from voxel asteroids and planets -> refine and assemble components -> weld blocks into ship or station grids -> power and pilot under inertia -> collide, fight, or deform -> repair and redesign

## Design Notes

Space Engineers treats a ship as a grid of blocks where each block has mass, inertia, and hit points, and functional blocks (thrusters per direction, gyroscopes, reactors, cockpits) decide whether it can move at all; there is no ship stat sheet apart from the blocks. Collisions and weapons deform or destroy individual blocks, and terrain is editable voxels, so construction, mining, and damage share one physical model. Survival mode adds a refine-assemble production chain and suit oxygen and energy, and an in-game programmable block lets players automate ships with scripts.

## Relations

**uses**

- [Modular assembly](../mechanic/modular-assembly.md) (core): Ships and stations are small or large grids of armor and functional blocks; thrusters only push along their facing, so thrust coverage on each axis, gyroscope count, and power supply decide handling.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (core): Volumetric physics gives every block mass and inertia; ships drift under Newtonian motion with optional inertia dampeners, and gravity generators and planets pull loose objects.
- [Voxel destruction](../mechanic/voxel-destruction.md) (core): Asteroid and planet voxels can be drilled and carved, and armor blocks deform or break block by block under collisions and weapon fire.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Hand drills and ship drills mine ore from voxel deposits.
- [Production chains](../mechanic/production-chain.md) (supporting): Refineries turn ore into ingots and assemblers turn ingots into components for welding.
- [Conveyor transport](../mechanic/conveyor-transport.md) (supporting): Conveyor blocks connect inventories so refineries, assemblers, and cargo containers move items automatically, with sorters filtering flow.
- [Power grid](../mechanic/power-grid.md) (supporting): Reactors, solar panels, batteries, and hydrogen engines feed every functional block on a grid; unpowered blocks stop.
- [Player programming](../mechanic/player-programming.md) (supporting): The programmable block runs player-written C# scripts that read and command blocks on the grid.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): Sensors, timer blocks, and event controllers trigger block actions without code.
- [Survival meters](../mechanic/survival-meters.md) (supporting): In survival the suit tracks health, energy, oxygen, and hydrogen.
- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (supporting): Air vents pressurize sealed rooms with oxygen; breaches depressurize them.
- [Blueprints](../mechanic/blueprints.md) (supporting): Grids save as blueprints that a projector block displays for welding and that are shared on Steam Workshop.
- [Modding API](../mechanic/modding-api.md) (supporting): A C# modding API, Workshop, and mod.io support custom blocks and logic.
- [Subsystem damage](../mechanic/subsystem-damage.md) (supporting): Each block has hit points, and damaged functional blocks such as thrusters, reactors, and gyroscopes stop working until welded back.

## Sources

- [Space Engineers](../source/src-wikipedia-space-engineers.md)
- [Space Engineers on Steam](../source/src-steam-2026-space-engineers.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
