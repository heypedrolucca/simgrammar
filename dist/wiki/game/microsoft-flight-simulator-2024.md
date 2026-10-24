# Microsoft Flight Simulator 2024

*Game* · `microsoft-flight-simulator-2024` · status: **sourced**

The successor to Microsoft Flight Simulator (2020) that adds a career mode of certified aviation jobs, walk-around preflight, revised aircraft systems, and modeled ground surfaces to the streamed whole-Earth flight sim.

| field | value |
|---|---|
| aliases | MSFS 2024 |
| year | 2024 |
| developer | Asobo Studio |
| platforms | PC, Console, VR |
| subgenre | Flight sim |
| sim domain | Physical / mechanical, Planetary / natural, Occupational |
| player role | Operator / pilot |
| agency model | Direct avatar |
| time model | Real-time with pause |
| sim scale | Individual |
| fidelity | High-fidelity |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player, Co-op |
| modding | Scripting |
| production tier | AAA |
| agent count order | ~100 |
| emergence | 2 |
| influence | 1 |
| influenced by | [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md) |
| cluster *(computed)* | C03 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 12 |

## Summary

The successor to Microsoft Flight Simulator (2020) that adds a career mode of certified aviation jobs, walk-around preflight, revised aircraft systems, and modeled ground surfaces to the streamed whole-Earth flight sim.

## Core Loop

choose a career job -> walk around the aircraft for preflight -> start systems -> fly the mission profile (firefighting, rescue, cargo hook, airline) -> earn experience, reputation, and certifications -> unlock specializations

## Design Notes

Career mode turns the 2020 sandbox into a progression game: aerial firefighting, search and rescue, crop dusting, helicopter cargo hook, outsize cargo in the Airbus Beluga, arctic cargo in the A400M, and airline flights are gated by certifications and specializations earned through experience and reputation. Aircraft physics and systems (electrical, fuel, pneumatic, hydraulic) were revised, and stones, gravel, and grass are modeled in 3D and affect wheels. The launch showed the cost of a streamed world: an overwhelmed database cache caused long loads and missing content.

## Relations

**influenced by**

- [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md)

**uses**

- [Flight aerodynamics](../mechanic/flight-aerodynamics.md) (core): Aircraft physics were revised, and ground contact models 3D stones, gravel, and grass that affect wheels during takeoff, landing, and taxi.
- [Contracts and orders](../mechanic/contracts-orders.md) (core): Career jobs include aerial firefighting, search and rescue, crop dusting, helicopter cargo hook, Beluga outsize cargo, A400M arctic cargo, and airline passenger flights.
- [Career ladder](../mechanic/career-ladder.md) (core): Starting from an airport the player chooses, experience earns certifications and specializations that unlock job types.
- [Reputation](../mechanic/reputation.md) (supporting): Career reputation accumulates alongside experience.
- [Procedural checklists](../mechanic/procedural-checklists.md) (supporting): A walk-around preflight handles covers, doors, and service items, and revised electrical, fuel, pneumatic, and hydraulic systems gate start-up.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): The pilot walks around the aircraft on foot during preflight.
- [Weather](../mechanic/weather.md) (supporting)
- [Embodied skill control](../mechanic/embodied-skill-control.md) (supporting)
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting)
- [Modding API](../mechanic/modding-api.md) (supporting)
- [Real-world data feeds](../mechanic/real-world-data-feeds.md) (supporting): The streamed whole-Earth world of the 2020 game continues, and the launch showed the dependence when an overwhelmed database cache caused long loads and missing content.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**deploys:** [ML reconstruction of the planet from aerial imagery](../technique/satellite-world-reconstruction.md)

**precedent for:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

## Sources

- [Microsoft Flight Simulator 2024](../source/src-wikipedia-microsoft-flight-simulator-2024.md)

---
Provenance: created in run `2026-10-24-catalog-gf`; reviewed in `2026-10-24-review-fixes`.
