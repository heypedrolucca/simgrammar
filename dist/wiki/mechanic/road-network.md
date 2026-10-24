# Road networks

*Mechanic* · `road-network` · status: **sourced**

Roads and paths define connectivity; buildings must connect to function, and travel cost depends on network geometry.

| field | value |
|---|---|
| aliases | roads, path network, connectivity |
| family | Logistics & networks |
| substrate | Network / graph, Cellular grid |
| math basis | Graph search, Network flow |
| feedback | None |
| player interface | Placement |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Could procedural road generation that follows terrain and demand make player road-drawing optional without losing authorship? |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Sid Meier's Civilization](../game/civilization.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Road tiles or segments form a graph whose nodes are intersections and building access points. Each building checks for a road connection; unconnected buildings do not function, grow, or receive services. Travel along the graph has a cost per segment set by road type, speed limit, and length, used by pathfinding and trip generation. In Micropolis, the released SimCity engine, a zone scans its perimeter for a road; if none exists the traffic test fails and residential and commercial zones shrink. Caesar III walkers move only on roads, so road shape determines service coverage. Cities: Skylines adds a road hierarchy with lanes and capacities. Banished treats roads as a speed boost rather than a requirement. Inputs: player-placed road segments. Outputs: connectivity per building and travel costs between points.

## Player Experience

Drawing the city's skeleton. Players lay roads first and fill blocks after, so road layout fixes later possibilities. Disconnected buildings are an immediate, readable failure, while inefficient geometry shows up slowly as long trips and congestion.

## Design Levers

- whether connection is required or only speeds movement
- road types with different speeds, capacities, and costs
- placement freedom: grid-locked, free curves, or segments
- intersection rules and traffic controls
- cost per segment and upkeep

## Failure Modes

- Grid-only placement makes every city look the same.
- Free placement without snapping guides makes clean layouts hard.
- Dead-end tolerance that is too forgiving removes any layout pressure.

## Dynamics

- Road layout determines which areas are reachable and therefore where growth happens.
- Hierarchies of arterials and local streets emerge under congestion pressure.
- Coupled with walker or coverage systems, road shape becomes a service-distribution tool.

## Open Questions

- Could procedural road generation that follows terrain and demand make player road-drawing optional without losing authorship?

## Backlinks (computed)

**required by:** [Traffic congestion](../mechanic/traffic-congestion.md), [Walker service delivery](../mechanic/walker-service-delivery.md)

**used by:** [Anno 117: Pax Romana](../game/anno-117.md), [Caesar III](../game/caesar-3.md), [Cities: Skylines](../game/cities-skylines.md), [Sid Meier's Civilization](../game/civilization.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md), [Manor Lords](../game/manor-lords.md), [Transport Tycoon](../game/transport-tycoon.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)
- [Caesar III](../source/src-wikipedia-caesar-iii.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
