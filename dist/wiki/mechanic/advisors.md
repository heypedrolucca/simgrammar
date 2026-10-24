# Advisors

*Mechanic* · `advisors` · status: **sourced**

In-world advisor characters monitor simulation indicators, summarize problems, and recommend actions.

| field | value |
|---|---|
| aliases | advisor council, counselors, department advisors |
| family | Information & legibility |
| substrate | UI layer, Rule system |
| math basis | Utility / decision theory, Information theory |
| feedback | None |
| player interface | Observation only |
| legibility | 4 |
| emergence potential | 1 |
| authoring cost | 3 |
| compute cost | 1 |
| tuning difficulty | 2 |
| ai leverage | 4 |
| maturity | Classic |
| core count *(computed)* | 0 |
| earliest game *(computed)* | [Hamurabi](../game/hamurabi.md) |
| earliest year *(computed)* | 1968 |
| prevalence *(computed)* | 6 |
| prevalence share *(computed)* | 0.034 |
| subgenre spread *(computed)* | 5 |
| technique count *(computed)* | 2 |
| technique exposure *(computed)* | 1.125 |

## Definition

An advisor layer watches a set of indicators (budget balance, unemployment, crime, service coverage, happiness, military strength) and maps threshold crossings or rule matches to authored messages spoken by a named character, usually with a recommended action. It owns no simulation state: only trigger conditions, a priority per message, cooldowns, and an optional persona per department. Each evaluation interval it tests its conditions, ranks firing messages by severity, suppresses those still on cooldown, and presents the top one as a pop-up, voiced line, or entry in an advisor panel the player opens on demand. Inputs are aggregate state variables; outputs are text and, in some games, a one-click link to the relevant tool. Canonical forms: the department advisors of SimCity 2000 and SimCity 4, the Super NES SimCity advisor Dr. Wright who appears to report city problems, the advisor screens of the Civilization series, and Tropico's Penultimo.

## Player Experience

The player gets a running diagnosis without reading every graph. Early on advisors teach which variables matter and what usually fixes them; later the player weighs advice against their own model, and conflicting advisors make tradeoffs explicit. Bad or repetitive advice is felt as nagging.

## Design Levers

- which indicators each advisor watches and the threshold or trend that triggers a message
- diagnosis only versus a concrete recommendation or a one-click fix
- one generalist advisor versus a council of department advisors with conflicting priorities
- delivery mode: interrupting pop-up, voiced line, or passive panel opened on demand
- cooldown and repetition rules per message
- accuracy: whether advisors read true state, a lagged view, or a view biased toward their department

## Failure Modes

- A message keeps firing while the player cannot act on it, so players mute or ignore the advisor entirely.
- Advice derived from a single indicator recommends the wrong fix when the cause is an interaction, such as more police when crime is driven by unemployment.
- Advisors that are always right reduce the player to following instructions; advisors that are often wrong teach players to ignore all advice.
- Lines written for early-game states become irrelevant or wrong at late-game scale.

## Dynamics

- Advisors act as an embedded tutorial whose value fades as the player's own causal model improves.
- Department advisors arguing for opposite policies externalize tradeoffs such as tax revenue versus satisfaction.
- When advice is trusted, player builds converge on what the advisor recommends, narrowing strategic variety.

## Open Questions

- Can a language-model advisor grounded in live state queries answer arbitrary why-questions accurately enough to be trusted, and how should it express uncertainty?
- Does advice deliberately biased by an advisor's department or personality produce better decisions than neutral advice?

## Backlinks (computed)

**affected by:** [LLM explanation of simulation state](../technique/llm-explanation-of-state.md), [On-device small language models for characters](../technique/on-device-language-models.md)

**involved in:** [Why-query over the simulation log](../opportunity/causal-why-query.md), [Explained delegation to AI managers](../opportunity/explained-delegation.md)

**used by:** [Black & White](../game/black-and-white.md), [Sid Meier's Civilization](../game/civilization.md), [Hamurabi](../game/hamurabi.md), [SimCity 4](../game/simcity-4.md), [Suzerain](../game/suzerain.md), [Theme Hospital](../game/theme-hospital.md)

## Claims

- The Super NES version of SimCity added Dr. Wright, an advisor character who appears to report problems in the city. *(confidence: medium)* [[54](../source/src-wikipedia-simcity-1989.md)]

## Sources

- [SimCity (1989 video game)](../source/src-wikipedia-simcity-1989.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
