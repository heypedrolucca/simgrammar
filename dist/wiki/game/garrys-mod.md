# Garry's Mod

*Game* · `garrys-mod` · status: **sourced**

A Source engine physics sandbox in which players spawn props, ragdolls, and NPCs, join them with welds and constraints, and script whole new multiplayer game modes in Lua.

| field | value |
|---|---|
| aliases | GMod |
| year | 2004 |
| developer | Facepunch Studios |
| platforms | PC |
| subgenre | Physics sandbox |
| sim domain | Physical / mechanical, Computational / abstract |
| player role | Engineer / designer |
| agency model | Direct avatar, Programmatic |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | Emergent |
| multiplayer | Single-player, Co-op, Competitive |
| modding | Total conversion |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 3 |
| influence | 4 |
| cluster *(computed)* | C02 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 7 |

## Summary

A Source engine physics sandbox in which players spawn props, ragdolls, and NPCs, join them with welds and constraints, and script whole new multiplayer game modes in Lua.

## Core Loop

spawn props, ragdolls, and NPCs -> move and freeze them with the physics gun -> weld, rope, and motor them with the tool gun -> test the contraption or scene -> share it, or play a community game mode built on the same tools

## Design Notes

Garry's Mod exposes the Source engine's rigid-body physics directly: the physics gun grabs, rotates, and freezes any prop, and the tool gun adds welds, ropes, axles, motors, thrusters, and other constraints, so contraptions are built from rigid bodies and joints. Its larger contribution is that the whole game is scriptable in Lua and servers download addons on join, so most play happens inside player-made game modes such as Trouble in Terrorist Town, Prop Hunt, and DarkRP, and the add-on Wiremod adds sensors and logic gates. Garry's Mod began as a free Half-Life 2 mod in 2004 and became a paid Steam product in 2006.

## Relations

**uses**

- [Rigid-body physics](../mechanic/rigid-body-physics.md) (core): Every spawned prop and ragdoll is a physics object; the physics gun lifts, rotates, and freezes them, and collisions, gravity, and buoyancy follow the Source physics engine.
- [Modular assembly](../mechanic/modular-assembly.md) (core): The tool gun joins props with welds, ropes, axles, sliders, winches, motors, wheels, and thrusters, turning loose props into vehicles and machines.
- [Modding API](../mechanic/modding-api.md) (core): A Lua API covers entities, weapons, HUD, and game rules; servers send addons to clients on join, and community game modes (TTT, Prop Hunt, DarkRP) became the main way people play.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): The player is a first-person character who walks, flies with noclip, and wields the physics and tool guns.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Steam Workshop distributes saves, dupes, maps, and addons.
- [Signal circuits](../mechanic/signal-circuits.md) (supporting): The Wiremod addon adds wires, sensors, gates, and programmable chips to contraptions.
- [Blueprints](../mechanic/blueprints.md) (supporting): The duplicator tool and Advanced Duplicator addon copy and paste multi-prop contraptions.

## Backlinks (computed)

**precedent for:** [Mechanic modding by description](../opportunity/language-modding.md)

## Sources

- [Garry's Mod](../source/src-wikipedia-garrys-mod.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
