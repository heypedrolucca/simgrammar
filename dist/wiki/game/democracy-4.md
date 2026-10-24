# Democracy 4

*Game* · `democracy-4` · status: **sourced**

A turn-based government sim in which the player, as leader of a democracy, adjusts policy sliders whose weighted effects move statistics and overlapping voter groups, resolves dilemmas, and tries to balance the budget and win the next election.

| field | value |
|---|---|
| year | 2020 |
| year full release | 2022 |
| developer | Positech Games |
| platforms | PC, Console, Handheld |
| subgenre | Political sim |
| sim domain | Political / governance, Economic |
| player role | Ruler / statesman |
| agency model | Policy / parameter |
| time model | Turn-based |
| sim scale | Nation / polity |
| fidelity | Stylized |
| perspective | Text / UI |
| win structure | Survival duration |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~1,000 |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 11 |

## Summary

A turn-based government sim in which the player, as leader of a democracy, adjusts policy sliders whose weighted effects move statistics and overlapping voter groups, resolves dilemmas, and tries to balance the budget and win the next election.

## Core Loop

spend political capital to adjust policy sliders -> effects propagate through the weighted policy network -> statistics, situations, and voter group happiness shift -> resolve dilemmas and events -> make election promises -> win or lose the election

## Design Notes

Democracy 4 models a country as one visible causal graph: policies, statistics, situations, and voter groups are nodes, and the interface shows the weighted links in and out of each. The player is constrained by political capital, earned through loyal ministers and spent on policy changes, and by voters who belong to several groups at once. Political capital as a regenerating action currency is not yet a mechanic in the taxonomy (proposal political-capital).

## Relations

**uses**

- [Policy influence network](../mechanic/policy-influence-network.md) (core): Policies in seven areas (tax, economy, welfare, foreign policy, transport, law and order, public services) are sliders; the engine treats voters, groups, policies, ministers, and events as neurons in a homebrew network with bounded values, so weighted effects move statistics such as crime and air quality and the happiness of voter groups.
- [Elections](../mechanic/elections.md) (core): Before each general election the player makes two promises to the electorate; broken promises raise voter cynicism, and losing the election ends the game.
- [Interest groups](../mechanic/interest-groups.md) (core): Voter groups such as the religious, patriotic, parents, capitalists, socialists, liberals, and conservatives overlap, since each voter belongs to several, so pleasing every group is nearly impossible.
- [Dilemma cards](../mechanic/dilemma-cards.md) (supporting): Dilemmas, such as appointing a senior judge, must be resolved before the turn can end.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): Introducing or cancelling a policy costs political capital.
- [Taxation](../mechanic/taxation.md) (supporting): Excessive taxes cause tax evasion.
- [Loans and debt](../mechanic/loans-debt.md) (supporting): Deficits add to national debt that the player must pay down.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Situations such as pollution or homelessness persist while conditions hold, and events arrive outside player control.
- [Turn structure](../mechanic/turn-structure.md) (supporting)
- [Stats dashboards](../mechanic/stats-dashboards.md) (supporting)
- [Political capital](../mechanic/political-capital.md) (supporting): Political capital, earned through loyal ministers, is spent each turn to introduce, cancel, or adjust policies, so it caps how fast the government can change.

## Backlinks (computed)

**precedent for:** [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md), [Natural-language legislation](../opportunity/natural-language-legislation.md), [Participatory planning sandboxes](../opportunity/participatory-planning-sandboxes.md)

## Sources

- [Democracy 4](../source/src-wikipedia-democracy-4.md)
- [Democracy 4: the fixed income rewrite](../source/src-harris-2020-democracy4-fixed-income.md)
- [Democracy 4 comes to consoles](../source/src-positech-2024-democracy-4-consoles.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
