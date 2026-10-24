# SimTower

*Game* · `simtower` · status: **sourced**

A skyscraper management game in which the player stacks offices, condos, hotels, and shops and designs elevator service so tenants on daily routines do not wait long enough to stress out and leave.

| field | value |
|---|---|
| aliases | The Tower |
| year | 1994 |
| developer | OPeNBooK (Yoot Saito) |
| platforms | PC, Console |
| subgenre | Management / tycoon |
| subgenre secondary | City builder |
| sim domain | Urban, Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Completion |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C09 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 9 |

## Summary

A skyscraper management game in which the player stacks offices, condos, hotels, and shops and designs elevator service so tenants on daily routines do not wait long enough to stress out and leave.

## Core Loop

build floors, lobbies, and elevators -> place offices, condos, hotels, and shops -> tenants travel by elevator on daily routines -> long waits raise stress and drive tenants out -> rent and population raise the star rating -> unlock new facilities

## Design Notes

SimTower turns a building into a vertical transit problem: standard elevators span up to 30 floors and express elevators the full height, so the player designs shafts, sky lobbies, and stops to keep queues short as the tower grows toward 100 floors above ground and 9 below. Tenant stress, not money alone, gates the star rating from one to five and finally the Tower rating, which needs a cathedral on top. Events such as a terrorist bomb ransom, VIP visits that can unlock a star, fires, and pests interrupt the routine.

## Relations

**uses**

- [Service queues](../mechanic/service-queues.md) (core): Tenants wait at elevator lobbies; long waits raise stress, and stressed tenants move out.
- [Building placement](../mechanic/free-placement.md) (core): Floors and tenant units are placed on a side-view grid; tenant type and position set elevator demand.
- [Daily schedules](../mechanic/daily-schedules.md) (core): Office workers, residents, shoppers, and hotel guests travel at different times of day, creating rush periods at lobbies.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (core): Population and conditions advance the tower from one to five stars and then to Tower status, each step unlocking facility types.
- [Vertical layers](../mechanic/vertical-layers.md) (supporting): Up to 100 floors above ground and 9 below; standard elevators span 30 floors, express elevators the full height.
- [Agent pathfinding](../mechanic/agent-pathfinding.md) (supporting): People route between floors by elevators, escalators, and stairs.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Rent and sales income fund construction.
- [Random disasters](../mechanic/random-disasters.md) (supporting): Terrorist bomb threats with a ransom or search, fires, and pest infestations.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Sources

- [SimTower](../source/src-wikipedia-simtower.md)

---
Provenance: created in run `2026-10-24-catalog-ga`; reviewed in `2026-10-24-review-fixes`.
