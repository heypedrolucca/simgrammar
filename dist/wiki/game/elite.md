# Elite

*Game* · `elite` · status: **sourced**

A 3D space trading and combat game in which the player flies a single ship through eight seed-generated galaxies, buying and selling cargo and fighting pirates and police to raise a combat rating.

| field | value |
|---|---|
| year | 1984 |
| developer | David Braben and Ian Bell |
| platforms | Mainframe / early micro, PC, Console |
| subgenre | Space sim |
| sim domain | Cosmic / space, Economic |
| player role | Operator / pilot |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Interplanetary+ |
| fidelity | Stylized |
| perspective | First-person |
| win structure | Open sandbox |
| failure model | Hard restart |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | None |
| production tier | Indie |
| agent count order | ~10 |
| emergence | 2 |
| influence | 5 |
| cluster *(computed)* | C08 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 6 |

## Summary

A 3D space trading and combat game in which the player flies a single ship through eight seed-generated galaxies, buying and selling cargo and fighting pirates and police to raise a combat rating.

## Core Loop

buy cargo at a station -> hyperspace to a system within fuel range -> fight or evade pirates and police -> dock by matching the station's rotation -> sell for profit -> buy weapons and equipment -> raise combat rating

## Design Notes

Each of the eight galaxies and its 256 systems is regenerated from a seed rather than stored, which let a large universe fit in an 8-bit micro and made procedural generation the core of the design. Commodity prices differ by system, and fuel limits each hyperjump to 7 light years, so route choice is the main economic decision. The goal of reaching the Elite combat rank is open-ended; the player chooses between trading, piracy, bounty hunting, and mining.

## Relations

**uses**

- [Procedural terrain](../mechanic/procedural-terrain.md) (core): Eight galaxies of 256 planets each are generated from seed numbers at runtime; each system's name, economy, government, and description derive from the seed.
- [Trade routes](../mechanic/trade-routes.md) (core): Commodity prices vary by system economy; the player buys cheap and sells dear between systems, constrained by cargo bay size and the 7 light-year fuel limit per jump.
- [Embodied skill control](../mechanic/embodied-skill-control.md) (core): Real-time wireframe dogfights and manual docking that requires matching a rotating station's spin unless a docking computer is bought.
- [Reputation](../mechanic/reputation.md) (supporting): Legal status (clean, offender, fugitive) worsens with piracy and illegal cargo and draws police ships.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Combat rating rises with kills from Harmless toward Elite; most versions also offer Galactic Navy missions with special rewards.
- [Resource extraction](../mechanic/resource-extraction.md) (supporting): Mining lasers break asteroids into fragments that can be scooped and sold.

## Backlinks (computed)

**influenced:** [Elite Dangerous](../game/elite-dangerous.md), [EVE Online](../game/eve-online.md)

## Sources

- [Elite (video game)](../source/src-wikipedia-elite.md)

---
Provenance: created in run `2026-10-24-catalog-gg`.
