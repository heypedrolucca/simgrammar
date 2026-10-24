# Kenshi

*Game* · `kenshi` · status: **sourced**

A squad-based open-world RPG with no hero character, where any recruit can starve, lose limbs, train skills by doing, be enslaved, or found an outpost among reactive factions.

| field | value |
|---|---|
| year | 2013 |
| year full release | 2018 |
| developer | Lo-Fi Games |
| platforms | PC |
| subgenre | Systemic RPG |
| subgenre secondary | Colony sim |
| sim domain | Military / conflict, Political / governance, Biological / ecological |
| player role | Overseer |
| agency model | Direct unit control, Zoning / placement, Order queue |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Systemic |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Permadeath |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 4 |
| influence | 2 |
| cluster *(computed)* | C05 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 16 |

## Summary

A squad-based open-world RPG with no hero character, where any recruit can starve, lose limbs, train skills by doing, be enslaved, or found an outpost among reactive factions.

## Core Loop

wander the world with a squad -> fight, trade, steal, or get captured -> injuries and hunger reduce stats while skills train from use -> recruit and found an outpost -> factions react and world states shift

## Design Notes

There is no main character: every recruit and NPC is a potential equal, with no hero units given stronger stats, and the world and shops do not scale to the player, so early characters are weaker than most people they meet. Progress comes from use-based skill gain, which makes losing fights a form of training. Deaths of notable faction leaders change world states, such as towns taken over by a new faction. Chris Hunt developed it alone until 2013, and it was one of the first games in Steam Early Access.

## Relations

**uses**

- [Injury body model](../mechanic/injury-body-model.md) (core): Each limb has its own health; limbs can be damaged or severed and replaced with prosthetic or robotic limbs, and blood loss and injuries reduce stats and movement while squadmates carry the wounded.
- [Agent skills](../mechanic/agent-skills.md) (core): Skills rise from the actions they describe, such as stealing for thievery and fighting for combat, with stats and appearance changing as characters grow.
- [Unit commands](../mechanic/unit-commands.md) (core): The player commands any squad member directly in real time with pause; no character is privileged, and the squad acts together.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (core): Many factions and species with relations to each other; the player can aid or oppose them, and deaths of notable figures shift world states.
- [Reputation](../mechanic/reputation.md) (supporting): Player standing with each faction changes access and hostility.
- [Survival meters](../mechanic/survival-meters.md) (supporting): Starvation reduces character stats.
- [Building placement](../mechanic/free-placement.md) (supporting): Outposts are built and upgraded into fortified havens or businesses.
- [Work priorities](../mechanic/work-priorities.md) (supporting): Squad members keep job lists for base work and production.
- [Production chains](../mechanic/production-chain.md) (supporting)
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting): Zone soil types and terrain affect outpost farming.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Research unlocks equipment and technologies.
- [Raid defense](../mechanic/raid-defense.md) (supporting): Outposts must be defended against attackers.
- [Weather](../mechanic/weather.md) (supporting): Some weather, such as acid rain, harms characters.
- [Permadeath](../mechanic/permadeath.md) (supporting)
- [Statistical combat resolution](../mechanic/stat-combat-resolution.md) (supporting): Fights resolve from character combat skills, weapon stats, and armor, with damage applied to individual limbs.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Generated dream and replay views](../opportunity/dream-replay-layer.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md)

## Sources

- [Kenshi (video game)](../source/src-wikipedia-kenshi.md)
- [Kenshi on Steam](../source/src-steam-2026-kenshi.md)

---
Provenance: created in run `2026-10-24-catalog-gb`; reviewed in `2026-10-24-review-fixes`.
