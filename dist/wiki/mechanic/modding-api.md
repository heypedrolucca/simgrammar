# Modding API

*Mechanic* · `modding-api` · status: **sourced**

Official hooks for scripts and data definitions let players change and extend the simulation's content and rules.

| field | value |
|---|---|
| aliases | mod support, scripting API, data-driven modding |
| family | Multiplayer & persistence |
| substrate | Player-authored logic, Rule system |
| math basis | Computation theory |
| feedback | Reinforcing (positive) |
| player interface | Programming |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [X-Plane](../game/x-plane.md) |
| earliest year *(computed)* | 1995 |
| prevalence *(computed)* | 30 |
| prevalence share *(computed)* | 0.172 |
| subgenre spread *(computed)* | 16 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

The game exposes two surfaces: data definitions for entities, recipes, and parameters that the engine loads at startup, and a scripting runtime that registers handlers for game events and calls an API to read and change state. Factorio mods use modified Lua 5.2 and pass through settings, prototype (data), and runtime (control) stages in a fixed lifecycle, with the runtime stage event-driven. RimWorld loads XML definitions and C# assemblies; Crusader Kings III exposes event, trigger, and effect scripting; Minecraft's Java Edition relies largely on third-party loaders. A mod manager resolves load order and dependencies. Inputs: mod files. Outputs: changed content, rules, and UI.

## Player Experience

Players reshape the game to their taste, from small fixes to total conversions, and the game keeps renewing years after release. Modders gain a creative outlet and an audience, and non-modders browse mod lists to assemble their own version of the game.

## Design Levers

- surface breadth: data only, data plus scripting, or full code injection
- sandboxing and determinism requirements, such as lockstep multiplayer
- API stability and versioning policy
- load-order and dependency management
- distribution channel and discovery, such as an official mod portal or Steam Workshop

## Failure Modes

- Game updates break mods, and players delay updating or abandon saves.
- Large mod lists conflict and degrade performance in ways that are hard to diagnose.
- Unsandboxed code mods carry security risk to players' machines.

## Dynamics

- Popular mods become de facto features, and developers later absorb them into the base game.
- Moddable games keep long active communities and sales tails.
- Mods expose and fix balance problems faster than official patches.

## Open Questions

- Can coding models let non-programmers write working mods from natural-language descriptions against a documented API?
- What API design keeps generated mods sandboxed, deterministic, and compatible across updates?

## Backlinks (computed)

**involved in:** [Event-sourced simulation runtime](../opportunity/event-sourced-sim-runtime.md), [Mechanic modding by description](../opportunity/language-modding.md), [Automated mechanic discovery](../opportunity/mechanic-discovery-search.md)

**used by:** [Arma 3](../game/arma-3.md), [Autonauts](../game/autonauts.md), [BeamNG.drive](../game/beamng-drive.md), [Besiege](../game/besiege.md), [Cities: Skylines](../game/cities-skylines.md), [Cities: Skylines II](../game/cities-skylines-2.md), [Command: Modern Operations](../game/command-modern-operations.md), [Creatures](../game/creatures.md), [DCS World](../game/dcs-world.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md), [Factorio](../game/factorio.md), [Farming Simulator 25](../game/farming-simulator-25.md), [Game Dev Tycoon](../game/game-dev-tycoon.md), [Garry's Mod](../game/garrys-mod.md), [Kerbal Space Program](../game/kerbal-space-program.md), [Microsoft Flight Simulator (2020)](../game/microsoft-flight-simulator-2020.md), [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [Mindustry](../game/mindustry.md), [Minecraft](../game/minecraft.md), [Noita](../game/noita.md), [Paralives](../game/paralives.md), [Plague Inc.](../game/plague-inc.md), [Project Zomboid](../game/project-zomboid.md), [Satisfactory](../game/satisfactory.md), [Screeps](../game/screeps.md), [shapez 2](../game/shapez-2.md), [Space Engineers](../game/space-engineers.md), [Teardown](../game/teardown.md), [The Powder Toy](../game/the-powder-toy.md), [X-Plane](../game/x-plane.md)

## Sources

- [Factorio Lua API documentation](../source/src-wube-2026-factorio-lua-api.md)

---
Provenance: created in run `2026-10-24-taxonomy-m7`.
