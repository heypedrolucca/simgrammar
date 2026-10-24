# Needs decay

*Mechanic* · `needs-decay` · status: **asserted**

Each agent has needs such as hunger, energy, social, and fun that decay over time and are restored by actions.

| field | value |
|---|---|
| aliases | motives, need meters |
| family | Agents & behavior |
| substrate | Agent-based, Aggregate stocks |
| math basis | System dynamics / ODEs, Queueing theory, Utility / decision theory |
| feedback | Balancing (negative) |
| player interface | Observation only, Placement |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 17 |
| earliest game *(computed)* | [Little Computer People](../game/little-computer-people.md) |
| earliest year *(computed)* | 1985 |
| prevalence *(computed)* | 30 |
| prevalence share *(computed)* | 0.172 |
| subgenre spread *(computed)* | 9 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each agent holds a vector of bounded need stocks (typically 0-100). Every tick each stock decays at a per-need rate, optionally modified by traits, activity, and environment. Actions or objects restore specific needs by fixed or quality-scaled amounts. Low values feed downstream systems: mood, action selection priority, health, or death.

## Player Experience

Constant low-grade triage. The player reads meters, anticipates which need will bottom out first, and arranges the environment or schedule so agents can meet needs without supervision. Neglect is visible and personal.

## Design Levers

- number of needs and which are lethal versus mood-only
- decay rate per need and modifiers by trait, age, or activity
- restoration amount and duration per action or object quality
- threshold values that trigger warnings, priority overrides, or breakdowns
- whether needs are shown as raw meters, icons, or only through behavior

## Failure Modes

- Too many needs turn play into chore management with no strategic choice.
- Uniform decay rates make every agent identical and remove personality.
- Fast decay with slow restoration produces unavoidable death spirals early in a run.
- Hidden needs read as random misbehavior when agents act on them.

## Dynamics

- Synchronized decay creates rush hours at kitchens, beds, and bathrooms.
- Needs compete for agent time, so throughput falls as needs rise, coupling productivity to comfort.
- Better objects restore more per use, creating an upgrade treadmill.

## Open Questions

- Can needs be inferred from behavior by learned agents rather than declared as fixed meters?
- What is the minimal need set that still yields distinct personalities?

## Relations

**synergy**

- [Smart objects](../mechanic/smart-objects.md): Objects advertising need restoration turn decaying needs into autonomous, legible daily behavior (The Sims).

## Backlinks (computed)

**generalizes:** [Creature care](../mechanic/creature-care.md), [Survival meters](../mechanic/survival-meters.md)

**involved in:** [Factories with a living workforce](../opportunity/living-workforce-factories.md), [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md)

**used by:** [Black & White](../game/black-and-white.md), [Creatures](../game/creatures.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Going Medieval](../game/going-medieval.md), [inZOI](../game/inzoi.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Little Computer People](../game/little-computer-people.md), [Nintendogs](../game/nintendogs.md), [Papers, Please](../game/papers-please.md), [Paralives](../game/paralives.md), [Planet Coaster](../game/planet-coaster.md), [Planet Zoo](../game/planet-zoo.md), [Princess Maker 2](../game/princess-maker-2.md), [Prison Architect](../game/prison-architect.md), [RimWorld](../game/rimworld.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Songs of Syx](../game/songs-of-syx.md), [Space Haven](../game/space-haven.md), [Surviving Mars](../game/surviving-mars.md), [Tamagotchi](../game/tamagotchi.md), [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md), [Theme Hospital](../game/theme-hospital.md), [Theme Park](../game/theme-park.md), [This War of Mine](../game/this-war-of-mine.md), [Timberborn](../game/timberborn.md), [Two Point Hospital](../game/two-point-hospital.md), [Zoo Tycoon](../game/zoo-tycoon.md)

---
Provenance: created in run `2026-10-23-bootstrap`; reviewed in `2026-10-24-review-fixes`.
