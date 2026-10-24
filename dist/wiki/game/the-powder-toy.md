# The Powder Toy

*Game* · `the-powder-toy` · status: **sourced**

An open-source falling-sand sandbox where hundreds of elements interact cell by cell under simulated air pressure, heat, gravity, and electricity.

| field | value |
|---|---|
| aliases | TPT |
| year | 2008 |
| developer | The Powder Toy contributors |
| platforms | PC, Mobile, Web |
| subgenre | Physics sandbox |
| sim domain | Physical / mechanical, Computational / abstract |
| player role | Observer / gardener |
| agency model | Design then test, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Micro |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Single-player, Async / shared content |
| modding | Scripting |
| production tier | Hobbyist / free |
| agent count order | None |
| emergence | 4 |
| influence | 2 |
| cluster *(computed)* | C07 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 9 |

## Core Loop

paint elements onto the grid -> unpause the simulation -> watch particles fall, flow, burn, and react under pressure, heat, and electricity -> adjust or add elements -> save and share the build

## Design Notes

The Powder Toy combines a per-particle falling-sand layer with coarser fields for air pressure, air velocity, and heat, so explosions push air, air moves powders, and temperature thresholds change element states such as ice to water to steam. Electricity runs through conductive elements via sparks, and players build working logic gates, engines, and nuclear reactors from them. Element count passed 250 by 2025; the source is GPLv3 and the in-game save browser is the main distribution channel for builds.

## Relations

**uses**

- [Falling-sand materials](../mechanic/falling-sand-materials.md) (core): Each cell holds one particle of an element such as powder, liquid, gas, or solid, which moves by local rules each frame; element types numbered 258 as of February 2025.
- [Material interactions](../mechanic/material-interactions.md) (core): Element pairs react by rule: acid dissolves most materials, acid and base neutralize into salt water, fuels ignite, and neutrons from radioactive elements can drive chain reactions.
- [Heat transfer](../mechanic/heat-transfer.md) (core): Particles carry temperature that conducts to neighbors; melting and boiling thresholds change states, and the heat display shows the field.
- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (core): A coarser grid of air pressure and velocity moves particles and is pushed by explosions and fans and blocked by walls.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): Sparks conduct through metals and semiconductors to power switches, logic gates, and machines built from elements.
- [Fire spread](../mechanic/fire-spread.md) (supporting): Fire and plasma ignite flammable elements and spread through fuel.
- [Content sharing](../mechanic/content-sharing.md) (supporting): An online save browser with votes and comments distributes community builds.
- [Modding API](../mechanic/modding-api.md) (supporting): A Lua API adds elements and automation scripts; the source is GPLv3 on GitHub.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting): The simulation can be paused and stepped frame by frame.

## Backlinks (computed)

**influenced:** [Noita](../game/noita.md)

**precedent for:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md)

## Sources

- [The Powder Toy](../source/src-wikipedia-the-powder-toy.md)
- [The Powder Toy official site](../source/src-powdertoy-2026-official-site.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
