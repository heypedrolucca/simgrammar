# Territorial control

*Mechanic* · `territorial-control` · status: **asserted**

Map regions have an owner and a current controller; occupation flips control in war, and peace, purchase, or integration transfers ownership at a cost in time, unrest, or political currency.

| field | value |
|---|---|
| aliases | province ownership, occupation and annexation, claims and integration, coring |
| family | Conflict & defense |
| substrate | Network / graph, Rule system, Aggregate stocks |
| math basis | Game theory, System dynamics / ODEs |
| feedback | Both |
| player interface | Orders, Observation only |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Sid Meier's Civilization](../game/civilization.md) |
| earliest year *(computed)* | 1991 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

Map regions have an owner and a current controller; occupation flips control in war, and peace, purchase, or integration transfers ownership at a cost in time, unrest, or political currency.

## Definition

Owns, per map region (province, county, state, star system, city), an owner, a controller, and an integration state such as core, claim, incorporated, or newly conquered, plus claims that other factions hold on it. Military presence or a completed siege sets the controller; ownership changes only through a peace settlement, inheritance, purchase, or capture rule; and a newly owned region ramps from low to full integration over time or for a price, yielding less and generating more unrest until then. Europa Universalis IV separates owner from controller, makes new provinces costly to core with administrative power, and counts uncored land toward overextension, which raises unrest. Crusader Kings III ties counties to titles and de jure claims and adds a county control value that drops after conquest. Victoria 3 incorporates states over time; Hearts of Iron IV separates core from occupied states; Stellaris takes systems by building outposts and spends influence on claims against rivals. Unlike faction-diplomacy, which owns relations between factions, this mechanic owns who holds each piece of the map.

## Player Experience

Expansion has a shape and a hangover. The player plans conquests around claims, watches borders shift as sieges complete, then spends years digesting new land before it pays off. The map itself becomes the scoreboard, and an overstretched realm with restless new provinces is a visible warning to slow down.

## Design Levers

- separation of owner and controller, and what occupation alone grants
- integration path: time, a currency such as administrative power or influence, or culture and religion matching
- penalties for unintegrated land: reduced output, unrest, overextension, or rebel spawns
- claim types and how claims are created, fabricated, inherited, or expire
- region granularity: provinces, counties, states, systems, or cities

## Failure Modes

- Integration costs too low make snowballing conquest the only strategy; too high and expansion stops being worth it.
- Border gore and fragmented holdings from inheritance or peace deals become tedious to manage without consolidation tools.
- Players treat the map as a coloring exercise and ignore the systems that integration was meant to engage.

## Dynamics

- Conquest snowballs because new land adds resources and manpower, while integration costs and unrest apply the brake.
- Claims and de jure boundaries steer wars toward historically plausible borders.
- Occupation without ownership creates leverage for peace negotiations, coupling the map to war score.

## Open Questions

- Could AI factions that reason about claims and integration costs expand in ways players read as purposeful rather than greedy?
- What integration model keeps conquest consequential without becoming a waiting timer?

## Backlinks (computed)

**used by:** [Sid Meier's Civilization](../game/civilization.md), [Crusader Kings III](../game/crusader-kings-3.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Stellaris](../game/stellaris.md), [Victoria 3](../game/victoria-3.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-b`.
