# Regret minimization and search for imperfect-information games

*Technique* · `imperfect-information-solvers` · status: **sourced**

Self-play algorithms that minimize counterfactual regret over information sets, refined by real-time subgame search, compute hard-to-exploit strategies that bluff and hide information and beat top humans at poker, Stratego, and Scotland Yard.

| field | value |
|---|---|
| aliases | CFR, MCCFR, Libratus, DeepStack, Pluribus, ReBeL, DeepNash, Student of Games |
| category | Game-theoretic solvers |
| year | 2019 |
| maturity | Research |
| trl | 5 |
| runtime | Offline authoring, Client real-time |
| determinism impact | Mitigable |
| horizon | 3-5 years |
| risks | Compute cost, Legibility, Controllability |
| affects count *(computed)* | 6 |

## Summary

Self-play algorithms that minimize counterfactual regret over information sets, refined by real-time subgame search, compute hard-to-exploit strategies that bluff and hide information and beat top humans at poker, Stratego, and Scotland Yard.

## Mechanism

A decision point is an information set: all histories the player cannot tell apart. CFR traverses the game tree repeatedly; at each information set it computes each action's counterfactual regret (how much better it would have done, weighted by the probability that others reach that set) and sets the next strategy by regret matching, proportional to positive cumulative regret. The average strategy converges to a Nash equilibrium in two-player zero-sum games, and Monte Carlo CFR samples the tree to scale. Large games are abstracted (bucketed hands and bet sizes) into an offline blueprint that is refined during play by subgame search: Libratus used nested subgame solving, DeepStack re-solved to a depth limit with a learned value function, and Pluribus searched a few moves ahead while letting each opponent pick among four continuation strategies at the leaves. ReBeL and Student of Games learn values over public belief states and search with them, reducing to AlphaZero-style search in perfect-information games. DeepNash instead learns a policy model-free with Regularised Nash Dynamics and no search. Outputs are mixed strategies, so the agent bluffs at calibrated rates.

## Limitations

- Convergence guarantees hold for two-player zero-sum games; Pluribus's six-player play works empirically without them, and cooperative or general-sum simulation games fall outside the theory.
- Large games need designed abstractions of actions and states; a simulation with continuous economies and many units has no obvious abstraction to solve.
- Runtime search costs seconds per decision (Pluribus averaged about 20 seconds per hand on two CPUs), far above per-frame budgets for many agents.
- Equilibrium play avoids being exploited rather than exploiting weak players, which can feel passive, and randomized bluffs read as arbitrary unless the game explains them.

## Sources

- src-brown-2018-libratus
- src-moravcik-2017-deepstack
- src-brown-2019-pluribus
- src-facebook-2019-pluribus-blog
- src-brown-2020-rebel
- src-perolat-2022-deepnash
- src-schmid-2023-student-of-games

## Relations

**affects**

- [Fog of war](../mechanic/fog-of-war.md) (Deepens): AI players reason over unseen state as a belief distribution and play strategies that are hard to exploit, instead of cheating with full map knowledge or ignoring hidden units, so concealment and feints work against the AI as they would against a person.
- [Scouting knowledge](../mechanic/scouting-knowledge.md) (Deepens): Equilibrium strategies put a value on information, so AI opponents scout, hide their own attributes, and avoid revealing them through their actions, giving the player's scouting system a real counterpart.
- [Auctions](../mechanic/auctions.md) (Replaces substrate): AI bidders play mixed strategies over private valuations instead of bidding a fixed fraction of value, which removes simple exploits such as always outbidding the AI by one unit.
- [Military operations](../mechanic/military-operations.md) (Deepens): Deception becomes a stable part of AI play, as DeepNash bluffed with hidden unit identities in Stratego, so operational wargames could field opponents that feint and conceal force composition at calibrated rates.
- [Rival firms](../mechanic/rival-firms.md) (Deepens): Competitors with private costs or plans can bluff in price wars and market entry, and designers can measure how exploitable a fixed AI pricing script is by computing a best response against it.
- [Negotiation](../mechanic/negotiation.md) (Deepens): Bargaining with hidden reservation values is an imperfect-information game; equilibrium strategies bluff and concede in ways scripted thresholds cannot.

## Backlinks (computed)

**applied in:** [Negotiating faction AI](../opportunity/negotiating-faction-ai.md)

**built upon by:** [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md)

## Claims

- Libratus beat top professionals at heads-up no-limit Texas hold'em (Science, January 2018). *(confidence: high)* [[288](../source/src-brown-2018-libratus.md)]
- DeepStack beat professional players with statistical significance over 44,000 hands of heads-up no-limit hold'em using recursive re-solving with a learned value function. *(confidence: high)* [[289](../source/src-moravcik-2017-deepstack.md)]
- Pluribus beat elite professionals at six-player no-limit hold'em, winning about 5 big blinds per 100 hands over 10,000 hands; its blueprint took 8 days of Monte Carlo CFR on a 64-core server (under $150 of cloud compute) and it played on two CPUs at about 20 seconds per hand. *(confidence: high)* [[290](../source/src-brown-2019-pluribus.md), [291](../source/src-facebook-2019-pluribus-blog.md)]
- ReBeL combined self-play RL with search, provably converging to a Nash equilibrium in two-player zero-sum games, and reached superhuman heads-up no-limit hold'em with less domain knowledge. *(confidence: high)* [[292](../source/src-brown-2020-rebel.md)]
- DeepNash reached a top-3 all-time ranking among expert humans on the Gravon Stratego platform using model-free Regularised Nash Dynamics and no search (Science, December 2022). *(confidence: high)* [[293](../source/src-perolat-2022-deepnash.md)]
- Student of Games (Science Advances, November 2023) used one sound algorithm across chess, Go, heads-up no-limit poker, and Scotland Yard, beating the strongest openly available poker agent and the prior best Scotland Yard agent. *(confidence: high)* [[294](../source/src-schmid-2023-student-of-games.md)]

## Sources

- [Superhuman AI for heads-up no-limit poker: Libratus beats top professionals](../source/src-brown-2018-libratus.md)
- [DeepStack: Expert-level artificial intelligence in heads-up no-limit poker](../source/src-moravcik-2017-deepstack.md)
- [Superhuman AI for multiplayer poker](../source/src-brown-2019-pluribus.md)
- [Pluribus: First AI to beat pros in 6-player poker](../source/src-facebook-2019-pluribus-blog.md)
- [Combining Deep Reinforcement Learning and Search for Imperfect-Information Games](../source/src-brown-2020-rebel.md)
- [Mastering the game of Stratego with model-free multiagent reinforcement learning](../source/src-perolat-2022-deepnash.md)
- [Student of Games: A unified learning algorithm for both perfect and imperfect information games](../source/src-schmid-2023-student-of-games.md)

---
Provenance: created in run `2026-10-24-techniques-rl-design`; reviewed in `2026-10-24-technique-links`.
