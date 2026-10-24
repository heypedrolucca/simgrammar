# Crusader Kings III

*Game* · `crusader-kings-3` · status: **sourced**

A character-driven grand strategy game in which the player rules as successive heads of a medieval dynasty from 867 or later to 1453, managing traits, stress, vassal opinion, marriages, and succession across a map of feudal titles.

| field | value |
|---|---|
| aliases | CK3 |
| year | 2020 |
| developer | Paradox Development Studio |
| platforms | PC, Console |
| subgenre | Grand strategy |
| subgenre secondary | Systemic RPG |
| sim domain | Political / governance, Social / interpersonal, Military / conflict |
| player role | Ruler / statesman |
| agency model | Direct unit control, Policy / parameter |
| time model | Real-time with pause |
| sim scale | Nation / polity |
| fidelity | Systemic |
| perspective | Top-down / side 2D |
| win structure | Open sandbox |
| failure model | Permadeath |
| narrative mode | Hybrid |
| multiplayer | Single-player, Competitive |
| modding | Total conversion |
| production tier | AA |
| agent count order | 10,000+ |
| emergence | 4 |
| influence | 2 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 4 |
| mechanic count *(computed)* | 20 |

## Summary

A character-driven grand strategy game in which the player rules as successive heads of a medieval dynasty from 867 or later to 1453, managing traits, stress, vassal opinion, marriages, and succession across a map of feudal titles.

## Core Loop

play the current ruler -> manage vassal opinion, council, and stress -> arrange marriages, schemes, and wars over claims -> ruler dies -> heir inherits titles under succession law -> realm fragments or consolidates

## Design Notes

CK3 makes the player a character rather than a state: realm strength depends on vassals whose itemized opinions, traits, and family ties decide whether they serve or rebel. Succession laws make death the main source of disruption, and stress penalizes playing a character against type, which pushes players to roleplay their traits. Event content is authored but fired from on_actions and character state, so the same templates produce different stories in different courts; culture and religion conversion is not yet a mechanic in the taxonomy (proposal culture-religion-conversion).

## Relations

**uses**

- [Dynasty succession](../mechanic/dynasty-succession.md) (core): On death, play passes to the player heir and titles pass under the realm's succession law, so partition can split a realm among children; the game ends if no viable heir remains, and dynasty heads spend Renown on bonuses for every dynasty member.
- [Personality traits](../mechanic/personality-traits.md) (core): Personality, education, and genetic traits modify the six skills (Diplomacy, Martial, Stewardship, Intrigue, Learning, Prowess), opinions, and which event options a character can take.
- [Opinion modifiers](../mechanic/opinion-modifiers.md) (core): Each character's opinion of another is an itemized list of modifiers from traits, relations, actions, and events, many expiring over time; discontented vassals join factions pressing for independence, a rival claimant, or less crown authority.
- [Agent skills](../mechanic/agent-skills.md) (supporting): Skills grow from education and from perks in six lifestyles, each with three skill trees.
- [Relationship values](../mechanic/relationship-values.md) (supporting): Friends, rivals, and lovers form between characters and shift opinions and event outcomes.
- [Romance and family](../mechanic/romance-family.md) (supporting): Marriages create alliances and heirs, making match choice a political decision.
- [Trait inheritance](../mechanic/trait-inheritance.md) (supporting): Genetic traits such as strong or poor health pass to children.
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting)
- [Stability and unrest](../mechanic/stability-unrest.md) (supporting): Vassal factions accumulate strength and can revolt when their demands are refused.
- [Faction diplomacy](../mechanic/faction-diplomacy.md) (supporting): Wars are fought over claims, and marriages and alliances link realms.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (supporting): Events are called from on_actions, decisions, and interactions, with weighted options and scheduled follow-ups.
- [Tech tree](../mechanic/tech-tree.md) (supporting): Lifestyle perk trees and cultural innovations unlock abilities and buildings.
- [Causal breakdown tooltips](../mechanic/causal-tooltips.md) (supporting): Nested tooltips let players open explanations of terms inside other tooltips.
- [Stress accumulation](../mechanic/stress-accumulation.md) (core): Acting against personality traits and suffering events add stress; crossing stress levels fires mental-break events whose coping options can add traits (from level 2 up), and extreme stress can kill the character.
- [Political capital](../mechanic/political-capital.md) (supporting): Prestige and piety accrue from rank, traits, and deeds and are spent on actions such as creating titles (prestige) and faith decisions (piety).
- [Culture and religion conversion](../mechanic/culture-religion-conversion.md) (supporting): Counties carry a faith and a culture; the court chaplain can convert a county's faith and the steward can promote the ruler's culture, while faith hostility sets opinion penalties from 0 to -30.
- [Territorial control](../mechanic/territorial-control.md) (supporting): Counties belong to titles with de jure hierarchies, and wars are fought to press claims on them; conquered counties start with low county control.
- [War score and peace terms](../mechanic/war-score-peace.md) (supporting): War score from battles and occupation lets the attacker enforce the war goal at full score, while either side can offer white peace.
- [Statistical combat resolution](../mechanic/stat-combat-resolution.md) (supporting): Battles resolve from army size, men-at-arms, knights, commander skill, and terrain, in phases that run until one side is routed.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)

## Backlinks (computed)

**precedent for:** [Content-elastic event systems](../opportunity/content-elastic-events.md), [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md), [Negotiating faction AI](../opportunity/negotiating-faction-ai.md), [Placement that tells stories](../opportunity/placement-that-tells-stories.md)

## Sources

- [Crusader Kings III](../source/src-wikipedia-crusader-kings-3.md)
- [Event modding (Crusader Kings III)](../source/src-paradoxwikis-2026-ck3-event-modding.md)
- [Victoria 3 nested tooltip system](../source/src-pcgamesn-2022-victoria-3-nested-tooltips.md)

---
Provenance: created in run `2026-10-24-catalog-gi`; reviewed in `2026-10-24-review-fixes`.
