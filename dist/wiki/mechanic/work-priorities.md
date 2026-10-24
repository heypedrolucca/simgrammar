# Work priorities

*Mechanic* · `work-priorities` · status: **sourced**

The player sets which agents do which job types in what order, and agents self-assign from that priority table.

| field | value |
|---|---|
| aliases | work tab, labor assignments, job priorities |
| family | Agents & behavior |
| substrate | Rule system, Agent-based |
| math basis | Scheduling, Optimization |
| feedback | None |
| player interface | Parameter |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [SimAnt](../game/simant.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a matrix of agents by job types holding enabled flags or priority numbers, plus a fixed ordering of job types. When an agent is idle it scans job types in priority order, breaking ties by column order, and takes an available job of the highest priority it can do, usually the nearest. RimWorld's work tab has a standard mode (checkmarks, columns further left more important) and a manual mode with priorities 1 (highest) to 4; all available work at one priority is done before the next, blank cells are never done, incapable work types are excluded, and allowed areas restrict where jobs are taken. Dwarf Fortress uses per-dwarf labor toggles, and Oxygen Not Included combines per-duplicant errand priorities with 1-9 priorities on individual buildings. Inputs: the job queue, skills, distances. Outputs: who does what, and how fast the group responds to new work.

## Player Experience

The player acts as a manager, matching people to jobs by skill and interest, then debugging the table when hauling never happens or the doctor is busy cooking. The table is where strategy is expressed without micromanaging each task.

## Design Levers

- granularity of job types
- number of priority levels and tie-break rules
- global agent-by-type priorities versus per-task or per-building overrides
- interaction with distance: nearest job first versus highest priority first
- automatic suggestions based on skill

## Failure Modes

- Priority inversion: an agent hauls a distant item at priority 1 while a patient bleeds, because all priority-1 work is done before the next level.
- Large matrices become spreadsheet management that players solve once with a template and stop engaging with.
- Poor tie-breaking sends agents across the map for low-value tasks.
- Hidden ordering within a job type surprises players.

## Dynamics

- Fixing one starved job type exposes the next bottleneck, so the table evolves as the group grows.
- Priorities aligned with skills create specialists, which reinforces skill gaps.
- Emergencies force temporary reshuffles or direct control, producing spikes of micromanagement.

## Open Questions

- Can a manager agent translate high-level intents (keep everyone fed, prioritize medicine) into the priority table and explain its settings?
- Does automatic assignment remove the managerial decision or only the spreadsheet tedium?

## Backlinks (computed)

**involved in:** [Intent-level orders](../opportunity/intent-level-orders.md)

**used by:** [Banished](../game/banished.md), [Going Medieval](../game/going-medieval.md), [Kenshi](../game/kenshi.md), [Oxygen Not Included](../game/oxygen-not-included.md), [RimWorld](../game/rimworld.md), [SimAnt](../game/simant.md)

## Sources

- [Work](../source/src-rimworldwiki-2026-work.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
