# Valheim

*Game* · `valheim` · status: **sourced**

A co-op Viking survival game in a seeded procedural world of biomes where players gather, build structurally supported shelters, eat for stat buffs, and defeat biome bosses to progress.

| field | value |
|---|---|
| year | 2021 |
| year full release | 2026 |
| developer | Iron Gate Studio |
| platforms | PC, Console, Handheld |
| subgenre | Survival sim |
| subgenre secondary | Sandbox world |
| sim domain | Physical / mechanical, Biological / ecological |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | Third-person |
| win structure | Completion |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player, Co-op |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C05 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 14 |

## Summary

A co-op Viking survival game in a seeded procedural world of biomes where players gather, build structurally supported shelters, eat for stat buffs, and defeat biome bosses to progress.

## Core Loop

explore seeded biomes -> gather wood, stone, and ore -> build shelters that must be supported and roofed -> eat food for health and stamina -> craft better gear -> summon and defeat each biome's boss -> sail to harder biomes

## Design Notes

Food is a reward rather than a punishment: eating raises maximum health and stamina and speeds regeneration, and there is no starvation, so the survival layer pushes players toward better food rather than threatening death. This consumable-buff model does not fit survival-meters cleanly (proposal filed). Building uses a support model in which stability falls with distance from the ground, so architecture follows material limits, and uncovered wood decays to half durability in rain. Progression is gated by eight bosses, each summoned with an offering. Early access began in February 2021 and 1.0 shipped in September 2026.

## Relations

**uses**

- [Structural integrity](../mechanic/structural-integrity.md) (core): Stability runs from blue (grounded) to red; it falls with horizontal and vertical distance from ground, a piece cannot exceed its support's stability, and vertical limits are 16 m for wood and stone and 24 m for core wood.
- [Procedural terrain](../mechanic/procedural-terrain.md) (core): Each world is generated from a seed and divided into biomes (Meadows, Black Forest, Swamp, Mountains, Plains, Ocean, Mistlands, Deep North, Ashlands), each with its own resources, enemies, and boss.
- [Hand crafting](../mechanic/hand-crafting.md) (core): Workbenches, forges, and other stations craft tools, weapons, and building pieces; new materials unlock new recipes.
- [Survival meters](../mechanic/survival-meters.md) (supporting): Food raises maximum health and stamina for a time instead of causing starvation; stamina drains when running or attacking.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Skills rise to level 100 through use and affect damage and stamina drain; dying reduces skill levels.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (supporting): Comfort from nearby furnishings lengthens the Rested buff.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Each boss leaves a trophy that grants a power at a central altar and opens the next tier of materials.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Uncovered or submerged wood decays to 50% durability; tools lose durability.
- [Weather](../mechanic/weather.md) (supporting): Rain wets the player and rots exposed wood.
- [Raid defense](../mechanic/raid-defense.md) (supporting): Random events send enemies against bases.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting)
- [Animal husbandry](../mechanic/animal-husbandry.md) (supporting): Some animals can be tamed and bred.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting)
- [Loss on death](../mechanic/loss-on-death.md) (supporting): On death the player's equipment and inventory stay in a tombstone at the death site, and skill levels drop, so the player must travel back to recover gear.

## Sources

- [Valheim](../source/src-wikipedia-valheim.md)
- [Valheim on Steam](../source/src-steam-2026-valheim.md)
- [Building](../source/src-valheimwiki-2026-building.md)

---
Provenance: created in run `2026-10-24-catalog-gb`.
