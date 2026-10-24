# Spoilage

*Mechanic* · `spoilage` · status: **sourced**

Perishable goods lose value or rot over time depending on storage conditions such as temperature and containers.

| field | value |
|---|---|
| aliases | perishables, food rot, freshness |
| family | Resources & production |
| substrate | Aggregate stocks, Rule system |
| math basis | System dynamics / ODEs |
| feedback | Balancing (negative) |
| player interface | Observation only, Placement |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 1 |
| maturity | Established |
| open questions | What spoil-time distribution across goods produces interesting routing without making long chains infeasible? |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Hamurabi](../game/hamurabi.md) |
| earliest year *(computed)* | 1968 |
| prevalence *(computed)* | 10 |
| prevalence share *(computed)* | 0.057 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each perishable item or stack carries a freshness value or age that advances each tick at a rate set by item type and storage conditions; at a threshold it becomes rotten, converts into a spoiled item, or is destroyed. RimWorld stops rot for food kept at or below 0 C, so walk-in freezers are standard; Don't Starve moves food from fresh to stale to spoiled and finally to rot, with ice boxes slowing the clock; Factorio: Space Age gives biological items spoil times from about two hours down to a few minutes, cannot be delayed, turns spoiled items into Spoilage, and passes ingredient freshness on to recipe outputs. Inputs: item type, time, storage environment. Outputs: current freshness, value or effect scaling, and spoil events.

## Player Experience

A clock on every stockpile. Players stop hoarding and start thinking in flow: produce close to consumption, build cold storage, preserve food, or accept waste. Opening a storeroom to find a harvest rotted is a sharp, memorable loss.

## Design Levers

- spoil time per item type
- storage modifiers such as temperature, containers, and preservation methods
- whether freshness is binary (fresh or rotten) or continuous and scales value
- what spoiled goods become: nothing, a waste item, or a useful input such as fertilizer
- freshness inheritance across recipes

## Failure Modes

- Spoilage that is cheap to stop, such as one freezer that halts all decay, becomes a one-time build tax.
- Short spoil times on items with long logistics routes make some chains impossible without explanation.
- Hidden freshness values make sudden losses feel unfair.

## Dynamics

- Shifts optimal play from stockpiling to just-in-time throughput; Factorio's developers state that buffering is not helpful under spoilage.
- Cold storage couples food to power and temperature systems, so a power failure becomes a famine risk.
- Seasonal harvests plus spoilage create a winter preservation problem.
- Freshness-priority handling (pick freshest or oldest first) creates new logistics rules.

## Open Questions

- What spoil-time distribution across goods produces interesting routing without making long chains infeasible?

## Relations

**synergy**

- [Storage and buffers](../mechanic/storage-capacity.md): Storage conditions decide spoilage rates, making cold storage valuable.

## Backlinks (computed)

**used by:** [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Don't Starve](../game/dont-starve.md), [Factorio](../game/factorio.md), [Going Medieval](../game/going-medieval.md), [Hamurabi](../game/hamurabi.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Project Zomboid](../game/project-zomboid.md), [RimWorld](../game/rimworld.md), [Subnautica](../game/subnautica.md), [The Long Dark](../game/the-long-dark.md)

## Sources

- [Friday Facts #414 - Spoils of Agriculture](../source/src-wube-2024-fff-414-spoils-of-agriculture.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
