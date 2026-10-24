# Hamurabi

*Game* · `hamurabi` · status: **sourced**

A ten-turn text game in which the player, as the Babylonian king Hammurabi, splits a grain stock between feeding people, planting acres, and buying land while harvests, rats, and plague vary at random.

| field | value |
|---|---|
| aliases | The Sumer Game, King of Sumeria |
| year | 1968 |
| developer | Doug Dyment (Digital Equipment Corporation) |
| platforms | Mainframe / early micro |
| subgenre | City builder |
| sim domain | Economic, Urban |
| player role | Ruler / statesman |
| agency model | Policy / parameter |
| time model | Turn-based |
| sim scale | Settlement |
| fidelity | Abstract |
| perspective | Text / UI |
| win structure | Score / ranking |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Hobbyist / free |
| agent count order | Aggregate only |
| emergence | 2 |
| influence | 3 |
| cluster *(computed)* | C12 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 6 |

## Summary

A ten-turn text game in which the player, as the Babylonian king Hammurabi, splits a grain stock between feeding people, planting acres, and buying land while harvests, rats, and plague vary at random.

## Core Loop

read the steward's yearly report -> trade grain for land at a random price -> allocate grain to food and seed -> harvest, rats, arrivals, and plague resolve -> next year

## Design Notes

Three stocks (people, acres, bushels of grain) and three yearly allocations make the whole game one stock-and-flow puzzle: grain is food, seed, and the currency for land at once, so every bushel has competing uses. Randomness enters only through harvest yield, rat losses, a land price of 17 to 26 bushels per acre, arrivals, and a plague that halves the population, so the player manages expected value under variance. Dyment wrote it in FOCAL for the PDP-8 from a description of The Sumerian Game (1964); David Ahl's BASIC version spread it as a type-in listing and seeded Kingdom, Dukedom, and Santa Paravia en Fiumaccio.

## Relations

**uses**

- [Turn structure](../mechanic/turn-structure.md) (core): Ten rounds, each one year: a status report, then three typed decisions (acres to buy or sell, bushels to feed, acres to plant) before the year resolves.
- [Goods consumption](../mechanic/goods-consumption.md) (core): People must be fed grain each year; if at least 45 percent starve in one round the game ends early.
- [Crop cultivation](../mechanic/crop-cultivation.md) (core): Planted acres consume seed grain and return a random yield per acre at year end; each person can farm only a set amount of land, so labor caps planting.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Each year carries a chance of plague that halves the population.
- [Spoilage](../mechanic/spoilage.md) (supporting): Rats eat a random amount of stored grain each year, a loss on holding stock.
- [Advisors](../mechanic/advisors.md) (supporting): Each round opens with a steward's report of births, deaths, harvest, rat losses, and land price.

## Claims

- Hamurabi derives from The Sumerian Game (1964) by Mabel Addis and William McKay; Dyment wrote the FOCAL version after learning of it, and David Ahl expanded it in BASIC. *(confidence: high)* [[24](../source/src-wikipedia-hamurabi.md), [4](../source/src-wikipedia-city-building-game.md)]

## Sources

- [Hamurabi (video game)](../source/src-wikipedia-hamurabi.md)
- [City-building game](../source/src-wikipedia-city-building-game.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
