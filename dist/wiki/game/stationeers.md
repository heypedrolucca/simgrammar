# Stationeers

*Game* · `stationeers` · status: **sourced**

A first-person space station survival game whose core is an atmospheric simulation of gas mixtures, pressure, temperature, and combustion that the player must engineer with pipes, power, and programmable logic.

| field | value |
|---|---|
| year | 2017 |
| developer | RocketWerkz |
| platforms | PC |
| subgenre | Survival sim |
| subgenre secondary | Sandbox world |
| sim domain | Physical / mechanical, Industrial / logistics, Cosmic / space |
| player role | Engineer / designer |
| agency model | Direct avatar, Programmatic |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Systemic |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player, Co-op |
| modding | Content |
| production tier | Indie |
| agent count order | None |
| emergence | 3 |
| influence | 1 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 12 |

## Summary

A first-person space station survival game whose core is an atmospheric simulation of gas mixtures, pressure, temperature, and combustion that the player must engineer with pipes, power, and programmable logic.

## Core Loop

land with a starter kit -> mine and smelt ore -> build an airtight frame -> pipe, filter, and heat a breathable atmosphere -> power and automate with logic chips -> expand while fixing pressure, fire, and temperature failures

## Design Notes

The atmosphere is the main simulated system: each sealed volume and pipe network carries a mix of gases with temperature and pressure, so heating a room raises its pressure, mixing fuel and oxygen can burn or explode, and a pressure difference across a wall can blow it out. Survival needs are deliberately front-loaded; later play is building plant that keeps the atmosphere stable, then automating it with IC10 chips programmed in an assembly language. The game has been in early access since 2017.

## Relations

**uses**

- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (core): Rooms and pipe networks hold mixtures of oxygen, nitrogen, carbon dioxide, volatiles, pollutants, and water with pressure and temperature; gases mix, and combustion consumes fuel and oxygen and releases heat.
- [Heat transfer](../mechanic/heat-transfer.md) (core): Gas temperature changes pressure and habitability; radiators, heat exchangers, heaters, and coolers move heat between pipes, rooms, and the planet's atmosphere.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (core): Pipes, pumps, filtration units, mixers, and regulators route gases between devices; pipes and tanks fail when pressure exceeds their rating.
- [Survival meters](../mechanic/survival-meters.md) (core): Early survival requires breathable gas, food, water, and suit temperature; suits carry tanks and filters until a habitat is sealed.
- [Power grid](../mechanic/power-grid.md) (supporting): Solar panels, generators, and batteries feed cable networks; overloaded cables burn out.
- [Player programming](../mechanic/player-programming.md) (supporting): IC10 chips run player-written assembly that reads and writes device logic values such as pressure and temperature.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): Logic readers, writers, memory, and sensors chain devices without code.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Ore is mined from deformable voxel terrain.
- [Production chains](../mechanic/production-chain.md) (supporting): Furnaces and arc furnaces smelt ore into ingots, and autolathes and other fabricators turn ingots into kits.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting): Hydroponic plants need light, water, and suitable gases, and exchange carbon dioxide for oxygen.
- [Structural integrity](../mechanic/structural-integrity.md) (supporting): Walls hold limited pressure differences; exceeding them causes fatigue and explosive decompression.
- [Building placement](../mechanic/free-placement.md) (supporting): Frames, walls, pipes, and devices are placed on a grid piece by piece, and placement decides airtightness.

## Sources

- [Stationeers on Steam](../source/src-steam-2026-stationeers.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
