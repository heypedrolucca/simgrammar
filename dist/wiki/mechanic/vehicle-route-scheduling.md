# Vehicle routes and schedules

*Mechanic* · `vehicle-route-scheduling` · status: **sourced**

Vehicles are assigned ordered stops with load and unload rules to move goods or passengers between nodes.

| field | value |
|---|---|
| aliases | vehicle orders, routes, timetables, train schedules |
| family | Logistics & networks |
| substrate | Agent-based, Rule system, Network / graph |
| math basis | Scheduling, Optimization |
| feedback | None |
| player interface | Orders, Parameter |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Could natural-language order entry ("keep this mine's output moving to the steel mill") replace order lists without losing player control? |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Railroad Tycoon](../game/railroad-tycoon.md) |
| earliest year *(computed)* | 1990 |
| prevalence *(computed)* | 10 |
| prevalence share *(computed)* | 0.057 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.1 |

## Definition

Each vehicle holds an order list: an ordered sequence of stops, each with load and unload rules and optional wait conditions. The vehicle travels to each stop in turn, applies its rules, and continues. OpenTTD offers full load of any or all cargo, unload, transfer with partial payment for feeder services, no loading, go-via waypoints, timetables, conditional jumps, and shared orders across vehicles. Transport Tycoon pays by delivery time, distance, and quantity, so mail must be fast while coal tolerates long routes. Factorio train schedules use wait conditions such as full cargo, inactivity, or circuit signals. Inputs: orders, vehicles, cargo at stops. Outputs: cargo movement, revenue, and station service frequency.

## Player Experience

Programming a fleet. Players design routes, tune load rules, and watch vehicles run. Well-tuned routes make money unattended; badly tuned ones leave vehicles waiting at empty stations.

## Design Levers

- available order types and wait conditions
- payment model by distance, time, and cargo type
- shared orders and fleet management tools
- vehicle capacity, speed, and reliability
- station ratings that respond to service frequency

## Failure Modes

- Full-load orders at low-supply stations park vehicles forever.
- Complex order systems without templates make fleet changes tedious.
- Revenue models that ignore time make every route identical.

## Dynamics

- Feeder and trunk networks emerge from transfer orders.
- Station competition between companies or players shifts cargo flows.
- Fleet growth eventually saturates track or roads, coupling routing to signaling and congestion.

## Open Questions

- Could natural-language order entry ("keep this mine's output moving to the steel mill") replace order lists without losing player control?

## Backlinks (computed)

**affected by:** [LLM-guided evolutionary program search](../technique/alphaevolve-algorithm-discovery.md)

**generalizes:** [Public transit lines](../mechanic/public-transit.md)

**used by:** [Anno 117: Pax Romana](../game/anno-117.md), [Anno 1800](../game/anno-1800.md), [Big Ambitions](../game/big-ambitions.md), [Captain of Industry](../game/captain-of-industry.md), [Factorio](../game/factorio.md), [Railroad Tycoon](../game/railroad-tycoon.md), [Satisfactory](../game/satisfactory.md), [shapez 2](../game/shapez-2.md), [Transport Tycoon](../game/transport-tycoon.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Manual/Orders](../source/src-openttd-2026-manual-orders.md)
- [Transport Tycoon](../source/src-wikipedia-transport-tycoon.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
