# Dated technology timeline

*Mechanic* · `dated-tech-timeline` · status: **asserted**

New vehicle models, platforms, or products enter and leave availability on a calendar tied to in-game dates rather than to research, forcing fleet or platform renewal.

| field | value |
|---|---|
| aliases | era availability, calendar unlocks, model introduction dates, historical timeline |
| family | Progression & goals |
| substrate | Rule system |
| math basis | Scheduling, Optimization |
| feedback | None |
| player interface | Observation only, Choice / cards |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Railroad Tycoon](../game/railroad-tycoon.md) |
| earliest year *(computed)* | 1990 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

New vehicle models, platforms, or products enter and leave availability on a calendar tied to in-game dates rather than to research, forcing fleet or platform renewal.

## Definition

Owns a catalog of models (vehicles, consoles, components, building types), each with an introduction date, a retirement or obsolescence date, and stats, plus the rule that checks the in-game calendar each period and adds models to or removes them from what the player can buy or target. Availability depends only on the date, not on player spending, so every company gains the same options at the same time. New models often arrive with lower launch reliability or a short exclusive preview, and retired models can no longer be bought while existing units keep aging. Transport Tycoon (1994) introduces road, rail, sea, and air models on a timeline across its calendar, so fleets are renewed as better vehicles arrive and old ones lose reliability; Railroad Tycoon releases locomotives by era; Game Dev Tycoon launches and retires fictional consoles on a fixed timeline that forces platform bets. It differs from tech-tree, where unlocks are bought with accumulated research in an order the player chooses; here time alone unlocks.

## Player Experience

History arrives on schedule. The player watches the calendar for the next locomotive or console, plans when to switch, and lives with a fleet or catalog that ages out from under them. A new era is a forced renewal decision rather than a reward the player earned.

## Design Levers

- introduction and retirement dates per model, and whether they vary slightly between games
- start year and calendar speed, which choose the eras a game covers
- prototype or exclusive preview windows and launch reliability
- whether old models are withdrawn or stay buyable
- size of each generational jump

## Failure Modes

- Games that run past the last introduction date stall with nothing new to buy.
- Retiring a model without a successor leaves a role with no buyable vehicle or platform.
- Fixed dates become memorized, so experienced players plan purchases around known release years.
- Generational jumps so large that switching is always immediate remove the renewal decision.

## Dynamics

- Fleet renewal waves follow major introductions and cause cash crunches and service gaps.
- Every company gains new models at once, so competition shifts to who adopts and finances renewal best.
- Launch and retirement dates decide which platform bets pay off, as with console choice in Game Dev Tycoon.

## Open Questions

- Could introduction dates respond to simulated demand and rival research, making the timeline emergent rather than fixed?
- Does a historical timeline reward knowledge of real history in ways that help or hurt replayability?

## Backlinks (computed)

**used by:** [Game Dev Tycoon](../game/game-dev-tycoon.md), [Railroad Tycoon](../game/railroad-tycoon.md), [SimCity 2000](../game/simcity-2000.md), [Transport Tycoon](../game/transport-tycoon.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
