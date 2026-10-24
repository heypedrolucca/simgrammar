# Conveyor transport

*Mechanic* · `conveyor-transport` · status: **sourced**

Items move continuously on belts or lanes with throughput limits, splitters, merges, and priorities.

| field | value |
|---|---|
| aliases | belts, conveyor belts, transport belts |
| family | Logistics & networks |
| substrate | Network / graph, Rule system |
| math basis | Network flow, Queueing theory |
| feedback | None |
| player interface | Placement |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 3 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [Factorio](../game/factorio.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 9 |
| prevalence share *(computed)* | 0.052 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Belts form directed chains of tiles; each tile holds a fixed number of item slots per lane and moves items forward at a tier-dependent speed. Items enter from inserters, machines, or side-loading and exit at the end, onto another belt, or into a machine. Splitters divide and merge flows, often with priority and filter settings; undergrounds and bridges cross other belts. Factorio holds 4 items per lane per tile and carries 15, 30, 45, or 60 items per second across both lanes for transport, fast, express, and turbo belts. Internally it groups adjacent belts into transport lines and stores the gaps between items, so a free-flowing line updates only its end gaps each tick. Satisfactory, Dyson Sphere Program, and Mindustry use similar belt tiers, and Shapez raises belt speed through upgrades. Inputs: items placed on belts. Outputs: items delivered at a throughput capped by the slowest segment.

## Player Experience

Layout as the main puzzle. Players route belts around each other, balance lanes, and design compact buses, and they can see throughput problems as gaps or backed-up lines. A compressed belt feeding a full row of machines is a visible proof of a correct design.

## Design Levers

- throughput per tier and number of lanes
- splitter, merger, and priority or filter options
- crossing options such as undergrounds, bridges, or vertical lifts
- item density and whether mixed items share a lane
- belt cost and unlock schedule

## Failure Modes

- Spaghetti layouts become unreadable and players stop understanding their own factory.
- Lane imbalance and side-loading rules are opaque without wikis.
- Belt counts at large scale cost simulation time; Factorio's transport-line rewrite was made to cut this cost.

## Dynamics

- Main-bus and ratio-block conventions emerge from throughput caps, and players share them as blueprints.
- Belt saturation sets factory module sizes, so each tier upgrade reshapes layouts.
- Mixed-item belts create sushi designs and clogging failure modes.

## Open Questions

- Could layout assistants that propose belt routing under player constraints keep the puzzle while removing tedium?
- What is the smallest set of belt primitives that still supports deep layout optimization?

## Relations

**synergy**

- [Production chains](../mechanic/production-chain.md): Belts make recipe chains spatial, turning ratios into a layout puzzle (Factorio, Satisfactory).

## Backlinks (computed)

**involved in:** [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Simulation games as agent benchmarks](../opportunity/sims-as-agent-benchmarks.md)

**used by:** [Big Pharma](../game/big-pharma.md), [Captain of Industry](../game/captain-of-industry.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Factorio](../game/factorio.md), [Mindustry](../game/mindustry.md), [Satisfactory](../game/satisfactory.md), [shapez 2](../game/shapez-2.md), [Space Engineers](../game/space-engineers.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Friday Facts #176 - Belts optimization for 0.15](../source/src-wube-2017-fff-176-belts-optimization.md)
- [Transport belts/Physics](../source/src-factoriowiki-2026-transport-belt-physics.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
