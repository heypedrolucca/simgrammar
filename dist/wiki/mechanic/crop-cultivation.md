# Crop cultivation

*Mechanic* · `crop-cultivation` · status: **sourced**

Planted crops progress through growth stages over days or seasons depending on water, soil, and season, then are harvested.

| field | value |
|---|---|
| aliases | farming, growing, agriculture |
| family | Resources & production |
| substrate | Cellular grid, Aggregate stocks, Rule system |
| math basis | System dynamics / ODEs, Optimization |
| feedback | None |
| player interface | Placement, Direct manipulation, Orders |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| core count *(computed)* | 8 |
| earliest game *(computed)* | [Hamurabi](../game/hamurabi.md) |
| earliest year *(computed)* | 1968 |
| prevalence *(computed)* | 25 |
| prevalence share *(computed)* | 0.144 |
| subgenre spread *(computed)* | 10 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Each planted cell or field holds a crop type, a growth progress value, and condition flags such as watered, fertilized, or diseased. Each tick or day, progress advances at a base rate multiplied by modifiers for soil fertility, water, light, temperature, and season; outside allowed conditions growth stops or the plant dies. At maturity the crop is harvested for a yield, sometimes scaled by care or skill, and the cell resets, regrows, or loses fertility. Harvest Moon and Stardew Valley require daily watering and tie crops to seasons of a fixed calendar; RimWorld scales growth by soil fertility and light and halts it outside a temperature band; Farming Simulator turns field preparation, sowing, fertilizing, and harvesting into vehicle operations; Manor Lords and Farthest Frontier track soil fertility per field and reward crop rotation. Inputs: seeds, labor or player actions, environmental conditions. Outputs: harvested goods and an updated field state.

## Player Experience

Planning around a delayed payoff. The player commits land and time now for a harvest days or a season later, then guards the field against weather, pests, and neglect. In avatar farming games the daily watering round becomes a ritual; in colony sims the growing season becomes a deadline that sets how much must be stored for winter.

## Design Levers

- growth duration per crop and number of visible stages
- which conditions gate growth (water, light, temperature, season, fertility) and whether violating them pauses or kills the crop
- single-harvest versus regrowing crops
- yield and quality modifiers from fertilizer, skill, or care
- soil fertility depletion and recovery rules, including rotation or fallow
- labor or action cost of planting, tending, and harvesting

## Failure Modes

- Daily manual tending scales poorly, so large farms become rote clicking until automation such as sprinklers arrives.
- One crop with the best value per day dominates and planting choice disappears.
- Season-change crop deaths feel arbitrary when the calendar is not prominent.
- Growth too fast relative to consumption makes food trivial; growth too slow with harsh winters makes early runs unwinnable.

## Dynamics

- Harvests arrive in pulses, creating labor peaks that compete with construction and hauling.
- Seasonal growth windows couple farming to storage and spoilage, turning winter into a stockpiling test.
- Soil depletion pushes expansion onto new land or forces rotation schedules.
- Weather events and blights can wipe out a season and cascade into famine.

## Open Questions

- Can learned plant growth models give crops plausible responses to microclimate that players can still reason about?
- How much automation can farming absorb before cultivation stops being a decision?

## Relations

**synergy**

- [Daily action budget](../mechanic/daily-action-budget.md): Watering and harvesting consume the daily energy budget, forcing farm sizing tradeoffs.
- [Seasons](../mechanic/seasons.md): Season-locked crops create a calendar of planting decisions.

## Backlinks (computed)

**involved in:** [Learned regional weather](../opportunity/learned-weather-layer.md)

**used by:** [Autonauts](../game/autonauts.md), [Banished](../game/banished.md), [Captain of Industry](../game/captain-of-industry.md), [Don't Starve](../game/dont-starve.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Farming Simulator 25](../game/farming-simulator-25.md), [Farthest Frontier](../game/farthest-frontier.md), [Going Medieval](../game/going-medieval.md), [Hamurabi](../game/hamurabi.md), [Harvest Moon](../game/harvest-moon.md), [Kenshi](../game/kenshi.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Manor Lords](../game/manor-lords.md), [Minecraft](../game/minecraft.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Pharaoh](../game/pharaoh.md), [Project Zomboid](../game/project-zomboid.md), [RimWorld](../game/rimworld.md), [Schedule I](../game/schedule-i.md), [Stardew Valley](../game/stardew-valley.md), [Stationeers](../game/stationeers.md), [The Farmer Was Replaced](../game/the-farmer-was-replaced.md), [Timberborn](../game/timberborn.md), [Valheim](../game/valheim.md), [Viva Piñata](../game/viva-pinata.md)

## Sources

- [Harvest Moon (video game)](../source/src-wikipedia-harvest-moon.md)
- [Stardew Valley](../source/src-wikipedia-stardew-valley.md)

---
Provenance: created in run `2026-10-24-taxonomy-m1`.
