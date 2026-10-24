# X-Plane

*Game* · `x-plane` · status: **sourced**

A flight sim whose flight model computes forces on small elements of each wing, control surface, and propeller from aircraft geometry, used for entertainment and in FAA-approved training devices.

| field | value |
|---|---|
| year | 1995 |
| developer | Laminar Research |
| platforms | PC, Mobile |
| subgenre | Flight sim |
| sim domain | Physical / mechanical, Planetary / natural |
| player role | Operator / pilot |
| agency model | Direct avatar, Design then test |
| time model | Real-time with pause |
| sim scale | Individual |
| fidelity | Professional-grade |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 2 |
| influence | 3 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 1 |
| mechanic count *(computed)* | 8 |

## Summary

A flight sim whose flight model computes forces on small elements of each wing, control surface, and propeller from aircraft geometry, used for entertainment and in FAA-approved training devices.

## Core Loop

pick or design an aircraft -> set location and weather -> fly by hand or autopilot -> blade-element forces respond to geometry and air -> land -> revise the aircraft in Plane Maker

## Design Notes

X-Plane uses blade element theory: wings, control surfaces, and propellers are split into elements and aerodynamic forces are computed on each from geometry, rather than looked up from performance tables, so an aircraft drawn in the bundled Plane Maker flies according to its shape. That approach underpins its use in FAA-approved training systems when paired with suitable hardware. A plugin SDK exposes simulator data for instruments, cockpits, and external hardware.

## Relations

**uses**

- [Flight aerodynamics](../mechanic/flight-aerodynamics.md) (core): Blade element theory splits wings, control surfaces, and propellers into small elements and computes aerodynamic forces on each from geometry and physical parameters.
- [Modular assembly](../mechanic/modular-assembly.md) (supporting): Plane Maker lets users define aircraft geometry and components and then fly the result in the simulator.
- [Weather](../mechanic/weather.md) (supporting): X-Plane 12 reworked clouds, turbulence, and atmospheric effects, and version 12.3 added a weather-radar system.
- [Procedural checklists](../mechanic/procedural-checklists.md) (supporting)
- [Embodied skill control](../mechanic/embodied-skill-control.md) (supporting)
- [Modding API](../mechanic/modding-api.md) (supporting): The plugin SDK lets developers read simulator data and add instruments, cockpit interfaces, and hardware support.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

## Sources

- [X-Plane (simulator)](../source/src-wikipedia-x-plane.md)

---
Provenance: created in run `2026-10-24-catalog-gf`; reviewed in `2026-10-24-review-fixes`.
