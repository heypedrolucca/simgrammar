# Ultima Online

*Game* · `ultima-online` · status: **sourced**

A persistent fantasy MMO in which players progress through skills without classes or levels, craft goods for a player-driven economy, own persistent houses, and could attack each other anywhere until the 2000 split into Trammel and Felucca.

| field | value |
|---|---|
| aliases | UO |
| year | 1997 |
| developer | Origin Systems |
| platforms | PC |
| subgenre | MMO world |
| subgenre secondary | Systemic RPG |
| sim domain | Economic, Social / interpersonal |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Asynchronous persistent |
| sim scale | Region |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Persistent MMO |
| modding | Scripting |
| production tier | AAA |
| agent count order | ~1,000 |
| emergence | 4 |
| influence | 4 |
| cluster *(computed)* | C08 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 10 |

## Summary

A persistent fantasy MMO in which players progress through skills without classes or levels, craft goods for a player-driven economy, own persistent houses, and could attack each other anywhere until the 2000 split into Trammel and Felucca.

## Core Loop

practice skills by using them -> gather resources and craft goods -> trade with other players -> build and furnish a house -> fight monsters or other players -> recover from death and re-equip

## Design Notes

Ultima Online tried to simulate a world rather than a set of classes: skills grow with practice, goods come from player crafting, and houses persist on the map. Its planned artificial-life ecology, in which animal behavior responded to ecological events, was removed during beta because players killed creatures faster than they could spawn. Unrestricted player killing at launch led to the 2000 Trammel and Felucca split into consensual and open PvP facets, an early rule-zoned world (proposal pvp-security-zones); fans later reverse-engineered it to build server emulators.

## Relations

**uses**

- [Agent skills](../mechanic/agent-skills.md) (core): Progression is skill-based with no levels or classes; skills improve as the character uses them, so a character's abilities record what the player has practiced.
- [Persistent shared world](../mechanic/persistent-world.md) (core): Shards keep persistent player houses and goods; unrestricted PvP at launch was split in 2000 into a consensual-PvP Trammel facet and an open-PvP Felucca facet.
- [Hand crafting](../mechanic/hand-crafting.md) (core): The economy is craft-based: players gather materials and craft the weapons, armor, and goods other players buy.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting)
- [Player organizations](../mechanic/player-organizations.md) (supporting): Player guilds such as Shadowclan formed persistent communities.
- [Reputation](../mechanic/reputation.md) (supporting): Criminal acts against other players carry consequences whose rules changed over the game's life.
- [Building placement](../mechanic/free-placement.md) (supporting): Players place houses on open land in the shared world.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting)
- [Loss on death](../mechanic/loss-on-death.md) (supporting): A dead character leaves a corpse that other players can loot; item insurance, added in 2003, keeps chosen items for a fee.
- [PvP security zones](../mechanic/pvp-security-zones.md) (supporting): The 2000 Renaissance expansion split the world into Trammel, where player-versus-player combat is consensual, and Felucca, where it is open.

## Backlinks (computed)

**influenced:** [EVE Online](../game/eve-online.md)

**precedent for:** [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md)

## Sources

- [Ultima Online](../source/src-wikipedia-ultima-online.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
