# Survival meters

*Mechanic* · `survival-meters` · status: **sourced**

The avatar's bodily stocks such as hunger, thirst, warmth, and fatigue deplete over time and, if unmanaged, drain health and kill.

| field | value |
|---|---|
| aliases | hunger clock, food clock, vital stats |
| family | Biology & health |
| substrate | Aggregate stocks, Rule system |
| math basis | System dynamics / ODEs, Control theory |
| feedback | Both |
| player interface | Observation only, Direct manipulation |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| specializes | [Needs decay](../mechanic/needs-decay.md) |
| open questions | Can drain rates adapted by a learned player model keep survival pressure steady from early to late game without feeling rubber-banded? |
| core count *(computed)* | 8 |
| earliest game *(computed)* | [The Oregon Trail](../game/oregon-trail.md) |
| earliest year *(computed)* | 1971 |
| prevalence *(computed)* | 13 |
| prevalence share *(computed)* | 0.075 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a few bounded stocks on the avatar or party, such as hunger, thirst, body temperature, fatigue, and sometimes sanity or calories. Each tick each stock falls at a base rate modified by activity, weather, and clothing; eating, drinking, resting, or standing near heat restores it. At zero or past a threshold the stock drains health, applies penalties, or kills. Don't Starve uses a default maximum hunger of 150 that drains 75 per game day, and at zero health drains 1.25 per second; The Long Dark tracks calories, body temperature, fatigue, and hunger against cold nights and weather; The Oregon Trail asks each round how much food to eat and kills the party through starvation, cold, or untreated illness. Roguelikes such as Rogue and NetHack use a food clock. Inputs are time, environment, and consumption; outputs are health drain and penalties.

## Player Experience

Constant pressure to keep moving. The player plans every trip around food, water, and warmth, weighs risky exploration against returning to safety, and feels relief at a full stomach by a fire. The meters make the world feel hostile and give mundane items life-or-death value.

## Design Levers

- which meters exist and which are lethal versus only penalizing
- base drain rates and modifiers from activity, temperature, and gear
- restoration value of each consumable and its availability in the world
- consequence at zero: health drain rate, penalties, or instant death
- difficulty presets that scale drain and resource scarcity

## Failure Modes

- Fast drain with scarce restoration forces repetitive eating and drinking that crowds out exploration.
- Abundant food trivializes meters by midgame, so they become noise.
- Several meters with overlapping warnings overload attention without adding decisions.

## Dynamics

- Low meters reduce the ability to gather, which accelerates decline into a death spiral.
- Meters couple the avatar to weather, day-night temperature, and cooking or crafting systems.
- Players build bases and routes around reliable sources of food, water, and heat.

## Open Questions

- Can drain rates adapted by a learned player model keep survival pressure steady from early to late game without feeling rubber-banded?

## Relations

**specializes**

- [Needs decay](../mechanic/needs-decay.md)

## Backlinks (computed)

**used by:** [Big Ambitions](../game/big-ambitions.md), [Don't Starve](../game/dont-starve.md), [Hardspace: Shipbreaker](../game/hardspace-shipbreaker.md), [Kenshi](../game/kenshi.md), [Minecraft](../game/minecraft.md), [The Oregon Trail](../game/oregon-trail.md), [Project Zomboid](../game/project-zomboid.md), [Space Engineers](../game/space-engineers.md), [Stationeers](../game/stationeers.md), [Subnautica](../game/subnautica.md), [The Long Dark](../game/the-long-dark.md), [Valheim](../game/valheim.md), [The Legend of Zelda: Breath of the Wild](../game/zelda-breath-of-the-wild.md)

## Sources

- [Hunger](../source/src-dontstarvewiki-2026-hunger.md)
- [The Long Dark](../source/src-wikipedia-the-long-dark.md)
- [The Oregon Trail (1971 video game)](../source/src-wikipedia-oregon-trail-1971.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
