# Spore

*Game* · `spore` · status: **sourced**

A five-stage game in which the player guides a species from cell to galactic empire, building its body, vehicles, and buildings in part-based editors whose creations are shared automatically through the Sporepedia.

| field | value |
|---|---|
| year | 2008 |
| developer | Maxis |
| platforms | PC |
| subgenre | Ecosystem / evolution |
| subgenre secondary | God game, 4X strategy |
| sim domain | Biological / ecological, Cosmic / space |
| player role | God |
| agency model | Direct avatar, Direct unit control, Design then test |
| time model | Real-time with pause |
| sim scale | Interplanetary+ |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player, Async / shared content |
| modding | Content |
| production tier | AAA |
| agent count order | ~100 |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

A five-stage game in which the player guides a species from cell to galactic empire, building its body, vehicles, and buildings in part-based editors whose creations are shared automatically through the Sporepedia.

## Core Loop

eat to earn DNA points -> edit body parts to change abilities -> befriend or fight other species -> stage completes and grants consequence traits -> next stage changes the rules -> colonize and terraform planets -> creations upload to the Sporepedia and populate other players' galaxies

## Design Notes

Spore's evolution is player design rather than selection: body parts bought with DNA points set speed, attack, and social abilities directly, and nothing is inherited by differential survival. Its distinctive system is the part-based editors (18 share one interface) whose creations are stored as compact descriptions of a few kilobytes and reconstructed procedurally, which let Maxis upload every creation and redistribute them as the inhabitants of other players' galaxies (over 100 million by May 2009). Each of the five stages swaps in a different genre's rules, and play style in each stage assigns consequence traits that carry forward.

## Relations

**uses**

- [Modular assembly](../mechanic/modular-assembly.md) (core): Creature, building, and vehicle editors assemble parts such as mouths, legs, and arms whose choice sets abilities, diet options, and stats; textures and animation are applied procedurally to the assembled topology.
- [Content sharing](../mechanic/content-sharing.md) (core): Every creation uploads automatically to the Sporepedia and is redistributed to populate other players' worlds, so other players' designs fill the galaxy without manual import.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (core): Each stage ends at a progress threshold and hands the species to a new rule set (cell, creature, tribal, civilization, space), with three consequence traits awarded from how aggressive or social the player was.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): The player directly steers the cell, the creature, and later a spaceship.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Tribal and civilization stages switch to commanding up to 12 tribe members, then vehicles and cities.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Creature-stage species, tribes, nations, and space empires such as the Grox can be befriended through social actions or conquered.
- [Terraforming](../mechanic/terraforming.md) (supporting): In the space stage rocky planets can be terraformed, their ecosystems changed, and features such as mountains and lakes added.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting)

## Backlinks (computed)

**precedent for:** [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md)

## Sources

- [Spore (2008 video game)](../source/src-wikipedia-spore.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
