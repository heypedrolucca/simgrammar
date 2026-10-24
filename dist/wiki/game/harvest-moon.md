# Harvest Moon

*Game* · `harvest-moon` · status: **sourced**

An early farming sim for the Super Famicom in which the player has two and a half years to restore an inherited farm through daily crop watering, livestock care, and courting one of five eligible women.

| field | value |
|---|---|
| aliases | Bokujō Monogatari |
| year | 1996 |
| developer | Amccus |
| platforms | Console, Handheld |
| subgenre | Farming sim |
| subgenre secondary | Life sim |
| sim domain | Biological / ecological, Social / interpersonal |
| player role | Inhabitant |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player |
| modding | None |
| production tier | AA |
| agent count order | ~10 |
| emergence | 2 |
| influence | 4 |
| cluster *(computed)* | C05 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

An early farming sim for the Super Famicom in which the player has two and a half years to restore an inherited farm through daily crop watering, livestock care, and courting one of five eligible women.

## Core Loop

clear land and plant seasonal crops -> water daily and tend livestock -> ship produce for money -> buy animals, seeds, and upgrades -> build relationships and attend festivals -> marry and raise a child before the father's evaluation

## Design Notes

Director Yasuhiro Wada started the project with three principles (no fighting, uniqueness, and tactile real-time action), and a team of 8 to 10 people at Pack-In-Soft scaled it back to fit SNES limits. The farm rules are forgiving but daily: unwatered crops stop growing instead of dying, chickens need only feed but can die if left outside, and cows must be fed, talked to, brushed, and milked or they sicken. Play is bounded by a two-and-a-half-year term that ends with the father's evaluation of the farm and family, which makes marriage and a child goals alongside crops and livestock.

## Relations

**uses**

- [Crop cultivation](../mechanic/crop-cultivation.md) (core): Crops need water every day; a missed day halts growth rather than killing the plant, and each crop belongs to a season.
- [Animal husbandry](../mechanic/animal-husbandry.md) (core): Chickens must be fed and kept indoors or they can die; cows need daily feed, talking, brushing, and milking, and fall sick or die if neglected.
- [Seasons](../mechanic/seasons.md) (core): A four-season calendar sets which crops can grow and when festivals occur.
- [Daily action budget](../mechanic/daily-action-budget.md) (supporting): A stamina pool limits work each day; power berries found around the map raise it.
- [Romance and family](../mechanic/romance-family.md) (supporting): Five eligible women can be courted; marriage and a child count toward the final evaluation.
- [Relationship values](../mechanic/relationship-values.md) (supporting): Villagers' and candidates' affection rises with talking and gifts.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): After two and a half years the father evaluates the farm, family, and relationships.
- [Day-night cycle](../mechanic/day-night-cycle.md) (supporting): After dark only the bar stays open, so shopping and visits must fit daylight.

## Backlinks (computed)

**influenced:** [Stardew Valley](../game/stardew-valley.md)

## Sources

- [Harvest Moon (video game)](../source/src-wikipedia-harvest-moon.md)
- [Harvest Moon (SNES) guide](../source/src-fogu-2026-harvest-moon-snes.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
