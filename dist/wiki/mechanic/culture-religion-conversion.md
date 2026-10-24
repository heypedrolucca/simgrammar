# Culture and religion conversion

*Mechanic* · `culture-religion-conversion` · status: **asserted**

Provinces or population groups carry culture and faith identities that drift or are converted by missionaries, policies, and rulers, changing unrest, opinion, and bonuses.

| field | value |
|---|---|
| aliases | conversion, assimilation, missionaries, faith spread, ethics attraction |
| family | Population & lineage |
| substrate | Aggregate stocks, Rule system |
| math basis | Social network models, System dynamics / ODEs |
| feedback | Reinforcing (positive) |
| player interface | Orders, Choice / cards, Parameter |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 3 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Europa Universalis IV](../game/europa-universalis-4.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Summary

Provinces or population groups carry culture and faith identities that drift or are converted by missionaries, policies, and rulers, changing unrest, opinion, and bonuses.

## Definition

Owns categorical identity attributes (culture, faith, and in some games ideology or ethics) per province, county, or population group, plus conversion progress or a per-period conversion share. Each period progress accrues from sources such as assigned missionaries or court officials, state religion and laws, assimilation into the majority culture, buildings, and the ruler's or government's alignment, against resistance from population size, development, or fervor; when progress completes the attribute flips, or in population-group models a fraction of each group switches. Other systems read the identities: a mismatch with the ruler or state adds unrest and opinion penalties, a match or accepted status grants bonuses, and shared or hostile identities shape alliances and wars. Victoria 3 stores its population as pops that share profession, culture, religion, and state. Crusader Kings III applies opinion penalties between faiths by hostility and lets rulers convert counties' faith and culture. Europa Universalis IV converts province religion with missionaries. It differs from population-strata, which owns class tiers and promotion; identity is orthogonal to class.

## Player Experience

The map has a second layer of identity beneath its borders. The player conquers land that will not accept them, then spends missionaries, officials, or decades of policy converting it, choosing between tolerating diversity and its unrest or homogenizing at a cost. Faiths and cultures spreading, splitting, and reforming become the long arcs of a campaign.

## Design Levers

- conversion speed and the resistance factors (population size, development, fervor)
- which agents or policies can convert (missionaries, court officials, laws, buildings)
- binary flip per province versus a share of each population group per period
- penalties and bonuses attached to matching or mismatched identities
- tolerance and acceptance rules that let mixed identities coexist
- whether players can found, reform, or hybridize faiths and cultures

## Failure Modes

- Cheap, certain conversion homogenizes every realm and erases the identity layer by mid-game.
- Severe unrest from mismatched identity turns conquering other cultures into a trap and narrows play to one strategy.
- Faiths and cultures that differ only in numeric modifiers feel interchangeable.
- Treating the conversion of real faiths and peoples as a pure optimization can read as endorsing forced conversion.

## Dynamics

- Majority identities grow by assimilation, a reinforcing loop toward homogeneous heartlands with contested borderlands.
- Identity mismatch feeds unrest and revolt, coupling conversion to stability and military occupation.
- Shared faiths and cultures become alliance lines, so identity maps shape diplomacy.

## Open Questions

- Can language models generate new faiths and cultures whose doctrines produce consistent mechanical effects and believable schisms?
- Can conversion run as diffusion through social networks of individual agents rather than as a per-province progress bar?

## Backlinks (computed)

**used by:** [Crusader Kings III](../game/crusader-kings-3.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Stellaris](../game/stellaris.md), [Victoria 3](../game/victoria-3.md)

## Claims

- Victoria 3 pops share profession, culture, religion, state, and workplace. *(confidence: medium)* [[70](../source/src-paradoxwikis-2026-vic3-pops.md)]
- Crusader Kings III applies faith hostility opinion modifiers from 0 to -30 between characters. *(confidence: medium)* [[71](../source/src-paradoxwikis-2026-ck3-opinion.md)]

## Sources

- [Pops](../source/src-paradoxwikis-2026-vic3-pops.md)
- [Opinion](../source/src-paradoxwikis-2026-ck3-opinion.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
