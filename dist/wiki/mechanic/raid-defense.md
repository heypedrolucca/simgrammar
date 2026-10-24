# Raid defense

*Mechanic* · `raid-defense` · status: **sourced**

Settlements defend against periodic attacks with walls, turrets, traps, and fighters placed and commanded by the player.

| field | value |
|---|---|
| aliases | base defense, sieges, attack waves |
| family | Conflict & defense |
| substrate | Agent-based, Rule system |
| math basis | Graph search, Optimization, Probability / statistics |
| feedback | Both |
| player interface | Placement, Orders |
| legibility | 4 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 3 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Caesar III](../game/caesar-3.md) |
| earliest year *(computed)* | 1998 |
| prevalence *(computed)* | 14 |
| prevalence share *(computed)* | 0.08 |
| subgenre spread *(computed)* | 7 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

An attack generator spawns hostile groups at map edges, by drop, or by tunneling, sized by a threat budget; attackers path toward targets such as colonists, valuables, or polluting buildings, and resolve combat against walls with hit points, turrets with range and ammunition, traps, and defenders. RimWorld raids arrive by walking, drop pods, sappers who dig through walls, or sieges, sized by raid points; Factorio biters attack polluting structures and evolve stronger forms; Dwarf Fortress has goblin sieges; Mindustry and They Are Billions use scheduled waves. Inputs: threat budget, attacker types, map. Outputs: damage, casualties, loot, and the defensive layout's measured strength.

## Player Experience

Long build phases punctuated by short, tense fights. The player designs killboxes and chokepoints, stocks ammunition and medicine, and learns each attacker type's counter. A breached wall is a crisis that tests the whole colony.

## Design Levers

- attack frequency and size, often from adaptive threat scaling
- attacker types that bypass static defense, such as sappers, flyers, or drop pods
- pathing rules and how attackers choose targets
- defense costs, maintenance, and ammunition supply
- warning time before arrival
- player control of fighters during the fight

## Failure Modes

- A single killbox design defeats every raid, so defense stops being a decision; RimWorld's sapper and breach raids counter this by digging or blasting through walls.
- Pathfinding exploits let attackers be lured into infinite loops.
- Raids that interrupt every build session feel like chores rather than tests.

## Dynamics

- Defense layout constrains the whole settlement plan, pulling walls, chokepoints, and storage together.
- Wounded defenders strain medical and food systems after each fight, so raids cascade into other systems.
- Arms races appear as attacker variety forces layered defenses.

## Open Questions

- Can attacker AI that learns the player's defenses across raids prevent dominant killbox designs without feeling unfair?
- What raid frequency keeps defense meaningful in games whose main loop is building?

## Backlinks (computed)

**used by:** [Caesar III](../game/caesar-3.md), [Contraband Police](../game/contraband-police.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Dyson Sphere Program](../game/dyson-sphere-program.md), [Factorio](../game/factorio.md), [Farthest Frontier](../game/farthest-frontier.md), [Going Medieval](../game/going-medieval.md), [Kenshi](../game/kenshi.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Manor Lords](../game/manor-lords.md), [Mindustry](../game/mindustry.md), [RimWorld](../game/rimworld.md), [Screeps](../game/screeps.md), [Valheim](../game/valheim.md)

## Sources

- [Raid points](../source/src-rimworldwiki-2026-raid-points.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
