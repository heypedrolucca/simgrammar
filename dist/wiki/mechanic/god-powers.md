# God powers

*Mechanic* · `god-powers` · status: **sourced**

The player spends a power resource on miracles that alter terrain, weather, or creatures.

| field | value |
|---|---|
| aliases | miracles, divine intervention, spells |
| family | Control & automation |
| substrate | Rule system, Aggregate stocks |
| math basis | System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Direct manipulation, Choice / cards |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Populous](../game/populous.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 5 |
| prevalence share *(computed)* | 0.029 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.5 |

## Definition

The player is an external force that cannot command agents directly but can cast powers on the world. State owned: a power pool (mana, belief, prayer power) and the set of unlocked powers with costs and cooldowns. The pool fills from a simulation quantity, typically the number or devotion of followers, and casting spends it to apply an effect at a target: raise or lower land, flood, earthquake, swamp, volcano, rain, lightning, heal, or summon. Effects then propagate through the other systems (terrain, hydrology, population). Canonical forms: Populous, where raising and lowering land is the basic power, mana comes from followers building houses, and more mana unlocks earthquakes, floods, swamps, and volcanoes; Black & White, where worshipping villagers generate power for miracles cast by gesture; From Dust; WorldBox.

## Player Experience

The player feels large and indirect. Problems are solved by reshaping the world rather than ordering people, and destruction is satisfying. The loop of growing followers to earn more power to help or punish them gives a sense of patronage.

## Design Levers

- power source: followers, belief, devotion, or time
- cost, area, and cooldown per power
- unlock order of powers
- whether powers are destructive, constructive, or both
- casting input: menu, gesture, or physical manipulation
- how much the world's systems amplify or resist each power

## Failure Modes

- One dominant power used repeatedly trivializes opponents.
- Gesture recognition that misreads input makes casting frustrating and unreliable under pressure.
- Powers with fixed scripted effects feel like animations rather than interventions in a simulation.

## Dynamics

- Follower-funded power creates a reinforcing loop: help followers grow to gain power to help them more.
- Terrain-altering powers chain into hydrology and settlement systems, such as floods that relocate a whole population.
- In competitive god games, power denial (reducing enemy followers) matters as much as casting.

## Open Questions

- Can players describe a miracle in language and have a generative system produce effects grounded in the world's physics rather than from a fixed list?
- How do learned agents that react to miracles, such as fear or worship, change the follower loop?

## Relations

**synergy**

- [Terraforming](../mechanic/terraforming.md): Miracles that raise land or move water are terraforming delivered as power.

## Backlinks (computed)

**affected by:** [Genie foundation world models](../technique/genie-world-models.md)

**involved in:** [Language-agent society terrarium](../opportunity/llm-society-terrarium.md), [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

**used by:** [Black & White](../game/black-and-white.md), [From Dust](../game/from-dust.md), [Populous](../game/populous.md), [SimEarth](../game/simearth.md), [Species: Artificial Life, Real Evolution](../game/species-alre.md)

## Claims

- In Populous, raising and lowering land is the most basic power, mana comes from followers building houses, and increasing mana unlocks earthquakes, floods, swamps, and volcanoes. *(confidence: medium)* [[76](../source/src-wikipedia-populous.md)]
- In Black & White, villagers worshipping around the Temple generate power for miracles, which can be cast by gestures with the Hand. *(confidence: medium)* [[77](../source/src-wikipedia-black-and-white.md)]

## Sources

- [Populous (video game)](../source/src-wikipedia-populous.md)
- [Black & White (video game)](../source/src-wikipedia-black-and-white.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
