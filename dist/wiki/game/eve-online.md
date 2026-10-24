# EVE Online

*Game* · `eve-online` · status: **sourced**

A single-universe space MMO in which players mine, manufacture, trade, and fight in ships that are destroyed for good, inside a player-made economy and a galaxy of high-, low-, and null-security space where player alliances claim sovereignty.

| field | value |
|---|---|
| aliases | Eve Online, EVE |
| year | 2003 |
| developer | CCP Games |
| platforms | PC |
| subgenre | MMO world |
| subgenre secondary | Space sim |
| sim domain | Economic, Cosmic / space, Military / conflict |
| player role | Inhabitant |
| agency model | Direct avatar, Order queue |
| time model | Asynchronous persistent |
| sim scale | Interplanetary+ |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Persistent MMO |
| modding | None |
| production tier | AA |
| agent count order | 10,000+ |
| emergence | 5 |
| influence | 4 |
| influenced by | [Elite](../game/elite.md), [Ultima Online](../game/ultima-online.md) |
| cluster *(computed)* | C06 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 12 |

## Summary

A single-universe space MMO in which players mine, manufacture, trade, and fight in ships that are destroyed for good, inside a player-made economy and a galaxy of high-, low-, and null-security space where player alliances claim sovereignty.

## Core Loop

train skills in real time -> mine, salvage, or run missions for materials and ISK -> manufacture or buy ships and modules on the player market -> fit ships and fly into space of a chosen security level -> lose ships in combat and replace them -> corporations and alliances fight over sovereignty

## Design Notes

EVE keeps one economy for all players: nearly everything is player-made and ship losses are permanent, so wars create manufacturing demand. Risk and reward are tied to space security, with the most profitable activities in low-sec and null-sec, where the NPC police do not destroy aggressors. CCP hired an economist in 2007 to oversee the economy. Security-graded zones and permanent asset loss on destruction are not yet mechanics in the taxonomy (proposals pvp-security-zones, loss-on-death).

## Relations

**influenced by**

- [Elite](../game/elite.md)
- [Ultima Online](../game/ultima-online.md)

**uses**

- [Player-driven markets](../mechanic/player-driven-market.md) (core): Players gather raw materials and manufacture nearly all ships and modules, then trade them in a supply-and-demand market with price history charts, where manipulation such as ramping and bear raids is possible.
- [Persistent shared world](../mechanic/persistent-world.md) (core): One shared universe on the Tranquility server holds more than 5,000 stargate-linked systems plus about 2,500 wormhole systems; system security from 1.0 to -1.0 sets whether CONCORD police destroy aggressors.
- [Player organizations](../mechanic/player-organizations.md) (core): Corporations led by a CEO assign roles, tax members, declare wars for a weekly fee, and join alliances that claim sovereignty over null-sec systems.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Skills have prerequisites, and capital-ship skills take several times longer to train than frigate skills.
- [Real-time clock](../mechanic/real-time-clock.md) (supporting): Skills train in real time, including while logged off, from a queue of up to 50 skills.
- [Modular assembly](../mechanic/modular-assembly.md) (supporting): Ships are fitted with modules in high, mid, and low slots plus semi-permanent rigs.
- [Production chains](../mechanic/production-chain.md) (supporting): Blueprints turn gathered materials into ships and modules.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Players mine asteroids and salvage wrecks for materials.
- [Elections](../mechanic/elections.md) (supporting): Players elect the Council of Stellar Management, which carries requests to CCP; the first election in 2008 had 66 candidates for nine seats.
- [Reputation](../mechanic/reputation.md) (supporting): Unprovoked aggression in secure space costs security status and draws police response.
- [Loss on death](../mechanic/loss-on-death.md) (core): A destroyed ship and its fittings are gone for good, part of its cargo and modules drops in a lootable wreck, and ship insurance pays back part of the hull's value.
- [PvP security zones](../mechanic/pvp-security-zones.md) (core): Each system's security from 1.0 to -1.0 decides whether CONCORD police destroy aggressors; high-sec deters player attacks, low- and null-sec leave them to players, and the riskier zones hold the richer activities.

## Backlinks (computed)

**precedent for:** [Agent ambassadors between player worlds](../opportunity/agent-ambassadors-async.md), [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md), [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md)

## Sources

- [Eve Online](../source/src-wikipedia-eve-online.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
