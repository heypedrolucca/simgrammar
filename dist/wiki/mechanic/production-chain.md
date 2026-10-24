# Production chains

*Mechanic* · `production-chain` · status: **sourced**

Buildings or machines convert input goods into output goods via fixed recipes and cycle times, forming multi-step dependency trees.

| field | value |
|---|---|
| aliases | supply chains, processing chains, recipes |
| family | Resources & production |
| substrate | Rule system, Network / graph |
| math basis | Optimization, Network flow, System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Placement, Parameter |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 15 |
| earliest game *(computed)* | [M.U.L.E.](../game/mule.md) |
| earliest year *(computed)* | 1983 |
| prevalence *(computed)* | 38 |
| prevalence share *(computed)* | 0.218 |
| subgenre spread *(computed)* | 12 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each producer holds a recipe (input amounts, output amounts, cycle time), an input buffer, an output buffer, and a progress timer. Each tick, if inputs and power or labor are present and the output buffer has room, progress advances; on completion inputs are consumed and outputs added. Chained producers form a directed graph from raw resources to finished goods whose steady-state throughput is set by recipe ratios and the slowest stage. The Settlers (1993) chains wheat through a mill to a bakery; Anno 1800 gives each building a fixed cycle time so players build in ratios; Factorio and Satisfactory expose rates directly and add alternate recipes, modules, and productivity bonuses. GlassBox, the SimCity (2013) engine, expresses production as rules that move or combine resources held in a unit's bins. Inputs: raw goods, labor, energy. Outputs: intermediate and final goods, plus a blocked or starved state per producer.

## Player Experience

Building machines that build things. The player traces a desired product back through its tree, sizes each stage, and watches for the stage that starves or backs up. Satisfaction comes from a balanced line running unattended; tension comes from every new product adding a branch to an already crowded layout.

## Design Levers

- recipe depth and branching factor of the dependency tree
- cycle times and ratios, and whether they are round numbers players can compute
- alternate recipes and multi-output recipes that create choices
- buffer sizes at inputs and outputs
- modifiers such as modules, worker skill, or productivity bonuses
- how chains are displayed: hidden, per-building stats, or a full production overview

## Failure Modes

- A single optimal ratio per product, once solved, turns play into copying calculator output.
- Deep trees of single-use intermediates add layout work without adding decisions.
- Starvation far upstream is hard to diagnose without flow statistics, so players blame the wrong building.

## Dynamics

- The slowest stage sets throughput, so the bottleneck moves each time players fix one, creating a chase loop.
- Shared intermediates create contention between chains and force priority decisions.
- Coupled with logistics, layout distance becomes part of the recipe cost.
- Machines that build machines produce exponential factory growth, capped by inputs, space, or threat.

## Open Questions

- Can AI generate recipe graphs that are solvable, non-degenerate, and on-theme, cutting content cost for factory games?
- Do players learn chain design faster from flow visualizations or from AI explanations of bottlenecks?

## Relations

**synergy**

- [Storage and buffers](../mechanic/storage-capacity.md): Buffers decouple steps of a chain; their fill levels reveal bottlenecks.

## Backlinks (computed)

**involved in:** [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Generated recipe graphs](../opportunity/generated-recipe-graphs.md), [Factories with a living workforce](../opportunity/living-workforce-factories.md), [Automated mechanic discovery](../opportunity/mechanic-discovery-search.md), [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md), [Simulation games as agent benchmarks](../opportunity/sims-as-agent-benchmarks.md)

**used by:** [A Tale in the Desert](../game/a-tale-in-the-desert.md), [Against the Storm](../game/against-the-storm.md), [Anno 117: Pax Romana](../game/anno-117.md), [Anno 1800](../game/anno-1800.md), [Autonauts](../game/autonauts.md), [Big Pharma](../game/big-pharma.md), [Caesar III](../game/caesar-3.md), [Capitalism](../game/capitalism.md), [Captain of Industry](../game/captain-of-industry.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Eco](../game/eco.md), [EVE Online](../game/eve-online.md), [Factorio](../game/factorio.md), [Farming Simulator 25](../game/farming-simulator-25.md), [Farthest Frontier](../game/farthest-frontier.md), [Foundation](../game/foundation.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Kenshi](../game/kenshi.md), [Manor Lords](../game/manor-lords.md), [Mindustry](../game/mindustry.md), [M.U.L.E.](../game/mule.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Pharaoh](../game/pharaoh.md), [Railroad Tycoon](../game/railroad-tycoon.md), [Satisfactory](../game/satisfactory.md), [Schedule I](../game/schedule-i.md), [shapez 2](../game/shapez-2.md), [Songs of Syx](../game/songs-of-syx.md), [Space Engineers](../game/space-engineers.md), [Space Haven](../game/space-haven.md), [SpaceChem](../game/spacechem.md), [Stardew Valley](../game/stardew-valley.md), [Stationeers](../game/stationeers.md), [Transport Tycoon](../game/transport-tycoon.md), [Tropico 6](../game/tropico-6.md), [Victoria 3](../game/victoria-3.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [GDC 2012: Breaking down SimCity's Glassbox engine](../source/src-cifaldi-2012-glassbox-engine.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
