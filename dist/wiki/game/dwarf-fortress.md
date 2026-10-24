# Dwarf Fortress

*Game* · `dwarf-fortress` · status: **sourced**

A colony sim in which the player directs a fortress of autonomous dwarves inside a procedurally generated world whose history, geology, fluids, bodies, and minds are all simulated.

| field | value |
|---|---|
| aliases | Slaves to Armok: God of Blood Chapter II: Dwarf Fortress |
| year | 2006 |
| developer | Bay 12 Games |
| platforms | PC |
| subgenre | Colony sim |
| subgenre secondary | Systemic RPG |
| sim domain | Social / interpersonal, Physical / mechanical, Biological / ecological |
| player role | Overseer |
| agency model | Order queue, Zoning / placement, Indirect incentive, Direct unit control |
| time model | Real-time with pause |
| sim scale | Settlement |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Cascading collapse |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | Hobbyist / free |
| agent count order | ~100 |
| emergence | 5 |
| influence | 5 |
| cluster *(computed)* | C01 |
| core count *(computed)* | 8 |
| mechanic count *(computed)* | 29 |

## Summary

A colony sim in which the player directs a fortress of autonomous dwarves inside a procedurally generated world whose history, geology, fluids, bodies, and minds are all simulated.

## Core Loop

embark and dig -> designate jobs, stockpiles, and workshops -> dwarves self-assign labors and craft -> needs, emotions, and stress accumulate -> migrants, caravans, sieges, and beasts arrive -> fortress thrives or collapses into the world's legends

## Design Notes

Tarn Adams's stated principles are to break a system into parts, avoid overplanning, and base each model on a real-world analog; he describes the game as a story generator. The fortress is embarked inside a world whose geology and history were already simulated, and the fortress's own events flow back into that history through Legends, so a collapse becomes a record that a later adventurer can visit. Strange moods let an inspired dwarf seize a workshop to make a named artifact and go insane if materials are missing, which turns the production system into a story source. The game was free and donation-funded from 2006; a paid Steam edition with sprite graphics followed in December 2022, still short of a 1.0 version.

## Relations

**uses**

