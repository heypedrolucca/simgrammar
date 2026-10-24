# FTL: Faster Than Light

*Game* · `ftl` · status: **sourced**

A roguelite starship sim where the player allocates reactor power and directs crew through room-level oxygen, fire, breach, and system-damage simulation while fleeing a rebel fleet across eight sectors.

| field | value |
|---|---|
| aliases | FTL |
| year | 2012 |
| developer | Subset Games |
| platforms | PC, Mobile |
| subgenre | Space sim |
| sim domain | Cosmic / space, Military / conflict |
| player role | Commander |
| agency model | Direct unit control, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Household / crew |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Campaign |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 3 |
| influence | 3 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 6 |
| mechanic count *(computed)* | 14 |

## Summary

A roguelite starship sim where the player allocates reactor power and directs crew through room-level oxygen, fire, breach, and system-damage simulation while fleeing a rebel fleet across eight sectors.

## Core Loop

jump to a beacon -> resolve an event or fight -> allocate reactor power and direct crew under fire -> repair breaches, fires, and systems -> spend scrap on upgrades -> stay ahead of the rebel fleet to the flagship

## Design Notes

FTL models a ship as rooms with oxygen levels, doors, systems, and crew positions; hits create breaches, fires, and system damage that crew must walk to and repair, so a combat is a spatial triage problem as well as a damage race. The reactor's power bars are the central budget shared by shields, engines, weapons, oxygen, and medbay, and the player shifts them during paused combat. Manual reactor power allocation and per-system damage that removes capacity until repaired have no dedicated taxonomy ids (power-grid is the closest fit); both are recorded as new-mechanic proposals.

## Relations

**uses**

- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (core): Each room has an oxygen level that equalizes through open doors, drains through hull breaches and opened airlocks, and is refilled by the oxygen system; crew suffocate in empty rooms.
- [Fire spread](../mechanic/fire-spread.md) (supporting): Hits and events start fires that spread between rooms, damage systems and crew, and burn oxygen; crew extinguish them or the player vents the room.
- [Crisis countdown](../mechanic/crisis-countdown.md) (core): Each jump advances the rebel fleet across the sector map; overtaken beacons yield hard fights and no reward, forcing a trade between exploration and speed.
- [Permadeath](../mechanic/permadeath.md) (core): Losing the ship or all crew ends the run and deletes the save; dead crew members are gone.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Crew gain skill in piloting, engines, shields, weapons, repair, and combat through use, improving station bonuses.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Eight species have fixed traits such as faster repair, fire immunity, or extra combat damage.
- [Unit commands](../mechanic/unit-commands.md) (core): The player moves crew between rooms to man stations, repair systems and breaches, fight boarders, and put out fires; crew act on their own only within the room they occupy.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Each sector is a generated map of about twenty beacons with stores, hazards, and events.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Beacon events offer text choices, with extra options unlocked by specific crew, systems, or equipment, and some quests chain across beacons.
- [Fog of war](../mechanic/fog-of-war.md) (supporting): Beacon contents are unknown until visited unless revealed by upgrades such as long-range scanners.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting): Pause is the main tactical tool for issuing orders mid-combat.
- [Power allocation](../mechanic/power-allocation.md) (core): Reactor power bars are assigned among shields, engines, weapons, oxygen, medbay, and other systems, usually while paused in combat; each system caps how many bars it accepts, and damage removes usable bars until crew repair it.
- [Statistical combat resolution](../mechanic/stat-combat-resolution.md) (supporting): Each weapon shot rolls against the target's evasion, shield layers absorb hits, and hits damage the room and the system inside it.
- [Subsystem damage](../mechanic/subsystem-damage.md) (core): Hits damage the system in the struck room (shields, weapons, engines, oxygen, piloting), removing its usable power bars until crew repair it, and the player targets enemy rooms to disable specific systems.

## Sources

- [FTL: Faster Than Light](../source/src-wikipedia-ftl.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
