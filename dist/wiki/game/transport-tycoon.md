# Transport Tycoon

*Game* · `transport-tycoon` · status: **sourced**

A transport business sim in which the player builds road, rail, sea, and air networks between towns and industries over a century, earning by delivery speed and distance while vehicles age and break down.

| field | value |
|---|---|
| aliases | Transport Tycoon Deluxe |
| year | 1994 |
| developer | Chris Sawyer |
| platforms | PC, Console, Mobile |
| subgenre | Transport / logistics |
| subgenre secondary | Business / economic sim |
| sim domain | Industrial / logistics, Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Direct unit control |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Score / ranking |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player, Competitive |
| modding | Content |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 4 |
| influenced by | [Railroad Tycoon](../game/railroad-tycoon.md), [SimCity 2000](../game/simcity-2000.md), [Theme Park](../game/theme-park.md) |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 18 |

## Summary

A transport business sim in which the player builds road, rail, sea, and air networks between towns and industries over a century, earning by delivery speed and distance while vehicles age and break down.

## Core Loop

survey towns and industries -> build stations, track, roads, docks, and airports -> give vehicles order lists -> payment by cargo, distance, and delivery time -> station ratings and towns grow -> replace aging vehicles and expand

## Design Notes

Transport Tycoon extends Railroad Tycoon to four transport modes on one isometric map and makes cargo value decay with transit time, so mail suits short or fast routes while coal keeps its value over long hauls. Stations only collect from nearby towns and industries, and a station rating decides how much of an industry's output it receives, which rewards frequent, fast service. Vehicles lose reliability with age and new models arrive on a timeline from 1930 to 2030 (1950 to 2050 in Deluxe), so the fleet must be renewed; date-driven model availability is proposed as dated-tech-timeline. Town councils rate each company through the Local Authority system, which can block new stations. OpenTTD, a reverse-engineered reimplementation first released in 2004, continues the design.

## Relations

**influenced by**

- [Railroad Tycoon](../game/railroad-tycoon.md)
- [SimCity 2000](../game/simcity-2000.md)
- [Theme Park](../game/theme-park.md)

**uses**

- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) (core): Trains, road vehicles, ships, aircraft, and helicopters run order lists between stations; revenue depends on cargo type, distance, quantity, and delivery time.
- [Service coverage](../mechanic/service-coverage.md) (core): Stations accept and supply cargo only within a catchment around them, and station ratings set how much nearby industries hand over.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (core): Vehicle reliability falls with age, breakdowns become more frequent, and vehicles must be serviced and eventually replaced; prototypes offer better specs with reliability risk.
- [Production chains](../mechanic/production-chain.md) (supporting): Primary industries feed secondary ones and finished goods go to towns; poorly served industries can close.
- [Rail signaling](../mechanic/rail-signaling.md) (supporting): Bi-directional signals in the original; Deluxe adds one-way signals.
- [Deposit depletion](../mechanic/deposit-depletion.md) (supporting): Some resource sites run out and new ones appear.
- [Reputation](../mechanic/reputation.md) (supporting): Local Authority ratings per town fall with poor service and tree clearing and can block demolition and new stations.
- [Contracts and orders](../mechanic/contracts-orders.md) (supporting): Towns offer subsidies for serving specific routes.
- [Rival firms](../mechanic/rival-firms.md) (supporting): Up to seven AI transport companies compete for the same towns and industries.
- [Equity and buyouts](../mechanic/equity-buyouts.md) (supporting): Deluxe adds trading company shares and buying out competitors.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): The company starts with an interest-bearing loan.
- [Road networks](../mechanic/road-network.md) (supporting): Road vehicles use town roads and player-built roads from depots.
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Terraforming](../mechanic/terraforming.md) (supporting)
- [Delivery-time payment](../mechanic/delivery-time-payment.md) (supporting): Revenue per delivery depends on cargo type, quantity, distance, and transit time; mail and passengers lose value quickly while coal tolerates long, slow hauls.
- [Dated technology timeline](../mechanic/dated-tech-timeline.md) (supporting): Road, rail, sea, and air models are introduced on a timeline from 1930 to 2030 (1950 to 2050 in Deluxe), new models carry reliability risk, and aging fleets must be renewed as better models arrive.
- [Track laying](../mechanic/track-laying.md) (supporting): Rail track, including slopes, bridges, and tunnels, is laid piece by piece on the isometric tile map, with costs for terrain changes and demolition.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**influenced:** [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md)

## Sources

- [Transport Tycoon](../source/src-wikipedia-transport-tycoon.md)

---
Provenance: created in run `2026-10-24-catalog-ge`; reviewed in `2026-10-24-review-fixes`.
