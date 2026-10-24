# Cities: Skylines

*Game* · `cities-skylines` · status: **sourced**

A city builder in which road-following zones, agent citizens who route to work along computed paths, district policies, and player-drawn transit lines make traffic flow the central design problem.

| field | value |
|---|---|
| year | 2015 |
| developer | Colossal Order |
| platforms | PC, Console, Handheld |
| subgenre | City builder |
| subgenre secondary | Transport / logistics |
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
| multiplayer | Single-player |
| modding | Scripting |
| production tier | AA |
| agent count order | 10,000+ |
| emergence | 4 |
| influence | 4 |
| influenced by | [SimCity 4](../game/simcity-4.md) |
| cluster *(computed)* | C10 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 15 |

## Summary

A city builder in which road-following zones, agent citizens who route to work along computed paths, district policies, and player-drawn transit lines make traffic flow the central design problem.

## Core Loop

draw roads and zone along them -> citizens move in, commute, and shop along computed routes -> population milestones unlock services and map tiles -> set district policies, taxes, and budgets -> fix traffic with road hierarchy and transit -> expand

## Design Notes

Colossal Order carried the road and transit systems of its Cities in Motion series into a full city builder, so every citizen and vehicle is an agent taking the fastest route and congestion is read directly from visible jams. Zoning cells are generated along whatever road geometry the player draws, freeing layouts from a fixed grid, and districts let the player apply policies and tax rates to painted areas. Paradox approved the project after the reception of SimCity (2013), the game was built for Steam Workshop mods, and widely used mods replace core systems such as traffic rules.

## Relations

**influenced by**

- [SimCity 4](../game/simcity-4.md)

**uses**

- [Zoning](../mechanic/zoning.md) (core): Zoning cells follow the shape of drawn roads; residential, commercial, industrial, and office zones develop and level up.
- [Road networks](../mechanic/road-network.md) (core): Road type sets lanes, speed, and zone frontage; network geometry such as interchanges and one-way systems decides throughput.
- [Traffic congestion](../mechanic/traffic-congestion.md) (core): Each citizen takes the fastest route to work or other destinations; poor road design shows up as visible jams that delay services and deliveries.
- [Public transit lines](../mechanic/public-transit.md) (core): Player-drawn bus, tram, train, metro, ferry, and taxi lines carry passengers, cut congestion, and earn fares.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (supporting): Citizens and vehicles path individually through roads, paths, and transit.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Population milestones unlock services, zoning types, policies, and purchase of up to 25 map tiles.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): District policies restrict development types, set district tax rates, or make transit free.
- [Power grid](../mechanic/power-grid.md) (supporting)
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (supporting): Water and sewage pipes; sewage released upstream contaminates downstream intakes.
- [Service coverage](../mechanic/service-coverage.md) (supporting): Service buildings reach buildings by network distance and dispatch vehicles.
- [Education and workforce](../mechanic/education-workforce.md) (supporting): Elementary (300), high school (1,000), and university (4,500) capacities move citizens through four education levels that higher-level jobs require.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): Citizens age and die; an initial cohort moving in together can age into a wave of deaths that overloads hearses.
- [Land value](../mechanic/land-value.md) (supporting): Services and parks raise land value, pollution and noise lower it, and land value helps buildings level up.
- [Modding API](../mechanic/modding-api.md) (supporting): Steam Workshop and a mod-friendly architecture; mods add assets, maps, and new behavior.
- [Travel mode choice](../mechanic/travel-mode-choice.md) (supporting): Citizens choose between walking, driving, and the player's bus, tram, train, metro, ferry, and taxi lines when routing to destinations, so new lines shift demand off roads.

## Backlinks (computed)

**influenced:** [Cities: Skylines II](../game/cities-skylines-2.md), [Paralives](../game/paralives.md)

**precedent for:** [Calibrated serious simulations](../opportunity/calibrated-serious-sims.md), [Mechanic modding by description](../opportunity/language-modding.md), [Mean-field crowds and traffic](../opportunity/mean-field-crowds.md), [Participatory planning sandboxes](../opportunity/participatory-planning-sandboxes.md), [Symbolic simulation, neural rendering](../opportunity/symbolic-sim-neural-render.md)

## Claims

- Cities: Skylines is credited with reviving the SimCity style of city builder after SimCity (2013). *(confidence: medium)* [[4](../source/src-wikipedia-city-building-game.md), [14](../source/src-wikipedia-cities-skylines.md)]

## Sources

- [Cities: Skylines](../source/src-wikipedia-cities-skylines.md)
- [Education](../source/src-paradoxwikis-2026-skylines-education.md)
- [City-building game](../source/src-wikipedia-city-building-game.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
