# DCS World

*Game* · `dcs-world` · status: **sourced**

A combat flight sim platform of study-level aircraft modules with clickable cockpits and modeled subsystems, flown in missions and on multiplayer servers built with a Lua-scriptable mission editor.

| field | value |
|---|---|
| aliases | Digital Combat Simulator, DCS |
| year | 2008 |
| developer | Eagle Dynamics |
| platforms | PC |
| subgenre | Flight sim |
| subgenre secondary | Wargame / military sim |
| sim domain | Military / conflict, Physical / mechanical |
| player role | Operator / pilot |
| agency model | Direct avatar |
| time model | Real-time with pause |
| sim scale | Individual |
| fidelity | Professional-grade |
| perspective | First-person |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player, Co-op, Competitive |
| modding | Scripting |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 3 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 10 |

## Summary

A combat flight sim platform of study-level aircraft modules with clickable cockpits and modeled subsystems, flown in missions and on multiplayer servers built with a Lua-scriptable mission editor.

## Core Loop

pick a module and mission -> cold start through cockpit switches -> fly and navigate -> find targets with sensors -> employ weapons and survive defenses -> recover and land -> debrief

## Design Notes

DCS treats each aircraft as a set of subsystems (engines, fuel, electrical, hydraulics, radios, sensors) operated through individually clickable cockpit controls, so procedures and failures follow from system state rather than scripts. Its fidelity reaches professional use: the U.S. Air Force's 355th Training Squadron has used the A-10C module, and French and Ukrainian pilots have trained on modules. The business model is a free base with two aircraft and two maps, with paid aircraft and map modules from Eagle Dynamics and third parties sharing one client.

## Relations

**uses**

- [Flight aerodynamics](../mechanic/flight-aerodynamics.md) (core): Aircraft modules are built from real-world data; the F-16C uses a professional flight model with a fly-by-wire flight control system.
- [Procedural checklists](../mechanic/procedural-checklists.md) (core): Clickable cockpits operate modeled engines, fuel, electrical, hydraulic, and radio systems, so start-up and weapon employment follow real procedures.
- [Military operations](../mechanic/military-operations.md) (core): Missions pit aircraft against air and ground units with sensors and weapons; users host PvE and PvP servers running their own missions.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (supporting)
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): The mission editor builds single-player and multiplayer missions with Lua scripting.
- [Modding API](../mechanic/modding-api.md) (supporting): Lua mission scripting and third-party module development extend the platform.
- [Weather](../mechanic/weather.md) (supporting)
- [Projectile ballistics](../mechanic/projectile-ballistics.md) (supporting): Missiles, bombs, and gun rounds fly as simulated projectiles, so release parameters such as speed, altitude, and range decide hits.
- [Subsystem damage](../mechanic/subsystem-damage.md) (supporting): Modules carry damage models, revised over the platform's development, so hits degrade the aircraft's modeled systems and how it flies.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

## Claims

- The `year` value records 2008, when DCS: Black Shark, the first standalone DCS title, was released; the free DCS World platform entered open beta in May 2012. *(confidence: medium)* [[16](../source/src-wikipedia-dcs-world.md)]

## Sources

- [DCS World](../source/src-wikipedia-dcs-world.md)

---
Provenance: created in run `2026-10-24-catalog-gf`; reviewed in `2026-10-24-review-fixes`.
