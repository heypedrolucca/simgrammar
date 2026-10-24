# Board confidence

*Mechanic* · `board-confidence` · status: **sourced**

An evaluator such as a board, owner, or chairman sets expectations, updates a confidence stock from results against them, and fires the player below a threshold.

| field | value |
|---|---|
| aliases | job security, owner expectations, board expectations, sacking |
| family | Risk & failure |
| substrate | Aggregate stocks, Rule system |
| math basis | System dynamics / ODEs, Probability / statistics |
| feedback | Balancing (negative) |
| player interface | Observation only, Choice / cards |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Out of the Park Baseball](../game/out-of-the-park-baseball.md) |
| earliest year *(computed)* | 1999 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

An evaluator such as a board, owner, or chairman sets expectations, updates a confidence stock from results against them, and fires the player below a threshold.

## Definition

Owns a set of expectations (league finish, cup progress, budget balance, profit, playing style, youth development) imposed or agreed at the start of a season or term, and a confidence stock held by an evaluator such as a board, owner, chairman, or fan base. After each match, report, or period the stock moves by the gap between results and expectations, weighted by importance and recency; crossing warning levels triggers meetings, ultimatums, or budget cuts, and falling below the floor ends the job. Expectations are re-set from the organization's reputation and resources, so success raises the bar. Football Manager has the board judge the manager's performance and, with fan confidence, decide whether the manager is sacked; other sports management games set owner or chairman goals for each season. It differs from elections, where an electorate decides tenure at fixed dates, and from scenario-objectives, which test a fixed goal at a deadline; here a continuously updated stock can end the job at any time.

## Player Experience

A clock on the player's job. Every result moves a meter the player does not fully control, so a run of bad form becomes existential and a promised top-four finish hangs over every match. Success raises expectations, so security never fully arrives.

## Design Levers

- how expectations are set: imposed from reputation or negotiated with the player
- weight per result and how fast older results fade
- warning thresholds and the events they trigger (meetings, ultimatums, budget cuts)
- firing threshold and whether the player continues in a new job
- separate evaluators (board, owner, fans) and how they combine
- grace period after hiring

## Failure Modes

- Expectations re-set too aggressively after success make long tenures impossible, punishing good play.
- Sackings driven by short streaks feel arbitrary when simulated results have high variance.
- Confidence that forgives too easily makes the threat vanish after one good season.
- Hidden weights leave players unsure which goal actually matters.

## Dynamics

- Players manage expectations as well as results, for example by accepting modest targets to buy safety.
- High-variance match engines produce sudden sackings that become career stories.
- Being fired and hired by another club turns failure into a career path instead of a game over.

## Open Questions

- Can language-model board members with distinct priorities negotiate expectations with the player in conversation and remember broken promises?
- What weighting of recent results makes sackings feel deserved under a high-variance match simulation?

## Backlinks (computed)

**used by:** [Football Manager](../game/football-manager.md), [Motorsport Manager](../game/motorsport-manager.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md)

## Claims

- In Football Manager the board judges the manager's performance. *(confidence: medium)* [[59](../source/src-wikipedia-football-manager.md), [60](../source/src-wikipedia-football-manager-2005.md)]

## Sources

- [Football Manager](../source/src-wikipedia-football-manager.md)
- [Football Manager 2005](../source/src-wikipedia-football-manager-2005.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
