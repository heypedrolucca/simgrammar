# Songs of Syx

*Game* · `songs-of-syx` · status: **sourced**

A low-fantasy city builder in which tens of thousands of individually simulated citizens and slaves of several races live in a growing city-state whose armies of up to 50,000 units fight real-time battles.

| field | value |
|---|---|
| year | 2020 |
| developer | Gamatron AB |
| platforms | PC |
| subgenre | City builder |
| subgenre secondary | Grand strategy |
| sim domain | Urban, Military / conflict, Political / governance |
| player role | Ruler / statesman |
| agency model | Zoning / placement, Policy / parameter, Direct unit control |
| time model | Real-time with pause |
| sim scale | City |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | 10,000+ |
| emergence | 3 |
| influence | 1 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 9 |

## Summary

A low-fantasy city builder in which tens of thousands of individually simulated citizens and slaves of several races live in a growing city-state whose armies of up to 50,000 units fight real-time battles.

## Core Loop

lay out houses, streets, and workshops -> tens of thousands of citizens and slaves work, worship, and seek their desires -> appoint nobles to run the realm -> supply and train armies -> fight real-time battles -> trade, ally, or conquer neighboring kingdoms

## Design Notes

Songs of Syx scales individual simulation to city size: each of tens of thousands of citizens and slaves has a race, religion, fears, and desires, and each soldier in battles of up to 50,000 units needs supplies. Nobles can be appointed or imported to manage the kingdom but may try to usurp the player. The game has been in early access since September 2020 with no fixed 1.0 date.

## Relations

**uses**

- [Population strata](../mechanic/population-strata.md) (core): Citizens and slaves of several races, each with distinct needs, religion, and roles.
- [Unit commands](../mechanic/unit-commands.md) (core): Real-time battles of up to 50,000 individual units commanded by the player.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Each citizen's needs and desires drive behavior.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (supporting): Tens of thousands of agents path through streets to work and services.
- [Supply lines](../mechanic/supply-lines.md) (supporting): Every soldier must be supplied.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Alliances, trade, and war with other kingdoms.
- [Trade routes](../mechanic/trade-routes.md) (supporting)
- [Production chains](../mechanic/production-chain.md) (supporting)
- [Stability and unrest](../mechanic/stability-unrest.md) (supporting): Appointed nobles may try to usurp the ruler.

## Sources

- [Songs of Syx on Steam](../source/src-steam-2026-songs-of-syx.md)

---
Provenance: created in run `2026-10-24-catalog-ga`.
