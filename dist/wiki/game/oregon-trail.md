# The Oregon Trail

*Game* · `oregon-trail` · status: **sourced**

An educational turn-based travel sim in which the player buys supplies and sets rations for a wagon journey to Oregon while random events, weather, and illness threaten the party.

| field | value |
|---|---|
| aliases | Oregon |
| year | 1971 |
| developer | Don Rawitsch, Bill Heinemann, and Paul Dillenberger; later MECC |
| platforms | Mainframe / early micro, PC |
| subgenre | Survival sim |
| sim domain | Biological / ecological, Economic |
| player role | Overseer |
| agency model | Policy / parameter |
| time model | Turn-based |
| sim scale | Household / crew |
| fidelity | Stylized |
| perspective | Text / UI |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | Hobbyist / free |
| agent count order | None |
| emergence | 2 |
| influence | 4 |
| cluster *(computed)* | C12 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 5 |

## Summary

An educational turn-based travel sim in which the player buys supplies and sets rations for a wagon journey to Oregon while random events, weather, and illness threaten the party.

## Core Loop

buy supplies at the outset and at forts -> choose food consumption and pace each leg -> random events, weather, and illness hit the party -> hunt for food and cross rivers -> reach Oregon or die on the trail

## Design Notes

Three student teachers wrote it in two weeks for a Minneapolis classroom, where it debuted on 3 December 1971; MECC distributed it on its time-sharing network from 1975 and on the Apple II from 1980. The 1971 model is a few stocks (food, bullets, clothing, supplies, cash) spent over about twelve two-week rounds, with one or two random events and weather drawn each round and typed hunting that rewards speed. The 1985 graphical version added adjustable pace and rations, river crossings by fording, caulking, or ferry, a party of five, professions that set difficulty and score, and tombstones left by earlier players.

## Relations

**uses**

- [Survival meters](../mechanic/survival-meters.md) (core): Food, clothing, and medical supplies are stocks drawn down each round at a player-chosen consumption rate; low food, cold without clothing, and untreated illness kill the traveler.
- [Random disasters](../mechanic/random-disasters.md) (core): Each round closes with one or two random events and weather, such as storms, wagon breakdowns, snakebites, or attacks, that cost supplies or health.
- [Turn structure](../mechanic/turn-structure.md) (core): The trip is a sequence of two-week rounds with fixed phases: stop at a fort or not, hunt or not, set consumption, then travel and resolve events.
- [Weather](../mechanic/weather.md) (supporting): Weather each round affects travel and illness.
- [Permadeath](../mechanic/permadeath.md) (supporting): Dead party members are gone; the 1985 version leaves a tombstone with an epitaph.

## Sources

- [The Oregon Trail (1971 video game)](../source/src-wikipedia-oregon-trail-1971.md)
- [The Oregon Trail (1985 video game)](../source/src-wikipedia-oregon-trail-1985.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
