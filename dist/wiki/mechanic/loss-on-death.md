# Loss on death

*Mechanic* · `loss-on-death` · status: **sourced**

When a character or ship is destroyed, its carried or fitted assets are lost or dropped at the death site for the owner or others to recover, with insurance or retrieval rules as softeners.

| field | value |
|---|---|
| aliases | full loot, item drop on death, corpse run, ship loss and insurance |
| family | Risk & failure |
| substrate | Rule system |
| math basis | Utility / decision theory, Game theory |
| feedback | Reinforcing (positive) |
| player interface | Direct manipulation, Observation only |
| legibility | 5 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Ultima Online](../game/ultima-online.md) |
| earliest year *(computed)* | 1997 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

When a character or ship is destroyed, its carried or fitted assets are lost or dropped at the death site for the owner or others to recover, with insurance or retrieval rules as softeners.

## Definition

Owns the rules applied to an entity's assets at death: which items are destroyed, which drop into a container (corpse, tombstone, wreck) at the death location, who may loot it and for how long, and what compensation applies, such as insurance payouts or protected items. On death the inventory is partitioned by those rules, a container entity is spawned with a despawn timer or permanence, and the character respawns elsewhere or not at all. Ultima Online left corpses lootable by other players and added item insurance in 2003; EVE Online destroys ships for good and drops part of the cargo and fittings in a wreck. Valheim leaves the player's items in a tombstone at the death site; Minecraft drops the inventory where the player died. Unlike permadeath, which removes the character, this mechanic removes or relocates possessions while the character usually continues.

## Player Experience

Risk is measured in gear. The player decides what to carry into danger, keeps backups at home, and after a death makes a tense run back to recover a corpse or tombstone. In player-versus-player worlds the same rule makes every fight a gamble for the other side's equipment.

## Design Levers

- share of assets destroyed, dropped, or kept
- who can loot dropped assets and for how long before they despawn
- insurance or protected-slot systems and their cost
- respawn location relative to the death site
- additional death costs such as skill or experience loss

## Failure Modes

- Full loot in open player-versus-player worlds lets strong players farm weak ones, a problem Ultima Online answered by splitting off the consensual-PvP Trammel facet in 2000.
- Short despawn timers turn a death far from home into an unrecoverable loss that ends play sessions.
- Players hoard their best gear and never use it, so the items the loss rule protects stop being played.

## Dynamics

- Asset destruction creates steady demand for replacements, sustaining player crafting and markets.
- Corpse runs become memorable expeditions, often with friends.
- Players match the value of a loadout to the risk of the area, producing cheap disposable kits for dangerous trips.

## Open Questions

- Could AI-run recovery services or scavenger agents make dropped assets part of the world's economy rather than a pure loss?
- What mix of destroyed and recoverable assets keeps risk meaningful without driving players to hoard?

## Backlinks (computed)

**used by:** [EVE Online](../game/eve-online.md), [Minecraft](../game/minecraft.md), [Ultima Online](../game/ultima-online.md), [Valheim](../game/valheim.md)

## Sources

- [Ultima Online](../source/src-wikipedia-ultima-online.md)
- [Eve Online](../source/src-wikipedia-eve-online.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
