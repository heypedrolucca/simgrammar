# Language models grounded in strategic planning for negotiation games

*Technique* · `cicero-strategic-dialogue` · status: **sourced**

Meta's Cicero couples a dialogue language model with a planning engine that infers other players' intentions from the board and conversation, so its free-text negotiation proposes and follows concrete joint plans, reaching human-level Diplomacy.

| field | value |
|---|---|
| aliases | Cicero, CICERO, piKL, Richelieu |
| category | Game-theoretic solvers |
| year | 2022 |
| maturity | Research |
| trl | 5 |
| runtime | Server real-time |
| determinism impact | Breaks |
| horizon | 1-2 years |
| risks | Consistency / hallucination, Controllability, Content safety, Compute cost, Player trust / reception |
| builds on | [Regret minimization and search for imperfect-information games](../technique/imperfect-information-solvers.md) |
| affects count *(computed)* | 5 |

## Summary

Meta's Cicero couples a dialogue language model with a planning engine that infers other players' intentions from the board and conversation, so its free-text negotiation proposes and follows concrete joint plans, reaching human-level Diplomacy.

## Mechanism

Each phase, a planning module predicts every player's likely actions from the board state and the dialogue so far. It starts from a policy model trained on human games and refines it with piKL, a regret-minimization search regularized by a KL penalty toward the human-like policy, so predictions stay plausible while improving expected value. The resulting plan fixes intents: the actions Cicero intends to take and the actions it proposes to each recipient. A dialogue language model, trained on human game messages and conditioned on the board, the message history, and these intents, generates candidate messages, which are filtered for consistency with the plan and the game state. Incoming messages update the predicted intents of others, which changes the plan and therefore what Cicero says next. The planner also models what others expect Cicero to do. Because messages are generated from intents rather than freely, what Cicero says tracks what it plans to do.

## Limitations

- Built for one game: the dialogue model and the move policy were trained on human Diplomacy games and messages, so another game needs comparable data or a substitute.
- Released weights are licensed for non-commercial use only (CC-BY-NC 4.0), and the repository is archived, so a studio cannot ship the released model.
- Training assumed a GPU cluster (example 256 GPUs) and inference loads large models per agent, which is costly for a game with several AI factions per player.
- Evaluation used an anonymous league; how players negotiate and whether they trust an opponent they know is an AI was not measured.

## Relations

**affects**

- [Faction diplomacy](../mechanic/faction-diplomacy.md) (Enables new form): Diplomacy becomes free-text negotiation with AI factions that propose specific joint moves, commit to them, and change plans when persuaded, instead of accept or decline treaty menus driven by opinion scores.
- [Natural-language interaction](../mechanic/natural-language-interaction.md) (Deepens): Typed messages are translated into predicted intents that feed a planner, so what the player says changes what the AI does on the map, and the AI's replies are constrained to match its own plan.
- [Reputation](../mechanic/reputation.md) (Deepens): An AI that models what others expect it to do can also track whether the player's stated intentions matched their moves, turning standing into a learned estimate of trustworthiness rather than a scalar moved by scripted events.
- [Negotiation](../mechanic/negotiation.md) (Enables new form): Planner-grounded dialogue lets AI counterparties propose, counter, and keep terms in free text instead of accepting or rejecting fixed offers.
- [War score and peace terms](../mechanic/war-score-peace.md) (Deepens): Peace terms could be negotiated in language against the war score, with the planner checking what the opponent will actually accept.

**builds on**

- [Regret minimization and search for imperfect-information games](../technique/imperfect-information-solvers.md)

## Backlinks (computed)

**applied in:** [Agent ambassadors between player worlds](../opportunity/agent-ambassadors-async.md), [Natural-language legislation](../opportunity/natural-language-legislation.md), [Negotiating faction AI](../opportunity/negotiating-faction-ai.md)

## Claims

- Cicero averaged more than double the human score over 40 games in an anonymous online Diplomacy league and ranked in the top 10% of participants who played more than one game (Science, November 2022). *(confidence: high)* [[155](../source/src-fair-2022-cicero.md), [156](../source/src-meta-2022-cicero-project.md)]
- Cicero pairs a controllable dialogue model with a planning engine that models other players' likely moves from the board and the conversation and predicts what others think Cicero will do. *(confidence: high)* [[156](../source/src-meta-2022-cicero-project.md), [155](../source/src-fair-2022-cicero.md)]
- The released code is MIT-licensed but model weights are CC-BY-NC 4.0, training scripts target a Slurm cluster (example configuration 256 GPUs), and the repository was archived read-only on 2025-04-17. *(confidence: high)* [[157](../source/src-facebookresearch-2022-diplomacy-cicero.md)]
- Richelieu (2024) built an LLM Diplomacy agent combining planning with memory and reflection, goal-directed negotiation, and self-play memory augmentation without human game data. *(confidence: medium)* [[158](../source/src-guan-2024-richelieu.md)]

## Sources

- [Human-level play in the game of Diplomacy by combining language models with strategic reasoning](../source/src-fair-2022-cicero.md)
- [CICERO](../source/src-meta-2022-cicero-project.md)
- [diplomacy_cicero](../source/src-facebookresearch-2022-diplomacy-cicero.md)
- [Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy](../source/src-guan-2024-richelieu.md)

---
Provenance: created in run `2026-10-24-techniques-rl-design`; reviewed in `2026-10-24-technique-links`.
