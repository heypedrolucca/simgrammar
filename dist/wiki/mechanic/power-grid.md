# Power grid

*Mechanic* · `power-grid` · status: **sourced**

Generators produce energy that is distributed over a connected network to consumers; shortfalls cause brownouts or shutdowns.

| field | value |
|---|---|
| aliases | electricity network, power network |
| family | Resources & production |
| substrate | Network / graph, Aggregate stocks |
| math basis | Network flow, System dynamics / ODEs |
| feedback | Both |
| player interface | Placement, Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [SimCity](../game/simcity-1989.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 19 |
| prevalence share *(computed)* | 0.109 |
| subgenre spread *(computed)* | 7 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Generators, consumers, and optional storage are joined by poles, wires, or adjacency into connected components. Each tick each component sums generation and demand; if supply covers demand every consumer runs, otherwise a shortfall rule applies: proportional slowdown, priority shedding, or outages in some order. Factorio spreads power evenly so machines slow proportionally (a 300 kW load on 180 kW of solar runs at 60%), dispatches solar first, then steam engines, turbines, and fusion, discharges accumulators only when other sources fall short, and charges every connected machine an idle drain. Micropolis, the released SimCity engine, walks conductive tiles outward from each plant, spends one unit of capacity per tile (700 per coal plant, 2,000 per nuclear plant), and when capacity runs out reports brownouts and leaves the remaining tiles unpowered. Oxygen Not Included gives wires a load capacity and damages overloaded wires. Inputs: generator output (fuel, weather, time of day), consumer demand, topology. Outputs: a satisfaction ratio per component and the operating state of each consumer.

## Player Experience

A clear supply-demand puzzle with a visible penalty. Players watch the satisfaction bar, add generation ahead of growth, and learn that a fuel shortage at the plant can slow the very machines that supply its fuel. Night, weather, and storage add a timing layer to an otherwise static capacity problem.

## Design Levers

- shortfall rule: proportional slowdown, priority tiers, or hard outages
- connection model: pole radius, wires with capacity, or adjacency
- generator variability by fuel, time of day, and weather, plus storage buffers
- idle drain and standby consumption
- wire or transformer capacity limits and overload consequences

## Failure Modes

- A single global power pool without topology reduces the mechanic to a number to keep positive.
- Proportional slowdown can cause a death spiral when brownouts slow the miners and inserters that fuel the generators, a known trap in early Factorio steam power.
- Overload damage without clear warnings reads as random breakage.

## Dynamics

- Growth outpaces generation in steps, so power becomes a recurring stop-and-fix cadence.
- Variable sources such as solar and wind plus storage create daily cycles of surplus and deficit that decide what runs when.
- Grid topology sets the blast radius of failures: one broken link can isolate a district.
- Circuit or priority controls let players build load shedding, coupling power to automation.

## Open Questions

- Would learned grid operators that forecast demand and weather turn power from a capacity check into a dispatch problem players manage?
- How much electrical realism (voltage, phase, line losses) can players absorb before the grid stops being legible?

## Relations

**synergy**

- [Production chains](../mechanic/production-chain.md): Machines draw power, so production throughput becomes coupled to generation capacity.

## Backlinks (computed)

**involved in:** [Simulation games as agent benchmarks](../opportunity/sims-as-agent-benchmarks.md), [Weather-coupled energy grids](../opportunity/weather-coupled-grids.md)

**used by:** [Captain of Industry](../game/captain-of-industry.md), [Cities: Skylines](../game/cities-skylines.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Elite Dangerous](../game/elite-dangerous.md), [Factorio](../game/factorio.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Mindustry](../game/mindustry.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Prison Architect](../game/prison-architect.md), [Satisfactory](../game/satisfactory.md), [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [SimCity (2013)](../game/simcity-2013.md), [Space Engineers](../game/space-engineers.md), [Space Haven](../game/space-haven.md), [Stationeers](../game/stationeers.md), [Subnautica](../game/subnautica.md), [Surviving Mars](../game/surviving-mars.md), [Timberborn](../game/timberborn.md)

## Sources

- [Electric system](../source/src-factoriowiki-2026-electric-system.md)
- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
