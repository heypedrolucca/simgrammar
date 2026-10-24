# Collection goals

*Mechanic* · `collection-goals` · status: **sourced**

Catalogs of items, species, or bundles give the player sets to complete for rewards or recognition.

| field | value |
|---|---|
| aliases | catalogs, bundles, collection logs, museum donations |
| family | Progression & goals |
| substrate | Rule system |
| math basis | Combinatorics, Probability / statistics |
| feedback | None |
| player interface | Observation only, Direct manipulation |
| legibility | 5 |
| emergence potential | 1 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Gran Turismo](../game/gran-turismo.md) |
| earliest year *(computed)* | 1997 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.75 |

## Definition

The game defines named sets of collectibles (items, fish, insects, fossils, species, recipes) and tracks which members the player has obtained, donated, or observed. State owned: per set, a membership checklist and completion state. Update rule: when the player acquires or submits a qualifying item, mark it; when a set is complete, grant a reward or unlock. Collection drives engagement with other systems because members are spread across seasons, locations, and rarities. Canonical forms: Stardew Valley's Community Center, with six rooms and thirty bundles whose rewards repair the quarry bridge, greenhouse, minecarts, and bus, Animal Crossing: New Horizons' museum and Critterpedia, and Viva Pinata's species journal with per-species visit, resident, and romance requirements.

## Player Experience

A gentle, open checklist. The player plans around a missing fish that appears only in rain in autumn, feels a click when a set completes, and has a reason to explore every corner of the simulation.

## Design Levers

- set size and rarity distribution of members
- seasonal, weather, or location gating of members
- reward type: functional unlocks, cosmetics, or none
- fixed versus randomized set contents, such as Stardew Valley remixed bundles
- whether items are consumed by submission
- visibility of missing members as silhouettes or hints

## Failure Modes

- The last few rare members take far longer than the rest, turning completion into a grind.
- Members missable for a season or year punish players who fall behind.
- Functional rewards locked behind collection force players who dislike collecting through it.

## Dynamics

- Collection targets route player attention through seasons, weather, and locations they would otherwise skip.
- Players share calendars and spreadsheets of where and when members appear.
- Alternative completion routes, such as the Joja membership in Stardew Valley, frame collection as a moral choice.

## Open Questions

- Can generated collectible sets tied to world state, such as species that evolved in this run, keep collection goals meaningful in procedural worlds?
- What rarity curve keeps the final members exciting rather than grinding?

## Backlinks (computed)

**affected by:** [LLM-adjudicated state transitions (LLM as game mechanic)](../technique/llm-rule-adjudication.md)

**used by:** [Animal Crossing: New Horizons](../game/animal-crossing-new-horizons.md), [Equilinox](../game/equilinox.md), [Gran Turismo](../game/gran-turismo.md), [Gran Turismo 7](../game/gran-turismo-7.md), [Infinite Craft](../game/infinite-craft.md), [Stardew Valley](../game/stardew-valley.md), [Viva Piñata](../game/viva-pinata.md)

## Claims

- Stardew Valley's Community Center has six rooms and thirty bundles; completing rooms repairs the quarry bridge, greenhouse, minecarts, and bus, and a Joja membership replaces bundles with payments. *(confidence: medium)* [[66](../source/src-stardewvalleywiki-2026-bundles.md)]

## Sources

- [Bundles](../source/src-stardewvalleywiki-2026-bundles.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
