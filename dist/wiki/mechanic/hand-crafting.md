# Hand crafting

*Mechanic* · `hand-crafting` · status: **sourced**

The player or avatar combines carried components into items from a recipe list, gated by workstations and known recipes.

| field | value |
|---|---|
| aliases | crafting, recipe crafting, survival crafting |
| family | Resources & production |
| substrate | Rule system |
| math basis | Combinatorics |
| feedback | Reinforcing (positive) |
| player interface | Direct manipulation, Choice / cards |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 6 |
| earliest game *(computed)* | [Ultima Online](../game/ultima-online.md) |
| earliest year *(computed)* | 1997 |
| prevalence *(computed)* | 17 |
| prevalence share *(computed)* | 0.098 |
| subgenre spread *(computed)* | 8 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.75 |

## Definition

The player holds an inventory of components and a set of known recipes, each mapping an input multiset to an output item. A craft checks that inputs are present, any required station (workbench, forge, furnace) is nearby, and the recipe is unlocked, then consumes the inputs and produces the output instantly or after a short delay. Minecraft uses a 2x2 grid in the inventory and a 3x3 grid at a crafting table, with shaped recipes keyed to spatial arrangement; Don't Starve, Valheim, and Subnautica use menu lists gated by stations and blueprints; Ultima Online ties success to a crafting skill. Infinite Craft replaces the recipe table with a language model (Llama 2, later Llama 3.1) that generates the result of any new pair and stores it so every player gets the same answer. Inputs: carried items, station proximity, unlock state. Outputs: new items and consumed components.

## Player Experience

Gathering with intent. The player looks at a desired item, works back to its components, and goes out to collect them, so the recipe list becomes a shopping list that structures exploration. The first craft of a new tool is a small power spike that opens the next zone or task.

## Design Levers

- recipe count and depth of intermediate components
- discovery model: all visible, unlocked by research or blueprints, or found by experimentation
- station gating and whether stations must be nearby
- craft time and whether crafts can be queued or batched
- spatial grid versus list interface
- inventory limits that bound how much can be carried to a station

## Failure Modes

- Hidden recipes without in-game discovery aids push players to wikis, as in early Minecraft before its recipe book.
- Long chains of trivial intermediates turn crafting into inventory sorting.
- Crafting that is strictly better than found loot, or strictly worse, makes one of the two systems irrelevant.

## Dynamics

- Tool tiers gate access to materials, which gate the next tool tier, producing a progression ladder from rules alone.
- Inventory limits couple crafting to base building and storage chests.
- In multiplayer worlds players specialize in crafting lines and trade, as Ultima Online crafters did.

## Open Questions

- Can generative models produce open recipe spaces like Infinite Craft whose outputs also have balanced, mechanically meaningful stats rather than only names?
- How should discovery be explained to players when a model rather than a table decides what a combination yields?

## Backlinks (computed)

**affected by:** [LLM-adjudicated state transitions (LLM as game mechanic)](../technique/llm-rule-adjudication.md)

**involved in:** [Generated recipe graphs](../opportunity/generated-recipe-graphs.md)

**used by:** [A Tale in the Desert](../game/a-tale-in-the-desert.md), [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Autonauts](../game/autonauts.md), [Don't Starve](../game/dont-starve.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Factorio](../game/factorio.md), [Minecraft](../game/minecraft.md), [Project Sid](../game/project-sid.md), [Project Zomboid](../game/project-zomboid.md), [Satisfactory](../game/satisfactory.md), [Stardew Valley](../game/stardew-valley.md), [Subnautica](../game/subnautica.md), [The Long Dark](../game/the-long-dark.md), [This War of Mine](../game/this-war-of-mine.md), [Ultima Online](../game/ultima-online.md), [Valheim](../game/valheim.md), [The Legend of Zelda: Breath of the Wild](../game/zelda-breath-of-the-wild.md)

## Sources

- [Infinite Craft](../source/src-wikipedia-infinite-craft.md)
- [Minecraft](../source/src-wikipedia-minecraft.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
