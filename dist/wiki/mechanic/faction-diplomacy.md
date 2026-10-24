# Faction diplomacy

*Mechanic* · `faction-diplomacy` · status: **sourced**

Factions hold relations with each other, and treaties, alliances, and wars follow from interests and opinion.

| field | value |
|---|---|
| aliases | diplomatic relations, AI diplomacy, foreign relations |
| family | Social relations |
| substrate | Network / graph, Rule system, Aggregate stocks |
| math basis | Game theory, Social network models |
| feedback | Both |
| player interface | Choice / cards, Observation only |
| legibility | 3 |
| emergence potential | 4 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 4 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Balance of Power](../game/balance-of-power.md) |
| earliest year *(computed)* | 1985 |
| prevalence *(computed)* | 15 |
| prevalence share *(computed)* | 0.086 |
| subgenre spread *(computed)* | 7 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 0.812 |

## Definition

Owns a relation value for each pair of factions, the modifiers feeding it, and agreement states such as war, peace, truce, alliance, and vassalage. Events (trade, gifts, border friction, attacks, broken treaties) change the value, and many games drift it toward a baseline. A proposal is accepted when an AI evaluation combining relation, interests, relative power, and reputation passes a threshold. RimWorld faction goodwill runs -100 to 100: hostile at -75 or below, allied at 75 or above until it falls to 0; civil outlanders drift back into -50..50; trade gives +1 per 500 silver and returning a prisoner +12, while pirates stay at -100. Europa Universalis IV caps opinion at +200 and -200 with itemized reasons, adds 5 to alliance acceptance per point of diplomatic reputation, and allows a base of 4 diplomatic relations. Inputs: events, interests, power. Outputs: war declarations, trade access, military aid, coalitions.

## Player Experience

The player manages a web of relations as a resource: buying goodwill with gifts, timing betrayals, and reading acceptance breakdowns to see what a deal needs. Wars feel like consequences of accumulated grievances rather than random events.

## Design Levers

- relation scale, thresholds for state changes, and baseline drift
- modifier catalog and decay per event type
- AI acceptance formula (relation, power, interests, reputation) and how much of it is shown
- agreement types and their obligations, such as alliance calls to arms and truce lengths
- limits such as relation slots or diplomat counts

## Failure Modes

- Gift exploits: money converts linearly into friendship, so diplomacy becomes a purchase.
- AI that ignores its own interests or the balance of power feels suicidal, while AI that refuses for unshown reasons feels arbitrary.
- Factions locked at permanent hostility remove diplomacy from most of the threat model.
- Coalitions that form against the leader regardless of context read as rubber-banding.

## Dynamics

- Coalitions against an expanding player form from shared grievances, a balancing loop on growth.
- Alliance chains pull factions into wars they did not choose, producing cascading conflicts.
- Trade raises goodwill, which opens more trade, a reinforcing loop between economy and diplomacy.

## Open Questions

- Can language-model negotiators bargain, bluff, and keep commitments with players in ways players accept as fair and legible?
- How should opinion and interest be separated so AI factions betray for reasons players can foresee?

## Relations

**synergy**

- [Reputation](../mechanic/reputation.md): Standing with a faction gates treaties and trade.

## Backlinks (computed)

**affected by:** [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md), [Monte Carlo tree search for game AI](../technique/monte-carlo-tree-search.md)

**involved in:** [Agent ambassadors between player worlds](../opportunity/agent-ambassadors-async.md), [Language-agent society terrarium](../opportunity/llm-society-terrarium.md), [Negotiating faction AI](../opportunity/negotiating-faction-ai.md)

**used by:** [Balance of Power](../game/balance-of-power.md), [Caves of Qud](../game/caves-of-qud.md), [Sid Meier's Civilization](../game/civilization.md), [Crusader Kings III](../game/crusader-kings-3.md), [Elite Dangerous](../game/elite-dangerous.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Hearts of Iron IV](../game/hearts-of-iron-4.md), [Kenshi](../game/kenshi.md), [Kingdoms and Castles](../game/kingdoms-and-castles.md), [Songs of Syx](../game/songs-of-syx.md), [Spore](../game/spore.md), [Stellaris](../game/stellaris.md), [Suzerain](../game/suzerain.md), [Tropico 6](../game/tropico-6.md), [Victoria 3](../game/victoria-3.md)

## Sources

- [Goodwill](../source/src-rimworldwiki-2026-goodwill.md)
- [Diplomacy](../source/src-paradoxwikis-2026-eu4-diplomacy.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
