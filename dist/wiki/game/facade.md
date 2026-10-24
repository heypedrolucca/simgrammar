# Façade

*Game* · `facade` · status: **sourced**

A free 2005 interactive drama in which the player types natural language as a dinner guest of the married couple Grace and Trip while a drama manager sequences authored beats toward one of three endings.

| field | value |
|---|---|
| aliases | Facade |
| year | 2005 |
| developer | Procedural Arts |
| platforms | PC |
| subgenre | Social sim |
| sim domain | Social / interpersonal |
| player role | Inhabitant |
| agency model | Conversational, Direct avatar |
| time model | Real-time |
| sim scale | Household / crew |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | Academic / research |
| agent count order | ~1 |
| emergence | 2 |
| influence | 2 |
| boundary case | True |
| cluster *(computed)* | C08 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 5 |

## Summary

A free 2005 interactive drama in which the player types natural language as a dinner guest of the married couple Grace and Trip while a drama manager sequences authored beats toward one of three endings.

## Core Loop

type to or touch Grace and Trip -> parser maps input to a discourse act -> characters react and tension shifts -> drama manager picks the next beat -> secrets surface -> the couple reconciles, splits, or throws the player out

## Design Notes

Michael Mateas and Andrew Stern built Façade as a research artifact: Grace and Trip are written in A Behavior Language (ABL) as reactive behaviors, and a drama manager picks the next story beat from an authored library to follow a tension arc toward a climax. Typed text is mapped to a small set of discourse acts (the Versu paper counts 30 parameterized speech acts and 27 beats), which lets a limited body of authored dialogue answer open-ended input. It is a boundary case: the simulated systems are the parser, character behaviors, and beat sequencing over mostly authored dialogue, built for replay so players can find other outcomes.

## Relations

**uses**

- [Natural-language interaction](../mechanic/natural-language-interaction.md) (core): Typed sentences are matched by keywords and context to discourse acts such as agreeing, criticizing, or flirting, which Grace and Trip answer in character.
- [Storyteller director](../mechanic/storyteller-director.md) (core): A drama manager chooses the next beat whose preconditions match the state, steering toward a rising tension arc and one of three endings.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Revelations such as a confessed affair fire only when earlier beats and player choices set them up.
- [Relationship values](../mechanic/relationship-values.md) (supporting): As the couple argues, the player's responses read as taking one side, which shapes later beats.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): The player walks around the apartment in first person and can click objects or body parts to hug, comfort, or kiss.

## Sources

- [Façade (video game)](../source/src-wikipedia-facade.md)
- [Versu: A Simulationist Storytelling System](../source/src-evans-2014-versu.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
