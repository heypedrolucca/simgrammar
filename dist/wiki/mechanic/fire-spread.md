# Fire spread

*Mechanic* · `fire-spread` · status: **sourced**

Fire ignites and spreads across flammable cells or objects at rates set by fuel, wind, and moisture, consuming what it burns.

| field | value |
|---|---|
| aliases | fire propagation, wildfire |
| family | Environment & ecology |
| substrate | Cellular grid, Stochastic events |
| math basis | Cellular automata, Markov / stochastic processes, Continuum mechanics |
| feedback | Reinforcing (positive) |
| player interface | Observation only, Direct manipulation, Placement |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can learned combustion and smoke surrogates make fire visually rich while its spread stays readable and controllable? |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [SimCity](../game/simcity-1989.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 18 |
| prevalence share *(computed)* | 0.103 |
| subgenre spread *(computed)* | 8 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a burning state per cell, tile, or object (unburnt, burning, burnt), often with fuel and heat values. Each tick a burning unit consumes fuel and tries to ignite neighbors with a chance or rate scaled by their flammability, moisture, and wind direction; it goes out when fuel runs out or when water, rain, or firefighters remove it. Inputs are material flammability, weather, and suppression; outputs are destroyed structures and terrain, heat, and sometimes smoke or updrafts. SimCity spreads fire between flammable tiles and fire stations put it out; Breath of the Wild's chemistry engine lets fire change the state of materials such as grass, whose burning creates updrafts, and rain stops it; Far Cry 2 and Dwarf Fortress propagate fire through grass and trees.

## Player Experience

A small spark becomes an emergency. The player races to contain fire before it reaches stockpiles or homes, or uses it as a tool: burning a field to clear it, lighting grass to drive enemies, or riding the updraft. Fire teaches the player to read the map as fuel and firebreaks.

## Design Levers

- ignition sources and their rates: lightning, overheating, arson, player tools
- flammability, fuel load, and burn duration per material
- spread probability per neighbor and the wind bias on it
- moisture and weather modifiers, such as rain suppressing ignition
- suppression tools: water, firefighters, fire station coverage, firebreak materials

## Failure Modes

- Spread tuned slightly too high burns the whole map before the player can react; slightly too low makes fire a nonevent.
- Fire that ignores construction choices, such as stone burning like wood, removes the decision space.
- Large burning areas in cell-based implementations cost noticeable frame time during big fires.

## Dynamics

- Players build firebreaks and separate flammable storage, which changes settlement layout.
- Fire couples with weather and terrain: dry seasons and wind produce larger fires, and rain ends them.
- Players repurpose fire as a weapon or tool, such as burning grass under enemies or clearing forest.

## Open Questions

- Can learned combustion and smoke surrogates make fire visually rich while its spread stays readable and controllable?

## Relations

**synergy**

- [Weather](../mechanic/weather.md): Wind and dryness govern fire spread.

## Backlinks (computed)

**involved in:** [Learned regional weather](../opportunity/learned-weather-layer.md)

**used by:** [Banished](../game/banished.md), [Caesar III](../game/caesar-3.md), [Don't Starve](../game/dont-starve.md), [Dwarf Fortress](../game/dwarf-fortress.md), [From Dust](../game/from-dust.md), [FTL: Faster Than Light](../game/ftl.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Minecraft](../game/minecraft.md), [Noita](../game/noita.md), [Pharaoh](../game/pharaoh.md), [Prison Architect](../game/prison-architect.md), [RimWorld](../game/rimworld.md), [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [Space Haven](../game/space-haven.md), [Teardown](../game/teardown.md), [The Powder Toy](../game/the-powder-toy.md), [The Legend of Zelda: Breath of the Wild](../game/zelda-breath-of-the-wild.md)

## Sources

- [Change and Constant: Breaking Conventions with 'The Legend of Zelda: Breath of the Wild'](../source/src-fujibayashi-2017-botw-change-and-constant.md)
- [Breath of the Wild, science, and clever little lies](../source/src-thumbsticks-2017-botw-chemistry.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
