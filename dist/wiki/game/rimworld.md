# RimWorld

*Game* · `rimworld` · status: **sourced**

A colony sim where a few named colonists with needs, traits, injuries, and relationships survive on a frontier planet while a storyteller AI paces events.

| field | value |
|---|---|
| year | 2013 |
| year full release | 2018 |
| developer | Ludeon Studios |
| platforms | PC, Console |
| subgenre | Colony sim |
| subgenre secondary | Survival sim |
| sim domain | Social / interpersonal, Biological / ecological, Military / conflict |
| player role | Overseer |
| agency model | Order queue, Indirect incentive, Direct unit control |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Cascading collapse |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Total conversion |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 5 |
| influence | 4 |
| core loop | designate work -> colonists self-assign by priority -> needs and moods shift -> storyteller injects events -> colony adapts or collapses |
| influenced by | [Dwarf Fortress](../game/dwarf-fortress.md) |
| cluster *(computed)* | C04 |
| core count *(computed)* | 7 |
| mechanic count *(computed)* | 21 |

## Design Notes

Tynan Sylvester describes RimWorld as a story generator. Its systems are chosen for how legible and story-relevant their outputs are rather than for realism: thoughts are itemized with sources and durations, injuries are named body parts, and raids scale with colony wealth to keep tension.

## Relations

**influenced by**

- [Dwarf Fortress](../game/dwarf-fortress.md)

**uses**

- [Storyteller director](../mechanic/storyteller-director.md) (core): Selectable storytellers (Cassandra, Phoebe, Randy) choose incidents using a threat budget derived from colony wealth and time since the last major event.
- [Needs decay](../mechanic/needs-decay.md) (core): Colonists track food, rest, recreation, comfort, beauty, and other needs whose levels feed mood.
- [Mood and breakdowns](../mechanic/mood-breakdown.md) (core): Mood below trait-adjusted break thresholds triggers minor, major, or extreme mental breaks; high mood can grant inspirations.
- [Memories and thoughts](../mechanic/memories-thoughts.md) (core): Every mood effect is an itemized thought with a source and expiry, visible in the needs tab.
- [Work priorities](../mechanic/work-priorities.md) (core): A work tab matrix sets 1-4 priorities per colonist per job type; colonists self-assign.
- [Injury body model](../mechanic/injury-body-model.md) (core): Bodies are hierarchies of parts with hit points, bleeding, infection, scars, and prosthetics that change capacities like moving and manipulation.
- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md) (core): Raid strength scales with colony wealth, number of colonists, and difficulty, so growth raises danger.
- [Designation orders](../mechanic/designation-orders.md) (supporting)
- [Personality traits](../mechanic/personality-traits.md) (supporting)
- [Agent skills](../mechanic/agent-skills.md) (supporting)
- [Relationship values](../mechanic/relationship-values.md) (supporting)
- [Room recognition](../mechanic/room-recognition.md) (supporting)
- [Decoration and beauty](../mechanic/decoration-beauty.md) (supporting)
- [Raid defense](../mechanic/raid-defense.md) (supporting)
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting)
- [Spoilage](../mechanic/spoilage.md) (supporting)
- [Procedural characters](../mechanic/procedural-characters.md) (supporting)
- [Agent inspection](../mechanic/agent-inspection.md) (supporting)
- [Permadeath](../mechanic/permadeath.md) (supporting)
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Autonomy levels](../mechanic/autonomy-levels.md) (supporting): Drafting switches a colonist from self-assigned work to direct player control for combat or emergencies.

## Backlinks (computed)

**influenced:** [Going Medieval](../game/going-medieval.md), [Space Haven](../game/space-haven.md)

**precedent for:** [Why-query over the simulation log](../opportunity/causal-why-query.md), [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md), [Generated dream and replay views](../opportunity/dream-replay-layer.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md), [Intent-level orders](../opportunity/intent-level-orders.md), [Mechanic modding by description](../opportunity/language-modding.md), [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md), [Parallel autobalancing of economies](../opportunity/parallel-autobalance.md), [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md)

## Sources

- [RimWorld](../source/src-wikipedia-rimworld.md)

---
Provenance: created in run `2026-10-23-bootstrap`.
