# Renewable regrowth

*Mechanic* · `renewable-regrowth` · status: **sourced**

Harvested stocks such as forests, fish, game, and soil regenerate over time at density-dependent rates, allowing sustainable yield or overexploitation.

| field | value |
|---|---|
| aliases | resource regeneration, sustainable yield, regrowth |
| family | Resources & production |
| substrate | Aggregate stocks, Cellular grid, Agent-based |
| math basis | Population dynamics, System dynamics / ODEs |
| feedback | Both |
| player interface | Observation only, Placement |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Don't Starve](../game/dont-starve.md) |
| earliest year *(computed)* | 2012 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

A harvestable stock (trees on tiles, fish in a zone, animals in a region, soil fertility) regenerates each tick at a rate that depends on its current level: often logistic growth, sometimes a fixed respawn timer or seed spread to neighboring cells. Harvesting removes stock at the rate set by extraction; if harvest exceeds regrowth the stock falls and, below a threshold, can collapse or stop regenerating. Banished foresters replant cut trees around their lodge; Eco tracks plant and animal populations that players can overharvest; Minecraft saplings regrow trees only where players plant them. Inputs: harvest rate, current stock, environmental modifiers. Outputs: stock level and yield available per tick.

## Player Experience

Stewardship under temptation. Players can take more now and pay later, so they learn to harvest at a pace the land can sustain, replant deliberately, or move on. Watching a forest or fishery recover after a pause makes the system's memory visible.

## Design Levers

- regrowth curve shape (logistic, linear, or timer) and its maximum rate
- collapse threshold below which a stock stops recovering
- whether regrowth is automatic or needs planting or breeding
- spatial spread from neighboring cells versus regrowth in place
- visibility of stock levels and sustainable yield

## Failure Modes

- Fast regrowth makes stocks effectively infinite and removes the tradeoff.
- Collapse thresholds that are hidden make extinction feel like a sudden bug.
- Replanting that is free and instant reduces stewardship to placing one building.

## Dynamics

- Overharvesting produces boom-bust cycles in yield, the classic tragedy of the commons in shared or multiplayer worlds such as Eco.
- The maximum sustainable yield of a logistic stock is at half capacity, so optimal play keeps stocks at partial depletion.
- Coupled with predator-prey or habitat systems, harvest pressure ripples through an ecosystem.
- Rotating among harvest sites becomes a spatial schedule.

## Open Questions

- Can learned ecological models give regrowth realistic spatial patterns while keeping sustainable yield readable?
- Does shared regrowth in multiplayer reliably produce cooperative norms, or only collapse?

## Backlinks (computed)

**used by:** [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Banished](../game/banished.md), [Don't Starve](../game/dont-starve.md), [Eco](../game/eco.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Manor Lords](../game/manor-lords.md)

## Sources

- [Eco (2018 video game)](../source/src-wikipedia-eco-2018.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
