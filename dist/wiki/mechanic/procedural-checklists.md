# Procedural checklists

*Mechanic* · `procedural-checklists` · status: **sourced**

Operating simulated equipment requires performing ordered steps on modeled controls that mirror real procedures, with system states gating each step.

| field | value |
|---|---|
| aliases | cold start, startup procedures, study-sim procedures |
| family | Operation & procedure |
| substrate | Rule system |
| math basis | Computation theory, Scheduling |
| feedback | None |
| player interface | Direct manipulation |
| legibility | 3 |
| emergence potential | 2 |
| authoring cost | 4 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [X-Plane](../game/x-plane.md) |
| earliest year *(computed)* | 1995 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Equipment is modeled as interacting subsystems (electrical, fuel, hydraulic, engines, avionics) whose states are changed through individually operable controls. A procedure is an ordered sequence of control actions with preconditions on subsystem state; doing steps out of order produces the physical result of that order, such as a failed engine start, rather than an error message. DCS World models aircraft from real-world data, with clickable cockpit switches and subsystems such as engines, fuel, electrical, hydraulics, and radios, and the U.S. Air Force's 355th Training Squadron uses it as an A-10C instrument and weapons-systems trainer. Microsoft Flight Simulator offers interactive checklists with optional copilot assistance. Inputs: control manipulations. Outputs: subsystem states and operational readiness.

## Player Experience

Mastery through ritual. Players study manuals, practice startup sequences until they are reflexive, and feel competence when a complex machine comes alive under their hands. Mistakes teach how the systems connect.

## Design Levers

- number of modeled subsystems and controls
- strictness: whether wrong orders fail realistically or are forgiven
- assists such as auto-start, checklist overlays, or copilot automation
- manual and tutorial depth
- failure injection during procedures

## Failure Modes

- Long procedures before any action exclude newcomers unless an auto-start or assisted mode is offered.
- When the underlying systems are not simulated, steps become arbitrary button sequences.
- Missing feedback leaves players unable to tell which step went wrong.

## Dynamics

- Communities share checklists, tutorials, and training videos, and some organize realistic group operations.
- Injected failures turn memorized procedures into troubleshooting.
- Assists create a ladder from casual to study-level play inside one product.

## Open Questions

- Can a voice-driven AI instructor or crew member coach procedures adaptively from the live subsystem state?
- Can procedure models be extracted from real manuals automatically to cut the cost of new equipment?

## Backlinks (computed)

**involved in:** [Simulator instructor coaching](../opportunity/sim-instructor-coach.md)

**used by:** [DCS World](../game/dcs-world.md), [Hardspace: Shipbreaker](../game/hardspace-shipbreaker.md), [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [Silent Hunter III](../game/silent-hunter-3.md), [X-Plane](../game/x-plane.md)

## Sources

- [DCS World](../source/src-wikipedia-dcs-world.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
