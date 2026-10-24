# Railroad Tycoon

*Game* · `railroad-tycoon` · status: **sourced**

A railroad business sim in which the player lays track, builds stations, schedules trains to meet regional supply and demand, and battles rival barons through the stock market.

| field | value |
|---|---|
| aliases | Sid Meier's Railroad Tycoon |
| year | 1990 |
| developer | MPS Labs (MicroProse) |
| platforms | PC |
| subgenre | Transport / logistics |
| subgenre secondary | Business / economic sim |
| sim domain | Industrial / logistics, Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Direct unit control, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Score / ranking |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~10 |
| emergence | 3 |
| influence | 4 |
| influenced by | [SimCity](../game/simcity-1989.md) |
| cluster *(computed)* | C02 |
| core count *(computed)* | 6 |
| mechanic count *(computed)* | 15 |

## Summary

A railroad business sim in which the player lays track, builds stations, schedules trains to meet regional supply and demand, and battles rival barons through the stock market.

## Core Loop

lay track and place stations -> buy trains and set consists and stops -> carry cargo to stations where it is demanded -> revenue and industry growth -> raise capital through bonds and stock -> defend against rival barons

## Design Notes

Railroad Tycoon joins a train-operations model to a corporate-finance model. Stations come in four sizes (signal tower, depot, station, terminal) with growing service areas, and an economy setting chooses between a simple economy where big cities buy almost anything and a complex one where they buy only certain goods. The company starts with $1 million split between equity and a loan, raises more through bonds, and trades in a small stock market where rival barons attempt buyouts and rate wars. Meier took the idea from the board game 1830 and also cited SimCity. Track construction has no matching mechanic in the taxonomy (proposed as track-laying), and dated vehicle availability is proposed as dated-tech-timeline.

## Relations

**influenced by**

- [SimCity](../game/simcity-1989.md)

**uses**

- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) (core): Each train gets ordered stops and a consist of mail, passenger, and freight cars for nine commodity types; consists can be changed at any stop.
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (core): Stations supply and demand goods and passengers; under the complex economy cities accept only certain products, so routing follows demand.
- [Equity and buyouts](../mechanic/equity-buyouts.md) (core): A small stock market lets the player trade its own and rival stock; rivals use stock dealings to try to take over the player's railroad.
- [Rival firms](../mechanic/rival-firms.md) (core): AI railroad barons build competing lines and start rate wars over shared stations.
- [Building placement](../mechanic/free-placement.md) (core): Track is laid on a square tile grid and up to 32 stations are placed; the first station gets the engine shop where trains are built.
- [Service coverage](../mechanic/service-coverage.md) (supporting): Depots, stations, and terminals draw cargo from progressively larger surrounding areas.
- [Rail signaling](../mechanic/rail-signaling.md) (supporting): Signal towers act as passing loops and control train movements on shared track.
- [Production chains](../mechanic/production-chain.md) (supporting): Industries consume delivered freight and produce new cargo; players can build additional industries.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): Starting capital is half a loan; bonds raise more at interest rates tied to the economy.
- [Periodic ticks](../mechanic/periodic-ticks.md) (supporting): Accounts settle in two-year periods across a century of play.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Players can take direct control of individual train movements.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Delivery-time payment](../mechanic/delivery-time-payment.md) (supporting): Delivery revenue depends on cargo type, distance, and travel time, so fast trains earn more for passengers and mail.
- [Dated technology timeline](../mechanic/dated-tech-timeline.md) (supporting): New locomotive types become available as the calendar advances through the eras, from early steam engines toward diesels.
- [Track laying](../mechanic/track-laying.md) (core): Track is laid tile by tile across terrain whose slope and features add cost, linking up to 32 stations.

## Backlinks (computed)

**influenced:** [Sid Meier's Civilization](../game/civilization.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Transport Tycoon](../game/transport-tycoon.md)

## Sources

- [Railroad Tycoon (video game)](../source/src-wikipedia-railroad-tycoon.md)
- [Sid Meier](../source/src-wikipedia-sid-meier.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
