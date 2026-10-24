# LLM models of individual human choice

*Technique* · `human-behavior-simulation-models` · status: **sourced**

Language models conditioned on interviews or fine-tuned on millions of experimental choices that predict how specific people or populations answer surveys, play economic games, and choose in decision tasks.

| field | value |
|---|---|
| aliases | Centaur, interview-grounded agents, silicon samples, Psych-101 |
| category | Player modeling |
| year | 2025 |
| maturity | Research |
| trl | 3 |
| runtime | Analytics / live-ops, Design assist |
| determinism impact | Preserves |
| horizon | 3-5 years |
| risks | Evaluation difficulty, Consistency / hallucination, IP / provenance |
| builds on | [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md) |
| deployed in |  |
| affects count *(computed)* | 9 |

## Summary

Language models conditioned on interviews or fine-tuned on millions of experimental choices that predict how specific people or populations answer surveys, play economic games, and choose in decision tasks.

## Mechanism

Two approaches. Grounded agents put a person's two-hour interview transcript (or survey answers) in the prompt of a generative agent and ask it to answer new questions as that person; accuracy is normalized by how consistently the real person answers the same items two weeks later. Fine-tuned choice models transcribe experiments into natural language and train a model to predict each trial's choice: Centaur adds rank-8 QLoRA adapters (about 0.15% of parameters) to a frozen 4-bit Llama 3.1 70B and trains one epoch on Psych-101 (160 experiments, 60,092 participants, 10,681,650 choices), scoring held-out participants by negative log-likelihood against cognitive models. Earlier silicon-sample work conditions a model on demographic backstories to reproduce subgroup response distributions. In games the same pipeline would predict how players or simulated citizens choose among options described in text.

## Limitations

- Psych-101 is skewed toward WEIRD participants and toward learning and decision-making tasks; individual differences such as age were not in the prompts.
- Critics show Centaur performs well even without valid instructions, so its predictions on new game situations may track surface statistics.
- Interview-grounded agents need hours of data per person, which raises consent and privacy questions for player data.
- Centaur's 70B base needed about five days on one A100 to fine-tune; the 8B Minitaur variant generalized less robustly.
- No study yet validates these models on choices inside games, where options are visual, timed, and repeated.

## Sources

- src-park-2024-1000-people
- src-stanford-hai-2025-simulating-human-behavior
- src-binz-2025-centaur
- src-liu-2025-centaur-instruction-understanding
- src-orr-2025-not-even-wrong
- src-argyle-2023-out-of-one-many
- src-aher-2022-turing-experiments

## Relations

**affects**

- [Customer value choice](../mechanic/customer-value-choice.md) (Replaces substrate): Customer purchase decisions could be sampled from a model trained on human choice data, giving realistic heterogeneity and biases, instead of utility = value x preference - price with hand-set weights.
- [Crowd preferences](../mechanic/crowd-preferences.md) (Deepens): Visitor populations could be drawn from person-grounded profiles whose preferences and tolerances are measured against real people rather than sampled from designer distributions.
- [Elections](../mechanic/elections.md) (Deepens): Simulated electorates could be built from survey-grounded agents that reproduce subgroup opinion distributions, so vote shares respond to issues the way measured populations do.
- [Interest groups](../mechanic/interest-groups.md) (Deepens): A group's preferences over policies could be derived from simulated members (silicon samples) rather than a single authored ideology vector.
- [Personality traits](../mechanic/personality-traits.md) (Deepens): A character's disposition can be a rich text profile whose predicted Big Five scores and economic-game behavior match a real respondent, rather than a few discrete trait tags.
- [Dilemma cards](../mechanic/dilemma-cards.md) (Tunes / balances): Before ship, designers could estimate option pick rates for each card by querying a choice model on the card text; untested on game content.
- [Negotiation](../mechanic/negotiation.md) (Deepens): Counterparties whose acceptance follows models of human bargaining (fairness, anchoring) rather than a single reservation price.
- [Advertising and awareness](../mechanic/advertising-awareness.md) (Deepens): Segment-level response to advertising predicted from models of human choice instead of a flat awareness multiplier.
- [Travel mode choice](../mechanic/travel-mode-choice.md) (Tunes / balances): Mode-choice weights for time, cost, and comfort can be fitted to predicted human choices instead of hand-set.

**builds on**

- [Generative agents (memory stream, reflection, planning)](../technique/generative-agents.md)

## Backlinks (computed)

**applied in:** [AI liquidity in player markets](../opportunity/ai-liquidity-in-player-markets.md), [Human-calibrated customers](../opportunity/human-calibrated-customers.md), [Participatory planning sandboxes](../opportunity/participatory-planning-sandboxes.md)

## Claims

- Agents built from two-hour interviews with 1,052 U.S. adults replicated General Social Survey answers 85% as accurately as participants replicated their own answers two weeks later, and performed comparably on Big Five traits, five economic games, and five experiments, with smaller accuracy gaps across racial and ideological groups than demographics-only agents. *(confidence: high)* [[185](../source/src-stanford-hai-2025-simulating-human-behavior.md), [186](../source/src-park-2024-1000-people.md)]
- The later arXiv version reports normalized GSS accuracy of 83% for interview-only, 82% survey-only, 86% combined, and 74% demographics-only agents. *(confidence: medium)* [[186](../source/src-park-2024-1000-people.md)]
- Centaur predicted held-out participants better than 14 cognitive and statistical models and generalized to new cover stories, structural task changes, and new domains; the authors propose it for in silico prototyping of experiments. *(confidence: high)* [[187](../source/src-binz-2025-centaur.md)]
- With task instructions removed or replaced by misleading ones, Centaur still generally beat domain-specific cognitive models, which its critics read as reliance on statistical cues rather than understanding the task. *(confidence: medium)* [[188](../source/src-liu-2025-centaur-instruction-understanding.md), [189](../source/src-orr-2025-not-even-wrong.md)]
- Earlier work showed GPT-3 conditioned on survey backstories reproduces subgroup response distributions (algorithmic fidelity), while GPT-4-era models replicated classic experiments but showed a hyper-accuracy distortion on wisdom-of-crowds questions. *(confidence: high)* [[190](../source/src-argyle-2023-out-of-one-many.md), [191](../source/src-aher-2022-turing-experiments.md)]

## Sources

- [Generative Agent Simulations of 1,000 People](../source/src-park-2024-1000-people.md)
- [Simulating Human Behavior with AI Agents](../source/src-stanford-hai-2025-simulating-human-behavior.md)
- [A foundation model to predict and capture human cognition](../source/src-binz-2025-centaur.md)
- [Can Centaur truly simulate human cognition? The fundamental limitation of instruction understanding](../source/src-liu-2025-centaur-instruction-understanding.md)
- [Not Even Wrong: On the Limits of Prediction as Explanation in Cognitive Science](../source/src-orr-2025-not-even-wrong.md)
- [Out of One, Many: Using Language Models to Simulate Human Samples](../source/src-argyle-2023-out-of-one-many.md)
- [Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies](../source/src-aher-2022-turing-experiments.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`; reviewed in `2026-10-24-technique-links`.
