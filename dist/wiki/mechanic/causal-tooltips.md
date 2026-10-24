# Causal breakdown tooltips

*Mechanic* · `causal-tooltips` · status: **sourced**

Hovering a derived value shows the named modifiers that produce it, and terms inside the tooltip can be hovered in turn.

| field | value |
|---|---|
| aliases | nested tooltips, modifier breakdowns, tooltip breakdowns |
| family | Information & legibility |
| substrate | UI layer, Rule system |
| math basis | Probability / statistics |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 1 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 1 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Europa Universalis IV](../game/europa-universalis-4.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.3 |

## Definition

Any displayed derived value (mood, stability, price, income, work speed, battle strength) can be hovered to list its contributing terms, each with a label, source, sign, and magnitude, usually as base plus additive modifiers times multiplicative modifiers. Terms that are themselves derived or that name a game concept can be hovered again, opening a nested tooltip. The mechanic owns no simulation state but requires the simulation to compute values as explicit lists of labeled modifiers rather than opaque formulas. Update rule: on hover, read the modifier list for the value, sort and render it, and attach hover targets to sub-terms. Canonical forms: Paradox grand strategy (Europa Universalis IV, Stellaris), Crusader Kings III, which introduced nested tooltips on highlighted terms that Victoria 3 adopted, Victoria 3 tooltips breaking down battle calculations, RimWorld info-card stat breakdowns (skill and capacity factors behind work speed), and Civilization yield breakdowns.

## Player Experience

The player can interrogate any number until the lever appears. Opaque systems become debuggable: why is stability falling, which modifier expires next, what would fix it. Players who enjoy optimization dig through several levels; others glance at the top line.

## Design Levers

- recursion depth: one level of breakdown versus nested tooltips on every term
- whether tooltips can be pinned or locked so the player can move into them
- which modifiers are hidden from the breakdown, if any
- presentation of additive versus multiplicative terms, ordering, and rounding
- whether each modifier shows its remaining duration
- glossary links from terms to concept explanations

## Failure Modes

- Late-game modifier stacks grow into walls of numbers that no longer explain anything.
- Rounded or partial terms that do not sum to the displayed value erode trust in the whole interface.
- Values with clamps, caps, or nonlinear interactions are presented as simple sums and mislead.
- Hover-dependent design moves essential information off the main screen and works poorly with controllers and touch.

## Dynamics

- Full transparency speeds up optimization and exploit discovery, pushing play toward spreadsheet min-maxing.
- Because each new effect appears in breakdowns automatically, modifier architectures are easy for modders to extend legibly.
- Players learn the simulation's causal graph by walking tooltips, which lowers the need for external wikis.

## Open Questions

- When values come from a learned simulator instead of modifier lists, can attribution methods produce breakdowns players trust?
- Do counterfactual tooltips (what single change would flip this outcome) teach faster than additive breakdowns?

## Relations

**synergy**

- [Opinion modifiers](../mechanic/opinion-modifiers.md): Itemized modifiers are only legible when tooltips decompose them (Paradox titles).

## Backlinks (computed)

**affected by:** [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)

**involved in:** [Why-query over the simulation log](../opportunity/causal-why-query.md), [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md), [Negotiating faction AI](../opportunity/negotiating-faction-ai.md)

**used by:** [Crusader Kings III](../game/crusader-kings-3.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Victoria 3](../game/victoria-3.md)

## Claims

- Victoria 3 uses a nested tooltip system in which highlighted terms inside a tooltip open further tooltips, a system introduced by Crusader Kings III. *(confidence: medium)* [[64](../source/src-pcgamesn-2022-victoria-3-nested-tooltips.md)]
- Victoria 3 UX work repositioned tooltips so players can move into a nested tooltip without opening another, and added military tooltips that break down battle calculations. *(confidence: high)* [[65](../source/src-paradox-2023-victoria-3-dev-diary-74.md)]

## Sources

- [Victoria 3 nested tooltip system](../source/src-pcgamesn-2022-victoria-3-nested-tooltips.md)
- [Victoria 3 Dev Diary #74 - UX Improvements](../source/src-paradox-2023-victoria-3-dev-diary-74.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
