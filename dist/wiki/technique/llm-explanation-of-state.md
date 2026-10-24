# LLM explanation of simulation state

*Technique* · `llm-explanation-of-state` · status: **sourced**

Language models that read simulation state, modifier breakdowns, agent traces, or event logs and answer why and what-if questions or summarize what happened for players and designers.

| field | value |
|---|---|
| aliases | AI advisor chat, natural-language explanations of agent behavior, LLM commentator, log summarization |
| category | LLM narrative & dialogue |
| year | 2023 |
| maturity | Prototype |
| trl | 5 |
| runtime | Client real-time, Server real-time, Analytics / live-ops |
| determinism impact | Preserves |
| horizon | 1-2 years |
| risks | Consistency / hallucination, Evaluation difficulty, Latency, Player trust / reception |
| builds on |  |
| deployed in |  |
| affects count *(computed)* | 5 |

## Summary

Language models that read simulation state, modifier breakdowns, agent traces, or event logs and answer why and what-if questions or summarize what happened for players and designers.

## Mechanism

The game serializes the relevant slice of state (indicator values and their contributing modifiers, an agent's thought log and action trace, recent events) into the prompt, or exposes it through retrieval or tool calls over game data and documentation, and the model answers a player question or writes a summary. Zhang et al. first learn a compact representation of an agent's behavior from observed states and actions, then have the LLM explain from that representation, which limits hallucination and supports follow-up and what-if questions. For designers, a model can segment play logs into strategies and merge them into a graph to compare with the intended path. The explanation layer reads state and does not write it, so the simulation stays deterministic.

## Limitations

- Wrong but fluent causes: models are unreliable at inferring dynamics, so explanations are only trustworthy when causes are passed in from the simulation.
- Serializing large state (thousands of modifiers, long logs) into context is slow and costly; selection of what to include determines what can be explained.
- Hard to QA: the answer space is open-ended, and a confident wrong explanation damages trust more than no explanation.
- Shipped evidence is thin: known game examples are tech demos or research previews.

## Sources

- src-zhang-2023-explaining-agent-behavior
- src-nvidia-2026-ace-developer-page
- src-deepmind-2025-sima-2-blog
- src-peng-2024-player-driven-emergence
- src-wang-2024-text-world-simulators
- src-gallotta-2024-llms-games-survey

## Relations

**affects**

- [Advisors](../mechanic/advisors.md) (Deepens): Advisors can answer arbitrary player questions about the current situation and recommend actions in context, instead of speaking a fixed catalog of threshold-triggered messages.
- [Agent inspection](../mechanic/agent-inspection.md) (Explains): The inspection panel can answer why an agent did something by summarizing its needs, itemized mood terms, and recent thought log into a short causal account.
- [Causal breakdown tooltips](../mechanic/causal-tooltips.md) (Explains): A long nested modifier chain can be condensed into a ranked plain-language list of the largest causes and what would change them, while the numbers still come from the simulation.
- [Stats dashboards](../mechanic/stats-dashboards.md) (Explains): Graph changes can be annotated with narrated causes drawn from the event log, such as which policy or disaster preceded a drop.
- [History chronicle](../mechanic/history-chronicle.md) (Deepens): Recorded events can be retold as biographies, recaps, or highlight summaries for the player, a commentator and reteller role.

## Backlinks (computed)

**applied in:** [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Why-query over the simulation log](../opportunity/causal-why-query.md), [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md), [Explained delegation to AI managers](../opportunity/explained-delegation.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md), [Intent-level orders](../opportunity/intent-level-orders.md), [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

## Claims

- Explanations generated from a learned behavior representation plus an LLM were rated about as helpful as a human domain expert's, with little hallucination, and supported clarification and counterfactual follow-ups. *(confidence: medium)* [[170](../source/src-zhang-2023-explaining-agent-behavior.md)]
- NVIDIA lists a Total War: PHARAOH AI advisor that helps players learn the game's systems using a small on-device model connected to game data; no public release date was found. *(confidence: medium)* [[137](../source/src-nvidia-2026-ace-developer-page.md)]
- SIMA 2 explains its intended steps and answers questions about its behavior and environment in commercial 3D games. *(confidence: high)* [[109](../source/src-deepmind-2025-sima-2-blog.md)]
- GPT-4 converted 28 players' logs into narrative graphs, letting designers count 53 player-created narrative nodes that their design did not include. *(confidence: high)* [[171](../source/src-peng-2024-player-driven-emergence.md)]
- GPT-4 predicted whole text-game state transitions correctly at most 59.9% of the time and environment-driven changes at most 49.7%, so explanations of dynamics must be computed by the simulation and narrated, not inferred by the model. *(confidence: high)* [[172](../source/src-wang-2024-text-world-simulators.md)]
- A 2024 survey found research on LLM commentators and retellers of game events rather limited. *(confidence: medium)* [[135](../source/src-gallotta-2024-llms-games-survey.md)]

## Sources

- [Explaining Agent Behavior with Large Language Models](../source/src-zhang-2023-explaining-agent-behavior.md)
- [NVIDIA ACE for Games](../source/src-nvidia-2026-ace-developer-page.md)
- [SIMA 2: An Agent that Plays, Reasons, and Learns With You in Virtual 3D Worlds](../source/src-deepmind-2025-sima-2-blog.md)
- [Player-Driven Emergence in LLM-Driven Game Narrative](../source/src-peng-2024-player-driven-emergence.md)
- [Can Language Models Serve as Text-Based World Simulators?](../source/src-wang-2024-text-world-simulators.md)
- [Large Language Models and Games: A Survey and Roadmap](../source/src-gallotta-2024-llms-games-survey.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`.
