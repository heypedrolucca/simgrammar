# Rail signaling

*Mechanic* · `rail-signaling` · status: **sourced**

Block and path signals partition track so trains can share it without collision; throughput depends on signal design.

| field | value |
|---|---|
| aliases | train signals, block signals, path signals |
| family | Logistics & networks |
| substrate | Network / graph, Rule system |
| math basis | Scheduling, Graph search |
| feedback | None |
| player interface | Placement |
| legibility | 2 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Railroad Tycoon](../game/railroad-tycoon.md) |
| earliest year *(computed)* | 1990 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Signals placed on track divide it into blocks or guard reservable paths. A block signal admits a train only if the next block, meaning all track reachable up to the next signal, is empty. A path signal admits a train once it reserves a route through to the next signal, so trains on non-conflicting paths can share a block. Transport Tycoon (1994) had only bi-directional block signals, and Deluxe added one-way signals. OpenTTD adds pre-signals, where an entry signal opens only if an exit is green, plus path signals, and since version 12 shows only path signals by default. Factorio pairs rail signals with chain signals that mirror the state of the signals ahead. Inputs: signal placement, train positions and routes. Outputs: per-signal open or closed states, train waits, and network throughput.

## Player Experience

Traffic engineering on rails. Players learn why trains stop, then redesign junctions, stations, and signal spacing until flow is smooth. Deadlocks, with trains frozen in a loop that blocks itself, are a vivid and instructive failure, and fixing one is a satisfying puzzle.

## Design Levers

- available signal types: block, one-way, pre-signal, path, or chain
- default signal behavior and which types are exposed to new players
- train braking distance and the resulting minimum signal spacing
- whether trains reroute around blocked paths
- visual debugging aids such as block coloring and reservation display

## Failure Modes

- Rules learned mainly from community guides, such as Factorio's chain-in, rail-out convention, block new players.
- Deadlocks that occur long after a junction is built are hard to trace.
- Block signals that are too coarse cut throughput, and pre-signal logic can trigger on exits a train cannot reach.

## Dynamics

- Junction design becomes a shared craft, and community blueprints of standard intersections spread.
- Throughput limits push players toward one-way double track and dedicated stations.
- Adding trains raises throughput until signal capacity binds, after which waits and gridlock grow quickly.

## Open Questions

- Can an assistant explain a specific deadlock in plain language from the signal states, removing the wiki dependency?
- What minimal signal vocabulary still supports high-throughput designs?

## Relations

**synergy**

- [Signal circuits](../mechanic/signal-circuits.md): Circuit-controlled train stops and signals turn logistics into programmable dispatch.

## Backlinks (computed)

**used by:** [Factorio](../game/factorio.md), [Railroad Tycoon](../game/railroad-tycoon.md), [Satisfactory](../game/satisfactory.md), [Transport Tycoon](../game/transport-tycoon.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Why we recommend Path Signals](../source/src-openttd-2021-path-signals.md)
- [Manual/Signals](../source/src-openttd-2026-manual-signals.md)
- [Transport Tycoon](../source/src-wikipedia-transport-tycoon.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
