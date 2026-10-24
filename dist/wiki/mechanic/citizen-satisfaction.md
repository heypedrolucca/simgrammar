# Citizen satisfaction

*Mechanic* · `citizen-satisfaction` · status: **sourced**

An aggregate satisfaction score computed from services, conditions, and events modulates growth, productivity, and unrest.

| field | value |
|---|---|
| aliases | happiness, approval rating, city score |
| family | Governance & policy |
| substrate | Aggregate stocks |
| math basis | System dynamics / ODEs, Utility / decision theory |
| feedback | Both |
| player interface | Observation only |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 5 |
| earliest game *(computed)* | [Utopia](../game/utopia.md) |
| earliest year *(computed)* | 1982 |
| prevalence *(computed)* | 10 |
| prevalence share *(computed)* | 0.057 |
| subgenre spread *(computed)* | 3 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns one aggregate score (or one per district or class) computed each evaluation period from service levels, problems, and events, usually smoothed toward its previous value. Downstream systems read it: growth and migration, productivity, tax tolerance, election odds, and unrest. In Micropolis, the SimCity engine, a yearly evaluation sums seven problem values (crime, pollution, housing cost as 0.7 x average land value, taxes as rate x 10, traffic, unemployment, fires), maps the sum to a 0-1000 score, multiplies it by penalties for missing stadium, airport, or seaport (0.85 each), underfunded roads, police, and fire, and the share of unpowered zones, adjusts for population growth, and averages it with last year's score; an approval poll then gives 100 citizens a yes with probability score / 1000. Frostpunk (2018) splits the score into Hope and Discontent, and the game ends in revolt if hope stays too low or discontent too high for too long.

## Player Experience

A report card on the whole system. The player watches one number rise and fall, digs into the complaint list or overlays to find the cause, and fixes the top problem. In crisis games like Frostpunk it becomes the meter the player is always defending.

## Design Levers

- which inputs enter the score and their weights
- smoothing or averaging period, which sets how quickly fixes show up
- thresholds where satisfaction triggers growth, emigration, strikes, or game over
- single score versus separate scores per class, district, or faction
- how causes are explained (complaint lists, thoughts, polls, advisors)

## Failure Modes

- A single number hides which problem matters, so players chase the wrong fix without a breakdown view.
- Easy maximization by stacking one cheap amenity makes satisfaction irrelevant.
- Long smoothing makes improvements feel unrewarded and pushes players to over-correct.

## Dynamics

- Low satisfaction drives emigration, which lowers demand for services and can partly restore satisfaction for those who stay.
- Satisfaction tied to productivity creates spirals where unhappy workers produce less and services decline further.
- Scores averaged over time let a short crisis pass without punishment but punish sustained neglect.

## Open Questions

- Can LLM-voiced citizens explain their dissatisfaction in specific, accurate terms that point to real causes in the simulation?
- Is one aggregate score better or worse for play than many per-group scores when citizens can explain themselves?

## Relations

**synergy**

- [Stability and unrest](../mechanic/stability-unrest.md): Low satisfaction accumulates into unrest; unrest further lowers satisfaction.
- [Elections](../mechanic/elections.md): Satisfaction becomes votes, tying tenure to welfare (Tropico).
- [Immigration by attractiveness](../mechanic/immigration-attractiveness.md): Satisfied populations attract migrants; dissatisfied ones leave.

## Backlinks (computed)

**involved in:** [Participatory planning sandboxes](../opportunity/participatory-planning-sandboxes.md)

**used by:** [Against the Storm](../game/against-the-storm.md), [Sid Meier's Civilization](../game/civilization.md), [Frostpunk](../game/frostpunk.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Manor Lords](../game/manor-lords.md), [Rebel Inc.](../game/rebel-inc.md), [SimCity](../game/simcity-1989.md), [Tropico 6](../game/tropico-6.md), [Utopia](../game/utopia.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md)

## Sources

- [Micropolis: open-source SimCity source code](../source/src-hopkins-2008-micropolis.md)
- [Frostpunk](../source/src-wikipedia-frostpunk.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
