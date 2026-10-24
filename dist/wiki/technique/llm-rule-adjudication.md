# LLM-adjudicated state transitions (LLM as game mechanic)

*Technique* · `llm-rule-adjudication` · status: **sourced**

A language model computes the outcome of an interaction (two elements combined, an action on an object) from a text description of the inputs, with results cached so every player sees the same rule.

| field | value |
|---|---|
| aliases | LLM as rules engine, open-ended combination, text world simulator, memoized generation |
| category | Generative world model |
| year | 2024 |
| maturity | Shipped (niche) |
| trl | 7 |
| runtime | Server real-time |
| determinism impact | Mitigable |
| horizon | Now |
| risks | Consistency / hallucination, Legibility, Content safety, Compute cost |
| builds on |  |
| deployed in | [Infinite Craft](../game/infinite-craft.md) |
| affects count *(computed)* | 5 |

## Summary

A language model computes the outcome of an interaction (two elements combined, an action on an object) from a text description of the inputs, with results cached so every player sees the same rule.

## Mechanism

The game describes the inputs (two items, or an object state plus an action) as text and asks the model for the result, constrained to a short name, an icon, or a small state diff. Infinite Craft first looks the pair up in a database; only a never-tried pair goes to the model (Llama 2, later Llama 3.1), and the answer is stored, so the rule becomes fixed and shared by all players after the first query and the first finder is credited. The cache turns a stochastic model into a growing deterministic rule table and bounds cost to unique queries. Benchmarks of LLMs as text world simulators measure how often the predicted next state matches the true one.

## Limitations

- Accuracy: as a general state simulator GPT-4 is right on whole-state transitions at most 59.9% of the time, so errors compound over multi-step dynamics.
- Legibility: generated rules follow word association rather than a learnable system, so players cannot predict outcomes from principles.
- Cost and load scale with unique queries; Infinite Craft's traffic overloaded its servers.
- Outputs must be filtered for offensive results because every cached answer becomes permanent shared content.

## Relations

**affects**

- [Hand crafting](../mechanic/hand-crafting.md) (Enables new form): The recipe space becomes unbounded: any pair of items yields a generated result rather than a lookup in a finite designer table, and the first answer is cached as the permanent recipe.
- [Material interactions](../mechanic/material-interactions.md) (Enables new form): Interactions between arbitrary materials or elements can be resolved by a model rather than an authored pair table, but whole-state accuracy near 60% means results must be bounded to simple outputs and cached.
- [Generative content on demand](../mechanic/generative-content.md) (Deepens): Generated results are written back as shared, persistent rules rather than one-off text, so the world's content grows with play and stays consistent across players.
- [Collection goals](../mechanic/collection-goals.md) (Enables new form): Collections become open-ended races to discover never-generated items, with a First Discovery credit for the first player to create each one.
- [Combination discovery](../mechanic/combination-discovery.md) (Enables new form): A language model decides the result of each new combination and caches it, turning a finite authored recipe graph into an open one (Infinite Craft).

**deployed in**

- [Infinite Craft](../game/infinite-craft.md)

## Claims

- Infinite Craft (January 2024) starts from water, fire, wind, and earth and generates a new element and emoji with Llama 2 and Llama 3.1 for any untried pair, storing the result so each pair gives every player the same answer; traffic reached hundreds of millions of recipes a day. *(confidence: high)* [[67](../source/src-wikipedia-infinite-craft.md)]
- On 76,369 transitions from 31 text games, GPT-4 predicted the full next state correctly at most 59.9% of the time, up to 77.1% for action-driven and at most 49.7% for environment-driven changes; humans scored about 80% on a subset where GPT-4 scored about 50%. *(confidence: high)* [[172](../source/src-wang-2024-text-world-simulators.md)]
- Concordia's Game Master uses a language model to decide whether stated actions are physically plausible and what their effects are. *(confidence: high)* [[176](../source/src-vezhnevets-2023-concordia.md)]

## Sources

- [Infinite Craft](../source/src-wikipedia-infinite-craft.md)
- [Can Language Models Serve as Text-Based World Simulators?](../source/src-wang-2024-text-world-simulators.md)
- [Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia](../source/src-vezhnevets-2023-concordia.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`; reviewed in `2026-10-24-technique-links`.
