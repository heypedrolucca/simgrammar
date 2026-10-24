# Oxygen Not Included

*Game* · `oxygen-not-included` · status: **sourced**

A side-view colony sim in which a few duplicants survive inside an asteroid where every tile holds an element with mass and temperature, so air, liquids, heat, and germs flow through the base.

| field | value |
|---|---|
| aliases | ONI |
| year | 2017 |
| year full release | 2019 |
| developer | Klei Entertainment |
| platforms | PC |
| subgenre | Colony sim |
| subgenre secondary | Survival sim |
| sim domain | Physical / mechanical, Biological / ecological, Industrial / logistics |
| player role | Overseer |
| agency model | Order queue, Zoning / placement, Indirect incentive, Programmatic |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Cascading collapse |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 4 |
| influence | 3 |
| influenced by | [Dwarf Fortress](../game/dwarf-fortress.md), [Prison Architect](../game/prison-architect.md), [The Sims](../game/the-sims.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 6 |
| mechanic count *(computed)* | 23 |

## Summary

A side-view colony sim in which a few duplicants survive inside an asteroid where every tile holds an element with mass and temperature, so air, liquids, heat, and germs flow through the base.

## Core Loop

dig into the asteroid -> lay out rooms, pipes, and wires -> duplicants perform prioritized errands -> oxygen, heat, germs, and waste redistribute tile by tile -> stress and shortfalls surface -> rebuild toward closed, sustainable loops

## Design Notes

Each cell holds one element with a mass and a temperature, and heat moves between cells every 0.2 s tick by conduction, so insulation, phase changes, and overheating machines follow from one rule rather than from per-building scripts. Most machines emit byproducts (a natural gas generator makes 800 W plus polluted water and carbon dioxide), so the long game is closing loops so waste becomes input. Mood uses a morale-versus-expectation gap: learning skills raises a duplicant's expectation, so better-trained colonists need better food, rooms, and decor. Wikipedia names Dwarf Fortress, Prison Architect, and The Sims as design influences.

## Sources

- src-wikipedia-oxygen-not-included
- src-steam-2026-oxygen-not-included
- src-oniwiki-2026-morale
- src-oniwiki-2026-germs
- src-oxygennotincludedwiki-2026-thermal-conductivity
- src-oniwiki-2026-liquid-pipe
- src-oniwiki-2026-natural-gas-generator

## Relations

**influenced by**

- [Dwarf Fortress](../game/dwarf-fortress.md)
- [Prison Architect](../game/prison-architect.md)
- [The Sims](../game/the-sims.md)

**uses**

- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (core): Every tile holds one gas, liquid, or solid with a mass; gases diffuse and equalize when a chamber is opened, and liquids drain under gravity, so breathable oxygen must be produced and carbon dioxide managed.
- [Heat transfer](../mechanic/heat-transfer.md) (core): Cells exchange heat each 0.2 s tick with q = dT x dt x k x 1000, with multipliers for solid-gas and liquid-liquid contact; insulated tiles divide conductivity, and temperature thresholds melt, freeze, boil, or damage things.
- [Byproducts and waste](../mechanic/byproducts-waste.md) (core): Machines and duplicants emit polluted water, polluted oxygen, carbon dioxide, and heat; a natural gas generator consumes 90 g/s of gas for 800 W and outputs 67.5 g/s polluted water and 22.5 g/s CO2.
- [Fluid pipe networks](../mechanic/fluid-pipe-network.md) (core): Gas and liquid pipes carry packets between buildings; a liquid pipe segment holds 10 kg and moves packets once per second, capping a line at 10 kg/s, and pipe contents exchange heat with their tiles.
- [Mood and breakdowns](../mechanic/mood-breakdown.md) (core): Morale is the sum of timed buffs (Mess Hall +3, Private Bedroom +3, food up to +16, decor up to +12) compared to an expectation that rises with skills learned; each point under adds 2.5% stress per cycle up to 25%, full stress triggers a stress response, and 8 or more points over can trigger overjoyed responses.
- [Work priorities](../mechanic/work-priorities.md) (core): Every errand carries a priority, and each duplicant has per-errand-type priorities on the Priorities screen; duplicants pick the highest available errand and favor tasks they are good at.
- [Designation orders](../mechanic/designation-orders.md) (supporting): Dig, build, mop, and deconstruct orders placed on tiles.
- [Contagion](../mechanic/contagion.md) (supporting): Germs live on tiles, items, gases, and liquids; exposure past per-germ thresholds gives a contraction chance of 0.5 - 0.5 x tanh(resistance / 4).
- [Power grid](../mechanic/power-grid.md) (supporting): Coal, hydrogen, natural gas, and manual generators on wires and batteries; overloaded circuits take damage.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): Automation wires, sensors, and logic gates control doors, pumps, and generators; extended by the Automation Innovation update.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Skill points are spent on skills, which raise morale expectations.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Traits such as Germ Resistant or Allergies change resistances and stress reactions.
- [Room recognition](../mechanic/room-recognition.md) (supporting): Enclosed rooms that meet requirements become Mess Halls, Bedrooms, and similar rooms that grant morale buffs.
- [Decoration and beauty](../mechanic/decoration-beauty.md) (supporting): Decor around a duplicant is compared to its recent average and feeds morale.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting): Plants need specific temperatures, atmospheres, and irrigation.
- [Animal husbandry](../mechanic/animal-husbandry.md) (supporting): Critters are ranched for food and for their conversion of inputs into useful outputs.
- [Spoilage](../mechanic/spoilage.md) (supporting): Food rots unless refrigerated or kept in a sterile atmosphere.
- [Data overlays](../mechanic/data-overlays.md) (supporting): Oxygen, temperature, power, plumbing, and germ overlays show hidden cell state.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Research unlocks buildings.
- [Procedural terrain](../mechanic/procedural-terrain.md) (supporting): Asteroids are procedurally generated.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting)

## Backlinks (computed)

**influenced:** [Space Haven](../game/space-haven.md)

**precedent for:** [Bottleneck explainer for production networks](../opportunity/bottleneck-explainer.md), [Intent-level orders](../opportunity/intent-level-orders.md), [Learned material surrogates at world scale](../opportunity/learned-material-surrogates.md), [Factories with a living workforce](../opportunity/living-workforce-factories.md)

## Sources

- [Oxygen Not Included](../source/src-wikipedia-oxygen-not-included.md)
- [Oxygen Not Included on Steam](../source/src-steam-2026-oxygen-not-included.md)
- [Morale](../source/src-oniwiki-2026-morale.md)
- [Germs](../source/src-oniwiki-2026-germs.md)
- [Thermal Conductivity](../source/src-oxygennotincludedwiki-2026-thermal-conductivity.md)
- [Liquid Pipe](../source/src-oniwiki-2026-liquid-pipe.md)
- [Natural Gas Generator](../source/src-oniwiki-2026-natural-gas-generator.md)

---
Provenance: created in run `2026-10-24-catalog-gb`; reviewed in `2026-10-24-review-fixes`.
