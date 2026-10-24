# Designation orders

*Mechanic* · `designation-orders` · status: **asserted**

The player marks tiles or objects for work such as dig, chop, or build, and autonomous agents claim and execute the jobs.

| field | value |
|---|---|
| aliases | designations, job designations, work orders, zones of work |
| family | Control & automation |
| substrate | Rule system, Agent-based, Cellular grid |
| math basis | Scheduling, Graph search |
| feedback | None |
| player interface | Orders, Placement |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Dwarf Fortress](../game/dwarf-fortress.md) |
| earliest year *(computed)* | 2006 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

The player paints a designation onto tiles or objects (mine, chop, harvest, build, haul, deconstruct, hunt) instead of commanding a specific agent. Each designation creates a job entry with location, type, required skill or tool, and priority. Agents that are free and allowed to do that work query the job pool, score candidate jobs by priority, distance, and reachability, reserve one, path to it, and execute it; the designation clears on completion. State owned: the set of designations and their job entries and reservations. Inputs: player marks; outputs: jobs consumed by agent action selection. Canonical forms: Dwarf Fortress dig, chop, and gather designations, RimWorld mine, cut, haul, and deconstruct designations, Oxygen Not Included errands with 1 to 9 priorities, Dungeon Keeper digging, and Going Medieval.

## Player Experience

The player states what should happen and watches agents figure out who and how. Painting a mine and seeing dwarves converge on it feels like management rather than puppetry, and the gap between intent and execution, such as a dwarf walking across the map for one job, becomes a source of frustration and stories.

## Design Levers

- per-designation priority levels
- job claiming: nearest agent, best-skilled agent, or first free
- reservation and timeout rules for unreachable or abandoned jobs
- area painting tools versus per-object marking
- whether designations wait on prerequisites (materials, tools) or fail immediately
- interaction with per-agent work priorities and restrictions

## Failure Modes

- Unreachable designations jam the queue and agents repeatedly attempt and abandon them.
- Agents cross the whole map for a single low-value job because claiming ignores travel cost.
- Large designations starve critical work such as feeding and hauling without clear priority overrides.
- Players cannot see why a designation is not being worked: no one allowed, no path, or no materials.

## Dynamics

- Throughput depends on agent count, travel, and hauling, so mass designation exposes logistics bottlenecks.
- Accidental designations produce stories, such as mining into an aquifer or magma.
- Order of designation becomes a planning skill, since agents take jobs in the order the claiming rule finds them.

## Open Questions

- Can players state work goals in language (dig a three-room hall near the stockpile) and have a model translate them into designations reliably?
- Which claiming rule best balances efficiency with legible agent behavior?

## Relations

**synergy**

- [Hauling jobs](../mechanic/hauling-jobs.md): Designated work creates items that must be hauled, chaining jobs.

## Backlinks (computed)

**involved in:** [Intent-level orders](../opportunity/intent-level-orders.md)

**used by:** [Captain of Industry](../game/captain-of-industry.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Going Medieval](../game/going-medieval.md), [Oxygen Not Included](../game/oxygen-not-included.md), [RimWorld](../game/rimworld.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
