# Hydrology

*Mechanic* · `hydrology` · status: **sourced**

Water flows across terrain and through rivers by height differences, producing floods, droughts, irrigation, and dam management.

| field | value |
|---|---|
| aliases | water simulation, rivers and floods, irrigation |
| family | Environment & ecology |
| substrate | Cellular grid, Continuous physics |
| math basis | Continuum mechanics, Cellular automata |
| feedback | Balancing (negative) |
| player interface | Placement, Observation only |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 1 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| open questions | Can learned shallow-water surrogates run large terrain water at interactive rates while staying predictable enough to engineer against? |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Pharaoh](../game/pharaoh.md) |
| earliest year *(computed)* | 1999 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.1 |

## Definition

Owns water depth per cell on a terrain heightfield, often with source and sink rates, flow velocity, and soil moisture. Each tick water moves from higher to lower surface height between neighboring cells, evaporates, and is added by springs, rain, or rivers; moisture spreads from water to nearby land and gates crop growth. Timberborn links each tile to its four neighbors by virtual pipes, ticks every few hundred milliseconds, evaporates water, and runs recurring droughts that switch sources off and grow harsher; dams, levees, and floodgates regulate flow, and moisture falls off with distance and sharply uphill. From Dust and Cities: Skylines also simulate terrain water, while Pharaoh schedules a yearly Nile flood that waters floodplain farms. Inputs are terrain, sources, weather, and player structures; outputs are water levels, floods, and moisture.

## Player Experience

Engineering with a moving material. The player shapes terrain and builds dams to store water for dry spells, protects low ground from floods, and watches a mistake travel downstream. Droughts turn reservoir size into the main survival question, and a dam failure is a visible, traceable disaster.

## Design Levers

- grid resolution and tick rate of the flow solver
- source strength schedules, including drought and flood cycles and how fast they ramp
- evaporation rate, seepage, and moisture spread distance
- structures: dams, levees, floodgates, pumps, canals, and their flow controls
- whether water erodes or deposits terrain

## Failure Modes

- Fixed flow values on structures cause oscillations and waves; Timberborn's developers avoided hard-coded dam values for this reason.
- Abrupt switching of water sources makes water slosh unrealistically; Timberborn ramps source strength down before a drought starts.
- Water that leaks through gaps or ignores terrain edits reads as a bug and breaks trust in the system.
- Large water grids can dominate simulation cost and cap map size.

## Dynamics

- Upstream structures change downstream conditions, creating spatial dependencies across the map.
- Reservoir capacity becomes a stock that buffers seasonal or drought variability.
- Flooding couples with building placement, farmland, and disasters such as dam failure.

## Open Questions

- Can learned shallow-water surrogates run large terrain water at interactive rates while staying predictable enough to engineer against?

## Relations

**synergy**

- [Terraforming](../mechanic/terraforming.md): Reshaping terrain redirects water, so terrain editing becomes water engineering (From Dust, Timberborn).

## Backlinks (computed)

**affected by:** [Graph network simulators and neural operators](../technique/graph-network-simulators.md)

**involved in:** [Learned regional weather](../opportunity/learned-weather-layer.md)

**used by:** [From Dust](../game/from-dust.md), [Pharaoh](../game/pharaoh.md), [Terra Nil](../game/terra-nil.md), [Timberborn](../game/timberborn.md)

## Sources

- [Deep Dive: Designing the dynamic irrigation and water systems in Timberborn](../source/src-amielanczyk-2023-timberborn-water.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
