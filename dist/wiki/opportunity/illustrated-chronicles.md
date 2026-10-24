# Illustrated chronicles

*Opportunity* · `illustrated-chronicles` · status: **asserted**

Turn a run's event log into a readable, illustrated saga that players can share, making emergent stories legible and portable.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [History chronicle](../mechanic/history-chronicle.md), [Content sharing](../mechanic/content-sharing.md), [Simulated history generation](../mechanic/history-generation.md), [Procedural characters](../mechanic/procedural-characters.md) |
| applies | [LLM game master and narrative director](../technique/llm-game-master.md), [LLM explanation of simulation state](../technique/llm-explanation-of-state.md), [Text- and image-to-3D asset generation](../technique/text-to-3d-assets.md) |
| precedent | [Dwarf Fortress](../game/dwarf-fortress.md), [RimWorld](../game/rimworld.md), [Crusader Kings III](../game/crusader-kings-3.md), [Kenshi](../game/kenshi.md) |
| novelty | 2 |
| feasibility | 5 |
| impact | 2 |
| horizon | Now |
| key risks | Summaries invent drama the log does not support., Generated art quality and disclosure., Players who enjoy writing their own stories may feel replaced. |
| falsifiable signal | {'prediction': "A systemic simulation game will ship an automatic, shareable narrative summary of a run's history generated from its event log.", 'resolve_by': '2027-12-31', 'criteria': 'Feature first shipped after 2026-10-24 in a released title or official expansion with at least 1,000 Steam user reviews; patch notes or store text describe an automatically written run history the player can export or share.'} |
| priority *(computed)* | 2.756 |

## Thesis

Players of systemic games already write their runs up as stories (Boatmurdered, colony diaries). Dwarf Fortress's legends mode stores the raw material but presents it as a database. Summarization over event logs, with grounding to cited events and generated illustrations, can produce shareable chapters automatically, which also markets the game.

## Design Sketch

At the end of each in-game year, the chronicle drafts a chapter: key events, characters, turning points, written in a selectable voice and illustrated with generated images grounded in the logged entities. Every sentence links to its source events. Players edit and publish chronicles to a shared library.

## Key Risks

- Summaries invent drama the log does not support.
- Generated art quality and disclosure.
- Players who enjoy writing their own stories may feel replaced.

## Validation Experiment

Generate chronicles for 30 logged colony runs and have their players rate accuracy and whether they would share them. Success: average accuracy above 4 of 5 and more than half willing to share.

## Falsifiable signal

- **Prediction:** A systemic simulation game will ship an automatic, shareable narrative summary of a run's history generated from its event log.
- **Resolve by:** 2027-12-31
- **Criteria:** Feature first shipped after 2026-10-24 in a released title or official expansion with at least 1,000 Steam user reviews; patch notes or store text describe an automatically written run history the player can export or share.

## Relations

**applies**

- [LLM game master and narrative director](../technique/llm-game-master.md)
- [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)
- [Text- and image-to-3D asset generation](../technique/text-to-3d-assets.md)

**involves**

- [History chronicle](../mechanic/history-chronicle.md)
- [Content sharing](../mechanic/content-sharing.md)
- [Simulated history generation](../mechanic/history-generation.md)
- [Procedural characters](../mechanic/procedural-characters.md)

**precedent**

- [Dwarf Fortress](../game/dwarf-fortress.md)
- [RimWorld](../game/rimworld.md)
- [Crusader Kings III](../game/crusader-kings-3.md)
- [Kenshi](../game/kenshi.md)

---
Provenance: created in run `2026-10-24-synthesis`; reviewed in `2026-10-24-review-fixes`.
