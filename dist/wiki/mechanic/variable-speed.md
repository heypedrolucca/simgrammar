# Pause and speed control

*Mechanic* · `variable-speed` · status: **sourced**

The player pauses the simulation and switches between speed multipliers, trading attention against elapsed game time.

| field | value |
|---|---|
| aliases | real-time with pause, time compression, fast-forward |
| family | Time & pacing |
| substrate | Rule system |
| math basis | System dynamics / ODEs, Scheduling |
| feedback | None |
| player interface | Parameter |
| legibility | 5 |
| emergence potential | 1 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 1 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can learned surrogate simulators let players skip long quiet stretches without running full-fidelity ticks? |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Conway's Game of Life](../game/game-of-life.md) |
| earliest year *(computed)* | 1970 |
| prevalence *(computed)* | 82 |
| prevalence share *(computed)* | 0.471 |
| subgenre spread *(computed)* | 23 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a time scale, paused or one of several multipliers, and the rule that converts real time into simulation ticks. At higher speeds the loop runs more ticks per real second up to hardware limits; while paused no ticks run but the player can still give orders. Some games pause or slow automatically on events. RimWorld runs 60 ticks per second at normal speed and multiplies that by 3, 6, or 15, the last only in development mode, and runs as close to the target as the machine allows; SimCity and Paradox grand strategy games offer pause and several speeds; flight simulators call it time compression. Inputs are the player's speed choice and event triggers; outputs are the tick rate of every other system.

## Player Experience

Control over attention. The player slows down or pauses for crises and detailed orders, then fast-forwards through quiet stretches such as waiting for crops or construction. Pause makes real-time games playable at a thoughtful pace, and fast-forward removes dead time.

## Design Levers

- number of speeds and their multipliers
- whether orders can be given while paused
- auto-pause and auto-slowdown triggers, such as raids or letters
- speed restrictions in multiplayer or during events
- whether higher speeds change simulation fidelity, such as larger time steps

## Failure Modes

- High speeds the hardware cannot sustain silently run slower than shown, so late-game fast-forward feels broken.
- Larger time steps at high speed can destabilize physics or give different outcomes than normal speed.
- Multiplayer games must reconcile players' speed preferences, often by host control or voting.

## Dynamics

- Players alternate between paused planning and fast-forward waiting, creating a two-tempo play pattern.
- Fast-forward exposes the compute cost of every other system, making simulation performance a gameplay issue.
- Auto-pause rules decide which events players notice.

## Open Questions

- Can learned surrogate simulators let players skip long quiet stretches without running full-fidelity ticks?

## Backlinks (computed)

**involved in:** [Branch preview of policy futures](../opportunity/branch-preview-forecasts.md)

**used by:** [Against the Storm](../game/against-the-storm.md), [Anno 117: Pax Romana](../game/anno-117.md), [Anno 1800](../game/anno-1800.md), [Banished](../game/banished.md), [BeamNG.drive](../game/beamng-drive.md), [Big Ambitions](../game/big-ambitions.md), [Big Pharma](../game/big-pharma.md), [Caesar III](../game/caesar-3.md), [Capitalism](../game/capitalism.md), [Captain of Industry](../game/captain-of-industry.md), [Cities: Skylines](../game/cities-skylines.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Command: Modern Operations](../game/command-modern-operations.md), [Creatures](../game/creatures.md), [Crusader Kings III](../game/crusader-kings-3.md), [DCS World](../game/dcs-world.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Farming Simulator 25](../game/farming-simulator-25.md), [Farthest Frontier](../game/farthest-frontier.md), [Foundation](../game/foundation.md), [Frostpunk](../game/frostpunk.md), [Frostpunk 2](../game/frostpunk-2.md), [FTL: Faster Than Light](../game/ftl.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Conway's Game of Life](../game/game-of-life.md), [Going Medieval](../game/going-medieval.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [inZOI](../game/inzoi.md), [Jurassic World Evolution](../game/jurassic-world-evolution.md), [Kenshi](../game/kenshi.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Manor Lords](../game/manor-lords.md), [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [Mini Metro](../game/mini-metro.md), [Motorsport Manager](../game/motorsport-manager.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Paralives](../game/paralives.md), [Pharaoh](../game/pharaoh.md), [Plague Inc.](../game/plague-inc.md), [Planet Coaster](../game/planet-coaster.md), [Planet Zoo](../game/planet-zoo.md), [Prison Architect](../game/prison-architect.md), [Project Hospital](../game/project-hospital.md), [Project Zomboid](../game/project-zomboid.md), [Railroad Tycoon](../game/railroad-tycoon.md), [Rebel Inc.](../game/rebel-inc.md), [RimWorld](../game/rimworld.md), [RollerCoaster Tycoon](../game/rollercoaster-tycoon.md), [Silent Hunter III](../game/silent-hunter-3.md), [SimAnt](../game/simant.md), [SimCity](../game/simcity-1989.md), [SimCity 2000](../game/simcity-2000.md), [SimCity (2013)](../game/simcity-2013.md), [SimCity 4](../game/simcity-4.md), [SimEarth](../game/simearth.md), [SimLife](../game/simlife.md), [SimTower](../game/simtower.md), [Songs of Syx](../game/songs-of-syx.md), [Space Haven](../game/space-haven.md), [Species: Artificial Life, Real Evolution](../game/species-alre.md), [Stellaris](../game/stellaris.md), [Surviving Mars](../game/surviving-mars.md), [The Powder Toy](../game/the-powder-toy.md), [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md), [Theme Hospital](../game/theme-hospital.md), [Theme Park](../game/theme-park.md), [Timberborn](../game/timberborn.md), [Transport Tycoon](../game/transport-tycoon.md), [Tropico 6](../game/tropico-6.md), [Two Point Hospital](../game/two-point-hospital.md), [Universe Sandbox](../game/universe-sandbox.md), [Victoria 3](../game/victoria-3.md), [Workers & Resources: Soviet Republic](../game/workers-and-resources.md), [X-Plane](../game/x-plane.md), [Zoo Tycoon](../game/zoo-tycoon.md)

## Sources

- [Time](../source/src-rimworldwiki-2026-time.md)
- [Turns, rounds and time-keeping systems in games](../source/src-wikipedia-turns-rounds-and-time-keeping.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
