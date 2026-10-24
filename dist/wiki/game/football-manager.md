# Football Manager

*Game* · `football-manager` · status: **sourced**

A football club management series in which the player sets tactics, training, transfers, and finances while a match engine simulates games from the attributes of players drawn from a researched database of real footballers.

| field | value |
|---|---|
| aliases | Worldwide Soccer Manager |
| year | 2004 |
| developer | Sports Interactive |
| platforms | PC, Mobile, Handheld, Console |
| subgenre | Sports management |
| sim domain | Sports, Economic, Social / interpersonal |
| player role | Manager / owner |
| agency model | Policy / parameter, Direct unit control |
| time model | Turn-based |
| sim scale | Household / crew |
| fidelity | High-fidelity |
| perspective | Text / UI |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player, Competitive |
| modding | Content |
| production tier | AA |
| agent count order | 10,000+ |
| emergence | 4 |
| influence | 4 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 15 |

## Summary

A football club management series in which the player sets tactics, training, transfers, and finances while a match engine simulates games from the attributes of players drawn from a researched database of real footballers.

## Core Loop

scout and sign players -> set tactics and training -> the match engine simulates fixtures from attributes and instructions -> morale, form, and finances shift -> the board and fans judge results -> rebuild the squad over seasons

## Design Notes

Football Manager simulates the whole football world from a database of real players, staff, and clubs maintained by fan researchers, with tens of thousands of players developing, aging, and moving in loaded leagues. Matches are simulated from player attributes and tactical instructions and shown through a 2D engine in FM 2005 and a 3D engine from FM 2009. Information is uncertain: scouts and analysts reveal attributes and fit, and scout knowledge of an area is tracked (as 0 to 100 percent from FM 2018). Everton agreed in 2008 to use the database for scouting. Contract and transfer talks and the board's job-security judgment have no matching mechanics in the taxonomy (proposed as negotiation and board-confidence). The series began as Championship Manager in 1992 and was relaunched under this name with FM 2005 in 2004.

## Relations

**uses**

- [Attribute-driven match engine](../mechanic/attribute-match-engine.md) (core): Fixtures are simulated event by event from each player's attributes, condition, and morale and the manager's tactics and touchline instructions, shown in 2D or 3D.
- [Scouting knowledge](../mechanic/scouting-knowledge.md) (core): Players' attributes are shown only as well as the club's scouts know them; scout knowledge accumulates per region and is shown as a percentage from FM 2018.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (core): Players and staff are signed through transfers, loans, and contracts with wages, bonuses, and agents.
- [Agent skills](../mechanic/agent-skills.md) (core): Player attributes develop through training schedules, match experience, and coaching quality up to individual potential.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): Players peak and decline with age, retire, and are replaced by yearly youth intakes.
- [Procedural characters](../mechanic/procedural-characters.md) (supporting): Generated youth players enter the database each season alongside the real ones.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Personality and hidden attributes such as professionalism affect development and reactions.
- [Relationship values](../mechanic/relationship-values.md) (supporting): Squad hierarchy, cohesion, and player opinions of the manager are tracked from FM 2018.
- [Social exchanges](../mechanic/social-exchanges.md) (supporting): Team talks and private conversations with players praise, criticize, or promise, changing morale.
- [Dilemma cards](../mechanic/dilemma-cards.md) (supporting): Press conferences pose questions with answer options that change morale and media relations.
- [Reputation](../mechanic/reputation.md) (supporting): Club and manager reputation set who will sign; board and fan confidence decide whether the manager is sacked.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Club finances cover wage and transfer budgets, with taxes added in FM 2013.
- [Stats dashboards](../mechanic/stats-dashboards.md) (supporting): Data analysts and statistics screens report player and team performance.
- [Negotiation](../mechanic/negotiation.md) (supporting): Transfer fees are negotiated with selling clubs and contracts with players and their agents over wages, length, bonuses, and clauses, and talks can break down.
- [Board confidence](../mechanic/board-confidence.md) (supporting): The board sets season expectations and, with fan confidence, judges results against them; falling confidence brings warnings and then sacking.

## Backlinks (computed)

**precedent for:** [Explained delegation to AI managers](../opportunity/explained-delegation.md)

## Sources

- [Football Manager](../source/src-wikipedia-football-manager.md)
- [Football Manager 2005](../source/src-wikipedia-football-manager-2005.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
