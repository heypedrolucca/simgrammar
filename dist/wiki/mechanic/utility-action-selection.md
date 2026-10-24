# Utility action selection

*Mechanic* · `utility-action-selection` · status: **sourced**

Agents choose actions by scoring options against needs and context, then picking the highest or sampling among high scores.

| field | value |
|---|---|
| aliases | utility AI, utility scoring, needs-based AI |
| family | Agents & behavior |
| substrate | Agent-based |
| math basis | Utility / decision theory, Probability / statistics |
| feedback | Balancing (negative) |
| player interface | Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [The Sims](../game/the-sims.md) |
| earliest year *(computed)* | 2000 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 7 |
| technique exposure *(computed)* | 2.95 |

## Definition

Owns per-agent scoring weights and response curves rather than world state. Each decision cycle it enumerates candidate actions, scores each from inputs such as need levels, distance, personality, risk, and context passed through response curves and combined by product or weighted sum, then selects the top action or samples among high scorers. Dill and Mark (GDC 2010) present response curves, population distributions, and weighted random selection as a fix for the abrupt switches of if-then logic. The Sims picks the behavior that most increases happiness from object advertisements; The Sims 3 (Richard Evans) samples with a modified Boltzmann distribution whose temperature rises when a Sim is doing poorly; the Infinite Axis Utility System (Mark and Lewis, GDC 2015) multiplies normalized considerations. Inputs: candidate actions and their considerations. Outputs: the chosen action and, if exposed, a ranked list of reasons.

## Player Experience

Agents look like they are weighing options: they handle the urgent thing first but sometimes surprise. The player steers them indirectly by changing inputs such as needs, objects, and priorities, and reads odd choices as personality.

## Design Levers

- response curve shape per consideration
- combination rule (product, sum, max) and normalization
- selection rule: argmax, random among the top N, or softmax with a temperature
- inertia or commitment bonus that prevents switching between close options
- per-agent personality weights

## Failure Modes

- Dithering: two actions with close scores alternate, so agents start and abandon tasks.
- One consideration dominates the product or sum, and agents ignore everything else.
- Choices are hard to explain because each score is the product of many curves, so players see randomness.
- Weight tuning grows with the number of actions times considerations and resists local fixes.

## Dynamics

- Priorities emerge from scores rather than authored order, so new situations get plausible, unscripted responses.
- Coupled with needs decay, agents cycle through activities in rhythms that read as routines.
- Small weight changes ripple across a population, so balance patches visibly change agent culture.

## Open Questions

- Can language-model agents propose candidate actions that a utility layer then scores, combining open-ended options with predictable tuning?
- Can scoring functions learned from player-labeled preferences replace hand-built response curves?

## Backlinks (computed)

**affected by:** [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md), [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [Massively parallel GPU simulation](../technique/massively-parallel-simulation.md), [Monte Carlo tree search for game AI](../technique/monte-carlo-tree-search.md), [On-device small language models for characters](../technique/on-device-language-models.md), [Physical-world foundation models](../technique/physical-world-foundation-models.md)

**involved in:** [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md)

**used by:** [Prom Week](../game/prom-week.md), [The Sims](../game/the-sims.md), [Versu](../game/versu.md)

## Sources

- [Improving AI Decision Modeling Through Utility Theory](../source/src-dill-2010-utility-theory.md)
- [Utility system](../source/src-wikipedia-utility-system.md)
- [Some notes on programming objects in The Sims](../source/src-forbus-2001-programming-objects-sims.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
