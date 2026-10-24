# Care-dependent development

*Mechanic* · `care-dependent-development` · status: **sourced**

A creature's or character's accumulated care or attribute history selects which form or outcome it develops into at each stage boundary, from a fixed branching table.

| field | value |
|---|---|
| aliases | branching development, care-based evolution, raising outcomes, endings by upbringing |
| family | Biology & health |
| substrate | Rule system, Agent-based |
| math basis | Combinatorics, Markov / stochastic processes |
| feedback | None |
| player interface | Observation only, Choice / cards |
| legibility | 2 |
| emergence potential | 2 |
| authoring cost | 4 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Princess Maker 2](../game/princess-maker-2.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

A creature's or character's accumulated care or attribute history selects which form or outcome it develops into at each stage boundary, from a fixed branching table.

## Definition

Owns, per raised creature or character, a running history of care and attributes (tallies of neglect and discipline, stat values, behavior counts) and a developmental table that maps ranges of that history to next-stage forms or final outcomes. Between stages the history accumulates from care actions and scheduled activities; at each stage boundary the table is evaluated, by first matching branch or best score, and the chosen form replaces the old one, setting appearance, stats, behavior, lifespan, or an ending. Tamagotchi (1996) chooses its adult character from the quality of care it received, so neglect yields a different creature rather than only a sick one. Princess Maker 2 (1993) develops the daughter's attributes from age 10 to 18 and then selects one of 74 career endings from her attributes and history. It differs from creature-care, which owns need meters and care actions; from lifecycle-aging, whose stages advance without branching; and from trait-inheritance, where form comes from the parents' genes rather than the individual's own history.

## Player Experience

Raising with consequences. Every feeding, scolding, lesson, or missed call writes into a history the player cannot fully see, and the reveal at the next stage passes judgment on it. Players replay to see other branches, compare results with friends, and look up the tables to aim for a particular form or ending.

## Design Levers

- which history variables are tracked and how they are weighted
- number of stage boundaries and branches per boundary
- threshold placement and whether ties resolve by priority or chance
- visibility of the table (hidden, hinted, or shown)
- whether later care can redeem an early bad branch
- how different branches are mechanically, from cosmetic to changes in stats, lifespan, or ending

## Failure Modes

- Hidden tables push optimization to wikis and walkthroughs, after which players follow a recipe instead of raising.
- Branches that differ only cosmetically make care history feel irrelevant.
- Early branches that cannot be recovered punish new players for mistakes they could not understand.
- A single best branch turns the table into a target and removes variety.

## Dynamics

- Players compare outcomes socially (which character did yours become), turning private care into shared stories.
- Replays to collect branches convert one raising loop into a collection game.
- Players reverse-engineer the tables, and community guides become part of the game's culture.

## Open Questions

- Can generative models produce a distinct form or ending for every care history, and do players value that over a small set of collectible authored branches?
- How much of the table should be visible so that care feels intentional without becoming a recipe?

## Backlinks (computed)

**used by:** [Princess Maker 2](../game/princess-maker-2.md), [Tamagotchi](../game/tamagotchi.md)

## Claims

- Tamagotchi (1996) has Hunger, Happy, and Training meters, life stages, and an adult form that depends on care. *(confidence: medium)* [[61](../source/src-wikipedia-tamagotchi.md)]
- Princess Maker 2 covers the daughter's life from age 10 to 18 and has 74 endings. *(confidence: medium)* [[62](../source/src-wikipedia-princess-maker-2.md)]

## Sources

- [Tamagotchi](../source/src-wikipedia-tamagotchi.md)
- [Princess Maker 2](../source/src-wikipedia-princess-maker-2.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
