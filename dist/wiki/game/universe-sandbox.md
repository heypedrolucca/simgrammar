# Universe Sandbox

*Game* · `universe-sandbox` · status: **sourced**

A space physics sandbox where the player builds and alters star systems and watches Newtonian n-body gravity, collisions, and simplified planetary climate play out at adjustable speed.

| field | value |
|---|---|
| aliases | Universe Sandbox 2, Universe Sandbox² |
| year | 2008 |
| developer | Dan Dixon; Giant Army |
| platforms | PC, VR |
| subgenre | Physics sandbox |
| subgenre secondary | Space sim |
| sim domain | Cosmic / space, Planetary / natural |
| player role | Observer / gardener |
| agency model | Policy / parameter, Design then test |
| time model | Real-time with pause |
| sim scale | Interplanetary+ |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player, Async / shared content |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 1 |
| cluster *(computed)* | C07 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 7 |

## Summary

A space physics sandbox where the player builds and alters star systems and watches Newtonian n-body gravity, collisions, and simplified planetary climate play out at adjustable speed.

## Core Loop

load or build a system -> set masses, positions, and time step -> run gravity forward -> watch orbits, collisions, and climate respond -> tweak parameters or add bodies

## Design Notes

Every body attracts every other under Newtonian n-body gravity, so the player can test questions such as what happens if a star passes the Solar System and see the answer rather than read it. The current version (a rewrite released as Universe Sandbox 2 in 2014 and renamed in 2018, still in early access) adds composition from a small set of materials, collisions that leave molten craters, and a climate layer where sea ice tracks axial tilt and oceans boil near a star. The simulation is an instrument for parameter sweeps; there are no goals or agents.

## Relations

**uses**

- [Orbital mechanics](../mechanic/orbital-mechanics.md) (core): Newtonian n-body gravity acts between all bodies; the player edits mass, density, radius, and velocity and watches orbits, ejections, spin-apart breakup, and collisions follow.
- [Pause and speed control](../mechanic/variable-speed.md) (core): Simulation speed runs from real time to years per second and can be paused; larger time steps trade against accuracy, so fast runs can diverge from slow ones.
- [Planetary climate](../mechanic/planetary-climate.md) (supporting): Surface temperature, sea ice, and oceans respond to stellar distance and axial tilt; moving a planet can freeze or boil it.
- [Heat transfer](../mechanic/heat-transfer.md) (supporting): Collisions and stellar irradiance heat bodies, shown as molten surfaces and temperature maps.
- [Terraforming](../mechanic/terraforming.md) (supporting): Planets are composed from materials such as water, rock, iron, and gases, and oceans and mountains can be shaped.
- [Data overlays](../mechanic/data-overlays.md) (supporting): Orbit trails and surface temperature maps expose state that is otherwise invisible.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Player-made simulations are shared on Steam Workshop.

## Sources

- [Universe Sandbox](../source/src-wikipedia-universe-sandbox.md)
- [Universe Sandbox on Steam](../source/src-steam-2026-universe-sandbox.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
