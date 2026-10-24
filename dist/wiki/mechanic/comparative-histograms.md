# Comparative histograms

*Mechanic* · `comparative-histograms` · status: **sourced**

A player's solution is plotted against distributions of other players' scores on several metrics.

| field | value |
|---|---|
| aliases | score histograms, solution histograms |
| family | Information & legibility |
| substrate | UI layer |
| math basis | Probability / statistics, Optimization |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 1 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Established |
| requires | [Design performance rating](../mechanic/design-performance-rating.md) |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [SpaceChem](../game/spacechem.md) |
| earliest year *(computed)* | 2011 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.1 |

## Definition

After a solution passes validation, the game computes several independent metrics that trade off against each other and shows the player's value on each as a marker on a histogram of all players' (or friends') values for that puzzle. State owned: per-puzzle score distributions aggregated on a server, plus the player's best per metric. Update rule: on completion, simulate the solution, compute metrics, upload them, and fetch the current distributions. The metrics come from a design-evaluation mechanic; this mechanic owns only the population comparison. Canonical forms are Zachtronics games: SpaceChem ranks instructions, cycles, and reactors, and Zach Barth designed its global histograms so players could check a solution without being overwhelmed by the top players a leaderboard lists; Opus Magnum compares cost, cycles, and area; TIS-100, Shenzhen I/O, Infinifactory, and Exapunks use the same pattern.

## Player Experience

Instead of a rank, the player sees where they sit in a crowd on each axis. A solution that is slow but cheap still feels good, and a visible tail of better scores invites returning to a solved puzzle to shave cycles. Comparison is social but low in intimidation.

## Design Levers

- number of metrics and how strongly they trade off against each other
- global distribution versus friends-only comparison
- bin width and handling of outliers or exploit scores
- per-metric personal bests versus recognition of Pareto-optimal combinations
- whether any reward is attached to good scores (Zachtronics deliberately attaches none)

## Failure Modes

- Metrics that do not trade off collapse into one dominant solution, and the histograms show a single spike.
- Exploit or bugged solutions create impossible scores that distort the left tail.
- Late puzzles are attempted only by skilled survivors, so average players appear below median on every metric.
- Independent per-metric bars ignore balanced solutions; Opus Magnum players invented an unofficial sum metric to score them.

## Dynamics

- Players replay solved puzzles to move their marker, extending content life without new content.
- Communities build external record trackers for Pareto frontiers that the in-game histograms do not show.
- Friend comparison produces asynchronous rivalry without direct competition.

## Open Questions

- Can distributions seeded by automated solvers before launch give useful comparison targets without discouraging human players?
- Does showing a Pareto frontier instead of per-metric histograms change which tradeoffs players explore?

## Relations

**requires**

- [Design performance rating](../mechanic/design-performance-rating.md)

**synergy**

- [Design performance rating](../mechanic/design-performance-rating.md): Multi-metric ratings become social when plotted against everyone else's solutions (Opus Magnum).
- [Player programming](../mechanic/player-programming.md): Open-ended programming puzzles gain replay value from optimization histograms.

**tension**

- [Storyteller director](../mechanic/storyteller-director.md): Directed randomness makes scores incomparable across players.

## Backlinks (computed)

**affected by:** [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md)

**involved in:** [Quality-diversity scenario libraries](../opportunity/qd-scenario-libraries.md), [Simulation games as agent benchmarks](../opportunity/sims-as-agent-benchmarks.md), [Specification programming games](../opportunity/specification-programming-games.md)

**used by:** [Opus Magnum](../game/opus-magnum.md), [SpaceChem](../game/spacechem.md)

## Claims

- Zach Barth designed SpaceChem's global histograms so players could check their solutions without feeling overwhelmed by the top players a leaderboard would list. *(confidence: medium)* [[29](../source/src-wikipedia-spacechem.md)]
- Opus Magnum ranks solutions on cycles, cost, and area, and players combine them in an unofficial sum statistic. *(confidence: medium)* [[28](../source/src-wikipedia-opus-magnum.md)]
- Zachtronics deliberately offers no in-game rewards for optimization in Opus Magnum, so players who optimize do so for intrinsic reasons. *(confidence: high)* [[68](../source/src-couture-2019-road-to-igf-opus-magnum.md)]

## Sources

- [SpaceChem](../source/src-wikipedia-spacechem.md)
- [Opus Magnum](../source/src-wikipedia-opus-magnum.md)
- [Road to the IGF: Zachtronics' Opus Magnum](../source/src-couture-2019-road-to-igf-opus-magnum.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
