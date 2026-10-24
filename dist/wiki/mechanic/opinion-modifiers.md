# Opinion modifiers

*Mechanic* · `opinion-modifiers` · status: **sourced**

Opinions are sums of named, decaying modifiers from events and traits, itemized for the player.

| field | value |
|---|---|
| aliases | opinion breakdown, modifier stacks |
| family | Social relations |
| substrate | Rule system, Aggregate stocks |
| math basis | System dynamics / ODEs, Social network models |
| feedback | Balancing (negative) |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Established |
| core count *(computed)* | 1 |
| earliest game *(computed)* | [Europa Universalis IV](../game/europa-universalis-4.md) |
| earliest year *(computed)* | 2013 |
| prevalence *(computed)* | 2 |
| prevalence share *(computed)* | 0.011 |
| subgenre spread *(computed)* | 1 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns, for each observer-target pair, a list of named modifiers, each with a value, a source, and an expiry or decay rate. Opinion is the clamped sum of static modifiers (shared traits, faith, dynasty, attraction) and event modifiers (gifts, insults, broken promises), and the list is shown as a tooltip. Event modifiers decay toward zero or expire; some are permanent. Crusader Kings III: most opinion decays to 0, tyranny decays 0.25 per month, Friend gives +60 and Nemesis -120, Broke Truce -50 for 3 years, faith hostility 0 to -30, Beautiful +30 attraction, and predecessor opinion is the only inheritable kind. RimWorld pawn opinions are built the same way from social thoughts such as insulted (-15 for 20 days) and deep talk (+15). Europa Universalis IV caps nation opinion at +200 and -200 with itemized reasons. Inputs: events, traits, relations. Outputs: one opinion number for AI decisions plus its legible breakdown.

## Player Experience

The player reads exactly why someone likes or hates them and treats opinion as an account: stacking small positives, waiting out a scandal, or choosing which grudge to pay off. Itemized lists make social systems feel fair and gameable.

## Design Levers

- modifier catalog and magnitudes
- decay or expiry per modifier and whether repeats diminish
- clamp range and thresholds that change AI behavior
- balance between static and event modifiers
- which modifiers are hidden from the player

## Failure Modes

- Additive stacking lets players farm cheap positives, such as repeated gifts or feasts, to override severe grievances.
- Long tooltip lists overwhelm, so players read only the total.
- Linear sums ignore context, so a murderer can be liked if enough small bonuses stack.
- Hidden modifiers that contradict the visible list break trust in the itemization.

## Dynamics

- Players time requests around expiry, waiting for a negative modifier to lapse before asking a favor.
- Shared static modifiers such as faith and culture create blocs whose opinions move together.
- Modifier accounting turns relationships into economic decisions priced in gold or prestige.

## Open Questions

- Can modifiers be generated from free-form events described by a language model while keeping magnitudes balanced and itemized?
- Which nonlinear combination rules (per-category caps, context checks) keep opinions plausible without losing legibility?

## Relations

**synergy**

- [Triggered event chains](../mechanic/triggered-event-chains.md): Events add named modifiers, and modifiers gate later events, chaining stories.

## Backlinks (computed)

**involved in:** [Negotiating faction AI](../opportunity/negotiating-faction-ai.md)

**used by:** [Crusader Kings III](../game/crusader-kings-3.md), [Europa Universalis IV](../game/europa-universalis-4.md)

## Sources

- [Opinion](../source/src-paradoxwikis-2026-ck3-opinion.md)
- [Social](../source/src-rimworldwiki-2026-social.md)
- [Diplomacy](../source/src-paradoxwikis-2026-eu4-diplomacy.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
