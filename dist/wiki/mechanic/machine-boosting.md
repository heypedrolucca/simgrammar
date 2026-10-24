# Machine boosting

*Mechanic* · `machine-boosting` · status: **sourced**

Per-machine modifiers such as modules, beacons, clock speed, or coatings trade extra power, scarce items, or currency for faster or more productive machines.

| field | value |
|---|---|
| aliases | modules, overclocking, clock speed, beacons, proliferation |
| family | Resources & production |
| substrate | Rule system, Aggregate stocks |
| math basis | Optimization, System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Placement, Parameter |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Factorio](../game/factorio.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.1 |

## Definition

Owns, for each producing machine, a set of modifier slots or settings and the effect vector they sum to: speed, productivity (extra output per cycle), energy use, and sometimes pollution or quality. Cycle time divides by one plus the speed bonus, productivity fills a bonus bar that yields free outputs, and power draw scales with the boost, often superlinearly. Satisfactory clock speed runs from 1% to 250%, each of up to three Power Shards raises the cap by 50 points, and power scales with exponent 1.321928, so 250% draws 335.77% of base power. Factorio fills module slots with speed, productivity, efficiency, or quality modules, beacons project module effects onto nearby machines, and productivity bonuses are capped at +300%. Dyson Sphere Program coats items with proliferator so machines consuming them gain extra products or speed. Captain of Industry spends Unity on building boosts. Unlike production-chain, which owns recipes and buffers, and quality-tiers, which owns item grades, this mechanic owns the cost-benefit curve of pushing a single machine harder.

## Player Experience

An optimization layer on top of ratio planning. Players decide whether to build more machines or push the ones they have, weighing floor space and materials against a growing power bill. Slotting the last productivity module or overclocking a bottleneck machine is a satisfying fix, and the power spike that follows is the bill.

## Design Levers

- shape of the power or cost curve per unit of boost, linear or convex such as Satisfactory's exponent of about 1.32
- separate effect axes (speed, productivity, efficiency, pollution) and the tradeoffs bundled into one slot
- slot counts per machine and whether boosts can be shared with neighbors, as with beacons
- cost of the boost itself: crafted modules, rare world pickups such as Power Shards, or a currency such as Unity
- caps on stacked bonuses, such as Factorio's +300% productivity limit
- which machine types accept boosts: assemblers, drills, labs, turrets

## Failure Modes

- Productivity bonuses that stack without a cap create net-positive loops; Factorio caps productivity at +300% to prevent this.
- One dominant configuration, such as productivity modules everywhere with beacons for speed, becomes a solved template.
- Convex power costs that are not shown make overclocking feel like a sudden grid failure.
- Boosts gated on rare pickups push players into exploration chores unrelated to factory design.

## Dynamics

- Players trade space for power: compact boosted builds compete with sprawling unboosted ones.
- Productivity bonuses on late stages save every upstream input, so players boost the end of a chain first.
- Boosting a bottleneck moves the bottleneck to power generation, coupling factory design to the grid.

## Open Questions

- Can planners that solve module and clock settings for a target rate coexist with players who enjoy solving them by hand?
- Which cost curves keep boosted and unboosted builds both viable through the late game?

## Backlinks (computed)

**affected by:** [Quality-diversity search (MAP-Elites) for content and balance](../technique/quality-diversity-search.md)

**used by:** [Captain of Industry](../game/captain-of-industry.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Factorio](../game/factorio.md), [Mindustry](../game/mindustry.md), [Satisfactory](../game/satisfactory.md)

## Sources

- [Clock speed](../source/src-satisfactorywiki-2026-clock-speed.md)
- [Friday Facts #375 - Quality](../source/src-wube-2023-fff-375-quality.md)
- [Unity](../source/src-coiwiki-2026-unity.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
