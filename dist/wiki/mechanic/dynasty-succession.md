# Dynasty succession

*Mechanic* · `dynasty-succession` · status: **sourced**

When the player character dies, play continues as an heir chosen by inheritance rules.

| field | value |
|---|---|
| aliases | play as heir, succession laws, generational play |
| family | Population & lineage |
| substrate | Rule system, Network / graph |
| math basis | Graph search, Game theory |
| feedback | Balancing (negative) |
| player interface | Observation only, Parameter |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Europa Universalis IV](../game/europa-universalis-4.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 3 |
| prevalence share *(computed)* | 0.017 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a lineage graph over characters, a succession law, and the mapping from the player's identity to a living character. When the player character dies, the law ranks eligible heirs by kinship, age, gender rules, or election; titles and assets are assigned, possibly split among several heirs; and control passes to the designated player heir. If no valid heir exists, the run ends. Crusader Kings III offers primogeniture, ultimogeniture, house seniority, three partition variants, and elective laws for feudal titles; the player continues as the player heir, normally the primary heir, and partition splits realms among siblings; with no valid heir titles pass to the liege, and the run ends without a playable heir. Reigns (2016) continues with a successor monarch who keeps unlocked cards. Inputs: lineage, laws, deaths. Outputs: the new player character, title distribution, opinion resets, claimants.

## Player Experience

Death becomes a chapter break. The player plans for succession by raising, educating, and marrying heirs, fears the untested successor, and feels continuity through the dynasty rather than one person. Partition laws make every death a crisis of fragmentation.

## Design Levers

- succession law catalog and how players can change laws
- what carries over to the heir: wealth, titles, opinions, skills, unlocks
- partition versus single-heir distribution
- opinion penalties and claimant uprisings at succession
- game-over condition when no heir exists

## Failure Modes

- Partition fragments a large realm into small pieces, which players experience as punishment and work around with exploits.
- Successors who inherit everything make death meaningless.
- Heir-killing exploits (arranging deaths to reach a better heir) become optimal play.
- Sudden game over from a missing heir feels arbitrary if eligibility rules are opaque.

## Dynamics

- Rulers invest in heirs' education and marriages, coupling succession to lifecycle and romance.
- Succession crises spawn claimant wars, connecting lineage to diplomacy and conflict.
- Long runs become multi-generation stories that players chronicle as family histories.

## Open Questions

- Can generated character arcs give each heir a distinct reign narrative while succession rules stay mechanical?
- How much should the heir inherit to keep death meaningful without punishing long-term investment?

## Relations

**synergy**

- [Trait inheritance](../mechanic/trait-inheritance.md): Inherited traits make succession a long-term breeding and planning problem (Crusader Kings).

## Backlinks (computed)

**used by:** [Crusader Kings III](../game/crusader-kings-3.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Reigns](../game/reigns.md)

## Sources

- [Succession](../source/src-paradoxwikis-2026-ck3-succession.md)
- [Crusader Kings III](../source/src-wikipedia-crusader-kings-3.md)
- [Reigns (video game)](../source/src-wikipedia-reigns.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
