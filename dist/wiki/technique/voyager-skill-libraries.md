# LLM-written skill libraries (Voyager)

*Technique* · `voyager-skill-libraries` · status: **sourced**

An LLM agent that proposes its own next task, writes executable code to do it, refines the code from execution errors and self-checks, and stores verified programs in a retrievable skill library.

| field | value |
|---|---|
| aliases | Voyager, code-as-skill, lifelong learning agent |
| category | LLM agents |
| year | 2023 |
| maturity | Research |
| trl | 4 |
| runtime | Server real-time, Analytics / live-ops |
| determinism impact | Mitigable |
| horizon | 1-2 years |
| risks | Compute cost, Consistency / hallucination, Evaluation difficulty, Controllability, Latency |
| builds on |  |
| deployed in |  |
| affects count *(computed)* | 5 |

## Summary

An LLM agent that proposes its own next task, writes executable code to do it, refines the code from execution errors and self-checks, and stores verified programs in a retrievable skill library.

## Mechanism

Voyager drives a Minecraft bot through a JavaScript control API. An automatic curriculum asks GPT-4 for the next task given inventory, surroundings, and completed tasks, aiming to discover as many diverse things as possible. For each task GPT-4 writes a function that may call existing skills; the function runs, and the agent feeds back environment observations, execution errors, and a GPT-4 self-verification verdict, retrying up to four rounds before moving on. Verified functions are stored in a skill library indexed by an embedding of their description and retrieved (top-k) when writing later functions, so complex behaviors are composed from earlier ones. No model weights are trained; all learning is in the growing code library, which can be reused in a new world.

## Limitations

- Depends on a frontier code model; GPT-3.5 produced 5.7x fewer items and GPT-4 cost 15x more per token, so per-agent cost is high.
- Hallucinated tasks and calls: the curriculum proposed items that do not exist (copper sword), and generated code used invalid inputs or functions absent from the API, causing execution errors.
- Self-verification misjudges success (for example not recognizing a dropped string as proof a spider was defeated).
- Needs a scripting API that exposes game actions and state as text; it does not act from pixels.
- Long-horizon factory building in Factorio still fails at multi-step automation and spatial layout.

## Relations

**affects**

- [Player programming](../mechanic/player-programming.md) (Enables new form): The player can describe a behavior in language and the model writes, tests against the live game, and saves the program, so player code becomes a growing library of named skills rather than hand-typed scripts.
- [Agent skills](../mechanic/agent-skills.md) (Enables new form): An NPC's competence can be an accumulating library of composable, verified routines it wrote itself, so skill growth adds new behaviors rather than raising a numeric speed or quality level.
- [Delegation to AI managers](../mechanic/delegation-to-ai.md) (Enables new form): A delegated controller can acquire routines for situations its designers did not code by writing and verifying new functions, instead of running the fixed opponent-AI logic restricted to a subsystem.
- [Tech tree](../mechanic/tech-tree.md) (Tunes / balances): Exploration agents that unlock milestones 15.3x faster than earlier agents can be run as automated playtesters to measure how quickly and in what order a progression graph gets traversed.
- [Programming by demonstration](../mechanic/programming-by-demonstration.md) (Deepens): Demonstrated routines can be stored as verified, reusable code skills that generalize to new locations.

## Backlinks (computed)

**applied in:** [Mechanic modding by description](../opportunity/language-modding.md), [Simulation games as agent benchmarks](../opportunity/sims-as-agent-benchmarks.md), [Teachable sim companion](../opportunity/teachable-sim-companion.md)

## Claims

- Against prior LLM agents, Voyager obtained 3.3x more unique items, traveled 2.3x longer distances, and unlocked tech-tree milestones up to 15.3x faster, discovering 63 unique items in 160 prompting iterations. *(confidence: high)* [[198](../source/src-wang-2023-voyager.md)]
- The learned skill library let a fresh agent solve novel tasks in a new Minecraft world from scratch, where baselines struggled. *(confidence: high)* [[198](../source/src-wang-2023-voyager.md)]
- Code generation quality was the bottleneck: replacing GPT-4 with GPT-3.5 for code produced 5.7x fewer unique items, while GPT-4 cost 15x more per token. *(confidence: high)* [[198](../source/src-wang-2023-voyager.md)]
- In the 2025 Factorio Learning Environment, LLM agents writing code found growth strategies such as electric drilling but failed at complex automation such as electronic-circuit production, with weak spatial reasoning and error recovery. *(confidence: medium)* [[199](../source/src-hopkins-2025-factorio-learning-environment.md)]

## Sources

- [Voyager: An Open-Ended Embodied Agent with Large Language Models](../source/src-wang-2023-voyager.md)
- [Factorio Learning Environment](../source/src-hopkins-2025-factorio-learning-environment.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`; reviewed in `2026-10-24-technique-links`.
