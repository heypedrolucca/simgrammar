# Kerbal Space Program

*Game* · `kerbal-space-program` · status: **sourced**

A space flight sim where the player assembles rockets from parts and flies them under patched-conic orbital physics and atmospheric aerodynamics through a scaled-down planetary system.

| field | value |
|---|---|
| aliases | KSP |
| year | 2011 |
| year full release | 2015 |
| developer | Squad |
| platforms | PC, Console |
| subgenre | Space sim |
| subgenre secondary | Construction / engineering |
| sim domain | Cosmic / space, Physical / mechanical |
| player role | Engineer / designer |
| agency model | Design then test, Direct avatar |
| time model | Real-time with pause |
| sim scale | Interplanetary+ |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Total conversion |
| production tier | Indie |
| agent count order | None |
| emergence | 3 |
| influence | 4 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 15 |

## Summary

A space flight sim where the player assembles rockets from parts and flies them under patched-conic orbital physics and atmospheric aerodynamics through a scaled-down planetary system.

## Core Loop

assemble a craft from parts -> launch and stage through the atmosphere -> plan maneuver nodes and burn for orbit or transfer -> land, dock, or crash -> return science, funds, and reputation -> unlock parts and design a more ambitious craft

## Design Notes

Stock orbits use a patched-conic approximation: a vessel is attracted by one body at a time and switches at sphere-of-influence boundaries, so there are no Lagrange points, but coasting vessels can be propagated on rails during time warp. Vessels are trees of parts joined by joints of limited strength, so mass distribution, thrust placement, and staging order decide whether a design flies, wobbles, or tears apart. Failure (stranded or dead Kerbals, debris) is a source of player stories rather than a hard stop, and Career mode layers funds, reputation, and contracts on top of the physics sandbox.

## Relations

**uses**

- [Orbital mechanics](../mechanic/orbital-mechanics.md) (core): Patched conics: a vessel orbits one body at a time and switches at sphere-of-influence boundaries; maneuver nodes preview delta-v and the resulting trajectory; planets ride fixed rails rather than n-body motion.
- [Modular assembly](../mechanic/modular-assembly.md) (core): Craft are built in the Vehicle Assembly Building or Spaceplane Hangar from pods, tanks, engines, decouplers, wings, and science parts; part order sets the staging sequence, and each stage's mass, thrust, and fuel set its delta-v.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (core): Each part is a rigid body joined to its parent with a joint of limited strength; excess force breaks joints, so tall stacks wobble and hard impacts shed parts or kill Kerbals.
- [Flight aerodynamics](../mechanic/flight-aerodynamics.md) (supporting): Drag, lift, and control surfaces govern ascent profiles, spaceplanes, and aerobraking.
- [Heat transfer](../mechanic/heat-transfer.md) (supporting): Atmospheric entry heats parts; heat shields absorb it and overheated parts are destroyed.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Science from experiments unlocks part nodes in Science and Career modes.
- [Contracts and orders](../mechanic/contracts-orders.md) (supporting): Career contracts pay for objectives such as reaching an orbit or testing a part, with deadlines and penalties.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Career funds pay for parts, fuel, crew, and facility upgrades; contract payouts are the income.
- [Reputation](../mechanic/reputation.md) (supporting): Career reputation rises with completed contracts and falls with failures and Kerbal deaths.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (supporting): Manual ascents, landings, and docking reward piloting skill; SAS assists attitude hold.
- [Permadeath](../mechanic/permadeath.md) (supporting): Kerbals die in crashes and EVA accidents; Career mode costs reputation for deaths, and a difficulty option sets whether lost crews respawn.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Drills mine ore on planets and asteroids that converters turn into fuel, a system adopted from mods.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting): On-rails time warp skips long coasts; physics warp speeds powered flight at reduced stability.
- [Modding API](../mechanic/modding-api.md) (supporting): C# plugins and part configs extend the game; mods such as Real Solar System and Principia replace the planetary system and the orbital model.
- [Subsystem damage](../mechanic/subsystem-damage.md) (supporting): Parts are destroyed individually by impact or overheating, removing their engines, tanks, or controls from the craft.

## Sources

- [Kerbal Space Program](../source/src-wikipedia-kerbal-space-program.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
