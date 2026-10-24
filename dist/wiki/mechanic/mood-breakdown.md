# Mood and breakdowns

*Mechanic* · `mood-breakdown` · status: **sourced**

Mood aggregates needs, memories, and environment, and crossing thresholds triggers mental breaks or inspired performance.

| field | value |
|---|---|
| aliases | mental breaks, stress breaks, inspirations |
| family | Agents & behavior |
| substrate | Aggregate stocks, Stochastic events, Agent-based |
| math basis | Markov / stochastic processes, System dynamics / ODEs |
| feedback | Both |
| player interface | Observation only, Placement |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 5 |
| earliest game *(computed)* | [Dwarf Fortress](../game/dwarf-fortress.md) |
| earliest year *(computed)* | 2006 |
| prevalence *(computed)* | 8 |
| prevalence share *(computed)* | 0.046 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a per-agent mood value equal to a baseline plus the sum of active modifiers (needs, memories, environment, traits), usually smoothed toward that target, and a set of thresholds. While mood sits below a threshold a hazard rate rolls for a break whose severity rises with depth; during a break the agent leaves player control. High mood can roll for positive states. RimWorld: base mood 22 to 42 by difficulty; the bar moves toward its target at up to +12 per hour rising and -8 falling; break thresholds are 35%, 20%, and 5% (traits shift the minor one, capped 1-50%), with mean times between breaks of about 4, 0.8, and 0.5 days; above 49% mood, inspirations arrive with a mean interval of 410 - 400 x mood days and grant effects such as x1.8 work speed for 8 days. Dwarf Fortress keeps a hidden stress value, scaled by personality facets, that can end in tantrums or depression. Inputs: needs, memories, traits. Outputs: lost labor, destructive acts, temporary buffs.

## Player Experience

The player manages risk rather than events: watching mood bars near thresholds, removing stressors, and bracing when a disaster pushes several agents under at once. Breaks are memorable because they are partly random and partly the player's fault.

## Design Levers

- baseline per difficulty and weights of each mood input
- threshold levels and trait offsets
- hazard rate per band and severity table
- break catalog (sad wander, binge, tantrum, violence) and whether breaks harm others
- chance and size of positive states at high mood

## Failure Modes

- Cascades: one break creates negative memories in witnesses, and the group spirals beyond recovery after a random event, which feels unfair.
- Mood that is easy to max removes the system from mid and late game.
- Breaks that destroy hours of work feel punitive rather than dramatic.
- Opaque mood sources make breaks feel random.

## Dynamics

- Breakdown contagion: breaks generate negative memories in witnesses that lower their mood, a reinforcing loop.
- Players build mood infrastructure (recreation, beauty, fine meals) as defense, coupling mood to the economy.
- Inspirations reward stable groups with bursts of output, so content colonies pull further ahead.

## Open Questions

- Can breaks be generated as character-specific behavior by language-model agents instead of drawn from a fixed catalog, and still be legible?
- What hazard shape keeps breaks dramatic without producing unrecoverable cascades?

## Relations

**synergy**

- [Needs decay](../mechanic/needs-decay.md): Unmet needs feed mood; breakdowns make neglect dramatic instead of a silent efficiency loss.

## Backlinks (computed)

**used by:** [Dwarf Fortress](../game/dwarf-fortress.md), [Going Medieval](../game/going-medieval.md), [Oxygen Not Included](../game/oxygen-not-included.md), [RimWorld](../game/rimworld.md), [Space Haven](../game/space-haven.md), [Surviving Mars](../game/surviving-mars.md), [The Sims 4](../game/the-sims-4.md), [This War of Mine](../game/this-war-of-mine.md)

## Sources

- [Mental break](../source/src-rimworldwiki-2026-mental-break.md)
- [Mood](../source/src-rimworldwiki-2026-mood.md)
- [Inspiration](../source/src-rimworldwiki-2026-inspiration.md)
- [Stress](../source/src-dfwiki-2026-stress.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
