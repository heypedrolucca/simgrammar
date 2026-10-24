# Project Sid

*Game* · `project-sid` · status: **sourced**

An Altera research demonstration that runs 10 to 1,000-plus language-model agents with the concurrent PIANO architecture in Minecraft to study role specialization, collective rule-making, and cultural transmission.

| field | value |
|---|---|
| year | 2024 |
| developer | Altera |
| platforms | PC |
| subgenre | AI-native |
| subgenre secondary | Social sim, Political sim |
| sim domain | Social / interpersonal, Political / governance |
| player role | Observer / gardener |
| agency model | Indirect incentive |
| time model | Real-time |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | Generative |
| multiplayer | Single-player |
| modding | None |
| production tier | Academic / research |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 2 |
| influenced by | [Generative Agents (Smallville)](../game/generative-agents-smallville.md) |
| cluster *(computed)* | C08 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

An Altera research demonstration that runs 10 to 1,000-plus language-model agents with the concurrent PIANO architecture in Minecraft to study role specialization, collective rule-making, and cultural transmission.

## Core Loop

seed agents with personas and community goals -> concurrent modules perceive, remember, talk, and act in Minecraft -> cognitive controller commits a coherent decision -> roles specialize and rules are paid, debated, and amended -> beliefs and memes spread between towns

## Design Notes

PIANO runs about ten modules concurrently at different speeds (memory, action awareness, goal generation, social awareness, talking, skill execution), with fast non-language reflex networks and a cognitive controller that acts as a bottleneck and broadcasts one decision so speech and action stay consistent; GPT-4o was the strongest base model. In 30-agent runs agents settled into persistent roles (farmer, miner, engineer, guard, explorer, blacksmith) that collapsed without the social module. In a 29-agent constitution experiment with a 20 percent tax paid into community chests every 120 seconds, pro- and anti-tax influencers shifted votes, amendments passed, and payments followed the new rate. In a 500-agent run, Pastafarianism seeded by 20 priests spread to other towns; 1,000-agent attempts exceeded the Minecraft server's capacity. The preprint states no public code release.

## Relations

**influenced by**

- [Generative Agents (Smallville)](../game/generative-agents-smallville.md)

**uses**

- [Elections](../mechanic/elections.md) (core): Constituents give feedback on a constitution, amendments are generated, agents vote, and the amended constitution is distributed on a fixed schedule (feedback at 300 s, vote at 420 s, distribution at 600 s).
- [Taxation](../mechanic/taxation.md) (core): Agents deposit a share of inventory into community chests every 120 seconds at the constitutional rate, starting at 20 percent; when amendments cut it to 5-10 percent, payments fell to about 9 percent.
- [Gossip propagation](../mechanic/gossip-propagation.md) (core): Memes and a religion (Pastafarianism, seeded by 20 priests in one town) spread through agent conversations and travel; conversion was tracked by keyword use and had not saturated after two hours.
- [Memories and thoughts](../mechanic/memories-thoughts.md) (supporting): A memory module stores conversations, actions, and observations across short and long timescales.
- [Relationship values](../mechanic/relationship-values.md) (supporting): A social-awareness module infers other agents' sentiment, and the paper compares perceived with true likeability.
- [Hand crafting](../mechanic/hand-crafting.md) (supporting): Agents gather and craft Minecraft items; a 49-agent group plateaued at about 320 unique items over four hours.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting)
- [Generative content on demand](../mechanic/generative-content.md) (supporting): Goal generation, talking, and the cognitive controller run on language-model calls, with GPT-4o as the base model in the strongest configuration.

## Backlinks (computed)

**deploys:** [Many-agent LLM societies](../technique/llm-agent-societies.md)

**precedent for:** [Language-agent society terrarium](../opportunity/llm-society-terrarium.md)

## Claims

- Experiments ranged from 10 to 500 agents in reported results; runs above 1,000 agents were attempted but exceeded the Minecraft server's capacity. *(confidence: high)* [[32](../source/src-altera-2024-project-sid.md)]

## Sources

- [Project Sid: Many-agent simulations toward AI civilization](../source/src-altera-2024-project-sid.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
