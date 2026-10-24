# Injury body model

*Mechanic* · `injury-body-model` · status: **sourced**

Bodies are hierarchies of parts with their own damage, and wounds, bleeding, infection, and prosthetics change capacities such as moving and manipulation.

| field | value |
|---|---|
| aliases | body part damage, wound model, health hierarchy |
| family | Biology & health |
| substrate | Agent-based, Rule system |
| math basis | System dynamics / ODEs, Markov / stochastic processes |
| feedback | Both |
| player interface | Observation only, Orders |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| open questions | Can language models narrate injuries and recovery so deep body models stay legible without a dense health tab? |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Dwarf Fortress](../game/dwarf-fortress.md) |
| earliest year *(computed)* | 2006 |
| prevalence *(computed)* | 7 |
| prevalence share *(computed)* | 0.04 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.25 |

## Definition

Owns, per creature, a tree of body parts with hit points, tissue layers, or functions, plus a list of conditions such as cuts, burns, fractures, bleeding, infection, scars, and missing or artificial parts. Damage lands on a sampled part; part health feeds capacities such as consciousness, moving, manipulation, sight, breathing, and blood pumping, which scale work speed, combat, and survival. Each tick bleeding drains blood, infections race against immunity, and tended wounds heal. RimWorld derives capacities from parts: consciousness below 30% keeps a pawn from waking, moving below 15% incapacitates, each arm supplies half of manipulation, blood pumping at 0% is fatal, poor tending raises infection and scarring risk, and each bionic leg adds 12.5% moving. Dwarf Fortress damages tissue layers per part; Project Zomboid tracks wounds per body region. Inputs are damage and treatment; outputs are capacity multipliers, pain, and death.

## Player Experience

Injuries become specific stories: a colonist missing a hand works slower, a hunter with a shattered leg cannot flee. The player triages by which wound threatens life first, stops bleeding before worrying about infection, and plans around lasting disabilities or replaces parts with prosthetics.

## Design Levers

- granularity of the body tree: regions, organs, tissue layers
- mapping from part damage to capacities and from capacities to actions
- bleeding rate, infection chance, and healing rate, and how treatment quality modifies them
- permanence: scars, lost parts, chronic pain
- replacement options such as prosthetics, bionics, and transplants, and their availability

## Failure Modes

- Too many parts and conditions make the health screen unreadable, so players cannot tell what is lethal.
- Fine-grained damage with high lethality makes outcomes feel like dice rolls, such as death from one hit to a vital organ.
- Permanent disabilities without replacement paths make injured characters dead weight the player discards.

## Dynamics

- Injured agents work slower, lowering output and raising pressure on healthy ones.
- Demand for medicine, doctors, and prosthetics creates a medical economy.
- Disabilities shape character identity and the stories players tell about them.

## Open Questions

- Can language models narrate injuries and recovery so deep body models stay legible without a dense health tab?

## Backlinks (computed)

**affected by:** [Learned physics-based character control](../technique/physics-based-character-control.md)

**involved in:** [Learned motion for simulated crowds](../opportunity/neural-npc-motion.md)

**used by:** [Arma 3](../game/arma-3.md), [Caves of Qud](../game/caves-of-qud.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Kenshi](../game/kenshi.md), [Project Zomboid](../game/project-zomboid.md), [RimWorld](../game/rimworld.md), [Surgeon Simulator](../game/surgeon-simulator.md)

## Sources

- [Health](../source/src-rimworldwiki-2026-health.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
