# Monte Carlo tree search for game AI

*Technique* · `monte-carlo-tree-search` · status: **sourced**

A best-first search that grows a game tree from repeated simulated playouts and picks branches with a bandit rule such as UCT, letting AI players plan from a forward model without a hand-tuned evaluation function.

| field | value |
|---|---|
| aliases | MCTS, UCT, information-set MCTS |
| category | Game-theoretic solvers |
| year | 2006 |
| maturity | Shipped (niche) |
| trl | 7 |
| runtime | Client real-time |
| determinism impact | Mitigable |
| horizon | Now |
| risks | Latency, Controllability, Legibility |
| affects count *(computed)* | 5 |

## Summary

A best-first search that grows a game tree from repeated simulated playouts and picks branches with a bandit rule such as UCT, letting AI players plan from a forward model without a hand-tuned evaluation function.

## Mechanism

Each iteration has four steps. Selection descends from the root by a tree policy; UCT picks the child that maximizes mean reward plus c*sqrt(ln N / n), trading exploitation against exploration. Expansion adds an untried child. Simulation plays forward from that node with a cheap default policy (random or heuristic) to a terminal state or depth limit. Backpropagation adds the outcome to the visit count and value of every node on the path. The search is anytime: it stops after an iteration count or time budget and returns the most-visited action. It needs only a forward model that can copy a state, list legal actions, and apply them, so it works for rule sets without a known evaluation function. Variants add chance nodes, determinization or information-set trees for hidden information, simultaneous moves, and macro-actions that search over plans instead of single moves.

## Limitations

- Needs a fast, copyable forward model; a full simulation state with thousands of agents is expensive to clone and step, so practical use usually requires an abstracted model or macro-actions.
- Random playouts estimate value poorly in long-horizon systems with delayed consequences such as economies and colony survival unless a heuristic rollout policy or evaluation function is supplied.
- Time-budgeted search returns different moves on different hardware, which breaks replays and lockstep multiplayer unless budgets are counted in iterations with seeded randomness.
- Determinized search over hidden information averages over sampled worlds and can make choices that are only good if it could see the hidden state (strategy fusion).

## Relations

**affects**

- [Utility action selection](../mechanic/utility-action-selection.md) (Replaces substrate): Agents choose actions by sampling futures from the game's forward model and backing up outcomes, instead of scoring one-step options with hand-tuned utility curves, so choices account for consequences several actions ahead at a per-decision compute cost.
- [Military operations](../mechanic/military-operations.md) (Deepens): Tactical AI plans multi-unit action sequences within a time budget, as in Fable Legends' real-time tactical planning, rather than following scripted doctrine; the iteration budget becomes a difficulty lever.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (Deepens): AI factions can weigh war, peace, and alliance options by simulating future turns of the campaign, the kind of high-level campaign decision Total War: Rome II gave to MCTS, so choices respond to the actual strategic position instead of fixed opinion thresholds.
- [Rival firms](../mechanic/rival-firms.md) (Deepens): AI competitors can pick prices, expansions, and acquisitions by rolling the economic model forward, so rival play adapts to the player's position and to rule changes without bespoke heuristics per market rule.
- [Delegation to AI managers](../mechanic/delegation-to-ai.md) (Deepens): Governors or managers given a subsystem can search over action sequences toward the player-set goal with the same forward model, staying competent in rule configurations designers did not script for.

## Backlinks (computed)

**built upon by:** [Automated generation of game rules and mechanics](../technique/automated-rule-generation.md), [Self-play planning with learned models (AlphaZero, MuZero, Dreamer)](../technique/model-based-planning-muzero.md)

## Claims

- Kocsis and Szepesvari introduced UCT, applying the UCB1 bandit rule to node selection in Monte Carlo planning (ECML 2006); Coulom coined the name Monte Carlo tree search the same year. *(confidence: high)* [[225](../source/src-kocsis-2006-uct.md), [226](../source/src-wikipedia-monte-carlo-tree-search.md)]
- A 2012 survey in IEEE TCIAIG catalogued MCTS variants, enhancements, and applications in board, card, and video games after its first six years. *(confidence: medium)* [[227](../source/src-browne-2012-mcts-survey.md)]
- Total War: Rome II used MCTS in its high-level campaign AI, and Fable Legends used real-time MCTS for tactical planning (2015 talk). *(confidence: medium)* [[226](../source/src-wikipedia-monte-carlo-tree-search.md)]

## Sources

- [Bandit Based Monte-Carlo Planning](../source/src-kocsis-2006-uct.md)
- [A Survey of Monte Carlo Tree Search Methods](../source/src-browne-2012-mcts-survey.md)
- [Monte Carlo tree search](../source/src-wikipedia-monte-carlo-tree-search.md)

---
Provenance: created in run `2026-10-24-techniques-rl-design`.
