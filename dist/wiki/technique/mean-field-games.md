# Mean field games and mean-field learning

*Technique* · `mean-field-games` · status: **sourced**

Mean field game theory replaces an N-player game with one representative agent responding to the population distribution, and recent learning methods compute these equilibria for state spaces of hundreds of billions of states.

| field | value |
|---|---|
| aliases | MFG, mean field MARL, online mirror descent for MFGs |
| category | Game-theoretic solvers |
| year | 2021 |
| maturity | Research |
| trl | 3 |
| runtime | Offline authoring, Client real-time |
| determinism impact | Preserves |
| horizon | 3-5 years |
| risks | Legibility, Controllability |
| deployed in |  |
| affects count *(computed)* | 6 |

## Summary

Mean field game theory replaces an N-player game with one representative agent responding to the population distribution, and recent learning methods compute these equilibria for state spaces of hundreds of billions of states.

## Mechanism

Each agent is small, anonymous and interchangeable, so the game depends on others only through the population distribution m(t,x). An equilibrium is a fixed point: the representative agent's value function u solves a backward Hamilton-Jacobi-Bellman equation given m, and m evolves forward by a Fokker-Planck equation under the resulting policy. Numerical and learning methods iterate this pair: fictitious play averages past best responses; online mirror descent accumulates Q-values and updates the policy by a softmax of them; RL variants learn from samples when the model is unknown. Mean-field multi-agent RL applies the same idea locally, with each agent learning against the mean action of its neighbors. Cost scales with the size of the individual state space, not with the number of agents.

## Limitations

- Assumes anonymous, symmetric, individually negligible agents; named characters with unique state, or a player large enough to move the aggregate, need major-player extensions.
- Equilibrium describes settled behavior; the learning, overshoot and panic dynamics games often want are absent unless modeled separately.
- The forward-backward coupling needs the whole horizon at once, so player interventions mid-run require re-solving or a fast approximate solver.
- Convergence guarantees such as those for online mirror descent need monotonicity assumptions that game rules can violate.
- No game implementation was found in this run's sources.

## Sources

- src-lasry-2007-mean-field-games
- src-perolat-2021-mfg-omd
- src-yang-2018-mean-field-marl
- src-carmona-2020-mfg-finance-economics
- src-lauriere-2022-learning-mfg-survey

## Relations

**affects**

- [Traffic congestion](../mechanic/traffic-congestion.md) (Replaces substrate): Trip routing changes from each agent reacting to current travel times, which oscillates, to an equilibrium in which drivers anticipate congestion, computed once for the population at a cost independent of car count.
- [Crowd preferences](../mechanic/crowd-preferences.md) (Deepens): Park visitors can choose attractions in equilibrium with expected queues and crowding rather than greedily, producing realistic spreading of crowds across a park.
- [Service queues](../mechanic/service-queues.md) (Deepens): Queue choice and arrival timing become equilibrium behavior, so changing capacity at one service shifts load across the others as people anticipate the change.
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (Deepens): Prices can come from many small rational producers and consumers in equilibrium (as in MFG models of energy markets), instead of a fixed elasticity formula.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (Accelerates): One equilibrium policy over positions serves any number of agents, like a flow field that already includes congestion effects, replacing per-agent searches.
- [Travel mode choice](../mechanic/travel-mode-choice.md) (Deepens): Mode split solved as a population equilibrium in which each traveler responds to congestion created by everyone else.

## Backlinks (computed)

**applied in:** [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md), [Mean-field crowds and traffic](../opportunity/mean-field-crowds.md)

## Claims

- Lasry and Lions (2007) formulated mean field games as coupled forward-backward nonlinear PDEs for many rational players reacting to aggregates and showed the problems are generally well-posed. *(confidence: high)* [[217](../source/src-lasry-2007-mean-field-games.md)]
- Online mirror descent converged to MFG Nash equilibria under monotonicity, outperformed fictitious play, and solved MFGs with hundreds of billions of states. *(confidence: high)* [[218](../source/src-perolat-2021-mfg-omd.md)]
- Mean-field MARL let each agent learn against its neighbors' mean action, scaling multi-agent learning to many-agent battle games and solving the Ising model with model-free RL. *(confidence: high)* [[219](../source/src-yang-2018-mean-field-marl.md)]
- MFGs are applied to energy markets, bitcoin mining, macro-finance models and contract theory. *(confidence: medium)* [[220](../source/src-carmona-2020-mfg-finance-economics.md)]
- Learning methods for static, stationary and evolutive MFG equilibria and social optima are now surveyed as an established toolkit. *(confidence: medium)* [[221](../source/src-lauriere-2022-learning-mfg-survey.md)]

## Sources

- [Mean field games](../source/src-lasry-2007-mean-field-games.md)
- [Scaling up Mean Field Games with Online Mirror Descent](../source/src-perolat-2021-mfg-omd.md)
- [Mean Field Multi-Agent Reinforcement Learning](../source/src-yang-2018-mean-field-marl.md)
- [Applications of Mean Field Games in Financial Engineering and Economic Theory](../source/src-carmona-2020-mfg-finance-economics.md)
- [Learning in Mean Field Games: A Survey](../source/src-lauriere-2022-learning-mfg-survey.md)

---
Provenance: created in run `2026-10-24-techniques-sim-math`; reviewed in `2026-10-24-technique-links`.
