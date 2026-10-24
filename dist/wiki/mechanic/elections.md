# Elections

*Mechanic* · `elections` · status: **sourced**

Periodic votes by simulated or real voters determine tenure or policy.

| field | value |
|---|---|
| aliases | voting, polls |
| family | Governance & policy |
| substrate | Agent-based, Stochastic events, Rule system |
| math basis | Mechanism design / auctions, Probability / statistics, Social network models |
| feedback | Balancing (negative) |
| player interface | Observation only, Choice / cards |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [A Tale in the Desert](../game/a-tale-in-the-desert.md) |
| earliest year *(computed)* | 2003 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.438 |

## Definition

Owns an election calendar, an electorate (simulated voters, voting blocs, or real players), candidates or parties, and a counting rule. At each election every voter's choice is computed from satisfaction, group membership, and campaign effects, or cast by a real player; the counting rule (plurality, threshold, single transferable vote) picks the winner, which sets tenure, a ruler, or party strength. Losing can end the game or remove the player's powers. Democracy 4 (2020) gives each simulated citizen membership in several overlapping voter groups, so elections depend on keeping enough groups content; before each election the player makes two promises, and broken promises raise cynicism. Frostpunk 2 (2024) has a council of 100 faction delegates vote on each proposed law, needing 51 votes, or two thirds for laws that expand the Steward's power. Tropico lets El Presidente hold or rig elections. EVE Online has real players elect the Council of Stellar Management, using single transferable vote since the eighth council.

## Player Experience

A deadline for popularity. The player tracks polls, times unpopular reforms for just after an election, courts swing groups, and feels the stakes rise as election day nears. In player-run elections the experience shifts to campaigning and alliance-building.

## Design Levers

- election frequency and whether the player can call, delay, or cancel elections
- voter model: aggregate approval, blocs, or individually simulated voters with overlapping groups
- franchise rules that decide who votes and with what weight
- counting rule and thresholds
- consequence of losing (game over, loss of office, reduced powers)
- manipulation options such as rigging, promises, or campaign spending, and their costs

## Failure Modes

- Elections that only test approval above 50% add a pass or fail check without strategy.
- Cheap rigging or postponement removes the threat, so elections become a formality.
- Real-player elections with low turnout let organized blocs capture outcomes, which can be accepted as play or felt as unfair.

## Dynamics

- Election cycles create policy rhythms: unpopular measures early in a term, giveaways before the vote.
- Overlapping voter groups make every policy please someone and anger someone, which pushes players toward coalition math.
- Promise systems couple short-term electoral gain to long-term credibility.

## Open Questions

- Can LLM-driven voters and rival candidates respond to the player's actual speeches and platform, so campaigning is persuasion rather than slider tuning?
- How should simulated electorates balance realism (stable partisanship) against responsiveness to player choices?

## Backlinks (computed)

**affected by:** [LLM models of individual human choice](../technique/human-behavior-simulation-models.md), [Many-agent LLM societies](../technique/llm-agent-societies.md)

**involved in:** [Natural-language legislation](../opportunity/natural-language-legislation.md)

**used by:** [A Tale in the Desert](../game/a-tale-in-the-desert.md), [Democracy 4](../game/democracy-4.md), [Eco](../game/eco.md), [EVE Online](../game/eve-online.md), [Frostpunk 2](../game/frostpunk-2.md), [Project Sid](../game/project-sid.md), [Tropico 6](../game/tropico-6.md)

## Sources

- [Democracy 4](../source/src-wikipedia-democracy-4.md)
- [Frostpunk 2](../source/src-wikipedia-frostpunk-2.md)
- [Eve Online](../source/src-wikipedia-eve-online.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
