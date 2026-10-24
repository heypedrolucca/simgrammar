# Second Life

*Game* · `second-life` · status: **sourced**

A persistent 3D virtual world in which residents build objects from prims and meshes, script them in the Linden Scripting Language, own land in server-simulated regions, and trade goods and land for Linden Dollars exchangeable for real currency.

| field | value |
|---|---|
| aliases | SL |
| year | 2003 |
| developer | Linden Lab |
| platforms | PC |
| subgenre | MMO world |
| subgenre secondary | Sandbox world |
| sim domain | Economic, Social / interpersonal |
| player role | Inhabitant |
| agency model | Direct avatar, Programmatic |
| time model | Asynchronous persistent |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Third-person |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | None |
| multiplayer | Persistent MMO |
| modding | Scripting |
| production tier | AA |
| agent count order | 10,000+ |
| emergence | 3 |
| influence | 3 |
| boundary case | True |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

A persistent 3D virtual world in which residents build objects from prims and meshes, script them in the Linden Scripting Language, own land in server-simulated regions, and trade goods and land for Linden Dollars exchangeable for real currency.

## Core Loop

customize an avatar -> buy or rent land in a region -> build objects from prims and mesh -> script behavior in LSL -> sell creations, land, or services for Linden Dollars -> exchange Linden Dollars on the LindeX

## Design Notes

Linden Lab describes Second Life as a platform rather than a game: it has no set objective, and almost all content is built and scripted by residents, who keep copyright to it. It is a boundary case included for its user-content pipeline, server-side object scripting, and a virtual currency with a real-money exchange that produced real income for some residents. Each region is simulated on its own CPU core with Havok physics, which caps how many avatars and objects a place can hold.

## Relations

**uses**

- [Persistent shared world](../mechanic/persistent-world.md) (core): The world is a grid of 256 by 256 meter regions, each simulated on a dedicated CPU core with Havok physics and capped at 40 avatars on the mainland or 100 on private islands.
- [Player programming](../mechanic/player-programming.md) (core): Objects run Linden Scripting Language scripts on Linden Lab's servers, which is how built objects become interactive.
- [Player-driven markets](../mechanic/player-driven-market.md) (core): Residents trade land, goods, and services for Linden Dollars, which are bought and sold for real currency on the LindeX exchange; the Marketplace has listed about 2.1 million items.
- [Modular assembly](../mechanic/modular-assembly.md) (supporting): Objects are built from linked primitives, up to 256 per linked set, or from imported mesh.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (supporting)
- [Content sharing](../mechanic/content-sharing.md) (supporting): Creators keep copyright to their content and sell it to other residents.
- [Player organizations](../mechanic/player-organizations.md) (supporting): Groups give residents shared chat and voice channels.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting)

## Backlinks (computed)

**precedent for:** [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md)

## Sources

- [Second Life](../source/src-wikipedia-second-life.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
