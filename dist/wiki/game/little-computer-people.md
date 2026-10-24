# Little Computer People

*Game* · `little-computer-people` · status: **sourced**

A 1985 home-computer life sim in which one procedurally seeded little person lives in a cross-section of a three-story house, follows a daily routine, and depends on the player for food, water, and attention.

| field | value |
|---|---|
| aliases | Apple Town Story |
| year | 1985 |
| developer | Activision |
| platforms | Mainframe / early micro, PC, Console |
| subgenre | Life sim |
| subgenre secondary | Virtual pet |
| sim domain | Domestic / personal, Social / interpersonal |
| player role | Caretaker |
| agency model | Caretaking interaction, Conversational |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~1 |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 6 |

## Summary

A 1985 home-computer life sim in which one procedurally seeded little person lives in a cross-section of a three-story house, follows a daily routine, and depends on the player for food, water, and attention.

## Core Loop

watch the resident's routine -> hunger, thirst, and mood drift -> deliver food, water, gifts, or pats -> type polite requests -> mood decides whether he complies -> repeat across sessions

## Design Notes

Rich Gold conceived the game and David Crane built it at Activision; the documentation presents the little people as real beings living inside the computer, with the player as their caretaker. Each disk's serial number seeded the resident's name (from 256), shirt color, personality, and behavior, so every copy hosted a different person. There is no win condition: the resident cooks, reads, plays piano, phones, and types letters about his feelings on a day of about six real-time hours, and his mood gates whether typed requests are obeyed. The cassette C64 version dropped memory, letters, and card games, which shows which systems carried the sense of a persistent person.

## Relations

**uses**

- [Creature care](../mechanic/creature-care.md) (core): Keyboard commands deliver food (CTRL+F), add water to his tank (CTRL+W), deliver dog food, pat him, or give records and books; a resident left unfed turns green and sick until he eats.
- [Needs decay](../mechanic/needs-decay.md) (core): Hunger and thirst build between deliveries; unmet needs lower his mood and eventually make him visibly sick.
- [Procedural characters](../mechanic/procedural-characters.md) (core): The disk serial number seeds his name from a pool of 256, his shirt color, personality, and behavior parameters.
- [Daily schedules](../mechanic/daily-schedules.md) (supporting): He runs a routine of cooking, watching television, reading the newspaper, playing records, and dancing on a compressed day of about six real-time hours.
- [Natural-language interaction](../mechanic/natural-language-interaction.md) (supporting): Typed requests such as 'Please play piano' are matched against a keyword vocabulary; politeness helps, and a sad or sick resident may refuse.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Seeded personality and mood parameters change which activities he prefers, how often he invites the player to cards or writes letters, and how readily he obeys.

## Backlinks (computed)

**influenced:** [The Sims](../game/the-sims.md)

## Sources

- [Little Computer People](../source/src-wikipedia-little-computer-people.md)
- [Little Computer People](../source/src-c64wiki-2026-little-computer-people.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
