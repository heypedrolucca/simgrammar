# Creatures

*Game* · `creatures` · status: **sourced**

An artificial-life game in which the player hatches and raises Norns whose neural-network brains, simulated biochemistry, and haploid digital genomes produce learned behavior and heritable mutation.

| field | value |
|---|---|
| aliases | Creatures 1 |
| year | 1996 |
| developer | Millennium Interactive / Cyberlife Technology |
| platforms | PC, Console, Handheld |
| subgenre | Artificial life |
| subgenre secondary | Virtual pet |
| sim domain | Biological / ecological |
| player role | Caretaker |
| agency model | Caretaking interaction, Indirect incentive, Conversational |
| time model | Real-time with pause |
| sim scale | Individual |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Permadeath |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Scripting |
| production tier | AA |
| agent count order | ~10 |
| emergence | 4 |
| influence | 3 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 11 |

## Summary

An artificial-life game in which the player hatches and raises Norns whose neural-network brains, simulated biochemistry, and haploid digital genomes produce learned behavior and heritable mutation.

## Core Loop

hatch eggs -> Norns act on biochemical drives -> player rewards, punishes, and teaches words -> neural weights shift toward drive-reducing actions -> Norns breed and pass mutated genomes -> next generation behaves differently

## Design Notes

Steve Grand built each Norn as a stack of coupled models rather than a scripted pet: a neural network whose sight neurons are grouped one per object type, a biochemistry of chemicals and organs that sets drive levels, and a haploid genome with no dominance that codes for both. Learning is behaviorist: high drive levels act as punishment and reductions as reward, so the player's tickles and slaps only matter through the same chemistry. Because the genome builds the brain and body, mutations produce Norns that cannot see, lack organs, or never die, which the online breeding community catalogued and traded. Norns live about 40 hours, short enough for many generations.

## Relations

**uses**

- [Creature learning](../mechanic/creature-learning.md) (core): A neural-network brain maps sensed objects and drives to actions; drive reduction reinforces the action that preceded it, and the hand's tickle and slap act as reward and punishment through the same pathway.
- [Trait inheritance](../mechanic/trait-inheritance.md) (core): Haploid digital genomes with no dominant or recessive genes encode brain wiring, biochemistry, and organs; offspring genomes mutate, and every boxed copy shipped a unique starting set of egg genomes.
- [Needs decay](../mechanic/needs-decay.md) (core): Drives such as hunger and tiredness are concentrations in a simulated biochemistry that rise over time and fall when actions such as eating or resting succeed.
- [Creature care](../mechanic/creature-care.md) (core): The player's hand pointer feeds Norns, shows them objects, and tickles or slaps them; neglect leads to hunger, disease, and death, but care shapes behavior only indirectly through learning.
- [Natural-language interaction](../mechanic/natural-language-interaction.md) (supporting): Players teach nouns by naming objects a Norn is looking at and verbs with a learning computer, then type instructions that the Norn may choose to obey.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): Norns hatch, grow, breed, and die within roughly 40 hours of play.
- [Contagion](../mechanic/contagion.md) (supporting): Grendels steal food, injure Norns, and carry diseases that sicken the population.
- [Agent inspection](../mechanic/agent-inspection.md) (supporting)
- [Content sharing](../mechanic/content-sharing.md) (supporting): Exported Norns and genomes were swapped and bred across players by a large online community.
- [Modding API](../mechanic/modding-api.md) (supporting)
- [Permadeath](../mechanic/permadeath.md) (supporting)

## Backlinks (computed)

**precedent for:** [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

## Claims

- Norn genetics are haploid, with no dominant or recessive genes and no recombination between loci, and mutation can disable organs or produce Norns that cannot see or hear. *(confidence: medium)* [[15](../source/src-wikipedia-creatures-series.md)]

## Sources

- [Creatures (1996 video game)](../source/src-wikipedia-creatures-1996.md)
- [Creatures (video game series)](../source/src-wikipedia-creatures-series.md)

---
Provenance: created in run `2026-10-24-catalog-gd`.
