# Two Point Hospital

*Game* · `two-point-hospital` · status: **sourced**

A hospital management game and spiritual successor to Theme Hospital in which the player builds rooms, trains staff with traits and qualifications, and cures comic illnesses across a chain of hospitals.

| field | value |
|---|---|
| year | 2018 |
| developer | Two Point Studios |
| platforms | PC, Console, Handheld |
| subgenre | Management / tycoon |
| subgenre secondary | Medical sim |
| sim domain | Medical, Economic |
| player role | Manager / owner |
| agency model | Zoning / placement, Policy / parameter, Direct unit control |
| time model | Real-time with pause |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | None |
| multiplayer | Single-player, Co-op, Competitive, Async / shared content |
| modding | Content |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| influenced by | [Theme Hospital](../game/theme-hospital.md) |
| cluster *(computed)* | C03 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 15 |

## Summary

A hospital management game and spiritual successor to Theme Hospital in which the player builds rooms, trains staff with traits and qualifications, and cures comic illnesses across a chain of hospitals.

## Core Loop

build and decorate rooms -> hire staff with traits and train qualifications -> patients flow from GP to diagnosis to treatment -> cures earn money and reputation -> research and Kudosh unlock items -> earn stars to open the next hospital

## Design Notes

Two Point Hospital keeps Theme Hospital's room-blueprint and diagnosis-pipeline structure and adds a deeper staff layer: every hire has personality traits, a specialisation, and trainable qualifications, so the training room is a second production line beside the clinical one. Room prestige rises with room size and decoration and feeds staff happiness, which links interior design to staff retention. Progress spreads across many hospitals with one-to-three-star goals, and items unlock with Kudosh, a currency earned from challenges rather than money. Assistants can run marketing campaigns (proposed mechanic advertising-awareness).

## Relations

**influenced by**

- [Theme Hospital](../game/theme-hospital.md)

**uses**

- [Diagnosis and treatment](../mechanic/diagnosis-treatment.md) (core): Patients start in a GP's Office and move through further diagnostic rooms until diagnosed, then to a treatment room; illnesses are comic, such as Light-Headedness and Mock Star.
- [Staff hiring and rosters](../mechanic/staff-hiring.md) (core): Doctors, nurses, janitors, and assistants come with personality traits and specialisations that change performance; wages and morale must be managed.
- [Service queues](../mechanic/service-queues.md) (core): Patients queue at rooms while their health falls; untreated patients die, and long waits lower satisfaction.
- [Building placement](../mechanic/free-placement.md) (core): Rooms are drawn and furnished with required machines, plus corridors with toilets, cafes, vending machines, and staff rooms.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Staff earn qualifications in the training room that unlock or improve tasks.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Staff traits change efficiency and behavior.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (supporting): Room prestige depends on size and decoration and affects staff happiness.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Patients and staff need toilets, food, drinks, and rest.
- [Contagion](../mechanic/contagion.md) (supporting): Later levels bring epidemics with a limited vaccine supply; immunizing every infected patient earns a reward.
- [Wear and breakdown](../mechanic/wear-breakdown.md) (supporting): Machines degrade and need janitor maintenance.
- [Tech tree](../mechanic/tech-tree.md) (supporting): The Research room unlocks new rooms and machine upgrades.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Kudosh from challenges unlocks items; one star unlocks the next hospital.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Each hospital has star objectives; extra objectives raise the rating to two or three stars.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Steam Workshop support added in 2019.
- [Advertising and awareness](../mechanic/advertising-awareness.md) (supporting): Assistants in the marketing room run paid campaigns that draw more patients, optionally targeted at specific illnesses.

## Sources

- [Two Point Hospital](../source/src-wikipedia-two-point-hospital.md)

---
Provenance: created in run `2026-10-24-catalog-ge`.
