# Request-provider logistics

*Mechanic* · `request-provider-logistics` · status: **sourced**

Containers declare per-item requests and supplies, and a dispatcher sends drones or robots from providers to requesters without fixed routes.

| field | value |
|---|---|
| aliases | logistic robots, logistics drones, logistic network, supply and demand stations |
| family | Logistics & networks |
| substrate | Network / graph, Rule system |
| math basis | Scheduling, Queueing theory |
| feedback | Balancing (negative) |
| player interface | Placement, Parameter |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 3 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Factorio](../game/factorio.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a set of logistic containers, each with a role (provider, requester, storage, buffer) and per-item request amounts or supply and demand settings, plus a fleet of carriers with speed, cargo size, and range or charge, and the stations that define coverage and recharge carriers. Each update the dispatcher computes open demand (requested minus held minus in transit), picks a provider holding the item by priority and distance, and assigns an idle carrier in coverage, which travels directly and delivers. Factorio roboports define logistic zones in which robots move items among active provider, passive provider, storage, buffer, and requester chests in priority order, carrying 1 item at 3 tiles per second before research. Dyson Sphere Program interstellar logistics stations set each item slot to local or remote supply, demand, or storage and send up to 100 drones within a planet and 10 vessels between planets, pairing stations by priority. Unlike conveyor-transport, the player routes nothing; unlike hauling-jobs, carriers are dedicated machines rather than agents with other work; unlike vehicle-route-scheduling, there are no order lists.

## Player Experience

Logistics stops being a layout puzzle and becomes a declaration of intent. The player sets what each chest wants and has, then watches a cloud of robots or a stream of vessels move goods, adding roboports, chargers, or carriers where the swarm thins out. It arrives as a late-game reward that dissolves earlier belt problems while creating new coverage and throughput ones.

## Design Levers

- carrier speed, cargo size, and energy or charging model, and how research upgrades them
- coverage model: roboport zones, station range sliders, or minimum trip distances
- container roles and the priority order among them
- request thresholds and minimum load settings that batch trips
- carrier count limits per station and the cost of each carrier
- unlock timing relative to belts and trains

## Failure Modes

- A cheap, unconstrained robot network makes belts and layout obsolete once unlocked, removing the earlier puzzle.
- Charging queues at a few stations leave swarms of idle carriers that are hard to diagnose.
- Large carrier counts become a late-game compute cost in very large factories.
- Priority rules that send carriers to distant providers when near ones exist make the network look broken.

## Dynamics

- Factories split into belt-fed bulk lines and robot-fed low-volume or mixed-item stations.
- Coverage gaps and charging capacity become the new bottleneck, so players build infrastructure for the carriers themselves.
- Supply and demand settings across planets or outposts produce hub-and-spoke shipping patterns no one drew.

## Open Questions

- Could learned dispatch policies cut idle trips and charging queues while staying predictable to players?
- How should a game show open requests, in-transit items, and carrier states so the network can be debugged at a glance?

## Backlinks (computed)

**used by:** [Dyson Sphere Program](../game/dyson-sphere-program.md), [Factorio](../game/factorio.md)

## Sources

- [Logistic network](../source/src-factoriowiki-2026-logistic-network.md)
- [Interstellar Logistics Station](../source/src-dspwiki-2026-interstellar-logistics-station.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
