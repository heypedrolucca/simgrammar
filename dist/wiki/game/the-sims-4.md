# The Sims 4

*Game* · `the-sims-4` · status: **sourced**

The fourth mainline Sims game, built around a dominant emotion computed from moodlets, three-trait personalities with aspiration rewards, multitasking, room-based building, and an in-game Gallery for sharing creations.

| field | value |
|---|---|
| year | 2014 |
| developer | Maxis |
| platforms | PC, Console |
| subgenre | Life sim |
| sim domain | Domestic / personal, Social / interpersonal |
| player role | Caretaker |
| agency model | Direct unit control, Indirect incentive, Zoning / placement |
| time model | Real-time with pause |
| sim scale | Household / crew |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Permadeath |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | AAA |
| agent count order | ~10 |
| emergence | 3 |
| influence | 2 |
| influenced by | [The Sims 3](../game/the-sims-3.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 19 |

## Summary

The fourth mainline Sims game, built around a dominant emotion computed from moodlets, three-trait personalities with aspiration rewards, multitasking, room-based building, and an in-game Gallery for sharing creations.

## Core Loop

build a home or download one from the Gallery -> moodlets from events and surroundings set the dominant emotion -> emotion unlocks interactions and speeds skills -> pursue aspiration milestones and a career -> earn rewards -> share households and builds

## Design Notes

The Sims 4 makes emotion the central state: moodlets from actions, events, objects, and social interactions carry an emotion type and weight, and the strongest set the Sim's single dominant emotion, which gates emotional interactions and speeds matching skills. Adult personality is three traits plus a bonus trait from the chosen aspiration, and completing aspiration milestones grants reward traits. Build mode treats rooms as units that can be moved, duplicated, saved to a library, and shared through the Gallery; the base game became free to play on 2022-10-18. Neighborhood Stories, a free update that advances unplayed households, is the offscreen-life-progression mechanic.

## Relations

**influenced by**

- [The Sims 3](../game/the-sims-3.md)

**uses**

- [Memories and thoughts](../mechanic/memories-thoughts.md) (core): Moodlets carry an emotion type (such as Happy, Focused, Flirty, Angry, Tense, or Sad), an intensity, and a timer; the highest-weighted emotion becomes the Sim's dominant emotion.
- [Personality traits](../mechanic/personality-traits.md) (core): Adults hold three traits and children and teens two, plus one bonus trait from the aspiration; traits add moodlets, autonomous behaviors, and exclusive interactions.
- [Needs decay](../mechanic/needs-decay.md) (core): Six needs (Hunger, Bladder, Energy, Social, Hygiene, Fun) decay and spawn negative moodlets such as Hungry or Bored when low.
- [Mood and breakdowns](../mechanic/mood-breakdown.md) (supporting): Dominant emotions unlock emotion-specific interactions and raise gain for matching skills (Inspired for creative, Focused for mental, Energized for physical); extreme states such as Hysterical can kill.
- [Smart objects](../mechanic/smart-objects.md) (supporting): Objects advertise need, skill, and emotion gains, and Sims multitask, such as talking while cooking.
- [Building placement](../mechanic/free-placement.md) (supporting): Build mode draws walls and rooms, places premade rooms, and moves or duplicates whole rooms.
- [Blueprints](../mechanic/blueprints.md) (supporting): Sims, households, rooms, and lots can be saved to a personal library and placed again.
- [Content sharing](../mechanic/content-sharing.md) (supporting): The Gallery uploads and downloads Sims, households, rooms, and buildings from other players inside the game.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): Newborn, infant, toddler, child, teen, young adult, adult, and elder; toddlers were added in 2017 and newborn and infant in 2023.
- [Career ladder](../mechanic/career-ladder.md) (supporting): Careers require related skills, for example Cooking and Mixology for Culinary.
- [Agent skills](../mechanic/agent-skills.md) (supporting)
- [Relationship values](../mechanic/relationship-values.md) (supporting): Separate friendship and romance bars per pair.
- [Romance and family](../mechanic/romance-family.md) (supporting)
- [Social exchanges](../mechanic/social-exchanges.md) (supporting): Social menus are filtered by emotion and traits, with emotion-specific variants of interactions.
- [Autonomy levels](../mechanic/autonomy-levels.md) (supporting): Free will can be toggled; with it off Sims act only on player orders except for urgent needs.
- [Aspirations and wants](../mechanic/aspiration-wants.md) (supporting): The chosen aspiration grants a bonus trait and a track of milestones whose completion earns reward traits; short-term whims, later reworked as wants and fears, appear from emotions and traits.
- [Off-screen life progression](../mechanic/offscreen-life-progression.md) (supporting): Neighborhood Stories, added in a free update, advances unplayed households with events such as moves, relationships, and births, with settings that limit which households and event types it may touch.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Utility action selection](../mechanic/utility-action-selection.md) (supporting)

## Backlinks (computed)

**precedent for:** [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md)

## Sources

- [The Sims 4](../source/src-wikipedia-the-sims-4.md)
- [Motive](../source/src-simswiki-2026-motive.md)

---
Provenance: created in run `2026-10-24-catalog-gc`; reviewed in `2026-10-24-review-fixes`.
