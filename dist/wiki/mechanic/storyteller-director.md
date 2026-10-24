# Storyteller director

*Mechanic* · `storyteller-director` · status: **sourced**

A director AI chooses which events to fire and when, pacing them by a model of tension and the current state.

| field | value |
|---|---|
| aliases | AI director, AI storyteller, drama manager |
| family | Narrative & generation |
| substrate | Stochastic events, Rule system |
| math basis | Control theory, Markov / stochastic processes, Probability / statistics |
| feedback | Balancing (negative) |
| player interface | Observation only, Parameter |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Façade](../game/facade.md) |
| earliest year *(computed)* | 2005 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 1.0 |

## Definition

A director process tracks a pacing signal and runs a cycle that selects incidents from a catalog. Left 4 Dead's AI Director keeps an emotional intensity value per survivor that rises with damage, incapacitation, and nearby infected deaths and decays when not engaged; it cycles through Build Up (full threat until peak intensity), Sustain Peak (3-5 s), Peak Fade, and Relax (30-45 s of minimal spawns), spawns mobs every 90-180 s on Normal, and deals boss events (Tank, Witch, nothing) along the route. RimWorld storytellers weigh colony wealth, colonists, recent deaths or wounds, and time since the last major event; incident chance is a base chance times a population-intent factor, and presets differ (Cassandra escalates in cycles, Phoebe leaves long gaps, Randy is irregular). The director decides when and what; magnitude usually comes from adaptive threat scaling. Outputs: incident firing, spawn populations, item placement, music cues.

## Player Experience

Play has a rhythm of pressure and relief that feels authored even though it is generated. Players use calm windows to build and heal, brace when calm runs long, and talk about storytellers as personalities with moods and grudges.

## Design Levers

- pacing signal: per-player intensity, time since last threat, or colony state
- phase thresholds and durations for build-up, peak, and relaxation
- incident catalog, base weights, and state conditions such as population intent
- selectable presets that change cycle shape and randomness
- randomness floor and mercy rules after heavy losses

## Failure Modes

- Fixed cycles become predictable, and players learn to exploit relax windows.
- Irregular presets can stack several hard events, which feels unfair when combined with permadeath.
- Heavy rubber-banding makes skill feel irrelevant because the director compensates for good play.

## Dynamics

- Pressure and relief cycles create natural story beats that players retell as chapters.
- Combined with persistent injuries and permadeath, a poorly timed second incident starts cascades that become memorable runs.
- Players manipulate the director's inputs, such as population or wealth, to shape which incidents it can choose.

## Open Questions

- Can a language-model director author new incidents conditioned on colony state and characters, not just select from a catalog?
- Can learned models of player stress from play telemetry replace hand-built intensity formulas?
- How should a director balance dramatic pacing against fairness when deaths are permanent?

## Backlinks (computed)

**affected by:** [Genie foundation world models](../technique/genie-world-models.md), [LLM game master and narrative director](../technique/llm-game-master.md)

**involved in:** [Content-elastic event systems](../opportunity/content-elastic-events.md), [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md)

**used by:** [Façade](../game/facade.md), [RimWorld](../game/rimworld.md), [Versu](../game/versu.md)

## Sources

- [The AI Systems of Left 4 Dead](../source/src-booth-2009-ai-systems-l4d.md)
- [AI Storytellers](../source/src-rimworldwiki-2026-ai-storytellers.md)
- [Left 4 Dead](../source/src-wikipedia-left-4-dead.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
