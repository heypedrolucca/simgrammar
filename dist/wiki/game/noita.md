# Noita

*Game* · `noita` · status: **sourced**

A roguelite action game in which every pixel of the world is simulated as a falling-sand material that burns, melts, flows, and reacts, and the player builds wands from spells to dig through procedurally generated levels.

| field | value |
|---|---|
| year | 2019 |
| year full release | 2020 |
| developer | Nolla Games |
| platforms | PC |
| subgenre | Physics sandbox |
| sim domain | Physical / mechanical |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Campaign |
| failure model | Hard restart |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 4 |
| influence | 2 |
| influenced by | [The Powder Toy](../game/the-powder-toy.md) |
| cluster *(computed)* | C02 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 11 |

## Summary

A roguelite action game in which every pixel of the world is simulated as a falling-sand material that burns, melts, flows, and reacts, and the player builds wands from spells to dig through procedurally generated levels.

## Core Loop

descend into a procedurally generated biome -> fight enemies with wands that also reshape the pixel world -> survive fire, liquids, and gases set off by fighting -> buy or find spells and rebuild wands at the Holy Mountain -> descend again or die and restart

## Design Notes

Noita's Falling Everything engine simulates each pixel as a material with state (solid, powder, liquid, gas) and reaction rules, and solid bodies are Box2D rigid bodies that break into pixels when damaged. Because spells, enemies, and the player all act on that layer, combat routinely sets off chain events such as burning oil, steam explosions, flooding, and collapsing ceilings, and these kill the player as often as enemies do. Wand building composes spells with modifiers into programs with cast order and mana limits, and runs are permadeath.

## Relations

**influenced by**

- [The Powder Toy](../game/the-powder-toy.md)

**uses**

- [Falling-sand materials](../mechanic/falling-sand-materials.md) (core): Every pixel of terrain is a material that falls, flows, or rises by local rules, so digging, explosions, and spills reshape the level in real time.
- [Material interactions](../mechanic/material-interactions.md) (core): Materials react by rule: lava and water form rock and steam, wood burns into smoke, acid eats terrain, and alchemical liquids such as polymorphine or teleportatium apply their effects on contact.
- [Permadeath](../mechanic/permadeath.md) (core): A death ends the run and the world is regenerated; only some unlocks, such as new spells in the pool, persist.
- [Modular assembly](../mechanic/modular-assembly.md) (core): Wands have stats such as capacity, mana, recharge, and cast delay; spells and modifiers placed in a wand's slots execute in order, so arrangement changes what the wand does.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (supporting): Box2D rigid bodies such as crates, bricks, and detached terrain chunks can be kicked, thrown, and shattered.
- [Fire spread](../mechanic/fire-spread.md) (supporting): Fire spreads through wood, grass, oil, and gunpowder and burns the player and enemies alike.
- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (supporting): Liquids pool and flow and gases rise and spread through caves at pixel level.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Each seed generates biome layouts from hand-made tile pieces within a fixed order of biomes.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): The player controls one witch with levitation, kicking, and wand casting.
- [Modding API](../mechanic/modding-api.md) (supporting): Lua-based mods are supported and distributed through Steam Workshop.
- [Combination discovery](../mechanic/combination-discovery.md) (supporting): Each world seed defines two secret alchemy recipes (Lively Concoction and Alchemic Precursor), each made from three materials that players must find by experiment.

## Backlinks (computed)

**precedent for:** [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md)

## Sources

- [Noita (video game)](../source/src-wikipedia-noita.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
