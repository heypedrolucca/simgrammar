# Negotiating faction AI

*Opportunity* · `negotiating-faction-ai` · status: **asserted**

Grand strategy rivals that negotiate in language and plan around their promises, combining strategic search with dialogue.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Faction diplomacy](../mechanic/faction-diplomacy.md), [Opinion modifiers](../mechanic/opinion-modifiers.md), [Reputation](../mechanic/reputation.md), [Causal breakdown tooltips](../mechanic/causal-tooltips.md) |
| applies | [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md), [Regret minimization and search for imperfect-information games](../technique/imperfect-information-solvers.md), [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md) |
| precedent | [Crusader Kings III](../game/crusader-kings-3.md), [Stellaris](../game/stellaris.md), [Sid Meier's Civilization](../game/civilization.md), [Europa Universalis IV](../game/europa-universalis-4.md), [Balance of Power](../game/balance-of-power.md) |
| novelty | 3 |
| feasibility | 3 |
| impact | 3 |
| horizon | 1-2 years |
| falsifiable signal | {'prediction': 'A major grand strategy or 4X release will ship AI opponents that negotiate through free-text or generated-language diplomacy backed by a planner.', 'resolve_by': '2029-06-30', 'criteria': 'Developer statement or documentation describing language-based AI diplomacy in a title from Paradox, Firaxis, Amplitude, or a peer studio.'} |
| priority *(computed)* | 3.0 |

## Thesis

Diplomacy in grand strategy is reduced to acceptance scores on fixed proposals. Cicero showed in 2022 that grounding dialogue in a planner that predicts others' moves lets an agent negotiate and keep useful commitments in a seven-player game. Applying the pattern to faction diplomacy makes alliances, betrayals, and bargains first-class play, and opinion modifiers give the model a structured memory of who kept their word.

## Design Sketch

AI rulers send and answer proposals in text; each message is backed by an intent object (offer, demand, threat, promise) that the planner evaluates. Broken promises create named opinion modifiers visible to every faction. Players can still use classic proposal menus; text adds nuance such as conditional offers and side deals.

## Key Risks

- Planner cost scales badly with many factions.
- Players exploit language models with persuasion that the planner should ignore.
- Long campaigns exceed the consistency horizon of dialogue memory.

## Validation Experiment

In a five-faction diplomacy sandbox, compare menu-only AI with planner-plus-dialogue AI on player-rated plausibility, commitment-keeping rate, and win rates against scripted baselines. Success: higher plausibility and a commitment-keeping rate above 80 percent without exploitable persuasion loops in red-team play.

## Falsifiable signal

- **Prediction:** A major grand strategy or 4X release will ship AI opponents that negotiate through free-text or generated-language diplomacy backed by a planner.
- **Resolve by:** 2029-06-30
- **Criteria:** Developer statement or documentation describing language-based AI diplomacy in a title from Paradox, Firaxis, Amplitude, or a peer studio.

## Relations

**applies**

- [Language models grounded in strategic planning for negotiation games](../technique/cicero-strategic-dialogue.md)
- [Regret minimization and search for imperfect-information games](../technique/imperfect-information-solvers.md)
- [Grammar-constrained decoding for valid game actions](../technique/constrained-decoding.md)

**involves**

- [Faction diplomacy](../mechanic/faction-diplomacy.md)
- [Opinion modifiers](../mechanic/opinion-modifiers.md)
- [Reputation](../mechanic/reputation.md)
- [Causal breakdown tooltips](../mechanic/causal-tooltips.md)

**precedent**

- [Crusader Kings III](../game/crusader-kings-3.md)
- [Stellaris](../game/stellaris.md)
- [Sid Meier's Civilization](../game/civilization.md)
- [Europa Universalis IV](../game/europa-universalis-4.md)
- [Balance of Power](../game/balance-of-power.md)

---
Provenance: created in run `2026-10-24-synthesis`.
