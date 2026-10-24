# Agent skills

*Mechanic* · `agent-skills` · status: **sourced**

Agents gain skill through practice or training, and skill sets work speed, quality, and access to tasks.

| field | value |
|---|---|
| aliases | skill levels, learning by doing, experience levels |
| family | Agents & behavior |
| substrate | Agent-based, Aggregate stocks |
| math basis | System dynamics / ODEs, Probability / statistics |
| feedback | Both |
| player interface | Observation only, Parameter |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [Princess Maker 2](../game/princess-maker-2.md) |
| earliest year *(computed)* | 1993 |
| prevalence *(computed)* | 33 |
| prevalence share *(computed)* | 0.19 |
| subgenre spread *(computed)* | 16 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.25 |

## Definition

Each agent holds an experience stock and level per skill. Doing a task adds experience at a rate scaled by learning modifiers; crossing thresholds raises the level, and some games decay unused high levels. Level feeds work speed, success or botch chance, output quality, and minimum-level gates. RimWorld uses levels 0-20; experience to the next level rises from 1,000 at level 0 to 30,000 at level 19; passion sets learning to 35% (none), 100%, or 150%; skills above 9 decay by 30 to 3,600 XP per day; a daily cap of 4,000 XP per skill cuts further gains to 20%; construction speed is 50% plus 15% per level; some backstories make pawns incapable of a work type. The Sims raises skills through objects such as bookshelves and easels and gates promotions on them; Dwarf Fortress dwarves improve by repeating labors. Inputs: task time, learning modifiers. Outputs: speed, quality, eligibility for tasks.

## Player Experience

Agents become individuals with track records. The player assigns specialists, trains newcomers on low-stakes work, and feels the loss when a master crafter dies. Skill growth gives each character a slow progression arc that runs alongside the base's growth.

## Design Levers

- experience curve shape and level cap
- learning-rate modifiers such as passions, traits, age, and teachers
- decay of unused skills and daily learning caps
- effect curves per level on speed, quality, and failure chance
- hard gates (minimum level, incapable) versus soft penalties

## Failure Modes

- Uncapped or linear growth turns every long-lived agent into a master, flattening differences between characters.
- Grinding: players set agents to repeat cheap tasks to farm experience, which RimWorld counters with a daily learning cap.
- Steep effect curves make low-skill recruits useless, so new agents are dead weight rather than trainees.
- Decay without clear feedback reads as random loss of competence.

## Dynamics

- Specialization snowballs: the best agent at a job gets assigned it, which raises that skill further and widens gaps.
- Losing a specialist opens a capability hole that forces retraining or recruitment; with permadeath this is a common crisis.
- Coupled with quality tiers, item value depends on who made it, so assignment becomes an economic decision.

## Open Questions

- Can skills be represented as learned competence (policies that actually improve) rather than numeric multipliers, and does that change player attachment?
- Which decay and cap settings keep specialization meaningful without rewarding grinding?

## Relations

**synergy**

- [Staff hiring and rosters](../mechanic/staff-hiring.md): Hiring trades wage cost against skill, and skills grow with time on the roster.
- [Work priorities](../mechanic/work-priorities.md): Priorities route skilled agents to the jobs they do best.
- [Quality tiers](../mechanic/quality-tiers.md): Skilled workers produce higher-quality goods.

## Backlinks (computed)

**affected by:** [LLM-written skill libraries (Voyager)](../technique/voyager-skill-libraries.md)

**involved in:** [Factories with a living workforce](../opportunity/living-workforce-factories.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md)

**used by:** [Aurora 4X](../game/aurora-4x.md), [Bitburner](../game/bitburner.md), [Car Mechanic Simulator 2021](../game/car-mechanic-simulator-2021.md), [Crusader Kings III](../game/crusader-kings-3.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Eco](../game/eco.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md), [EVE Online](../game/eve-online.md), [Football Manager](../game/football-manager.md), [FTL: Faster Than Light](../game/ftl.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Going Medieval](../game/going-medieval.md), [House Flipper](../game/house-flipper.md), [inZOI](../game/inzoi.md), [Kenshi](../game/kenshi.md), [Out of the Park Baseball](../game/out-of-the-park-baseball.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Paralives](../game/paralives.md), [Princess Maker 2](../game/princess-maker-2.md), [Project Hospital](../game/project-hospital.md), [Project Zomboid](../game/project-zomboid.md), [RimWorld](../game/rimworld.md), [Silent Hunter III](../game/silent-hunter-3.md), [Space Haven](../game/space-haven.md), [Stardew Valley](../game/stardew-valley.md), [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md), [Theme Hospital](../game/theme-hospital.md), [Two Point Hospital](../game/two-point-hospital.md), [Ultima Online](../game/ultima-online.md), [Valheim](../game/valheim.md)

## Sources

- [Skills](../source/src-rimworldwiki-2026-skills.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
