# Where Winds Meet

*Game* · `where-winds-meet` · status: **asserted**

An open-world martial-arts RPG whose NPCs answer free-text and voice chat through a live language model, included as an early large-audience deployment of runtime LLM characters.

| field | value |
|---|---|
| year | 2024 |
| developer | Everstone Studio (NetEase Games) |
| platforms | PC |
| subgenre | Systemic RPG |
| subgenre secondary | AI-native |
| sim domain | Social / interpersonal, Military / conflict |
| player role | Inhabitant |
| agency model | Direct avatar, Conversational |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | Third-person |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player, Co-op |
| modding | None |
| production tier | AAA |
| agent count order | ~100 |
| emergence | 2 |
| influence | 2 |
| boundary case | True |
| core loop | explore the open world -> talk to NPCs in free text or voice -> take quests and fights -> build reputation and skills -> explore further |
| cluster *(computed)* | C08 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 5 |

## Summary

An open-world martial-arts RPG whose NPCs answer free-text and voice chat through a live language model, included as an early large-audience deployment of runtime LLM characters.

## Design Notes

Included as a boundary case for natural-language interaction at scale. The Steam AI disclosure describes NPC text and voice chat generated in real time from player input. The main questline and combat remain authored and rule-based, so the language model sits beside the simulation rather than inside its state.

## Relations

**uses**

- [Natural-language interaction](../mechanic/natural-language-interaction.md) (core): Players type or speak to NPCs and receive live generated replies, per the game's Steam AI disclosure.
- [Direct avatar control](../mechanic/direct-avatar.md) (core): Third-person martial-arts traversal and combat.
- [Reputation](../mechanic/reputation.md) (supporting)
- [Relationship values](../mechanic/relationship-values.md) (supporting)
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting)

## Backlinks (computed)

**deploys:** [Realtime speech-to-speech and expressive TTS for characters](../technique/realtime-voice-models.md)

## Claims

- The Steam page discloses AI-driven NPC text and voice chat that responds to player input in real time; global PC release was 2025-11-14. *(confidence: high)* [[50](../source/src-steam-2025-where-winds-meet.md)]

## Sources

- [Where Winds Meet on Steam](../source/src-steam-2025-where-winds-meet.md)

---
Provenance: created in run `2026-10-24-catalog-additions`.
