# Salience-gated language agents

*Opportunity* · `salience-gated-llm-agents` · status: **asserted**

Keep cheap utility scoring for every tick and call a language model only at salient moments, giving colony and life sims believable minds at a bounded cost.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Utility action selection](../mechanic/utility-action-selection.md), [Needs decay](../mechanic/needs-decay.md), [Memories and thoughts](../mechanic/memories-thoughts.md), [Social exchanges](../mechanic/social-exchanges.md), [Relationship values](../mechanic/relationship-values.md), [Personality traits](../mechanic/personality-traits.md) |
| applies | [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [On-device small language models for characters](../technique/on-device-language-models.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md) |
| precedent | [The Sims](../game/the-sims.md), [RimWorld](../game/rimworld.md), [inZOI](../game/inzoi.md), [Dwarf Fortress](../game/dwarf-fortress.md) |
| novelty | 3 |
| feasibility | 4 |
| impact | 4 |
| horizon | Now |
| falsifiable signal | {'prediction': 'At least three colony or life sims with over 1,000 Steam user reviews will call a language model for agents only on salient events rather than per decision.', 'resolve_by': '2028-12-31', 'criteria': 'Count titles released or patched after 2026-10-24 with more than 1,000 Steam user reviews; developer documentation, postmortems, or mod-verified behavior show model calls triggered by discrete events while routine behavior runs on non-model systems.'} |
| priority *(computed)* | 3.776 |

## Thesis

Rule-based utility agents are cheap and legible but repetitive; fully LLM-driven agents are expressive but cost tokens every decision and drift from game state. Most agent decisions in The Sims or RimWorld are routine (eat, sleep, haul) and need no language model. The memorable moments are rare: a breakup, a grudge, a mental break, a first meeting. A hybrid that reserves model calls for events above a salience threshold, and writes the result back as typed memories and relationship deltas, captures most of the believability at a small fraction of the cost. Small local models made this affordable in 2025; constrained decoding makes the write-back safe.

## Design Sketch

Colonists run a standard needs-and-utility loop. When an event crosses a salience score (death of a friend, public insult, near-starvation), the agent gets one model call with its trait list, recent memories, and the event, and must return a schema-valid object: a thought with mood value and duration, an optional relationship change, an optional one-line spoken reaction, and an optional new goal. The player sees these as ordinary thoughts in the inspector, now specific to the colonist's history.

## Key Risks

- Generated thoughts that contradict visible state erode trust faster than generic thoughts do.
- Salience thresholds tuned for drama can flood the log in crisis states.
- Local model quality varies by hardware tier, creating uneven experiences.

## Validation Experiment

Build a 20-colonist prototype with a pure-utility baseline and a salience-gated variant capped at one model call per colonist per in-game hour. Run blind playtests (n>=30) rating believability and attachment, log tokens per player-hour, and count state-contradiction errors per hour. Success: believability gain of at least one point on a 7-point scale at under 2,000 tokens per player-hour with contradiction rate below one per hour.

## Falsifiable signal

- **Prediction:** At least three colony or life sims with over 1,000 Steam user reviews will call a language model for agents only on salient events rather than per decision.
- **Resolve by:** 2028-12-31
- **Criteria:** Count titles released or patched after 2026-10-24 with more than 1,000 Steam user reviews; developer documentation, postmortems, or mod-verified behavior show model calls triggered by discrete events while routine behavior runs on non-model systems.

## Relations

**applies**

- [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md)
- [On-device small language models for characters](../technique/on-device-language-models.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

**involves**

- [Utility action selection](../mechanic/utility-action-selection.md)
- [Needs decay](../mechanic/needs-decay.md)
- [Memories and thoughts](../mechanic/memories-thoughts.md)
- [Social exchanges](../mechanic/social-exchanges.md)
- [Relationship values](../mechanic/relationship-values.md)
- [Personality traits](../mechanic/personality-traits.md)

**precedent**

- [The Sims](../game/the-sims.md)
- [RimWorld](../game/rimworld.md)
- [inZOI](../game/inzoi.md)
- [Dwarf Fortress](../game/dwarf-fortress.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
