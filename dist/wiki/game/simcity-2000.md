# SimCity 2000

*Game* · `simcity-2000` · status: **sourced**

The isometric sequel to SimCity that adds terrain elevation, an underground layer of water pipes and subways, separate zone tax rates, bonds, ordinances, and power plants that age out.

| field | value |
|---|---|
| year | 1993 |
| developer | Maxis |
| platforms | PC, Console, Handheld, Mobile |
| subgenre | City builder |
| sim domain | Urban, Economic |
| player role | Planner / mayor |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | City |
| fidelity | Systemic |
| perspective | Isometric |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | AA |
| agent count order | Aggregate only |
| emergence | 3 |
| influence | 3 |
| influenced by | [SimCity](../game/simcity-1989.md) |
| cluster *(computed)* | C10 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 15 |

## Summary

The isometric sequel to SimCity that adds terrain elevation, an underground layer of water pipes and subways, separate zone tax rates, bonds, ordinances, and power plants that age out.

## Core Loop

shape terrain and zone light or dense residential, commercial, industrial land -> lay power lines, water pipes, roads, and rail -> demand and land value grow zones -> set per-zone tax rates, ordinances, and bonds -> fund schools, hospitals, police, and fire -> rebuild aging plants

## Design Notes

SimCity 2000 keeps the original's grid-map model but adds a second plane: an underground view for water pipes, subways, and road tunnels, so infrastructure is laid on a separate layer from zoning. Finance gains levers (three tax rates, ordinances, bonds), and most of the nine power plant types have limited lifespans, so replacement becomes a recurring capital cost. Yearly newspapers built from city state replace the score screen, and extreme deficit spending ends the game.

## Relations

**influenced by**

- [SimCity](../game/simcity-1989.md)

**uses**

- [Zoning](../mechanic/zoning.md) (core): Residential, commercial, and industrial zones in light and dense variants, plus seaport and airport zones.
- [RCI demand](../mechanic/rci-demand.md) (core): Demand bars for residential, commercial, and industrial land, raised by connections to neighbor cities.
- [Power grid](../mechanic/power-grid.md) (core): Nine plant types including wind, hydro, solar, fusion, and microwave; most have limited lifespans and must be rebuilt.
- [Treasury and budget](../mechanic/budget-treasury.md) (core): Yearly budget with department funding; extreme deficit spending ends the game.
- [Taxation](../mechanic/taxation.md) (supporting): Separate tax rates for residential, commercial, and industrial zones.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): The player issues bonds to raise capital and pays interest on them.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): City ordinances enacted for ongoing cost and effect.
- [Vertical layers](../mechanic/vertical-layers.md) (supporting): An underground layer holds water pipes, subways, and road tunnels separate from the surface.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (supporting): Water from pumps travels through underground pipes to zones.
- [Terraforming](../mechanic/terraforming.md) (supporting): Land has elevation that the player can raise or lower before and during play.
- [Service coverage](../mechanic/service-coverage.md) (supporting): Schools, libraries, museums, hospitals, police, and fire stations cover surrounding zones.
- [Land value](../mechanic/land-value.md) (supporting): Query tool shows land value per tile, which shapes development.
- [Traffic congestion](../mechanic/traffic-congestion.md) (supporting): Query tool reports traffic on roads; highways and transit relieve it.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Disasters strike in play, and scenarios based on real cities stage specific ones.
- [Dated technology timeline](../mechanic/dated-tech-timeline.md) (supporting): Power plant types such as solar, fusion, and microwave and buildings such as arcologies become available in set invention years as the city's calendar advances.

## Backlinks (computed)

**influenced:** [SimCity 4](../game/simcity-4.md), [Transport Tycoon](../game/transport-tycoon.md)

## Sources

- [SimCity 2000](../source/src-wikipedia-simcity-2000.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
