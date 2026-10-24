# Generalist instructable game agents (SIMA)

*Technique* · `generalist-game-agents` · status: **sourced**

Agents that read screen pixels and natural-language instructions and output keyboard and mouse actions across many commercial 3D games, with later versions reasoning, conversing, and improving through self-generated tasks.

| field | value |
|---|---|
| aliases | SIMA, SIMA 2, scalable instructable multiworld agent |
| category | LLM agents |
| year | 2024 |
| maturity | Research |
| trl | 4 |
| runtime | Server real-time, Analytics / live-ops |
| determinism impact | Mitigable |
| horizon | 3-5 years |
| risks | Compute cost, Latency, Evaluation difficulty, Controllability |
| builds on |  |
| deployed in |  |
| affects count *(computed)* | 5 |

## Summary

Agents that read screen pixels and natural-language instructions and output keyboard and mouse actions across many commercial 3D games, with later versions reasoning, conversing, and improving through self-generated tasks.

## Mechanism

The agent sees only rendered frames and a language instruction and emits keyboard and mouse actions in real time, with no access to game source, state APIs, or per-game reward code. SIMA (2024) was trained on human gameplay with language annotations across nine commercial games and four research environments covering about 600 short skills (navigate, interact with objects, use menus). SIMA 2 (2025) puts a fine-tuned Gemini Flash-Lite model at the core, so the agent reasons about goals, states its plan, converses, and follows sketches or emoji. It then improves without human data: a Gemini task setter proposes tasks likely achievable from the current state, the agent attempts them, a Gemini reward model scores each trajectory from 0 to 100 (50 or more counts as success), and the agent trains on the scored experience.

## Limitations

- Weak combat and precise low-level control; failures in held-out games are often due to poor exploration.
- Short memory bounded by the context window, and trouble with long multi-step tasks that need goal verification.
- Built on Gemini Flash-Lite for latency; fine-tuning cost general reasoning (about 25.5% drop on AIME after SFT).
- Runs as a cloud model reading the screen, so per-session inference cost and round-trip latency apply; no public cost figures.
- Not available to players; the reward model was calibrated on a small set of trajectories.

## Relations

**affects**

- [Unit commands](../mechanic/unit-commands.md) (Enables new form): A companion can take open-ended spoken or typed orders, sketches, or emoji and carry them out with ordinary game controls, so the command vocabulary is no longer limited to the verbs a designer bound to buttons.
- [Delegation to AI managers](../mechanic/delegation-to-ai.md) (Enables new form): The player can hand an avatar or task to an agent that pursues a stated goal in any game it can see, without game-specific AI code, and that explains what it intends to do.
- [Natural-language interaction](../mechanic/natural-language-interaction.md) (Deepens): SIMA 2 converses about its surroundings, answers questions about the scene, and explains its actions, grounding dialogue in what it sees on screen.
- [Tech tree](../mechanic/tech-tree.md) (Tunes / balances): Self-improving agents that advance through a game's tech tree can serve as automated playtesters of progression in builds they were not trained on.
- [Programming by demonstration](../mechanic/programming-by-demonstration.md) (Enables new form): Agents that follow language instructions and watch play could learn routines from a single narrated demonstration instead of recorded literal steps.

## Backlinks (computed)

**applied in:** [Explained delegation to AI managers](../opportunity/explained-delegation.md), [Simulation games as agent benchmarks](../opportunity/sims-as-agent-benchmarks.md), [Teachable sim companion](../opportunity/teachable-sim-companion.md), [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

**built upon by:** [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md), [Open-ended co-generation of environments and agents](../technique/open-ended-environment-generation.md)

## Claims

- SIMA 1 learned about 600 basic skills across Valheim, Teardown, No Man's Sky, Wobbly Life, Satisfactory, Goat Simulator 3, Hydroneer, Space Engineers, and Eco; the multi-game agent outperformed per-game specialists, and an agent trained without one game performed nearly as well on it as a specialist. *(confidence: high)* [[132](../source/src-deepmind-2024-sima-blog.md), [133](../source/src-deepmind-2024-sima-paper.md)]
- SIMA 1 tasks completed in about 10 seconds and the agent could not do multi-step strategic planning. *(confidence: high)* [[132](../source/src-deepmind-2024-sima-blog.md)]
- SIMA 2 roughly doubled SIMA 1's average task success on training games, approaching human players, and beat SIMA 1 by over 10% on held-out ASKA and MineDojo, completing tasks in 26 of 50 MineDojo categories. *(confidence: high)* [[134](../source/src-deepmind-2025-sima-2-paper.md)]
- Through self-generated tasks and rewards in ASKA, SIMA 2 went from succeeding on under a quarter of a fixed task set to exceeding human reference scores and progressed further through ASKA's tech tree than earlier versions. *(confidence: high)* [[134](../source/src-deepmind-2025-sima-2-paper.md)]
- SIMA 2 was released only as a limited research preview to a small group of academics and game developers. *(confidence: high)* [[109](../source/src-deepmind-2025-sima-2-blog.md)]

## Sources

- [A generalist AI agent for 3D virtual environments](../source/src-deepmind-2024-sima-blog.md)
- [Scaling Instructable Agents Across Many Simulated Worlds](../source/src-deepmind-2024-sima-paper.md)
- [SIMA 2: An Agent that Plays, Reasons, and Learns With You in Virtual 3D Worlds](../source/src-deepmind-2025-sima-2-blog.md)
- [SIMA 2: A Generalist Embodied Agent for Virtual Worlds](../source/src-deepmind-2025-sima-2-paper.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`; reviewed in `2026-10-24-technique-links`.
