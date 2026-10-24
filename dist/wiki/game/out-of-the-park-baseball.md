# Out of the Park Baseball

*Game* · `out-of-the-park-baseball` · status: **sourced**

A text-based baseball management sim in which the player runs a franchise's roster, scouting, draft, trades, and finances while a pitch-by-pitch engine simulates games for career, historical, or fictional leagues.

| field | value |
|---|---|
| aliases | OOTP |
| year | 1999 |
| developer | Out of the Park Developments |
| platforms | PC |
| subgenre | Sports management |
| sim domain | Sports, Economic |
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
| production tier | Indie |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 11 |

## Summary

A text-based baseball management sim in which the player runs a franchise's roster, scouting, draft, trades, and finances while a pitch-by-pitch engine simulates games for career, historical, or fictional leagues.

## Core Loop

scout and draft players -> set rosters, lineups, and depth charts -> simulate games pitch by pitch -> players develop or decline -> trade, sign, and manage finances -> build a franchise across seasons

## Design Notes

OOTP simulates baseball pitch by pitch from player ratings and reports it as scrolling play-by-play text with a minimal diamond, plus 3D ballparks and ball flight from OOTP 15. Its range of setups defines it: real current leagues under the MLB and Minor League Baseball licenses from OOTP 16, historical play that drops the player into any era with real rookies arriving each season, and fictional leagues. Ratings are filtered through scouting, so the GM sees estimates rather than true values. The league keeps a full statistical history with HTML reports, so long careers build an almanac.

## Relations

**uses**

- [Attribute-driven match engine](../mechanic/attribute-match-engine.md) (core): Games are simulated pitch by pitch from batter, pitcher, and fielder ratings and managerial settings, in real time, pitch-by-pitch control, or bulk simulation.
- [Scouting knowledge](../mechanic/scouting-knowledge.md) (core): Player ratings are shown through a scout's evaluation, so accuracy depends on the scouting staff; the system was recoded in OOTP 14.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (core): The GM signs free agents, drafts amateurs, and hires managers, coaches, and scouts within a budget.
- [Agent skills](../mechanic/agent-skills.md) (core): Player ratings develop and decline over careers, including fielding development added in OOTP 14.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): Players age, retire, and are replaced by drafts and historical debuts.
- [Procedural characters](../mechanic/procedural-characters.md) (supporting): Fictional players are generated for fictional leagues and amateur drafts.
- [History chronicle](../mechanic/history-chronicle.md) (supporting): League histories, records, and player careers are stored and exported as HTML reports.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Franchise finances cover payroll, revenue, and budgets; the system was reworked in OOTP 16.
- [Stats dashboards](../mechanic/stats-dashboards.md) (supporting): Extensive statistics and reports cover every player, team, and season.
- [Negotiation](../mechanic/negotiation.md) (supporting): Contract offers to free agents and extensions to rostered players are accepted or rejected against each player's demands, and trades are proposed to AI general managers who accept, reject, or counter.
- [Board confidence](../mechanic/board-confidence.md) (supporting): Owners set expectations, and the general manager's job security falls when results and finances miss them, ending in dismissal.

## Sources

- [Out of the Park Baseball](../source/src-wikipedia-out-of-the-park-baseball.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
