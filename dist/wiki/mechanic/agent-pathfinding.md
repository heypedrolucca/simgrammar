# Agent pathfinding

*Mechanic* · `agent-pathfinding` · status: **sourced**

Agents compute routes through space using movement costs, and the routes they choose shape congestion, travel time, and access.

| field | value |
|---|---|
| aliases | pathing, navigation, route finding |
| family | Agents & behavior |
| substrate | Network / graph, Cellular grid, Agent-based |
| math basis | Graph search, Network flow |
| feedback | None |
| player interface | Placement, Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 3 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [SimTower](../game/simtower.md) |
| earliest year *(computed)* | 1994 |
| prevalence *(computed)* | 9 |
| prevalence share *(computed)* | 0.052 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 4 |
| technique exposure *(computed)* | 1.25 |

## Definition

Owns a traversal representation (tile grid, navmesh, or waypoint graph) with per-cell or per-edge movement costs and permissions, plus each agent's current path or a shared direction field. On request a search returns a least-cost route from position to goal; A* (Hart, Nilsson, and Raphael, 1968) expands nodes by cost so far plus an admissible heuristic. Paths are invalidated and recomputed when the map changes or agents block each other. Scale variants trade exactness for speed: Factorio (2019) abstracts each 32x32 chunk into terrain components and runs a reverse resumable A* over them to supply the heuristic for tile-level A*; Supreme Commander 2 searches a portal graph between 10x10 m sectors and shares flow fields so many units read one direction field instead of each searching. Inputs: terrain and floor costs, doors and allowed areas, other agents. Outputs: routes, travel times, and occupancy along routes that feed hauling, traffic, and defense.

## Player Experience

The player notices pathfinding mostly through layout: where doors, stockpiles, and roads go decides how far agents walk. In defense play the player builds mazes that lengthen enemy routes; in colony sims the player winces as a colonist crosses the map for one item. Failures are visible and comic, so players learn the cost model by watching.

## Design Levers

- movement cost per terrain, floor, road, or door type
- search method and hierarchy (grid A*, navmesh, hierarchical abstraction, flow fields) and per-tick search budget
- repath triggers and frequency when the map or obstacles change
- local avoidance between agents (none, steering, reservation) versus passing through each other
- agent map knowledge and permissions (full map, explored only, allowed areas, locked doors)

## Failure Modes

- Agents take absurd detours or get stuck because the cost model or permissions disagree with what the player sees on screen.
- Repathing storms after map edits become a late-game slowdown on large colony and factory maps.
- Per-unit paths ignore other units and stall at chokepoints; Emerson describes Supreme Commander 2's earlier single-path system compounding collisions into stops.
- Deterministic pathing invites exploits such as mazes and wall-hugging layouts that trivialize threats.

## Dynamics

- Shortest-path choices concentrate trips on a few links, producing congestion that lowers throughput without any explicit traffic rule.
- Defenders shape attacker routes with walls and gaps, so layout itself becomes the defense mechanic.
- Travel time silently becomes the largest work cost, so compact bases and well-placed stockpiles dominate efficiency.

## Open Questions

- Can learned crowd models or mean-field approximations replace per-agent search at city scale while preserving individual route choices?
- How much should paths reflect imperfect knowledge and preferences such as scenery or safety rather than shortest cost?

## Backlinks (computed)

**affected by:** [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md), [Agent-based automated playtesting and balancing](../technique/automated-playtesting.md), [Deep reinforcement learning policies for NPC opponents and navigation](../technique/deep-rl-npc-policies.md), [Mean field games and mean-field learning](../technique/mean-field-games.md)

**involved in:** [Mean-field crowds and traffic](../opportunity/mean-field-crowds.md)

**required by:** [Hauling jobs](../mechanic/hauling-jobs.md)

**used by:** [Cities: Skylines](../game/cities-skylines.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Mini Metro](../game/mini-metro.md), [Prison Architect](../game/prison-architect.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Screeps](../game/screeps.md), [SimCity (2013)](../game/simcity-2013.md), [SimTower](../game/simtower.md), [Songs of Syx](../game/songs-of-syx.md)

## Sources

- [A Formal Basis for the Heuristic Determination of Minimum Cost Paths](../source/src-hart-1968-astar.md)
- [Friday Facts #317 - New pathfinding algorithm](../source/src-wube-2019-fff-317-pathfinding.md)
- [Crowd Pathfinding and Steering Using Flow Field Tiles](../source/src-emerson-2013-flow-field-tiles.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
