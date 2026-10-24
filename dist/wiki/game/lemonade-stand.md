# Lemonade Stand

*Game* · `lemonade-stand` · status: **sourced**

A 1973 educational business sim in which the player runs a lemonade stand for 12 days, setting glasses made, advertising signs, and price against a daily weather report.

| field | value |
|---|---|
| year | 1973 |
| developer | Bob Jamison (MECC) |
| platforms | Mainframe / early micro, PC |
| subgenre | Business / economic sim |
| sim domain | Economic |
| player role | Manager / owner |
| agency model | Policy / parameter |
| time model | Turn-based |
| sim scale | Facility |
| fidelity | Abstract |
| perspective | Text / UI |
| win structure | Score / ranking |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Competitive |
| modding | None |
| production tier | Hobbyist / free |
| agent count order | Aggregate only |
| emergence | 1 |
| influence | 2 |
| cluster *(computed)* | C12 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 7 |

## Summary

A 1973 educational business sim in which the player runs a lemonade stand for 12 days, setting glasses made, advertising signs, and price against a daily weather report.

## Core Loop

read the weather report -> choose glasses to make, signs to buy, and price per glass -> demand resolves into sales -> profit or a storm loss -> reinvest the next day

## Design Notes

Lemonade Stand reduces a business to three daily inputs (glasses made, advertising signs, price per glass) and one exogenous variable, the weather (sunny, cloudy, or hot and dry), which shifts demand. Shocks are random: thunderstorms on cloudy days wipe out the day's investment, and street closures or wind that blows signs away also occur. Up to 30 players can each run an independent stand under the same weather. Signs are an early case of advertising spend used as a demand lever; the taxonomy has no mechanic for marketing spend, so the run proposes advertising-awareness.

## Relations

**uses**

- [Customer value choice](../mechanic/customer-value-choice.md) (core): Aggregate customers buy more at lower prices and with more advertising signs; sales are capped by the glasses made that day.
- [Weather](../mechanic/weather.md) (core): Each day is sunny, cloudy, or hot and dry, and the weather sets the demand level the price and sign choices act on.
- [Turn structure](../mechanic/turn-structure.md) (core): Twelve rounds of one day each: the player makes decisions, the day resolves, and an earnings report follows.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Cash on hand limits how many glasses and signs can be bought each day.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Thunderstorms void a day's profits; street closures and blown-away signs also occur.
- [Forecasting](../mechanic/forecasting.md) (supporting): The weather for the day is shown before the player commits to production.
- [Advertising and awareness](../mechanic/advertising-awareness.md) (supporting): Advertising signs bought each day raise that day's demand alongside price and weather, with no carryover between days.

## Sources

- [Lemonade Stand](../source/src-wikipedia-lemonade-stand.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
