# Command: Modern Operations

*Game* · `command-modern-operations` · status: **sourced**

A real-time operational military simulation in which the player commands air, naval, and land units drawn from a database of tens of thousands of real platforms, sensors, and weapons on a map of Earth, managing doctrine, emissions control, and missions.

| field | value |
|---|---|
| aliases | CMO |
| year | 2019 |
| developer | Warfare Sims |
| platforms | PC |
| subgenre | Wargame / military sim |
| sim domain | Military / conflict |
| player role | Commander |
| agency model | Direct unit control, Order queue |
| time model | Real-time with pause |
| sim scale | Region |
| fidelity | Professional-grade |
| perspective | Top-down / side 2D |
| win structure | Scenario goals |
| failure model | Soft / recoverable |
| narrative mode | Emergent |
| multiplayer | Single-player, Competitive, Co-op |
| modding | Scripting |
| production tier | Indie |
| agent count order | ~1,000 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C03 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 11 |

## Summary

A real-time operational military simulation in which the player commands air, naval, and land units drawn from a database of tens of thousands of real platforms, sensors, and weapons on a map of Earth, managing doctrine, emissions control, and missions.

## Core Loop

read the scenario briefing -> set doctrine, emissions control, and weapon release authority -> assign units to patrol, strike, and support missions -> sensors detect and classify contacts -> weapons engage under doctrine -> adjust missions as detections and losses accrue

## Design Notes

CMO simulates the sensor and weapon chain rather than abstract unit strengths: detection depends on radar propagation, terrain, thermal layers, and weather, and engagement depends on database specifications and doctrine. The player works mostly at mission and doctrine level and lets tactical AI fly and fight, so one player can run scenarios from patrol-boat skirmishes to global war. The Command engine also has a Professional Edition with full database editing, umpire-controlled multiplayer, and Monte Carlo analysis, sold to defense organizations.

## Relations

**uses**

- [Military operations](../mechanic/military-operations.md) (core): Every platform's sensors and weapons come from a database of tens of thousands of real systems; radar propagation, sensor degradation, terrain masking, sonar thermal layers, weather, jamming, and anti-radiation strikes are modeled for thousands of active platforms in real time.
- [Fog of war](../mechanic/fog-of-war.md) (core): Each side sees only what its sensors detect; emission control (EMCON) policies trade a unit's own detection range against revealing it to enemy passive sensors.
- [Delegation to AI managers](../mechanic/delegation-to-ai.md) (core): Units are assigned to patrol, strike, and support missions and executed by tactical AI under doctrine settings such as weapon release authority and EMCON.
- [Scouting knowledge](../mechanic/scouting-knowledge.md) (supporting): Contacts begin unidentified and are classified as sensor data accumulates.
- [Unit commands](../mechanic/unit-commands.md) (supporting): Direct orders override a unit's mission behavior.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting): Scenarios lasting hours to days of game time run with time acceleration and pause.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Over 600 official and community scenarios plus a quick battle generator.
- [Modding API](../mechanic/modding-api.md) (supporting): A Lua scripting engine and scenario editor let players build custom operations.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Scenarios are shared through the Steam Workshop.
- [Weather](../mechanic/weather.md) (supporting): Weather degrades sensors and affects engagements.
- [Projectile ballistics](../mechanic/projectile-ballistics.md) (supporting): Ballistics are among the modeled effects alongside sensor propagation, so weapon flight and impact follow database specifications.

## Sources

- [Command: Modern Operations](../source/src-wikipedia-command-modern-operations.md)
- [Command: Modern Operations on Steam](../source/src-steam-2019-command-modern-operations.md)

---
Provenance: created in run `2026-10-24-catalog-gi`.
