# inZOI

*Game* · `inzoi` · status: **sourced**

A Krafton life sim in early access since March 2025 in which the player oversees autonomous Zois with eight needs in dense cities, with optional on-device language model prompts and generative tools for patterns and objects.

| field | value |
|---|---|
| year | 2025 |
| developer | inZOI Studio (Krafton) |
| platforms | PC |
| subgenre | Life sim |
| sim domain | Domestic / personal, Social / interpersonal, Urban |
| player role | Caretaker |
| agency model | Direct unit control, Indirect incentive, Zoning / placement, Conversational |
| time model | Real-time with pause |
| sim scale | Household / crew |
| fidelity | Stylized |
| perspective | Free 3D camera |
| win structure | Open sandbox |
| failure model | Permadeath |
| narrative mode | Emergent |
| multiplayer | Single-player |
| modding | Content |
| production tier | AAA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 1 |
| influenced by | [The Sims](../game/the-sims.md) |
| cluster *(computed)* | C01 |
| core count *(computed)* | 2 |
| mechanic count *(computed)* | 17 |

## Summary

A Krafton life sim in early access since March 2025 in which the player oversees autonomous Zois with eight needs in dense cities, with optional on-device language model prompts and generative tools for patterns and objects.

## Core Loop

create Zois and build homes -> Zois act on needs and personality -> player directs actions or prompts thoughts -> jobs, relationships, rumors, and illness move through the city -> edit the city and generate new items -> share on Canvas

## Design Notes

inZOI casts the player as an intern at AR Company who manages a city of virtual people and its karma system. It pairs a Sims-style needs model (hunger, hygiene, bathroom, fun, social, energy, sleep, recognition) with city-scale free will that the developers say produces rumors, trends, and disease, plus optional direct control of a Zoi or vehicle. Generative models sit mainly in the creation layer: text prompts generate patterns and images for clothing and furniture, 2D images convert to 3D props, and an on-device small language model lets typed prompts steer a Zoi's thoughts and actions. City-wide progression of unplayed Zois is the offscreen-life-progression mechanic; karma has no mechanic id.

## Relations

**influenced by**

- [The Sims](../game/the-sims.md)

**uses**

- [Needs decay](../mechanic/needs-decay.md) (core): Eight needs (hunger, hygiene, bathroom, fun, social, energy, sleep, recognition) decay and drive Zois' free-will choices.
- [Generative content on demand](../mechanic/generative-content.md) (core): Text prompts generate patterns and images for outfits, props, and furniture; 2D images become 3D in-game objects; uploaded video becomes character motion.
- [Natural-language interaction](../mechanic/natural-language-interaction.md) (supporting): An on-device small language model lets the player type prompts that influence a Zoi's thoughts and actions.
- [Gossip propagation](../mechanic/gossip-propagation.md) (supporting): Autonomous interactions generate rumors that spread among Zois.
- [Contagion](../mechanic/contagion.md) (supporting): The developers list disease, alongside rumors and trends, among the outcomes that spread through Zois' autonomous interactions.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Personality and life experience shape each Zoi's actions and relationships.
- [Relationship values](../mechanic/relationship-values.md) (supporting)
- [Romance and family](../mechanic/romance-family.md) (supporting)
- [Career ladder](../mechanic/career-ladder.md) (supporting): Careers include active jobs played on site.
- [Agent skills](../mechanic/agent-skills.md) (supporting)
- [Lifecycle and aging](../mechanic/lifecycle-aging.md) (supporting): Zois age and die.
- [Building placement](../mechanic/free-placement.md) (supporting): Build mode places walls, roofs, stairs, fences, and gates; city edit changes streets, properties, and weather.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Canvas is the in-game platform for sharing characters, homes, and stories.
- [Direct avatar control](../mechanic/direct-avatar.md) (supporting): Players can switch from point-and-click orders to direct control of a Zoi or a vehicle.
- [Off-screen life progression](../mechanic/offscreen-life-progression.md) (supporting): City-wide free will keeps Zois across the city living autonomously while the player directs one household, producing rumors, trends, and disease; the fidelity of the update for distant Zois is not documented.
- [Pause and speed control](../mechanic/variable-speed.md) (supporting)
- [Utility action selection](../mechanic/utility-action-selection.md) (supporting)

## Backlinks (computed)

**deploys:** [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md), [Learned kinematic motion synthesis](../technique/learned-motion-synthesis.md), [On-device small language models for characters](../technique/on-device-language-models.md), [Text- and image-to-3D asset generation](../technique/text-to-3d-assets.md)

**precedent for:** [Generative decoration catalogs](../opportunity/generative-decoration-catalogs.md), [Local-first AI simulation games](../opportunity/local-first-ai-sims.md), [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md)

## Sources

- [inZOI](../source/src-wikipedia-inzoi.md)
- [inZOI on Steam](../source/src-steam-2025-inzoi.md)

---
Provenance: created in run `2026-10-24-catalog-gc`; reviewed in `2026-10-24-review-fixes`.
