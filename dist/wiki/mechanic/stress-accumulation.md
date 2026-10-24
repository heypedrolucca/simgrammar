# Stress accumulation

*Mechanic* · `stress-accumulation` · status: **sourced**

A slow per-agent stress stock integrates negative experiences scaled by personality and, as it crosses levels, triggers breaks or lasting changes.

| field | value |
|---|---|
| aliases | stress, stress levels, psychological stress |
| family | Agents & behavior |
| substrate | Aggregate stocks, Agent-based |
| math basis | System dynamics / ODEs, Markov / stochastic processes |
| feedback | Both |
| player interface | Observation only, Choice / cards |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Dwarf Fortress](../game/dwarf-fortress.md) |
| earliest year *(computed)* | 2006 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns a per-agent stress value with slow decay and a ladder of levels. Each experience adds or removes an amount scaled by personality, and the value relaxes toward zero only slowly, so stress is an integral of history rather than a snapshot of current conditions. Crossing a level triggers a break event, a coping trait, a lasting change in behavior, or death at the extreme. Dwarf Fortress keeps a hidden stress value from -1,000,000 to +1,000,000 with effects from +10,000, +25,000, and +50,000: emotions add or subtract stress, facets such as bravery, stress vulnerability, and anxiety scale it, long-term memories keep adding to it, and high stress leads to tantrums, depression, obliviousness, or insanity. Crusader Kings III adds stress when a character acts against its personality traits, fires mental-break events as stress levels are crossed, lets breaks at level 2 or higher change traits, and can kill at extreme stress, all without a mood meter. It differs from mood-breakdown, whose mood is a near-instant sum of current modifiers, and from memories-thoughts, which owns the event entries that can feed it.

## Player Experience

The player manages a slow-burning account of bad experiences rather than a moment-to-moment mood: a character can look fine while carrying stress from months ago. In Crusader Kings III this makes roleplay a resource decision, since acting against a character's traits costs stress that must later be shed; in Dwarf Fortress a fortress's past tragedies become a hidden debt that comes due.

## Design Levers

- stress per event type and the personality scaling applied to it
- decay rate toward zero and whether relief needs active coping (feasts, hobbies, vices)
- level thresholds and what each level triggers
- break catalog: tantrums, coping traits, personality change, death
- visibility of the value, hidden as in Dwarf Fortress or shown as in Crusader Kings III

## Failure Modes

- Hidden stress makes breakdowns look random, since the cause may be months old.
- Slow decay plus frequent stressors leaves a population chronically stressed after one disaster, with no recovery path.
- Cheap relief actions such as a feast or a vice reduce stress management to a periodic chore.
- Lethal stress at the top of the ladder can end a character or dynasty through bookkeeping rather than drama.

## Dynamics

- A shared tragedy stresses many agents at once, so breaks cluster weeks or months after the event.
- Breaks generate new stressors for witnesses, a reinforcing cascade, as in Dwarf Fortress tantrum spirals.
- Coping traits acquired through breaks permanently change characters, turning stress history into identity.

## Open Questions

- Does showing the stress value make breaks feel fair at the cost of drama, or can partial signals give warning without a meter?
- Can language-model agents express accumulated stress in dialogue and behavior before a threshold break, so players see it building?

## Backlinks (computed)

**used by:** [Crusader Kings III](../game/crusader-kings-3.md), [Dwarf Fortress](../game/dwarf-fortress.md)

## Claims

- Dwarf Fortress keeps a hidden stress value from -1,000,000 to +1,000,000 with effects from +10,000, +25,000, and +50,000; emotions add or subtract stress and facets such as bravery, stress vulnerability, and anxiety scale it. *(confidence: medium)* [[92](../source/src-dfwiki-2026-stress.md)]
- In Crusader Kings III, acting against personality traits adds stress that can be lethal, and stress breaks at level 2 or higher can change traits. *(confidence: medium)* [[93](../source/src-wikipedia-crusader-kings-3.md), [94](../source/src-paradoxwikis-2026-ck3-traits.md)]

## Sources

- [Stress](../source/src-dfwiki-2026-stress.md)
- [Crusader Kings III](../source/src-wikipedia-crusader-kings-3.md)
- [Traits](../source/src-paradoxwikis-2026-ck3-traits.md)

---
Provenance: created in run `2026-10-24-taxonomy-triage-a`.
