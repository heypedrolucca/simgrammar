# Elite Dangerous

*Game* · `elite-dangerous` · status: **sourced**

An online space sim set in a 1:1 procedurally generated Milky Way where players trade, fight, mine, and explore while a server-side background simulation shifts faction control from aggregate player actions.

| field | value |
|---|---|
| aliases | Elite: Dangerous |
| year | 2014 |
| developer | Frontier Developments |
| platforms | PC, Console, VR |
| subgenre | Space sim |
| subgenre secondary | MMO world |
| sim domain | Cosmic / space, Economic, Political / governance |
| player role | Operator / pilot |
| agency model | Direct avatar |
| time model | Asynchronous persistent |
| sim scale | Interplanetary+ |
| fidelity | Systemic |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player, Co-op, Competitive, Persistent MMO |
| modding | None |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| influenced by | [Elite](../game/elite.md) |
| cluster *(computed)* | C11 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 17 |

## Summary

An online space sim set in a 1:1 procedurally generated Milky Way where players trade, fight, mine, and explore while a server-side background simulation shifts faction control from aggregate player actions.

## Core Loop

take missions or cargo at a station -> jump between star systems -> trade, fight, mine, or explore -> earn credits, rank, and faction influence -> outfit or buy ships -> background simulation shifts faction control and system states

## Design Notes

Stellar Forge generates around 400 billion star systems from rules of star and planet formation and blends in about 150,000 systems from real astronomical data, so the galaxy is mostly unvisited. The server-side Background Simulation tracks minor-faction influence, economy, and states per system and updates them from what all players do, so Solo, Private Group, and Open players share one political map. Ship capability comes from outfitting modules within power and mass limits, and flight is Newtonian with a default flight-assist layer.

## Relations

**influenced by**

- [Elite](../game/elite.md)

**uses**

- [Persistent shared world](../mechanic/persistent-world.md) (core): One galaxy state is shared by Open, Private Group, and Solo players; Frontier's Background Simulation changes faction influence, system states, and markets over time from aggregate player activity.
- [Procedural terrain](../mechanic/procedural-terrain.md) (core): Stellar Forge generates a 1:1 Milky Way of about 400 billion systems, bodies, and landable planetary surfaces, blended with about 150,000 catalog systems.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (core): Six-axis Newtonian flight with optional flight assist; manual docking, supercruise approaches, and combat that balances power distributor pips and heat.
- [Trade routes](../mechanic/trade-routes.md) (supporting): Station markets differ by economy type; traders haul commodities between stations for price differences, limited by cargo capacity and jump range.
- [Supply-demand pricing](../mechanic/supply-demand-pricing.md) (supporting): Market supply and demand at each station shift prices as players buy and sell.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Minor factions hold influence shares per system and enter wars or elections when two factions' influence is close; Powerplay pledges players to one of 12 powers contesting territory.
- [Reputation](../mechanic/reputation.md) (supporting): Standing with minor factions and superpower navy ranks gate missions and system permits.
- [Contracts and orders](../mechanic/contracts-orders.md) (supporting): Mission boards offer delivery, combat, and data missions with deadlines and payouts that also move faction influence.
- [Modular assembly](../mechanic/modular-assembly.md) (supporting): Ships take modules in fixed slots (power plant, thrusters, frame shift drive, hardpoints); module mass and class set jump range, speed, and loadout.
- [Power grid](../mechanic/power-grid.md) (supporting): A power plant's output must cover module draw; over budget, modules shut down by player-set priority.
- [Heat transfer](../mechanic/heat-transfer.md) (supporting): Ship heat rises from weapons, fuel scooping near stars, and damage; overheating damages modules, and heat sinks dump it.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Mining lasers, collector limpets, and sub-surface charges extract ore from planetary rings.
- [Player organizations](../mechanic/player-organizations.md) (supporting): Squadrons and player-supported minor factions coordinate background simulation work.
- [Fog of war](../mechanic/fog-of-war.md) (supporting): System bodies are unknown until scanned; first discoverers are credited.
- [Power allocation](../mechanic/power-allocation.md) (supporting): The power distributor's pips are split among systems, engines, and weapons capacitors in flight, setting each capacitor's recharge; module priorities decide what shuts down when the power plant is over budget.
- [Subsystem damage](../mechanic/subsystem-damage.md) (supporting): Each ship module has its own integrity, and damage to the power plant, thrusters, or drive degrades or disables it until repaired.
- [Real-world data feeds](../mechanic/real-world-data-feeds.md) (supporting): About 150,000 star systems from real astronomical catalogs are blended into the procedurally generated galaxy.

## Sources

- [Elite Dangerous](../source/src-wikipedia-elite-dangerous.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
