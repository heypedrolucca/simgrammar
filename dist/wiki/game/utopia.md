# Utopia

*Game* · `utopia` · status: **contested**

A two-player Intellivision strategy game in which rival island rulers spend gold on buildings and boats in timed rounds, scoring points for how well their populations are housed, fed, and kept content.

| field | value |
|---|---|
| year | 1982 |
| developer | Don Daglow (Mattel Electronics) |
| platforms | Console, Mainframe / early micro |
| subgenre | City builder |
| sim domain | Urban, Economic, Political / governance |
| player role | Ruler / statesman |
| agency model | Zoning / placement, Direct unit control |
| time model | Real-time |
| sim scale | Settlement |
| fidelity | Abstract |
| perspective | Top-down / side 2D |
| win structure | Competitive victory |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Competitive |
| modding | None |
| production tier | AA |
| agent count order | Aggregate only |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

A two-player Intellivision strategy game in which rival island rulers spend gold on buildings and boats in timed rounds, scoring points for how well their populations are housed, fed, and kept content.

## Core Loop

spend gold on houses, farms, factories, forts, and boats -> round timer runs while boats fish and clouds rain on farms -> end-of-round income and score from population welfare -> rebels, storms, and pirates strike -> next round

## Design Notes

Utopia runs as up to 50 real-time rounds of 30 to 120 seconds, so the turn boundary is a clock rather than a player action; income from factories arrives at round end while fishing and rain income depend on what happens during the round. Two players share one screen with no AI opponent, and each can fund rebels on the other's island or sink the other's fishing boat with a PT boat, so the welfare score is contested directly. It is commonly cited as the first city-building game, though its release year is disputed between 1981 and 1982.

## Relations

**uses**

- [Building placement](../mechanic/free-placement.md) (core): Each player places houses, schools, factories, hospitals, and forts on tiles of their own island, paid for with gold bars.
- [Periodic ticks](../mechanic/periodic-ticks.md) (core): Rounds last 30 to 120 seconds for up to 50 rounds; factory output pays out and the score updates at each round's end.
- [Citizen satisfaction](../mechanic/citizen-satisfaction.md) (core): Points depend on population and how well it is housed, fed, and kept happy; neglect lowers the score and invites rebellion.
- [Stability and unrest](../mechanic/stability-unrest.md) (supporting): Rebels reduce the score and can destroy buildings; a rival can pay gold to fund rebels on the other island.
- [Weather](../mechanic/weather.md) (supporting): Randomly generated rain clouds earn income when they pass over a player's farms; tropical storms and hurricanes also occur.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Fishing boats earn income only while positioned over a moving school of fish.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Players steer fishing boats and PT boats directly; PT boats sink the opponent's fishing boat.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Gold bars are the single currency for all construction.

## Claims

- Wikipedia's infobox and lead date the Intellivision release to 1982-06-03 (Aquarius port 1983), while Guinness World Records names Utopia, released on the Intellivision in 1981, as the first city-building videogame. *(confidence: medium)* [[48](../source/src-wikipedia-utopia.md), [49](../source/src-guinness-2026-first-city-building-game.md)] **Disputed:** Release year: 1982 per Wikipedia versus 1981 per Guinness World Records and the original skeleton. This entry uses 1982, the dated release.

## Sources

- [Utopia (1981 video game)](../source/src-wikipedia-utopia.md)
- [First city-building videogame](../source/src-guinness-2026-first-city-building-game.md)
- [City-building game](../source/src-wikipedia-city-building-game.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
