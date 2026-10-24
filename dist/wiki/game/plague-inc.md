# Plague Inc.

*Game* · `plague-inc` · status: **sourced**

A strategy game in which the player evolves a pathogen's transmission, symptoms, and abilities to infect and kill the world's population before humanity's cure research finishes.

| field | value |
|---|---|
| aliases | Plague Inc: Evolved |
| year | 2012 |
| developer | Ndemic Creations |
| platforms | Mobile, PC, Console |
| subgenre | Ecosystem / evolution |
| sim domain | Medical, Biological / ecological |
| player role | God |
| agency model | Policy / parameter |
| time model | Real-time with pause |
| sim scale | Planet |
| fidelity | Stylized |
| perspective | Top-down / side 2D |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | Hybrid |
| multiplayer | Single-player, Competitive, Co-op |
| modding | Content |
| production tier | Indie |
| agent count order | Aggregate only |
| emergence | 2 |
| influence | 2 |
| cluster *(computed)* | C10 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 9 |

## Summary

A strategy game in which the player evolves a pathogen's transmission, symptoms, and abilities to infect and kill the world's population before humanity's cure research finishes.

## Core Loop

infect patient zero -> infections spread within and between countries -> earn DNA points -> buy transmission, symptom, and ability evolutions -> severity raises awareness and cure funding -> race to kill everyone before the cure completes

## Design Notes

James Vaughan's game inverts the epidemic model: the player owns the pathogen's parameters, and humanity's response (awareness, closures, cure research) is the opponent. The tension is between infectivity and severity, because visible symptoms and deaths accelerate the cure, so successful plans spread quietly and then turn lethal. Countries differ by climate and conditions the pathogen must adapt to, and the CDC invited Vaughan to discuss its infection model in 2013, though Ndemic has said it is not on par with scientific models. Evolved adds 10 disease types, 23 scenarios, versus and co-op modes, and a scenario creator with Workshop sharing.

## Relations

**uses**

- [Contagion](../mechanic/contagion.md) (core): Infection spreads within countries and between them along travel links, at rates set by the pathogen's transmission traits and each country's conditions, until countries are fully infected and then depopulated.
- [Tech tree](../mechanic/tech-tree.md) (core): DNA points buy nodes in three trees (transmission, symptoms, abilities); symptoms raise severity and lethality, and abilities resist climate and drugs.
- [Crisis countdown](../mechanic/crisis-countdown.md) (core): Once the disease is noticed, countries fund cure research shown as a global progress bar; finishing it ends the run, so the player races to kill before it fills.
- [Habitat suitability](../mechanic/habitat-suitability.md) (supporting): Hot, cold, and other national conditions slow a pathogen that lacks the matching resistance evolutions.
- [Alerts feed](../mechanic/alerts-feed.md) (supporting)
- [Stats dashboards](../mechanic/stats-dashboards.md) (supporting)
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Evolved ships 23 scenarios and 10 disease types, each with altered rules.
- [Modding API](../mechanic/modding-api.md) (supporting): The Evolved scenario creator builds custom plagues, worlds, and events, with over 10,000 shared on Steam Workshop.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**influenced:** [Rebel Inc.](../game/rebel-inc.md)

**precedent for:** [Calibrated serious simulations](../opportunity/calibrated-serious-sims.md)

## Claims

- The CDC invited creator James Vaughan to speak in March 2013 about the game's infection model. *(confidence: high)* [[30](../source/src-wikipedia-plague-inc.md), [31](../source/src-steam-2026-plague-inc-evolved.md)]

## Sources

- [Plague Inc.](../source/src-wikipedia-plague-inc.md)
- [Plague Inc: Evolved on Steam](../source/src-steam-2026-plague-inc-evolved.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
