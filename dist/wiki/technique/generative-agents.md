# Generative agents (memory stream, reflection, planning)

*Technique* · `generative-agents` · status: **sourced**

LLM-driven characters that store observations in a natural-language memory stream, retrieve them by recency, importance, and relevance, synthesize reflections, and plan their day top-down.

| field | value |
|---|---|
| aliases | generative agent architecture, Smallville agents, plan-act-reflect agents |
| category | LLM agents |
| year | 2023 |
| maturity | Shipped (niche) |
| trl | 7 |
| runtime | Server real-time, Client real-time |
| determinism impact | Breaks |
| horizon | Now |
| risks | Determinism, Compute cost, Consistency / hallucination, Latency, Controllability, Evaluation difficulty |
| builds on |  |
| deployed in | [Generative Agents (Smallville)](../game/generative-agents-smallville.md), [inZOI](../game/inzoi.md) |
| affects count *(computed)* | 9 |

## Summary

LLM-driven characters that store observations in a natural-language memory stream, retrieve them by recency, importance, and relevance, synthesize reflections, and plan their day top-down.

## Mechanism

Each agent appends observations as natural-language records to a memory stream. To act or speak, it retrieves records by a score that sums min-max normalized recency (exponential decay, factor 0.995 per game hour), importance (an LLM rating from 1 to 10 made when the record is stored), and relevance (embedding cosine similarity to the current situation), all with weight 1. When the summed importance of recent records exceeds 150, roughly two or three times a game day, the agent asks the LLM for high-level questions and inferences and stores the answers as reflections that can be retrieved like observations. Planning is top-down: a daily sketch is decomposed into hour chunks and then 5-15 minute actions, and the plan is revised when a perceived event warrants a reaction. Dialogue is generated from retrieved memories about the other agent. Cost-reduction variants replay stored plan-action sequences when a new plan matches an old one by embedding similarity and compress social context into short summaries, cutting LLM calls.

## Limitations

- Cost and wall-clock time: 25 agents over two game days cost thousands of dollars and took days to run on gpt-3.5-turbo (2023 prices).
- Retrieval failures and embellishment: agents sometimes miss relevant memories or add fabricated details to recalled events.
- Instruction-tuned models make agents overly formal and cooperative, and agents misread location norms such as single-occupancy bathrooms or closing hours.
- Each agent step is several sequential LLM calls (importance rating, retrieval-conditioned action, dialogue, reflection), so per-agent latency is seconds, which limits real-time populations unless calls are cached or batched.
- Behavior is not reproducible from a seed with hosted models; replays and saves must store generated outputs.

## Sources

- src-park-2023-generative-agents
- src-yu-2024-affordable-generative-agents
- src-gallotta-2024-llms-games-survey
- src-nvidia-2026-ace-developer-page
- src-steam-2025-inzoi

## Relations

**affects**

- [Memories and thoughts](../mechanic/memories-thoughts.md) (Enables new form): Memories become free-text records with LLM-rated importance, retrieved by recency, importance, and relevance, plus reflections that summarize many records into beliefs, instead of a fixed catalog of timed mood modifiers.
- [Daily schedules](../mechanic/daily-schedules.md) (Replaces substrate): Each agent writes its own day plan from its description and memories, decomposed into hour and 5-15 minute steps and revised on events, in place of authored routine tables; the player still sees rhythms of work, meals, and leisure.
- [Utility action selection](../mechanic/utility-action-selection.md) (Replaces substrate): The next action is chosen by prompting with the current plan step, perceived surroundings, and retrieved memories rather than by scoring options against need curves, so choices can reference past events and other agents.
- [Gossip propagation](../mechanic/gossip-propagation.md) (Deepens): Information moves through generated conversations whose content comes from memory retrieval, so what spreads, to whom, and how it is reworded emerge from dialogue; in Smallville party awareness rose from 4% to 52% of agents with 1.3% hallucinated answers.
- [Relationship values](../mechanic/relationship-values.md) (Replaces substrate): Relationships are held as remembered interactions and reflections about another agent rather than a numeric affinity, so a relationship's state is a set of retrievable facts; Smallville's acquaintance network density rose from 0.167 to 0.74 in two days.
- [Social exchanges](../mechanic/social-exchanges.md) (Enables new form): Agents open-endedly converse, invite, and coordinate (for example planning and attending a party) without a predefined catalog of social moves and preconditions.
- [Agent inspection](../mechanic/agent-inspection.md) (Explains): Because an agent's state is natural-language memories, plans, and reflections, the player or designer can read them directly or interview the agent about why it acted, which is how the original paper evaluated believability.
- [Off-screen life progression](../mechanic/offscreen-life-progression.md) (Deepens): Memory streams summarized at low frequency give off-screen characters histories that persist when the player returns.
- [Aspirations and wants](../mechanic/aspiration-wants.md) (Enables new form): Wants generated from an agent's own memories and reflections rather than rolled from a fixed table tied to an aspiration.

**deployed in**

- [Generative Agents (Smallville)](../game/generative-agents-smallville.md)
- [inZOI](../game/inzoi.md)

## Backlinks (computed)

**applied in:** [Factories with a living workforce](../opportunity/living-workforce-factories.md), [Language-agent society terrarium](../opportunity/llm-society-terrarium.md), [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md)

**built upon by:** [LLM models of individual human choice](../technique/human-behavior-simulation-models.md), [Many-agent LLM societies](../technique/llm-agent-societies.md)

## Claims

- In Smallville, 25 agents on gpt-3.5-turbo were rated for believability by 100 human raters (TrueSkill): full architecture 29.89, no reflection 26.88, no reflection or planning 25.64, human crowdworkers role-playing 22.95, no memory, planning, or reflection 21.21. *(confidence: high)* [[21](../source/src-park-2023-generative-agents.md)]
- Over two game days, knowledge of a seeded party spread from 1 to 13 of 25 agents and of a mayoral candidacy from 1 to 8, network density rose from 0.167 to 0.74, five of twelve invited agents attended the party, and 1.3% of 453 awareness answers were hallucinated. *(confidence: high)* [[21](../source/src-park-2023-generative-agents.md)]
- The simulation cost thousands of dollars in token credits and took multiple days of wall-clock time for 25 agents. *(confidence: high)* [[21](../source/src-park-2023-generative-agents.md), [135](../source/src-gallotta-2024-llms-games-survey.md)]
- Affordable Generative Agents used 31.1% of the baseline's tokens for a 3-agent town over two game days and 42.7% for the 25-agent town, by replaying cached plan-action policies (embedding match at cosine 0.97) and compressing about 2,000 prompt tokens of social context to about 100. *(confidence: high)* [[136](../source/src-yu-2024-affordable-generative-agents.md)]
- NVIDIA describes inZOI's Smart Zois as agents that plan, act, and reflect on their decisions using small language models, and inZOI's Steam disclosure says character actions and thoughts can be influenced through an on-device SLM. *(confidence: medium)* [[137](../source/src-nvidia-2026-ace-developer-page.md), [138](../source/src-steam-2025-inzoi.md)]

## Sources

- [Generative Agents: Interactive Simulacra of Human Behavior](../source/src-park-2023-generative-agents.md)
- [Affordable Generative Agents](../source/src-yu-2024-affordable-generative-agents.md)
- [Large Language Models and Games: A Survey and Roadmap](../source/src-gallotta-2024-llms-games-survey.md)
- [NVIDIA ACE for Games](../source/src-nvidia-2026-ace-developer-page.md)
- [inZOI on Steam](../source/src-steam-2025-inzoi.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`; reviewed in `2026-10-24-technique-links`, `2026-10-24-review-fixes`.
