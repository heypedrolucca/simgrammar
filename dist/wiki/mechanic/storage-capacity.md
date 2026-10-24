# Storage and buffers

*Mechanic* · `storage-capacity` · status: **sourced**

Goods occupy finite storage; buffers decouple producers from consumers, and full storage blocks production.

| field | value |
|---|---|
| aliases | buffers, warehouses, inventory limits, stockpiles |
| family | Resources & production |
| substrate | Aggregate stocks, Rule system |
| math basis | Queueing theory, System dynamics / ODEs |
| feedback | Balancing (negative) |
| player interface | Placement, Parameter, Observation only |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 1 |
| maturity | Classic |
| open questions | Can automatic buffer sizing advisors teach players about backpressure without solving the layout for them? |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Factorio](../game/factorio.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 9 |
| prevalence share *(computed)* | 0.052 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Storage containers, warehouses, stockpile zones, and machine input or output slots each hold a capacity measured in units, stacks, slots, or volume. Producers push into storage until it is full, then stall; consumers pull from it until it is empty, then starve. Between those limits, buffer level absorbs mismatches in timing. Factorio chests have fixed slot counts and machines hold small input and output buffers; RimWorld stockpile zones accept filtered items in priority order (low, normal, preferred, important, critical) and haulers move items toward higher-priority zones with space; Anno caps each good at an island-wide storage limit that warehouses raise; GlassBox in SimCity (2013) stores everything in capacity-limited resource bins, such as a house holding 20 of 30 food and 4 of 10 people. Inputs: incoming and outgoing flows. Outputs: stock level and full or empty states that gate adjacent processes.

## Player Experience

Buffers give breathing room and hide problems. Players size storage to survive supply gaps, then discover that a full warehouse has silently stopped a production line. Organizing what goes where becomes its own small design task.

## Design Levers

- capacity per container and whether it is per good, per slot, or shared
- filters and priorities that decide what goes where
- behavior when full: stall, overflow to the ground, or discard
- local buffers on machines versus central warehouses
- storage cost in space, money, or construction

## Failure Modes

- Very large storage hides every imbalance, so production ratios never matter.
- Tiny buffers make chains brittle and turn play into constant stop-and-go.
- Full storage stalls without alerts make the cause invisible.

## Dynamics

- Buffers absorb shocks such as raids, winters, and broken links, trading space for resilience.
- Full buffers propagate backpressure upstream, so one blocked output can stop an entire chain.
- Coupled with spoilage, storage becomes a liability instead of a safe stockpile.
- Players build overflow sinks or priority splits so critical chains never block.

## Open Questions

- Can automatic buffer sizing advisors teach players about backpressure without solving the layout for them?

## Backlinks (computed)

**involved in:** [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Weather-coupled energy grids](../opportunity/weather-coupled-grids.md)

**used by:** [Anno 1800](../game/anno-1800.md), [Banished](../game/banished.md), [Big Ambitions](../game/big-ambitions.md), [Captain of Industry](../game/captain-of-industry.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Factorio](../game/factorio.md), [Satisfactory](../game/satisfactory.md), [Timberborn](../game/timberborn.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Stockpile](../source/src-rimworldwiki-2026-stockpile.md)
- [GDC 2012: Breaking down SimCity's Glassbox engine](../source/src-cifaldi-2012-glassbox-engine.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
