# Trait inheritance

*Mechanic* · `trait-inheritance` · status: **sourced**

Offspring inherit traits or genes from their parents with recombination, variation, or mutation.

| field | value |
|---|---|
| aliases | genetics, breeding, heredity |
| family | Population & lineage |
| substrate | Agent-based, Stochastic events |
| math basis | Genetics / evolutionary computation, Markov / stochastic processes, Combinatorics |
| feedback | Reinforcing (positive) |
| player interface | Choice / cards, Observation only |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 5 |
| earliest game *(computed)* | [SimLife](../game/simlife.md) |
| earliest year *(computed)* | 1992 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 4 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Owns a genome per agent (gene list, trait set, or continuous parameters) and the reproduction operator that builds a child's genome from its parents: per-gene selection or crossover, optional dominance, and mutation with set rate and size. The genome then sets appearance, capabilities, or behavior parameters read by other systems. Creatures (1996) uses a haploid genome of about 320 genes coding receptors, reactions, and brain lobes, with crossover at gene boundaries, omissions, duplications, mutations, and genes that switch on at set ages. The Sims 2 passes appearance and personality with dominant and recessive genes; Crusader Kings III passes genetic traits; Planet Zoo genomes set lifespan, size, health, and fertility with an inbreeding penalty; Species: ALRE adds random values to numeric genes. Inputs: parent genomes, mutation parameters. Outputs: offspring traits and variation for selection or breeding.

## Player Experience

Breeding becomes a long game of chance: the player pairs parents for desired traits, gambles on outcomes, and watches family resemblance and surprises appear. Lineages carry identity.

## Design Levers

- genome representation (discrete traits, numeric genes, structural genes)
- inheritance rule (averaging, per-gene selection, dominance, linkage)
- mutation rate and size
- inbreeding penalties and diversity rewards
- visibility of genotype versus phenotype

## Failure Modes

- Averaging inheritance regresses everything to the mean and removes surprise.
- Eugenic optimization: players breed for top traits and the system becomes a stat grind, with uncomfortable framing in human-character games.
- High mutation rates produce non-viable offspring that read as broken.
- Hidden genetics with no inspection make breeding feel random.

## Dynamics

- Selective breeding by the player concentrates traits across generations.
- With natural selection, inheritance lets populations adapt to environments.
- Inbreeding in small populations produces defect clusters that force outbreeding or trade for new stock.

## Open Questions

- Can generative models map genomes to coherent novel appearances and behaviors rather than to a fixed set of parts?
- Which inheritance models keep breeding surprising without becoming a pure stat grind?

## Backlinks (computed)

**affected by:** [Continuous cellular automata and foundation-model search for artificial life](../technique/continuous-alife-and-asal.md)

**involved in:** [Open-ended evolution sandbox](../opportunity/open-ended-evolution-sandbox.md), [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

**required by:** [Natural selection](../mechanic/natural-selection.md)

**used by:** [Creatures](../game/creatures.md), [Crusader Kings III](../game/crusader-kings-3.md), [Planet Zoo](../game/planet-zoo.md), [SimLife](../game/simlife.md), [Species: Artificial Life, Real Evolution](../game/species-alre.md), [The Sims 2](../game/the-sims-2.md)

## Sources

- [Creatures: Artificial Life Autonomous Software Agents for Home Entertainment](../source/src-grand-1996-creatures-alife.md)
- [The Sims 2](../source/src-wikipedia-the-sims-2.md)
- [Crusader Kings III](../source/src-wikipedia-crusader-kings-3.md)
- [Planet Zoo](../source/src-wikipedia-planet-zoo.md)
- [Devblog #5: Thrive vs Species](../source/src-revolutionarygames-2016-thrive-vs-species.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
