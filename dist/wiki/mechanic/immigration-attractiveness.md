# Immigration by attractiveness

*Mechanic* · `immigration-attractiveness` · status: **sourced**

Population arrives or leaves based on attractiveness such as jobs, housing, and happiness relative to alternatives.

| field | value |
|---|---|
| aliases | migration, attractiveness, settler arrivals |
| family | Population & lineage |
| substrate | Aggregate stocks, Agent-based, Stochastic events |
| math basis | System dynamics / ODEs, Population dynamics |
| feedback | Balancing (negative) |
| player interface | Observation only, Placement |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Dwarf Fortress](../game/dwarf-fortress.md) |
| earliest year *(computed)* | 2006 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns an attractiveness score per settlement or region, computed from jobs, housing vacancy, wages or standard of living, services, happiness, and reputation, and a flow rule that turns the score difference against an outside reference or other regions into arrivals and departures per period. Arrivals usually need free housing, and departures follow sustained low scores. In Micropolis, the SimCity engine, residential migration rises and falls with employment, the ratio of jobs to residents. Victoria 3 moves pops within a market toward states with higher migration attraction, set mainly by standard of living, while migration laws filter who may move. RimWorld instead adds colonists through storyteller events such as wanderers joining. Inputs: jobs, housing, satisfaction, policy. Outputs: population inflow and outflow by type.

## Player Experience

The player grows population indirectly by making the place worth moving to, and loses it the same way. Growth feels earned and fragile: a housing shortage or unemployment spike shows up as people leaving.

## Design Levers

- factors in the attractiveness score and their weights
- reference point: a fixed outside world, competing regions, or other players
- flow elasticity per unit of score difference
- housing requirement and arrival batch size
- selectivity: which classes, cultures, or skills migrate, and policy filters

## Failure Modes

- Overshoot: migration responds fast to jobs, then unemployment spikes, then emigration, oscillating.
- Unconditional arrivals make population trivially easy and remove the planning puzzle.
- Opaque scores leave players unable to tell why people leave.
- Mass arrivals overwhelm services in one step and trigger cascades.

## Dynamics

- Growth raises demand for services and jobs, which lowers attractiveness until supply catches up, a balancing loop.
- Booms and busts as migration lags job creation.
- Inter-regional competition: improving one region drains its neighbors.

## Open Questions

- Can migration models calibrated to real census or survey data make city builders useful for planning education without hurting playability?
- How should attractiveness be explained so players can attribute departures to causes?

## Backlinks (computed)

**used by:** [Banished](../game/banished.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Victoria 3](../game/victoria-3.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)
- [Pops](../source/src-paradoxwikis-2026-vic3-pops.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
