# Suzerain

*Game* · `suzerain` · status: **sourced**

A text-based political narrative game in which the player, as newly elected President Anton Rayne of Sordland, makes dialogue and policy choices across one term that shift the budget, foreign alignment, and constitutional reform toward one of several endings.

| field | value |
|---|---|
| year | 2020 |
| developer | Torpor Games |
| platforms | PC, Console, Handheld, Mobile |
| subgenre | Political sim |
| sim domain | Political / governance, Social / interpersonal |
| player role | Ruler / statesman |
| agency model | Policy / parameter |
| time model | Turn-based |
| sim scale | Nation / polity |
| fidelity | Stylized |
| perspective | Text / UI |
| win structure | Campaign |
| failure model | Soft / recoverable |
| narrative mode | Authored |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 1 |
| influence | 1 |
| boundary case | True |
| cluster *(computed)* | C11 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 6 |

## Summary

A text-based political narrative game in which the player, as newly elected President Anton Rayne of Sordland, makes dialogue and policy choices across one term that shift the budget, foreign alignment, and constitutional reform toward one of several endings.

## Core Loop

read briefings and dialogue -> choose responses and policy decisions -> budget, alignment, and story flags update -> later options open or close -> reach an ending and a political-compass result

## Design Notes

Suzerain is mostly authored text, about 450,000 words, in which choices are recorded as state: the budget and accumulated decisions gate later dialogue options and endings. It is a boundary case included for how a political game can run on dilemma choices and state-gated story branches rather than an equation network. The ending screen places the player on an in-universe political compass computed from choices made across the term.

## Relations

**uses**

- [Dilemma cards](../mechanic/dilemma-cards.md) (core): Ministers, advisers, and family members present situations as dialogue, and multiple-choice responses on constitutional reform, economic model, security, and welfare trade off budget, alignment, and later options.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (core): Story chapters branch on recorded choices, opening or closing later scenes and deciding which ending the term reaches.
- [Treasury and budget](../mechanic/budget-treasury.md) (supporting): Available budget and resources are shown and drawn down by decisions.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Sordland can side with the western or eastern bloc or stay neutral, and deals with its neighbor Rumburg.
- [Policy toggles](../mechanic/policy-toggles.md) (supporting): Major choices set constitutional reforms and a market-driven or centrally planned economy.
- [Advisors](../mechanic/advisors.md) (supporting): Ministers and advisers brief the president and argue positions.

## Backlinks (computed)

**precedent for:** [Natural-language legislation](../opportunity/natural-language-legislation.md)

## Sources

- [Suzerain (video game)](../source/src-wikipedia-suzerain.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
