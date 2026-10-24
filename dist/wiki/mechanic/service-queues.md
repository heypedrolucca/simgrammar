# Service queues

*Mechanic* · `service-queues` · status: **asserted**

Agents wait in lines for limited-capacity services; waiting time feeds back into satisfaction and throughput.

| field | value |
|---|---|
| aliases | queues, waiting lines, queue lines |
| family | Logistics & networks |
| substrate | Agent-based, Rule system |
| math basis | Queueing theory |
| feedback | Balancing (negative) |
| player interface | Placement, Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Could generative agents with learned patience models make queues produce more varied and memorable behavior? |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [SimTower](../game/simtower.md) |
| earliest year *(computed)* | 1994 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Each service point (a ride, a clinic room, a checkout) has a service rate and a queue of waiting agents. Arriving agents join if the queue is not too long by their own tolerance; while waiting, their needs keep decaying and their satisfaction falls with waiting time; served agents leave and free the slot. RollerCoaster Tycoon builds explicit queue paths for rides, and guests think aloud about long waits. Theme Hospital and Two Point Hospital queue patients outside rooms; while they wait their health keeps falling, so long queues produce departures and deaths that lower the hospital's reputation. Inputs: arrival rate, service rate, capacity, tolerance. Outputs: queue length, waiting times, and satisfaction changes.

## Player Experience

Visible lines are an instant read on capacity. Players add service points, lengthen or shorten queue paths, and redistribute demand, learning from the line itself where the bottleneck is.

## Design Levers

- service rate per point and number of parallel points
- queue capacity and agents' tolerance before they balk or leave
- satisfaction decay while waiting
- queue discipline: first-in-first-out, priority, or player reordering
- information shown about wait times

## Failure Modes

- Fixed tolerance across all agents makes queues predictable and dull.
- Queues that grow without bound because agents never leave freeze the simulation.
- Invisible queues inside buildings hide the bottleneck.

## Dynamics

- Utilization near 100% causes waiting times to explode, the core queueing-theory result, so players learn to keep slack.
- Coupled with needs decay, long waits create secondary demand at food and toilet facilities.
- Demand shifts toward shorter queues, balancing load across service points.

## Open Questions

- Could generative agents with learned patience models make queues produce more varied and memorable behavior?

## Backlinks (computed)

**affected by:** [Mean field games and mean-field learning](../technique/mean-field-games.md)

**involved in:** [Mean-field crowds and traffic](../opportunity/mean-field-crowds.md)

**used by:** [Mini Metro](../game/mini-metro.md), [Project Hospital](../game/project-hospital.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [SimTower](../game/simtower.md), [Theme Hospital](../game/theme-hospital.md), [Theme Park](../game/theme-park.md), [Two Point Hospital](../game/two-point-hospital.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
