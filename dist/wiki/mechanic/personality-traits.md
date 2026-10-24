# Personality traits

*Mechanic* · `personality-traits` · status: **sourced**

Fixed or slow-changing traits change each agent's needs, preferences, and available actions.

| field | value |
|---|---|
| aliases | traits, personality points |
| family | Agents & behavior |
| substrate | Agent-based, Rule system |
| math basis | Utility / decision theory, Combinatorics |
| feedback | None |
| player interface | Observation only, Choice / cards |
| legibility | 4 |
| emergence potential | 3 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 3 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 3 |
| earliest game *(computed)* | [Little Computer People](../game/little-computer-people.md) |
| earliest year *(computed)* | 1985 |
| prevalence *(computed)* | 25 |
| prevalence share *(computed)* | 0.144 |
| subgenre spread *(computed)* | 11 |
| technique count *(computed)* | 1 |
| technique exposure *(computed)* | 0.188 |

## Definition

Owns a small per-agent set of discrete traits or continuous personality dimensions, assigned at generation or during development. Traits hold no dynamics of their own; other systems read them as modifiers: they scale need decay, shift utility scores and break thresholds, nullify or add memories, change opinions of others, and unlock or forbid actions. The Sims (2000) uses points in opposing pairs such as nice/grouchy and active/lazy that scale object advertisements (Feed Fish gives 1-11 Fun by Playful); The Sims 3 lets adults hold up to five traits; RimWorld traits such as Steadfast and Nervous shift the mental break threshold, and Psychopath nullifies several death thoughts. Crusader Kings III characters tend to hold three personality traits gained through childhood events at ages 9, 11, and 13, opposites are excluded, and stress breaks can change them. Inputs: generation or life events. Outputs: differentiated behavior from shared rules.

## Player Experience

Traits are the shorthand by which players recognize and cast characters. The player reads a trait list, predicts behavior, and assigns roles; contradictory combinations become memorable, and players chase or avoid specific traits when recruiting.

## Design Levers

- trait count per agent and exclusivity rules
- magnitude of each trait's modifiers and which systems it touches
- discrete traits versus continuous dimensions
- acquisition: fixed at birth, childhood events, life events, or stress
- visibility of traits to the player

## Failure Modes

- Strictly positive traits make recruitment a search for the same few, flattening variety.
- Flavor traits with no mechanical effect feel fake; traits with huge effects dwarf player choices.
- Too many traits per agent average out into bland behavior.

## Dynamics

- Traits that affect opinion create recurring frictions and friendships between particular pairs.
- Players build around trait combinations, so traits become strategy as well as flavor.
- Inherited or culturally transmitted traits drift across generations, coupling personality to lineage.

## Open Questions

- Can a natural-language persona replace a trait list while keeping behavior predictable enough for players to plan around?
- What is the smallest trait set that still produces distinct, recognizable characters?

## Sources

- src-forbus-2001-programming-objects-sims
- src-wikipedia-the-sims-3
- src-rimworldwiki-2026-mental-break
- src-rimworldwiki-2026-thoughts
- src-paradoxwikis-2026-ck3-traits

## Backlinks (computed)

**affected by:** [LLM models of individual human choice](../technique/human-behavior-simulation-models.md)

**involved in:** [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md)

**used by:** [Crusader Kings III](../game/crusader-kings-3.md), [Dwarf Fortress](../game/dwarf-fortress.md), [Football Manager](../game/football-manager.md), [FTL: Faster Than Light](../game/ftl.md), [Going Medieval](../game/going-medieval.md), [inZOI](../game/inzoi.md), [Little Computer People](../game/little-computer-people.md), [Motorsport Manager](../game/motorsport-manager.md), [Oxygen Not Included](../game/oxygen-not-included.md), [Paralives](../game/paralives.md), [Project Zomboid](../game/project-zomboid.md), [Prom Week](../game/prom-week.md), [RimWorld](../game/rimworld.md), [Space Haven](../game/space-haven.md), [Stellaris](../game/stellaris.md), [Suck Up!](../game/suck-up.md), [Surviving Mars](../game/surviving-mars.md), [The Sims](../game/the-sims.md), [The Sims 2](../game/the-sims-2.md), [The Sims 3](../game/the-sims-3.md), [The Sims 4](../game/the-sims-4.md), [This War of Mine](../game/this-war-of-mine.md), [Tomodachi Life](../game/tomodachi-life.md), [Two Point Hospital](../game/two-point-hospital.md), [Versu](../game/versu.md)

## Sources

- [Some notes on programming objects in The Sims](../source/src-forbus-2001-programming-objects-sims.md)
- [The Sims 3](../source/src-wikipedia-the-sims-3.md)
- [Mental break](../source/src-rimworldwiki-2026-mental-break.md)
- [Thoughts](../source/src-rimworldwiki-2026-thoughts.md)
- [Traits](../source/src-paradoxwikis-2026-ck3-traits.md)

---
Provenance: created in run `2026-10-24-taxonomy-m3`.
