# Taxation

*Mechanic* · `taxation` · status: **sourced**

Player-set tax rates convert economic activity into revenue at the cost of growth, happiness, or competitiveness.

| field | value |
|---|---|
| aliases | tax rate, tax policy |
| family | Economy & finance |
| substrate | Aggregate stocks |
| math basis | System dynamics / ODEs, Optimization |
| feedback | Both |
| player interface | Parameter |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| requires | [Treasury and budget](../mechanic/budget-treasury.md) |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [SimCity](../game/simcity-1989.md) |
| earliest year *(computed)* | 1989 |
| prevalence *(computed)* | 13 |
| prevalence share *(computed)* | 0.075 |
| subgenre spread *(computed)* | 6 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Owns one or more tax rates (global, by zone type, by class, or by good) and converts a tax base into revenue each accounting period, while applying a growth or satisfaction penalty that rises with the rate. In Micropolis, the SimCity engine, revenue = population x average land value / 120 x tax rate x a difficulty factor; the rate (0-20%) indexes a table that offsets all three RCI demand valves by +200 at 0%, 0 at 7%, and -600 at 20% on the easiest level, enters the citizens' problem list as rate x 10, and is subtracted from the city score. SimCity 2000 lets players set separate residential, commercial, and industrial rates. Democracy 4 ties tax policies to voter-group happiness and makes very high taxes cause evasion. Victoria 3 derives the tax base from a taxation law and lets the player set an overall tax level.

## Player Experience

Turning a dial between money now and growth later. The player raises taxes to fund services or pay debts, then watches demand or approval sag and searches for the rate the economy will bear.

## Design Levers

- tax base (population, land value, income, trade, goods) and how many separate rates exist
- shape of the penalty curve (linear, threshold, accelerating) and where the neutral rate sits
- lag between a rate change and its effect on growth or approval
- avoidance responses such as evasion, emigration, or capital flight
- who bears the tax and which groups react

## Failure Modes

- A fixed neutral point (Micropolis' 7%) becomes a memorized constant, so the lever is set once and forgotten.
- When revenue uses the rate at the moment of collection, as in Micropolis, players can keep taxes low most of the year and raise them just before collection.
- A single global rate removes distributional choices and the politics around them.

## Dynamics

- Revenue funds services that grow the tax base while high rates suppress growth, so a revenue-maximizing rate emerges.
- Different rates by zone or class let players steer development, such as cutting industrial taxes to attract jobs.
- Tax hikes during a crisis can trigger emigration that shrinks the base and deepens the deficit.

## Open Questions

- Could AI-simulated households and firms respond to tax changes with realistic avoidance and migration, making tax design a policy puzzle rather than one slider?
- How should tax effects be lagged so the tradeoff is felt without enabling raise-before-collection exploits?

## Relations

**requires**

- [Treasury and budget](../mechanic/budget-treasury.md)

## Backlinks (computed)

**affected by:** [Many-agent LLM societies](../technique/llm-agent-societies.md)

**used by:** [Caesar III](../game/caesar-3.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Sid Meier's Civilization](../game/civilization.md), [Democracy 4](../game/democracy-4.md), [Eco](../game/eco.md), [Foundation](../game/foundation.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Manor Lords](../game/manor-lords.md), [Project Sid](../game/project-sid.md), [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [SimCity 4](../game/simcity-4.md), [Victoria 3](../game/victoria-3.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)
- [SimCity 2000](../source/src-wikipedia-simcity-2000.md)
- [Democracy 4](../source/src-wikipedia-democracy-4.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
