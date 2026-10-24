# Motorsport Manager

*Game* · `motorsport-manager` · status: **sourced**

A racing team management game in which the player designs car parts across seasons, hires drivers and staff, and makes live strategy calls on tyres, pit stops, and weather while races are simulated.

| field | value |
|---|---|
| year | 2016 |
| developer | Playsport Games |
| platforms | PC |
| subgenre | Sports management |
| sim domain | Sports, Physical / mechanical, Economic |
| player role | Manager / owner |
| agency model | Policy / parameter, Direct unit control, Design then test |
| time model | Real-time with pause |
| sim scale | Household / crew |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 2 |
| influence | 1 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 10 |

## Summary

A racing team management game in which the player designs car parts across seasons, hires drivers and staff, and makes live strategy calls on tyres, pit stops, and weather while races are simulated.

## Core Loop

design and build car parts -> hire drivers, designers, and mechanics -> set race weekend strategy -> race simulates with tyre, fuel, and weather calls -> results earn money and standing -> develop next season's car

## Design Notes

Motorsport Manager splits the job into a between-races engineering game and a live race game. Between races the player commissions car parts and chooses which go into next season's car, trading performance against development time. During races the simulation runs in real time with pause, and the player decides tyre compounds, pit timing, and whether to gamble on a fast pit stop or stay on slicks as dynamic weather changes. Drivers have personality types that cause team drama and respond to tough love or support. A simpler mobile game of the same name was released on iOS in 2014; this entry covers the 2016 PC game.

## Relations

**uses**

- [Attribute-driven match engine](../mechanic/attribute-match-engine.md) (core): Races are simulated in real time from driver attributes, car part performance, tyres, fuel, and weather, with the player intervening on strategy.
- [Design performance rating](../mechanic/design-performance-rating.md) (core): Car parts are designed and built over time, rated on performance, and chosen for next season's car, which sets pace at pre-season testing.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (core): Drivers, team managers, mechanics, and designers are hired; skilled mechanics shorten pit stops.
- [Weather](../mechanic/weather.md) (core): Dynamic weather during sessions forces calls such as switching to intermediates or staying on slicks.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Drivers have distinct personality types that cause team drama and respond differently to tough love or support.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Tyres wear over a stint and car parts lose condition, so strategy balances pace against wear.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Prize money and sponsor income fund salaries and part development.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting): Races run in real time with pause and speed controls.
- [Negotiation](../mechanic/negotiation.md) (supporting): Driver and staff contracts are negotiated over wages, length, and bonuses, and candidates can reject offers and end talks.
- [Board confidence](../mechanic/board-confidence.md) (supporting): The chairman sets objectives each season, and missing them lowers the chairman's confidence until the player is fired.

## Sources

- [Motorsport Manager](../source/src-wikipedia-motorsport-manager.md)
- [Motorsport Manager on Steam](../source/src-steam-2026-motorsport-manager.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
