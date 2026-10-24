# Reigns

*Game* · `reigns` · status: **sourced**

A swipe-based card game in which the player, as a succession of medieval monarchs, accepts or rejects advisers' requests that push church, people, army, and treasury meters, and each reign ends when any meter empties or fills.

| field | value |
|---|---|
| year | 2016 |
| developer | Nerial |
| platforms | PC, Mobile, Console, Handheld |
| subgenre | Political sim |
| sim domain | Political / governance |
| player role | Ruler / statesman |
| agency model | Policy / parameter |
| time model | Turn-based |
| sim scale | Nation / polity |
| fidelity | Abstract |
| perspective | Text / UI |
| win structure | Survival duration |
| failure model | Permadeath |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 3 |
| boundary case | True |
| cluster *(computed)* | C11 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 5 |

## Summary

A swipe-based card game in which the player, as a succession of medieval monarchs, accepts or rejects advisers' requests that push church, people, army, and treasury meters, and each reign ends when any meter empties or fills.

## Core Loop

draw an adviser's card -> swipe left or right -> church, people, army, and treasury meters shift -> a meter hits empty or full -> the king dies -> the next reign begins with unlocked cards

## Design Notes

Reigns reduces governance to four bounded meters in which both extremes are fatal, so every choice is a balancing act rather than a maximization. The swipe interface, modeled on Tinder, keeps each decision binary and fast. It is a boundary case included for the dilemma-card mechanic and its use of death as progress between reigns.

## Relations

**uses**

- [Dilemma cards](../mechanic/dilemma-cards.md) (core): Advisers present cards that the player swipes left or right; each choice moves one or more of four meters (church, people, army, treasury), and the reign ends when any meter becomes completely full or completely empty.
- [Dynasty succession](../mechanic/dynasty-succession.md) (core): When a king's reign ends, play continues with a new king; unlocked cards and some effects carry across reigns, and the in-game years keep advancing.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Story cards chain across reigns, such as the Devil's visits in the years 666, 1332, and 1998.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Completing tasks unlocks new cards.
- [Permadeath](../mechanic/permadeath.md) (supporting)

## Backlinks (computed)

**precedent for:** [Content-elastic event systems](../opportunity/content-elastic-events.md)

## Sources

- [Reigns (video game)](../source/src-wikipedia-reigns.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
