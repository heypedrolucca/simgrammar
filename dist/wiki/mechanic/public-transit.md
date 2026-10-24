# Public transit lines

*Mechanic* · `public-transit` · status: **sourced**

Player-drawn lines with stops and vehicles carry passengers whose ridership depends on coverage, frequency, and transfers.

| field | value |
|---|---|
| aliases | transit lines, metro lines, bus lines |
| family | Logistics & networks |
| substrate | Network / graph, Agent-based |
| math basis | Network flow, Queueing theory, Graph search |
| feedback | Both |
| player interface | Placement, Parameter |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 3 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| specializes | [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md) |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [SimCity 4](../game/simcity-4.md) |
| earliest year *(computed)* | 2003 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

The player defines lines as ordered stop sequences and assigns vehicles with a capacity. Passengers spawn with origins and destinations and choose a route that may include transfers; vehicles load at stops up to capacity and unload at destinations. Ridership depends on stop catchment, frequency (vehicles per line), transfer penalties, and travel time compared with other modes. Mini Metro spawns passengers as shapes that travel to any station of a matching shape, lets about six wait before a station overcrowds, ends the game when a station stays overcrowded too long, and hands out new rolling stock weekly. Cities: Skylines II citizens weigh transit against driving and walking using travel time, comfort, and money costs. Inputs: lines, vehicles, passenger demand. Outputs: ridership, waiting times, overcrowding, and changes in mode share.

## Player Experience

Network design with immediate feedback. Players draw a line, watch riders pile up or flow, and redraw. Good transfer points and frequency matter more than raw coverage, and in Mini Metro the game is about deciding which stations can wait.

## Design Levers

- vehicle capacity and count per line
- passenger route choice model: matching shapes, shortest time, or utility with transfer penalties
- stop capacity and overcrowding consequences
- line constraints such as river crossings, line count, or budget
- fares, subsidies, and operating costs

## Failure Modes

- Passengers taking implausible routes because the route-choice model ignores transfer cost.
- Lines that run full or empty without explanation because demand is hidden.
- In city builders, transit that cannot reduce traffic because citizens' mode choice is too sticky.

## Dynamics

- Hub-and-spoke versus grid patterns emerge from transfer penalties.
- New lines shift demand rather than add it, moving overcrowding elsewhere.
- Coupled with land value and zoning, stations attract density, which raises ridership further.

## Open Questions

- Can agent route choice that is learned from real transit data be made legible enough for players to design against?
- What is the minimal passenger model that still punishes bad transfer design?

## Relations

**specializes**

- [Vehicle routes and schedules](../mechanic/vehicle-route-scheduling.md)

**synergy**

- [Traffic congestion](../mechanic/traffic-congestion.md): Transit is the relief valve for congestion; congestion is what makes transit worth building.

## Backlinks (computed)

**involved in:** [Mean-field crowds and traffic](../opportunity/mean-field-crowds.md)

**used by:** [Cities: Skylines](../game/cities-skylines.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Mini Metro](../game/mini-metro.md), [SimCity 4](../game/simcity-4.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Mini Metro (video game)](../source/src-wikipedia-mini-metro.md)
- [Cities: Skylines II Feature Highlight #2: Traffic AI](../source/src-paradox-2023-cs2-traffic-ai.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
