# Labor market

*Mechanic* · `labor-market` · status: **sourced**

Workers fill jobs by type and education; mismatches create unemployment or labor shortages that throttle production.

| field | value |
|---|---|
| aliases | jobs and workers, employment, workforce |
| family | Economy & finance |
| substrate | Aggregate stocks, Agent-based |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Balancing (negative) |
| player interface | Observation only, Placement |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Caesar III](../game/caesar-3.md) |
| earliest year *(computed)* | 1998 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.25 |

## Definition

Owns the worker supply by type (education, class, or profession) and the job slots by type that buildings offer, and matches them. Unmatched workers are unemployed; unfilled jobs leave buildings understaffed, and output scales with staffing. In Micropolis, the SimCity engine, Employment = jobs / (residents / 8) drives migration of (residents / 8) x (Employment - 1) per cycle, a labor ratio of residents to jobs clamped to 0-1.3 scales projected commercial and industrial growth, and unemployment is one of the problems citizens complain about. Cities: Skylines and Workers and Resources split workers by education, so a city without educated workers cannot staff offices or advanced plants. Victoria 3 hires pops into buildings by profession and wage, and Anno 1800 requires each residence tier to staff that tier's production buildings.

## Player Experience

Balancing homes against jobs. The player reads unemployment and vacancy numbers, builds housing or schools when factories sit idle, and learns that a new industry is useless without workers to run it.

## Design Levers

- number of worker types and whether higher types can fill lower jobs
- staffing-to-output curve (linear, threshold, or minimum crew)
- commute or catchment limits on which workers can reach which jobs
- migration response to unemployment and vacancies
- wages as a lever that shifts who takes which job

## Failure Modes

- Aggregate matching hides the cause of shortages, so players see idle buildings without knowing which worker type is missing.
- Education systems that push the whole population past the available jobs can stall industry with no clear fix.
- Instant matching removes the lag that makes workforce planning interesting.

## Dynamics

- Jobs attract migrants, migrants demand shops and services, and those create more jobs, producing boom cycles.
- A large employer far from housing generates commuter traffic and congestion.
- Education pays off with a long lag, so labor mismatches appear whenever the economy shifts.

## Open Questions

- Can agent-level career choice by learned or LLM agents produce realistic structural unemployment without hand-tuned migration formulas?
- How much labor detail (types, commutes, wages) can players manage before the mechanic becomes opaque?

## Backlinks (computed)

**affected by:** [Many-agent LLM societies](../technique/llm-agent-societies.md)

**used by:** [Anno 1800](../game/anno-1800.md), [Caesar III](../game/caesar-3.md), [Frostpunk](../game/frostpunk.md), [Pharaoh](../game/pharaoh.md), [Victoria 3](../game/victoria-3.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
