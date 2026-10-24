# Wear and breakdown

*Mechanic* · `wear-breakdown` · status: **sourced**

Assets lose condition with use and age, breakdown risk rises as condition falls, and maintenance or repair restores it.

| field | value |
|---|---|
| aliases | reliability, maintenance, durability |
| family | Risk & failure |
| substrate | Aggregate stocks, Stochastic events, Agent-based |
| math basis | Markov / stochastic processes, Queueing theory, System dynamics / ODEs |
| feedback | Both |
| player interface | Parameter, Orders |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Theme Park](../game/theme-park.md) |
| earliest year *(computed)* | 1994 |
| prevalence *(computed)* | 20 |
| prevalence share *(computed)* | 0.115 |
| subgenre spread *(computed)* | 11 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each asset holds a condition or reliability stock. Each update it decays by a base rate scaled by usage, age, and environment, and a breakdown is drawn with probability that rises as condition falls. A broken asset stops or malfunctions until a repair job, often done by a maintenance agent, restores it. In RollerCoaster Tycoon 2 (as reimplemented in OpenRCT2), reliability starts at 100% and drops every 256 ticks by the ride's unreliability factor plus an age penalty that grows from one-eighth of that factor in year one to double after eight years; breakdown types are weighted, brake failure is likelier in rain, players set inspection intervals for mechanics, and a repair restores reliability in proportion to the deficit. Transport Tycoon vehicles lose reliability between depot services; Theme Hospital machines explode if handymen do not repair them. Per-use item durability, as in Minecraft tools, is a variant without maintenance.

## Player Experience

A steady background of upkeep decisions. The player schedules inspections, staffs mechanics, and decides when an aging asset should be replaced instead of repaired. Breakdowns are visible interruptions with queues of angry customers or stalled trains.

## Design Levers

- decay rate per asset class and its usage and weather modifiers
- age penalty curve that forces eventual replacement
- breakdown probability as a function of condition, and the menu of breakdown types and severities
- maintenance interval, labor required, and repair restoration amount
- repair versus replacement cost
- a global breakdown setting (off, reduced, normal)

## Failure Modes

- Maintenance with no tradeoffs becomes a chore; OpenTTD exposes a setting to reduce or disable breakdowns, and many players use it.
- Too few maintenance workers lets breakdowns pile up faster than repairs, a spiral that is hard to diagnose.
- Hidden condition values make breakdowns feel random even when the player could have prevented them.

## Dynamics

- Aging fleets and rides create replacement waves that strain budgets years after the original build-out.
- Mechanic coverage becomes a routing and staffing problem coupled to park or network layout.
- Breakdowns create service queues and satisfaction drops that spread to nearby systems.

## Open Questions

- Can predictive maintenance tools that forecast failure from condition history become part of play instead of a hidden optimization?
- When does per-use durability add decisions rather than inventory chores?

## Backlinks (computed)

**used by:** [Aurora 4X](../game/aurora-4x.md), [Caesar III](../game/caesar-3.md), [Captain of Industry](../game/captain-of-industry.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md), [Farming Simulator 25](../game/farming-simulator-25.md), [iRacing](../game/iracing.md), [Motorsport Manager](../game/motorsport-manager.md), [Planet Coaster](../game/planet-coaster.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Screeps](../game/screeps.md), [SnowRunner](../game/snowrunner.md), [Surviving Mars](../game/surviving-mars.md), [The Long Dark](../game/the-long-dark.md), [Theme Hospital](../game/theme-hospital.md), [Theme Park](../game/theme-park.md), [Transport Tycoon](../game/transport-tycoon.md), [Two Point Hospital](../game/two-point-hospital.md), [Valheim](../game/valheim.md), [The Legend of Zelda: Breath of the Wild](../game/zelda-breath-of-the-wild.md), [Zoo Tycoon](../game/zoo-tycoon.md)

## Sources

- [OpenRCT2 source: Ride.cpp (ride reliability, inspection, and breakdowns)](../source/src-openrct2-2026-ride-breakdowns.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
