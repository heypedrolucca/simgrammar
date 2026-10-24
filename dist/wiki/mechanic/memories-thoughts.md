# Memories and thoughts

*Mechanic* · `memories-thoughts` · status: **sourced**

Events create itemized, time-limited mood modifiers or lasting memories that shape later behavior.

| field | value |
|---|---|
| aliases | moodlets, thoughts, memory stream |
| family | Agents & behavior |
| substrate | Agent-based, Rule system |
| math basis | System dynamics / ODEs, Probability / statistics |
| feedback | Balancing (negative) |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Seaman](../game/seaman.md) |
| earliest year *(computed)* | 1999 |
| prevalence *(computed)* | 10 |
| prevalence share *(computed)* | 0.057 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 1.312 |

## Definition

Owns a per-agent list of memory entries, each with a type, a source (event, object, or other agent), an effect magnitude, a start time, and an expiry or decay. Events append entries; each tick expired entries drop and the active set is summed into mood or opinion, with stacking rules that cap and discount repeats. RimWorld memory thoughts list mood effect, duration, stack limit, and a stack multiplier (mostly 0.75): My son died is -20 for 30 days, Ate lavish meal +12, and some traits nullify specific thoughts. The Sims 3 and The Sims 4 show the same idea as timed moodlets. Generative Agents (2023) stores memory as a natural-language stream retrieved by the sum of normalized recency (decay 0.995 per game hour), language-model-rated importance (1-10), and embedding relevance, and writes reflections when summed importance exceeds 150. Inputs: events with sources. Outputs: mood and opinion contributions, and retrieved context for decisions and dialogue.

## Player Experience

The player can read why an agent feels the way it does, line by line, and plans around expiry: a funeral penalty will pass in days, and a lavish meal can offset it now. Itemized memories turn hidden state into stories players retell.

## Design Levers

- magnitude and duration per event type
- stack limit and multiplier for repeated events
- decay shape (fixed expiry, linear, exponential) and which memories become permanent
- trait filters that nullify or amplify memory types
- retrieval weights (recency, importance, relevance) when memories drive decisions or dialogue

## Failure Modes

- Long lists of small thoughts become noise that players stop reading.
- Cheap positive thoughts (fine meals, art) are easy to farm and swamp negative events, draining drama.
- Short durations make tragedies trivial; long ones create unavoidable spirals after a single disaster.
- Natural-language memory streams grow without bound, raising retrieval cost and surfacing irrelevant memories.

## Dynamics

- One disaster writes negative memories into many agents at once, synchronizing their breakdown risk.
- Players schedule offsetting positive events, turning mood into a budget managed against expiry timers.
- Memories that name other agents seed opinions and grudges that outlive the event.

## Open Questions

- How should natural-language memory streams be compressed so retrieval stays relevant across years of game time?
- Which memories should be promoted from temporary modifiers to lasting personality change, and can that rule be learned?

## Relations

**synergy**

- [Mood and breakdowns](../mechanic/mood-breakdown.md): Itemized, expiring thoughts give mood a history the player can read and story-tell around (RimWorld).

## Backlinks (computed)

**affected by:** [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [On-device small language models for characters](../technique/on-device-language-models.md)

**involved in:** [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md), [Generated dream and replay views](../opportunity/dream-replay-layer.md), [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md)

**used by:** [Dwarf Fortress](../game/dwarf-fortress.md), [Generative Agents (Smallville)](../game/generative-agents-smallville.md), [Project Sid](../game/project-sid.md), [Prom Week](../game/prom-week.md), [RimWorld](../game/rimworld.md), [Seaman](../game/seaman.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md), [Versu](../game/versu.md)

## Sources

- [Thoughts](../source/src-rimworldwiki-2026-thoughts.md)
- [Generative Agents: Interactive Simulacra of Human Behavior](../source/src-park-2023-generative-agents.md)
- [Motive](../source/src-simswiki-2026-motive.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
