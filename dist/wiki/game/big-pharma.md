# Big Pharma

*Game* · `big-pharma` · status: **sourced**

A pharmaceutical factory and business sim in which the player routes ingredients through machines on conveyor belts to push their concentration into the range that activates cures while suppressing side effects, then sells into contested markets.

| field | value |
|---|---|
| year | 2015 |
| developer | Twice Circled |
| platforms | PC, Console, Handheld |
| subgenre | Factory / automation |
| subgenre secondary | Business / economic sim |
| sim domain | Industrial / logistics, Economic, Medical |
| player role | Engineer / designer |
| agency model | Zoning / placement, Design then test |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Abstract |
| perspective | Isometric |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 1 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 9 |

## Summary

A pharmaceutical factory and business sim in which the player routes ingredients through machines on conveyor belts to push their concentration into the range that activates cures while suppressing side effects, then sells into contested markets.

## Core Loop

import an ingredient -> route it through machines that change its concentration -> activate cures and remove side effects -> form pills and ship them -> grade and price against market demand and rivals -> research better machines

## Design Notes

Big Pharma's production puzzle is numeric: each ingredient carries cures and side effects that are active only inside concentration windows on a 0 to 20 scale, and machines raise, lower, combine, or transform effects at set concentrations. A line is a sequence of machines on conveyor belts in a fixed floor plan, so the order of operations and the space they take are both constraints. Products are graded from effectiveness, side effects, and market demand, and rival companies release competing drugs that saturate a disease's market. The primary challenge is line layout rather than corporate strategy, which places it in the factory-automation lineage with a business layer.

## Relations

**uses**

- [Production chains](../mechanic/production-chain.md) (core): Machines raise or lower an ingredient's concentration, combine materials, or transform effects; each effect is active only inside its concentration window on a 0 to 20 scale.
- [Conveyor transport](../mechanic/conveyor-transport.md) (core): Conveyor belts move materials between machines from intake ports to output ports, and machine order along the belt sets the recipe.
- [Product development](../mechanic/product-development.md) (core): Each finished drug gets a letter grade from its cure strength, side effects, and market demand, and the player names and prices it.
- [Rival firms](../mechanic/rival-firms.md) (core): Rival companies release competing drugs that saturate a disease's market and cut demand for the player's product.
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (supporting): Price and sales for each cure depend on demand and how crowded its market is.
- [Building placement](../mechanic/free-placement.md) (supporting): Machines are placed on a fixed factory floor where space limits line length.
- [Tech tree](../mechanic/tech-tree.md) (supporting): A research tree unlocks better machines and other benefits.
- [Scouting knowledge](../mechanic/scouting-knowledge.md) (supporting): Explorers search for new ingredients, and analysis machines reveal an ingredient's effects and maximum potency.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Scenarios set targets such as a financial milestone within a set number of years, at several difficulties.

## Sources

- [Big Pharma (video game)](../source/src-wikipedia-big-pharma.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
