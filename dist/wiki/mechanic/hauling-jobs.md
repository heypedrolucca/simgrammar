# Hauling jobs

*Mechanic* · `hauling-jobs` · status: **sourced**

Agents pick up and carry items between locations via a job queue, making hauling capacity a hidden throughput constraint.

| field | value |
|---|---|
| aliases | hauling, carrying jobs, item transport by agents |
| family | Logistics & networks |
| substrate | Agent-based, Rule system |
| math basis | Scheduling, Queueing theory, Graph search |
| feedback | Balancing (negative) |
| player interface | Parameter, Orders, Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| requires | [Agent pathfinding](../mechanic/agent-pathfinding.md) |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Dwarf Fortress](../game/dwarf-fortress.md) |
| earliest year *(computed)* | 2006 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.1 |

## Definition

Items on the ground or in the wrong storage generate hauling jobs that name a source item and a destination with space. Idle agents with hauling enabled pick jobs by priority and distance, path to the item, carry up to their capacity, and deliver. Throughput is bounded by the number of haulers, walking distance, carry capacity, and competing work. RimWorld haulers move items to the highest-priority stockpile with space, even out of lower-priority stockpiles; Dwarf Fortress splits hauling into labors for stone, wood, food, refuse, and furniture; The Settlers passes every good from flag to flag along roads, with one carrier per road segment; Banished and Timberborn rely on laborers or haulers whose numbers set delivery speed. Inputs: item locations, destinations, agent availability. Outputs: item movement and a job backlog.

## Player Experience

Watching the colony carry its own weight. Players notice that new production does not help when no one is free to carry it, then shorten distances, build local stockpiles, or assign more haulers. The constraint is visible on screen as piles of goods and idle workbenches.

## Design Levers

- carry capacity per agent and the effect of tools such as wheelbarrows or carts
- job selection rules: priority, distance, or reservation
- how many agents haul and whether hauling is a separate role
- stockpile priorities and filters that generate jobs
- whether production buildings have local storage or need pickup

## Failure Modes

- Hauling backlogs are hard to diagnose because the bottleneck is spread across many agents.
- Item ping-pong between stockpiles with similar priorities wastes agent time.
- Agents abandoning urgent work to haul low-value items reads as AI stupidity.

## Dynamics

- Distance between production and storage becomes a hidden cost, rewarding compact layouts.
- Hauling competes with every other job, so labor shortages appear as slowdowns everywhere at once.
- Coupled with needs, haulers take breaks, creating rhythmic dips in throughput.

## Open Questions

- Could learned job dispatch reduce visible AI stupidity while keeping hauling a resource the player manages?
- How should backlogs be visualized so players can find the true constraint?

## Relations

**requires**

- [Agent pathfinding](../mechanic/agent-pathfinding.md)

**synergy**

- [Storage and buffers](../mechanic/storage-capacity.md): Where stockpiles sit determines how much hauling labor the colony spends.

## Backlinks (computed)

**affected by:** [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md)

**involved in:** [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md)

**used by:** [Banished](../game/banished.md), [Captain of Industry](../game/captain-of-industry.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Surviving Mars](../game/surviving-mars.md), [Timberborn](../game/timberborn.md)

## Sources

- [Stockpile](../source/src-rimworldwiki-2026-stockpile.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
