# Prom Week

*Game* · `prom-week` · status: **sourced**

A 2012 browser social sim in which the player picks social exchanges among 18 high school students in the week before prom, with the Comme il Faut rule system deciding who wants to do what and how targets respond.

| field | value |
|---|---|
| year | 2012 |
| developer | UC Santa Cruz Expressive Intelligence Studio |
| platforms | Web |
| subgenre | Social sim |
| sim domain | Social / interpersonal |
| player role | Overseer |
| agency model | Direct unit control |
| time model | Turn-based |
| sim scale | Household / crew |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | Academic / research |
| agent count order | ~10 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 6 |

## Summary

A 2012 browser social sim in which the player picks social exchanges among 18 high school students in the week before prom, with the Comme il Faut rule system deciding who wants to do what and how targets respond.

## Core Loop

pick a level goal -> choose an initiator, a target, and a social exchange -> rules score volition and acceptance -> relationships, statuses, and history update -> new exchanges open -> the goal is met or the story turns another way

## Design Notes

Prom Week runs on Comme il Faut (CiF), which its UCSC authors describe as making social relationships playable: characters have traits, interests, statuses, and directed networks of liking, attraction, and respect, and more than 5,000 social considerations govern what each character wants and how others respond. The player never writes dialogue but chooses which social exchange a character initiates; CiF offers the exchanges a character is inclined toward, ranked by likelihood, and resolves acceptance from the social state of everyone involved, including what third parties think. Levels set story goals such as getting two characters to date, which turns the rule base into a puzzle with many solutions.

## Relations

**uses**

- [Social exchanges](../mechanic/social-exchanges.md) (core): Exchanges such as winking, being friendly, or being mean have preconditions; CiF rules decide whether the target accepts and update networks and statuses.
- [Relationship values](../mechanic/relationship-values.md) (core): Directed social networks track how much each character likes, is attracted to, and respects each other character; exchanges and third parties' opinions move the values.
- [Utility action selection](../mechanic/utility-action-selection.md) (supporting): A character's volition for each exchange is scored from matching rules, and only exchanges it is inclined toward are offered, ranked by likelihood.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Traits and interests weight which rules apply to a character.
- [Memories and thoughts](../mechanic/memories-thoughts.md) (supporting): Past exchanges are stored as social history that later rules reference.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Each level sets social goals, such as getting two named characters to date.

## Sources

- [Prom Week](../source/src-mccoy-2013-prom-week.md)
- [The Prom: An Example of Socially-Oriented Gameplay](../source/src-mccoy-2010-the-prom.md)
- [Prom Week Released on Facebook!](../source/src-treanor-2012-prom-week-released.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
