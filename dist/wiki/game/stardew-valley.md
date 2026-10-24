# Stardew Valley

*Game* · `stardew-valley` · status: **sourced**

A farming and life sim in which the player restores an inherited farm over four 28-day seasons, splitting a daily energy budget among crops, animals, mining, fishing, and friendships with Pelican Town's residents.

| field | value |
|---|---|
| year | 2016 |
| developer | ConcernedApe |
| platforms | PC, Console, Handheld, Mobile |
| subgenre | Farming sim |
| subgenre secondary | Life sim |
| sim domain | Biological / ecological, Social / interpersonal, Economic |
| player role | Inhabitant |
| agency model | Direct avatar, Zoning / placement |
| time model | Real-time |
| sim scale | Facility |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Soft / recoverable |
| narrative mode | Hybrid |
| multiplayer | Single-player, Co-op |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 2 |
| influence | 4 |
| influenced by | [Harvest Moon](../game/harvest-moon.md) |
| cluster *(computed)* | C05 |
| core count *(computed)* | 5 |
| mechanic count *(computed)* | 15 |

## Summary

A farming and life sim in which the player restores an inherited farm over four 28-day seasons, splitting a daily energy budget among crops, animals, mining, fishing, and friendships with Pelican Town's residents.

## Core Loop

plan the day -> spend energy watering, harvesting, mining, or fishing -> sell crops and artisan goods -> buy seeds, tools, and buildings -> gift and talk to villagers -> complete Community Center bundles -> new areas and seasons open

## Design Notes

Eric Barone built Stardew Valley alone over about five years in response to Harvest Moon, keeping its seasonal crop calendar and town relationships while leaving the long-term structure open-ended. Each day is bounded by an energy bar refilled each morning and a clock that forces sleep, so play is a daily allocation problem across farming, foraging, fishing, mining, and socializing. Friendship is a point stock (250 points per heart, 10 hearts for most villagers) that loses 2 points per day without conversation and accepts two gifts per week, with birthday gifts worth eight times as much. Community Center bundles make collection the main progression gate.

## Relations

**influenced by**

- [Harvest Moon](../game/harvest-moon.md)

**uses**

- [Crop cultivation](../mechanic/crop-cultivation.md) (core): Seasonal seeds need daily watering (rain or sprinklers substitute) and grow through stages over set day counts; most crops must be harvested before the season changes.
- [Seasons](../mechanic/seasons.md) (core): Four 28-day seasons gate which crops grow, which fish and forage appear, and which festivals occur.
- [Daily action budget](../mechanic/daily-action-budget.md) (core): An energy bar refills each morning, drains with tool use, and is restored by food; the clock forces bed by 2 a.m. or the player passes out and loses money.
- [Relationship values](../mechanic/relationship-values.md) (core): Each villager has a friendship stock of 250 points per heart up to 10 hearts; it decays 2 points per day without talking, takes two gifts a week, multiplies birthday gifts by 8, and unlocks heart events.
- [Collection goals](../mechanic/collection-goals.md) (core): Community Center bundles ask for sets of crops, forage, fish, and artisan goods; completed rooms repair town infrastructure and unlock areas, and the museum collects minerals and artifacts.
- [Animal husbandry](../mechanic/animal-husbandry.md) (supporting): Barns and coops house animals that produce eggs, milk, and wool when fed and cared for; animals cannot be slaughtered.
- [Romance and family](../mechanic/romance-family.md) (supporting): Twelve marriage candidates regardless of player gender; spouses help with chores, and couples can have children.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Farming, foraging, fishing, mining, and combat levels rise with practice and unlock recipes and professions.
- [Production chains](../mechanic/production-chain.md) (supporting): Kegs, preserves jars, and other machines convert crops and animal products into higher-value artisan goods over fixed processing times.
- [Quality tiers](../mechanic/quality-tiers.md) (supporting): Crops and animal products come in normal, silver, gold, and iridium quality.
- [Villager requests](../mechanic/villager-requests.md) (supporting): A help-wanted board posts item, fishing, and slaying requests from townspeople.
- [Hand crafting](../mechanic/hand-crafting.md) (supporting): Recipes turn gathered materials into sprinklers, fences, machines, and bombs.
- [Daily schedules](../mechanic/daily-schedules.md) (supporting): Villagers follow routines that vary by weekday, season, and weather.
- [Weather](../mechanic/weather.md) (supporting): Rain waters crops and changes fish and villager routines.
- [Building placement](../mechanic/free-placement.md) (supporting)

## Backlinks (computed)

**precedent for:** [Content-elastic event systems](../opportunity/content-elastic-events.md)

## Sources

- [Stardew Valley](../source/src-wikipedia-stardew-valley.md)
- [Friendship](../source/src-stardewwiki-2026-friendship.md)
- [Bundles](../source/src-stardewvalleywiki-2026-bundles.md)

---
Provenance: created in run `2026-10-24-catalog-gc`; reviewed in `2026-10-24-review-fixes`.