- [Simulated history generation](../mechanic/history-generation.md) (core): World generation builds elevation, rainfall, drainage, temperature, and vegetation layers, then simulates civilizations, sites, and historical figures for a player-chosen number of years before the fortress is embarked.
- [Designation orders](../mechanic/designation-orders.md) (core): The player designates digging, chopping, construction, and workshop jobs; dwarves with the matching labor enabled pick them up, and a manager can queue work orders automatically.
- [Mood and breakdowns](../mechanic/mood-breakdown.md) (core): Emotions add to or subtract from a hidden stress value (-1,000,000 to +1,000,000) with effects from +10,000, +25,000, and +50,000; stressed dwarves throw tantrums, fall into depression, or wander obliviously, prolonged stress leads to insanity, and one breakdown can spread unhappiness.
- [Injury body model](../mechanic/injury-body-model.md) (core): Body parts are layered tissues (skin, fat, muscle, bone, nerves) damaged individually in combat; injuries can be permanent and are treated in a hospital with traction benches, casts, sutures, and splints.
- [Fluid and gas simulation](../mechanic/fluid-gas-simulation.md) (core): Water and magma flow tile by tile with up to seven depth levels per tile, so breaching a river, cavern lake, or magma source floods connected tunnels.
- [Vertical layers](../mechanic/vertical-layers.md) (core): Z-levels, added in 2007, let the fortress descend level by level through soil and stone to caverns, the magma sea, and the underworld, connected by stairs and ramps.
- [History chronicle](../mechanic/history-chronicle.md) (core): Legends mode lists historical figures, sites, artifacts, and civilizations with a historical map; fortress deeds and retired adventurers are added, and the archive exports to XML.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Work quality and speed rise with skill gained through practice in each labor.
- [Needs decay](../mechanic/needs-decay.md) (supporting): Food, drink, and sleep, plus personal needs such as socializing or praying met at taverns, temples, and libraries.
- [Memories and thoughts](../mechanic/memories-thoughts.md) (supporting): Emotions become short-term memories; strong or revisited ones are promoted to long-term memories that keep adding stress.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Facets such as bravery, stress vulnerability, and anxiety scale how stress builds and dissipates.
- [Relationship values](../mechanic/relationship-values.md) (supporting): Friends, family, and pets; their deaths are major stressors.
- [Production chains](../mechanic/production-chain.md) (supporting): Ore is smelted to bars and alloyed; steel needs flux to make pig iron plus coke or charcoal, and magma can replace fuel.
- [Heat transfer](../mechanic/heat-transfer.md) (supporting): Tiles, materials, and creatures carry temperatures.
- [Fire spread](../mechanic/fire-spread.md) (supporting): Fires spread and burn dwarves and furniture.
- [Raid defense](../mechanic/raid-defense.md) (supporting): Ambushes, sieges, megabeasts, and forgotten beasts are met with squads, fortifications, and traps triggered by levers or pressure plates.
- [Adaptive threat scaling](../mechanic/adaptive-threat-scaling.md) (supporting): Wealthier and more populous fortresses attract sieges and megabeasts.
- [Immigration by attractiveness](../mechanic/immigration-attractiveness.md) (supporting): Migrant waves from the mountainhome grow as the fortress develops.
- [Trade routes](../mechanic/trade-routes.md) (supporting): Yearly caravans from neighboring civilizations are handled by a broker; caravans can be absent or hostile depending on history.
- [Room recognition](../mechanic/room-recognition.md) (supporting): Furniture defines bedrooms, dining halls, and offices; nobles demand rooms of rising value.
- [Crime and policing](../mechanic/crime-policing.md) (supporting): A justice system punishes assault, murder, and vandalism.
- [Crop cultivation](../mechanic/crop-cultivation.md) (supporting): Underground farming on soil layers; plump helmet mushrooms are brewed into wine.
- [Hauling jobs](../mechanic/hauling-jobs.md) (supporting): Dwarves carry goods to player-defined stockpiles.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Military squads in uniforms train at barracks and can be ordered to attack.
- [Stress accumulation](../mechanic/stress-accumulation.md) (core): Emotions from events add to or subtract from a hidden stress value (-1,000,000 to +1,000,000) scaled by facets such as stress vulnerability and bravery; above +10,000, +25,000, and +50,000 dwarves risk tantrums, depression, obliviousness, and insanity, and long-term memories keep adding stress.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Building placement](../mechanic/free-placement.md) (supporting)
- [Utility action selection](../mechanic/utility-action-selection.md) (supporting)
- [Storage and buffers](../mechanic/storage-capacity.md) (supporting)

## Backlinks (computed)

**influenced:** [Minecraft](../game/minecraft.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Prison Architect](../game/prison-architect.md), [RimWorld](../game/rimworld.md), [Space Haven](../game/space-haven.md)

**precedent for:** [Why-query over the simulation log](../opportunity/causal-why-query.md), [Generated dream and replay views](../opportunity/dream-replay-layer.md), [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md), [Intent-level orders](../opportunity/intent-level-orders.md), [Factories with a living workforce](../opportunity/living-workforce-factories.md), [Language-agent society terrarium](../opportunity/llm-society-terrarium.md), [Automated mechanic discovery](../opportunity/mechanic-discovery-search.md), [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md), [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md), [Simulation games as agent benchmarks](../opportunity/sims-as-agent-benchmarks.md)

## Sources

- [Dwarf Fortress](../source/src-wikipedia-dwarf-fortress.md)
- [Simulation Principles from Dwarf Fortress](../source/src-adams-2015-df-simulation-principles.md)
- [Legends](../source/src-dfwiki-2026-legends.md)
- [Stress](../source/src-dfwiki-2026-stress.md)

---
Provenance: created in run `2026-10-24-catalog-gb`; reviewed in `2026-10-24-review-fixes`.
