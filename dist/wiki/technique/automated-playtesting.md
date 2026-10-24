# Agent-based automated playtesting and balancing

*Technique* · `automated-playtesting` · status: **sourced**

Studios train imitation, reinforcement learning, and search agents to play builds, estimating level difficulty, pass and churn rates, progression pacing, map coverage, and exploits before players reach them.

| field | value |
|---|---|
| aliases | RL playtesting, human-like playtesting, difficulty prediction agents, game testing agents |
| category | Automated game design & playtesting |
| year | 2018 |
| maturity | Shipped (niche) |
| trl | 7 |
| runtime | Offline authoring, Analytics / live-ops |
| determinism impact | Preserves |
| horizon | Now |
| risks | Evaluation difficulty, Compute cost, Labor displacement |
| builds on | [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md) |
| affects count *(computed)* | 6 |

## Summary

Studios train imitation, reinforcement learning, and search agents to play builds, estimating level difficulty, pass and churn rates, progression pacing, map coverage, and exploits before players reach them.

## Mechanism

Agents play the game through an API or the rendered screen, in three families. Human-like agents are trained by supervised imitation of logged player moves, as with King's CNN on Candy Crush data, and their success rate on a new level predicts its difficulty for people. Goal-driven search or RL agents (A*, evolution strategies, deep RL) optimize task completion, and their action counts and success rates measure progression balance, as in EA's career-balancing study for The Sims Mobile. Curiosity agents are rewarded for novel states, maximizing map coverage to find stuck spots, missing collision, and unintended shortcuts. Agent results can feed a model of the player population: Roohi et al. combined RL agent pass rates with simulated skill, persistence, and boredom to predict per-level churn. In production, agents run against new builds inside the existing test pipeline and their coverage and failures are visualized for designers.

## Limitations

- Agents are not players: skill and style differ, and imitation agents need large logs of real player moves, which a new game lacks before launch.
- Integration dominates cost: EA SEED found engineering RL into production builds was the largest time sink, partly because development builds differ from the shipped game.
- Deep RL transfers poorly between games without heavy hyperparameter tuning, so cost grows roughly linearly with the number of titles.
- Open-ended simulation games have no single goal to optimize, so coverage or curiosity rewards stand in for design intent and can miss balance problems that only appear over long play.

## Sources

- src-gudmundsson-2018-human-like-playtesting
- src-zhao-2019-winning-isnt-everything
- src-bergdahl-2020-augmenting-automated-testing-drl
- src-gordillo-2021-curiosity-playtesting
- src-gillberg-2023-rl-testing-aaa
- src-roohi-2020-difficulty-churn
- src-deepmind-2025-sima-2-blog

## Relations

**affects**

- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md) (Tunes / balances): Agent pass rates plus a player-population model estimate how a difficulty ramp drives churn, so threat and difficulty curves can be tuned before release instead of from live telemetry.
- [Scenario objectives](../mechanic/scenario-objectives.md) (Tunes / balances): Each scenario or level gets a predicted pass rate from human-like agents, letting designers order and adjust goals and constraints against a target difficulty curve.
- [Career ladder](../mechanic/career-ladder.md) (Tunes / balances): Search agents measure how many actions each career path needs to reach each level, exposing careers that are much faster or slower than the rest, as in The Sims Mobile study.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (Tunes / balances): Curiosity and RL agents explore traversal exhaustively, finding stuck spots, missing collision, and shortcuts that scripted navmesh bots do not reach.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (Tunes / balances): Agents replaying the early game measure when resource and progression thresholds are reached, so unlock pacing is set from distributions instead of a few manual runs.
- [Statistical combat resolution](../mechanic/stat-combat-resolution.md) (Tunes / balances): Agent playthroughs estimate win rates and dominant unit mixes in statistical combat before release.

**builds on**

- [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md)

## Backlinks (computed)

**applied in:** [Content-elastic event systems](../opportunity/content-elastic-events.md), [Generated recipe graphs](../opportunity/generated-recipe-graphs.md), [Mechanic modding by description](../opportunity/language-modding.md), [Automated mechanic discovery](../opportunity/mechanic-discovery-search.md), [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md), [Quality-diversity scenario libraries](../opportunity/qd-scenario-libraries.md)

## Claims

- King's CNN trained on player moves in Candy Crush Saga and Candy Crush Soda Saga predicted human moves and level difficulty, correlating better with average difficulty than MCTS at a fraction of the compute (IEEE CIG 2018). *(confidence: high)* [[103](../source/src-gudmundsson-2018-human-like-playtesting.md)]
- EA used A* and evolution-strategy agents to balance The Sims Mobile careers during development and reported that deep RL needed heavy per-game tuning, so effort grew roughly linearly with the number of target games. *(confidence: high)* [[104](../source/src-zhao-2019-winning-isnt-everything.md)]
- EA SEED's RL test agents found a wall missing its collision mesh that scripted navmesh agents missed and located all five stuck areas in a test map, and curiosity rewards raised coverage of a complex 3D map. *(confidence: high)* [[105](../source/src-bergdahl-2020-augmenting-automated-testing-drl.md), [106](../source/src-gordillo-2021-curiosity-playtesting.md)]
- EA SEED added an experimental RL system to scripted-bot automated testing for AAA titles including Battlefield 2042 and Dead Space (2023) and reported that integration, not algorithms, consumed the most time. *(confidence: high)* [[107](../source/src-gillberg-2023-rl-testing-aaa.md)]
- RL agents combined with a player-population model of skill, persistence, and boredom predicted per-level pass and churn rates for Angry Birds Dream Blast. *(confidence: high)* [[108](../source/src-roohi-2020-difficulty-churn.md)]
- SIMA 2 (2025) follows language instructions in commercial 3D games through screen input and virtual keyboard and mouse and transfers skills across games, but still struggles with long-horizon tasks, memory, and precise low-level control. *(confidence: medium)* [[109](../source/src-deepmind-2025-sima-2-blog.md)]

## Sources

- [Human-Like Playtesting with Deep Learning](../source/src-gudmundsson-2018-human-like-playtesting.md)
- [Winning Isn't Everything: Enhancing Game Development with Intelligent Agents](../source/src-zhao-2019-winning-isnt-everything.md)
- [Augmenting Automated Game Testing with Deep Reinforcement Learning](../source/src-bergdahl-2020-augmenting-automated-testing-drl.md)
- [Improving Playtesting Coverage via Curiosity Driven Reinforcement Learning Agents](../source/src-gordillo-2021-curiosity-playtesting.md)
- [Technical Challenges of Deploying Reinforcement Learning Agents for Game Testing in AAA Games](../source/src-gillberg-2023-rl-testing-aaa.md)
- [Predicting Game Difficulty and Churn Without Players](../source/src-roohi-2020-difficulty-churn.md)
- [SIMA 2: An Agent that Plays, Reasons, and Learns With You in Virtual 3D Worlds](../source/src-deepmind-2025-sima-2-blog.md)

---
Provenance: created in run `2026-10-24-techniques-rl-design`; reviewed in `2026-10-24-technique-links`.
