# Many-agent LLM societies

*Technique* · `llm-agent-societies` · status: **sourced**

Simulations of hundreds to a million LLM-driven agents with concurrent cognitive modules, shared environments, and message buses that produce role specialization, rule changes, cultural spread, and polarization.

| field | value |
|---|---|
| aliases | Project Sid, PIANO, AgentSociety, Concordia, OASIS, generative agent-based modeling |
| category | Multi-agent social simulation |
| year | 2024 |
| maturity | Research |
| trl | 4 |
| runtime | Server real-time |
| determinism impact | Breaks |
| horizon | 3-5 years |
| risks | Compute cost, Consistency / hallucination, Controllability, Evaluation difficulty, Legibility |
| builds on | [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md) |
| deployed in | [Project Sid](../game/project-sid.md) |
| affects count *(computed)* | 8 |

## Summary

Simulations of hundreds to a million LLM-driven agents with concurrent cognitive modules, shared environments, and message buses that produce role specialization, rule changes, cultural spread, and polarization.

## Mechanism

Scaling generative agents from tens to thousands needs architecture and infrastructure changes. Project Sid's PIANO runs about ten modules concurrently (memory, action awareness, goal generation, social awareness, talking, skill execution) that read and write a shared agent state; fast modules use small non-LLM models and slow ones call an LLM, and a cognitive controller acts as a bottleneck that broadcasts one high-level decision so speech and actions stay consistent. AgentSociety gives each agent a profile plus emotion, needs, and cognition layers and simulates mobility, social contact, employment, and consumption across linked urban, social, and economic spaces, distributing agents over Ray processes and routing messages over MQTT. Concordia has agents state intended actions in natural language and a Game Master agent decide outcomes. OASIS runs up to one million agents inside a recommender-driven social feed.

## Limitations

- Scale ceilings come from the host game as well as the model: Project Sid agents became unresponsive above 1,000 agents on a Minecraft server.
- PIANO agents lack vision and spatial reasoning and have no innate drives such as survival or curiosity, so building and navigation are weak.
- Agents built on pretrained models reproduce known human institutions (taxes, votes, religion) rather than inventing new ones, so outcomes are bounded by training data.
- Per-agent LLM calls multiply with population; AgentSociety chose an API without request limits to avoid rate-limit artifacts, and none of these papers reports per-agent-hour cost in a form a game could budget against.
- Validation is qualitative (matching stylized findings), so designers cannot easily tune or test collective outcomes.

## Relations

**affects**

- [Elections](../mechanic/elections.md) (Replaces substrate): Voters become LLM agents that hear persuasion from other agents and vote on amendments, as in Project Sid's constitutional votes, instead of computing a vote from satisfaction and bloc membership.
- [Gossip propagation](../mechanic/gossip-propagation.md) (Deepens): Memes, beliefs, and a seeded religion spread through populations of 500 to one million agents, with content mutating in conversation and spread shaped by social structure or a recommender feed.
- [Labor market](../mechanic/labor-market.md) (Enables new form): Roles emerge from agents' social context and goals (farmers, miners, guards in 30-agent villages) rather than from job slots filled by education level; AgentSociety adds agent-level employment and consumption decisions.
- [Player legislation](../mechanic/player-legislation.md) (Enables new form): NPC populations can propose, debate, and vote on rule changes in natural language and then comply or not, so legislation is no longer limited to human players in a shared world.
- [Policy influence network](../mechanic/policy-influence-network.md) (Replaces substrate): A policy's effect on groups is measured by running it on a population of agents (AgentSociety's universal basic income and hurricane experiments) instead of reading hand-authored weighted edges from policies to voter groups.
- [Taxation](../mechanic/taxation.md) (Deepens): Tax compliance becomes an agent decision that responds to law changes and influencer messaging, as in Project Sid's 20% tax experiment, rather than an automatic deduction at the set rate.
- [Persistent shared world](../mechanic/persistent-world.md) (Deepens): A shared world can be populated by hundreds of autonomous agents that keep roles, culture, and rules while human players come and go; PIANO was built for real-time interaction with humans and other agents.
- [Off-screen life progression](../mechanic/offscreen-life-progression.md) (Replaces substrate): Unplayed households can be advanced by cheap language-agent societies that generate plausible life events instead of fixed event tables.

**builds on**

- [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md)

**deployed in**

- [Project Sid](../game/project-sid.md)

## Backlinks (computed)

**applied in:** [Agent ambassadors between player worlds](../opportunity/agent-ambassadors-async.md), [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md), [Language-agent society terrarium](../opportunity/llm-society-terrarium.md), [Natural-language legislation](../opportunity/natural-language-legislation.md), [Participatory planning sandboxes](../opportunity/participatory-planning-sandboxes.md)

## Claims

- In Minecraft, PIANO agents in 30-agent villages specialized into persistent roles (farmer, miner, guard, blacksmith) only when the social module was present; agents largely obeyed a 20% tax law and changed compliance after voted constitutional amendments, with pro- and anti-tax influencer agents shifting outcomes; a religion seeded by 20 priests kept spreading through a 500-agent population for two hours. *(confidence: high)* [[32](../source/src-altera-2024-project-sid.md)]
- Project Sid runs above 1,000 agents exceeded Minecraft server limits and agents became sporadically unresponsive, so the main cultural analysis used 500 agents. *(confidence: high)* [[32](../source/src-altera-2024-project-sid.md)]
- AgentSociety simulated over 10,000 agents with about 5 million interactions and reproduced qualitative findings on polarization, inflammatory message spread, universal basic income, and a hurricane shock. *(confidence: medium)* [[206](../source/src-piao-2025-agentsociety.md)]
- OASIS ran up to one million agents on X- and Reddit-like platforms, replicated information spreading, group polarization, and herd effects, and found stronger group dynamics at larger agent counts. *(confidence: medium)* [[207](../source/src-yang-2024-oasis.md)]
- Concordia formalizes a Game Master entity that grounds natural-language actions in physical, social, or digital space; its 2025 design pattern builds the Game Master from the same components as other entities so designers can configure scenarios without engine code. *(confidence: high)* [[176](../source/src-vezhnevets-2023-concordia.md), [177](../source/src-vezhnevets-2025-multi-actor-game-engine.md)]

## Sources

- [Project Sid: Many-agent simulations toward AI civilization](../source/src-altera-2024-project-sid.md)
- [AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society](../source/src-piao-2025-agentsociety.md)
- [OASIS: Open Agent Social Interaction Simulations with One Million Agents](../source/src-yang-2024-oasis.md)
- [Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia](../source/src-vezhnevets-2023-concordia.md)
- [Multi-Actor Generative Artificial Intelligence as a Game Engine](../source/src-vezhnevets-2025-multi-actor-game-engine.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`; reviewed in `2026-10-24-technique-links`.
