# Animal husbandry

*Mechanic* · `animal-husbandry` · status: **sourced**

Domestic animals are housed, fed, tended, and bred, and they yield products whose quantity and quality depend on their care.

| field | value |
|---|---|
| aliases | livestock, ranching, animal breeding |
| family | Biology & health |
| substrate | Agent-based, Aggregate stocks |
| math basis | Population dynamics, Genetics / evolutionary computation, System dynamics / ODEs |
| feedback | Both |
| player interface | Direct manipulation, Placement, Orders |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Classic |
| open questions | Can learned animal behavior and animation make individually simulated livestock expressive enough to deepen attachment without bespoke animation per species? |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Harvest Moon](../game/harvest-moon.md) |
| earliest year *(computed)* | 1996 |
| prevalence *(computed)* | 9 |
| prevalence share *(computed)* | 0.052 |
| subgenre spread *(computed)* | 6 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a herd of individual animals or a count per species, each with growth stage, food state, often affection or mood, and sometimes pregnancy and genes. Each day animals eat from grazing or stored fodder, grow toward maturity, and roll for products such as milk, eggs, or wool and for births; care actions raise affection or mood, which scales yield and quality. Stardew Valley tracks friendship from 0 to 1000 and mood from 0 to 255: unfed animals stop producing but do not die, mood under 70 can skip production, quality products need mood 150, and a nightly birth check governs pregnancies. RimWorld and Dwarf Fortress breed animals that must be fed, sheltered, trained, or slaughtered; Farming Simulator ties livestock productivity to feed. Inputs are feed, housing, and care; outputs are products, meat, and offspring.

## Player Experience

Routine care with compounding returns. The player builds pens and barns, keeps feed stocked through winter, and turns daily tending into reliable income. Animals can become personal: named, petted, and missed when lost to a predator or a hard winter.

## Design Levers

- feed requirement per animal and the balance between grazing and stored fodder
- time to maturity and product cycle per species
- how care, mood, and affection scale yield and quality
- breeding rate and population caps from housing size
- losses: disease, predators, exposure, slaughter decisions

## Failure Modes

- Unchecked breeding produces runaway herds that eat all fodder and then starve, a recurring colony-sim problem.
- Daily care actions with no decisions become chores players automate away or abandon.
- Animals that can never die or fall ill turn husbandry into passive income.

## Dynamics

- Feed demand links husbandry to crop fields and storage, especially before winter.
- Herds become targets for predators and raids, requiring fences and defense.
- Breeding for traits ties husbandry to inheritance and long-term planning.

## Open Questions

- Can learned animal behavior and animation make individually simulated livestock expressive enough to deepen attachment without bespoke animation per species?

## Backlinks (computed)

**used by:** [Autonauts](../game/autonauts.md), [Farming Simulator 25](../game/farming-simulator-25.md), [Going Medieval](../game/going-medieval.md), [Harvest Moon](../game/harvest-moon.md), [Minecraft](../game/minecraft.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Stardew Valley](../game/stardew-valley.md), [Valheim](../game/valheim.md), [Viva Piñata](../game/viva-pinata.md)

## Sources

- [Animals](../source/src-stardewvalleywiki-2026-animals.md)

---
Provenance: created in run `2026-10-24-taxonomy-m5`.
