# Surgeon Simulator

*Game* · `surgeon-simulator` · status: **sourced**

A physics comedy surgery game in which the player controls one hand with separate finger keys to perform transplants on the patient Bob before his vital signs fail.

| field | value |
|---|---|
| aliases | Surgeon Simulator 2013, Surgeon Simulator: Experience Reality |
| year | 2013 |
| developer | Bossa Studios |
| platforms | PC, Mobile, Console, Handheld, VR |
| subgenre | Medical sim |
| sim domain | Medical, Physical / mechanical |
| player role | Worker |
| agency model | Direct avatar |
| time model | Real-time |
| sim scale | Individual |
| fidelity | Abstract |
| perspective | First-person |
| win structure | Scenario goals |
| failure model | Hard restart |
| narrative mode | None |
| multiplayer | Single-player, Co-op |
| modding | None |
| production tier | Indie |
| agent count order | None |
| emergence | 2 |
| influence | 2 |
| boundary case | True |
| cluster *(computed)* | C07 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 4 |

## Summary

A physics comedy surgery game in which the player controls one hand with separate finger keys to perform transplants on the patient Bob before his vital signs fail.

## Core Loop

pick a procedure -> move the hand and press finger keys to grab tools -> cut, break, and remove body parts -> place the new organ -> keep Bob alive -> score and time

## Design Notes

Made in 48 hours at the 2013 Global Game Jam, the game turns control difficulty into the content: the mouse moves the hand, a mouse button rotates or lowers it, and A, W, E, R, and Space close individual fingers, a scheme modeled on Jurassic Park: Trespasser. Tools and organs are rigid bodies, so most outcomes come from collisions and dropped objects rather than authored surgical steps. Medicine is a comic frame with a thin vital-sign model; a heart rate at zero requires charging the defibrillators. Included as a boundary case for embodied control.

## Relations

**uses**

- [Embodied skill control](../mechanic/embodied-skill-control.md) (core): The mouse moves the hand, holding the right button rotates it, the left button lowers it, and A, W, E, R, and Space each close one finger, so grasping a scalpel is itself the challenge.
- [Rigid-body physics](../mechanic/rigid-body-physics.md) (core): Instruments, organs, and bones are physics objects that collide, slip, and fall, so most mistakes are physical accidents rather than authored failure states.
- [Injury body model](../mechanic/injury-body-model.md) (supporting): Damage to the patient drives a small vital-sign model; when heart rate reaches 0 the player must charge the defibrillators.
- [Scenario objectives](../mechanic/scenario-objectives.md) (supporting): Procedures such as heart and kidney transplants are replayed in an operating room, a bouncing ambulance, and zero gravity.

## Sources

- [Surgeon Simulator](../source/src-wikipedia-surgeon-simulator.md)
- [Bringing the ER to VR: Surgeon Simulator: Experience Reality](../source/src-invenglobal-2016-surgeon-simulator-vr.md)

---
Provenance: created in run `2026-10-24-catalog-gf`.
