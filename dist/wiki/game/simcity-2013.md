# SimCity (2013)

*Game* · `simcity-2013` · status: **sourced**

A SimCity reboot built on the agent-based GlassBox engine, in which agents carry workers, power, water, and goods between buildings and small cities share a region over an always-online connection.

| field | value |
|---|---|
| year | 2013 |
| developer | Maxis Emeryville |
| platforms | PC |
| subgenre | City builder |
| sim domain | Urban, Economic |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | City |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player, Async / shared content |
| modding | None |
| production tier | AAA |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 2 |
| influenced by | [SimCity 4](../game/simcity-4.md) |
| cluster *(computed)* | C09 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 14 |

## Summary

A SimCity reboot built on the agent-based GlassBox engine, in which agents carry workers, power, water, and goods between buildings and small cities share a region over an always-online connection.

## Core Loop

zone along roads -> GlassBox agents carry workers, goods, power, water, and sewage between buildings -> specialize the city in industries such as manufacturing, education, or tourism -> trade surpluses and share services with region neighbors -> pool resources into Great Works

## Design Notes

GlassBox replaces statistical maps with units that hold resource bins and agents that move resources between them, so a house holds a count of people and food, water travels as units, and traffic jams are the visible sum of commuting agents. Agents take the first available job and the first empty home rather than keeping persistent lives, and vehicles take the shortest route instead of the least loaded one, which players read as pathfinding errors. Cities were smaller than earlier games by design, and region play links them asynchronously through shared services, trade, and Great Works.

## Relations

**influenced by**

- [SimCity 4](../game/simcity-4.md)

**uses**

- [Zoning](../mechanic/zoning.md) (core): Residential, commercial, and industrial zones are painted along roads; buildings develop inside them.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (core): Sims go to the first job and first empty home they find; vehicles take the shortest route rather than the one with spare capacity.
- [Traffic congestion](../mechanic/traffic-congestion.md) (core): Jams emerge from masses of commuting Sim agents on the road network.
- [Asynchronous shared regions](../mechanic/async-shared-region.md) (core): Cities in a region connect by highway, rail, and water, trade resources, share services, and pool wealth into Great Works such as an arcology.
- [Power grid](../mechanic/power-grid.md) (supporting): Power is carried as resource units from plants to buildings.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (supporting): Water and sewage move as units through pipes between pumps, treatment, and buildings.
- [Deposit depletion](../mechanic/deposit-depletion.md) (supporting): Map resources are mostly finite, though groundwater recharges.
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (supporting): A simulated global market raises and lowers prices of key resources with supply and demand.
- [Service coverage](../mechanic/service-coverage.md) (supporting): Service buildings dispatch vehicle agents to calls.
- [Pollution spread](../mechanic/pollution-spread.md) (supporting): Pollution and traffic cross city borders within a region.
- [Population strata](../mechanic/population-strata.md) (supporting): Residents and businesses come in wealth levels with different demands.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)

## Backlinks (computed)

**precedent for:** [Agent ambassadors between player worlds](../opportunity/agent-ambassadors-async.md), [Mean-field crowds and traffic](../opportunity/mean-field-crowds.md)

## Sources

- [SimCity (2013 video game)](../source/src-wikipedia-simcity-2013.md)
- [GDC 2012: Breaking down SimCity's Glassbox engine](../source/src-cifaldi-2012-glassbox-engine.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
