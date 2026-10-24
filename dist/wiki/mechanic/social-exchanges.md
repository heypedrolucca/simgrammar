# Social exchanges

*Mechanic* · `social-exchanges` · status: **sourced**

Discrete social moves such as flirt, insult, or apologize have preconditions on social state and norms, and they update relationships.

| field | value |
|---|---|
| aliases | social moves, social interactions, social games |
| family | Social relations |
| substrate | Rule system, Agent-based |
| math basis | Utility / decision theory, Social network models |
| feedback | Both |
| player interface | Choice / cards, Observation only |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 4 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Established |
| requires | [Relationship values](../mechanic/relationship-values.md) |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [The Sims](../game/the-sims.md) |
| earliest year *(computed)* | 2000 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 1.312 |

## Definition

Owns a library of social exchange definitions, each with an intent, preconditions on the social state, initiator and responder desire rules, and effects for acceptance and rejection on relationships, statuses, and history. Each cycle an agent scores the exchanges it could start with each other agent, picks one, the responder evaluates acceptance, and the outcome is written to state and history. Comme il Faut in Prom Week defines exchanges with one intent, hard preconditions, initiator and responder influence rule sets, and at least accept and reject instantiations; volition sums the weights of over 5,000 influence rules across 34 statuses and 44 traits. RimWorld rolls chitchat, deep talk, slights, and insults with weights from opinion and compatibility; The Sims 3 defined hundreds of interactions from thousands of production rules (Evans, GDC 2010). Inputs: social state, traits, history. Outputs: relationship and status changes, logged events.

## Player Experience

The player chooses moves in a social puzzle, or watches agents make them, and learns the norms that make a move land. Rejections and backfires are part of the fun, and players develop social strategies such as softening a target before the big ask.

## Design Levers

- size of the exchange library and intents covered
- precondition strictness and which norms or statuses gate moves
- volition rule weights for initiators and responders
- effect magnitudes for accept and reject outcomes
- player control: choose moves, suggest, or only watch

## Failure Modes

- Small libraries repeat the same exchanges until characters feel scripted.
- Rule weights interact unpredictably across thousands of rules, so authors cannot predict outcomes.
- Exchanges change numbers without visible performance, so moves feel interchangeable.
- Spam: repeating the best-scoring move maxes relationships.

## Dynamics

- Logged exchanges become history that later rules reference, so past insults enable future revenge moves.
- Status effects spread socially, so one embarrassing exchange changes how a group treats a character.
- Exchange outcomes drive relationship values, which change the next exchange's odds, producing escalating arcs.

## Open Questions

- Can language models generate performances and new exchange types on the fly while a symbolic layer keeps preconditions and effects consistent?
- Can influence-rule weights be learned from player judgments of plausibility rather than authored?

## Relations

**requires**

- [Relationship values](../mechanic/relationship-values.md)

## Backlinks (computed)

**affected by:** [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [Realtime speech-to-speech and expressive TTS for characters](../technique/realtime-voice-models.md)

**involved in:** [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md)

**used by:** [Football Manager](../game/football-manager.md), [Prom Week](../game/prom-week.md), [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md), [Versu](../game/versu.md)

## Sources

- [Social Story Worlds With Comme il Faut](../source/src-mccoy-2014-social-story-worlds.md)
- [Modeling Individual Personalities in The Sims 3](../source/src-evans-2010-sims-3-personalities.md)
- [Social](../source/src-rimworldwiki-2026-social.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
