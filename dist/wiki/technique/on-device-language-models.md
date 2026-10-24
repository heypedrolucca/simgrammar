# On-device small language models for characters

*Technique* · `on-device-language-models` · status: **sourced**

Pruned, distilled, and 4-bit quantized language, speech, and embedding models that run on the player's GPU beside rendering to drive character decisions, dialogue, and voice without per-token server cost.

| field | value |
|---|---|
| aliases | NVIDIA ACE, Smart Zoi, PUBG Ally, co-playable characters, SLM NPCs, quantized local LLMs |
| category | Inference efficiency |
| year | 2025 |
| maturity | Shipped (niche) |
| trl | 7 |
| runtime | Client real-time |
| determinism impact | Mitigable |
| horizon | Now |
| risks | Consistency / hallucination, Latency, Controllability, Content safety, Player trust / reception |
| builds on |  |
| deployed in | [inZOI](../game/inzoi.md) |
| affects count *(computed)* | 5 |

## Summary

Pruned, distilled, and 4-bit quantized language, speech, and embedding models that run on the player's GPU beside rendering to drive character decisions, dialogue, and voice without per-token server cost.

## Mechanism

A 12B or 8B model is pruned in depth and width and distilled into an 8B, 4B, or 2B student (Minitron), then weights are quantized to 3-4 bits with second-order (GPTQ) or activation-aware (AWQ) methods, shrinking memory so a 2B model fits in about 1.5 GB of VRAM. An in-game inference SDK runs the models in-process and schedules them alongside graphics on the same GPU. A character loop chains on-device speech recognition, the small model (perceive, decide, act, reflect), text-to-speech, and facial animation, with an in-process embedding model for memory retrieval; slow strategic planning can be offloaded to a larger cloud model while fast decisions stay local. Fine-tuning a small model on a narrow game task can beat much larger general models on that task.

## Limitations

- Hardware floor: the inference SDK needs an RTX 30-series class GPU with 8 GB of VRAM minimum, which excludes many players and consoles, and the model competes with rendering for VRAM and GPU time.
- Small models are less capable at multi-step reasoning, so vendors offload strategic planning to cloud models, reintroducing cost and latency.
- Quality and safety filters must also run locally; local weights can be extracted or modified by players.
- Player reception risk: inZOI drew negative user reviews in May 2025 after Krafton announced its generative AI use.
- Exact model sizes and latency in shipped titles are mostly undisclosed.

## Sources

- src-sreenivas-2024-minitron
- src-frantar-2022-gptq
- src-lin-2023-awq
- src-nvidia-2025-ace-companions
- src-nvidia-2025-gamescom-ace
- src-nvidia-2026-ace-developer-page
- src-nvidia-2026-nvigi-core
- src-steam-2025-inzoi
- src-wikipedia-inzoi
- src-krafton-2026-pubg-ally-beta
- src-hiddendoor-2026-homepage

## Relations

**affects**

- [Natural-language interaction](../mechanic/natural-language-interaction.md) (Accelerates): Free-text and voice input to characters runs on the player's GPU, removing per-token server cost and network round trips, so open conversation can be offered to every player of a premium game.
- [Utility action selection](../mechanic/utility-action-selection.md) (Replaces substrate): Smart Zois pick actions with a small model that reads needs, surroundings, and inner thoughts rather than only scored need curves, while the game's action set stays the same.
- [Memories and thoughts](../mechanic/memories-thoughts.md) (Deepens): Characters generate text thoughts about events and reflect on past decisions, giving each agent a running inner monologue rather than a list of authored mood modifiers.
- [Advisors](../mechanic/advisors.md) (Replaces substrate): Total War: PHARAOH's ACE advisor answers questions about the game's systems from a small on-device model connected to game data, instead of firing authored lines when indicators cross thresholds.
- [Unit commands](../mechanic/unit-commands.md) (Enables new form): A co-playable teammate such as PUBG Ally takes spoken orders about movement, looting, and strategy mid-match and acts on them, a command channel that needs no menus or ping wheel.

**deployed in**

- [inZOI](../game/inzoi.md)

## Backlinks (computed)

**applied in:** [Intent-level orders](../opportunity/intent-level-orders.md), [Factories with a living workforce](../opportunity/living-workforce-factories.md), [Language-agent society terrarium](../opportunity/llm-society-terrarium.md), [Local-first AI simulation games](../opportunity/local-first-ai-sims.md), [Salience-gated language agents](../opportunity/salience-gated-llm-agents.md), [Research by named scientists](../opportunity/scientists-not-tech-trees.md), [Simulator instructor coaching](../opportunity/sim-instructor-coach.md), [Teachable sim companion](../opportunity/teachable-sim-companion.md), [Trainable creatures revival](../opportunity/trainable-creatures-revival.md)

## Claims

- Minitron pruning and distillation compressed Mistral NeMo 12B to an 8B model and Llama 3.1 8B to 4B, and NVIDIA's ACE character stack lists Minitron 8B, 4B, and 2B instruct models, the 2B fitting in about 1.5 GB of VRAM. *(confidence: high)* [[243](../source/src-sreenivas-2024-minitron.md), [244](../source/src-nvidia-2025-ace-companions.md)]
- GPTQ quantizes weights to 3-4 bits with minimal accuracy loss and generates 3.25-4.5x faster than FP16; AWQ's 4-bit runtime is over 3x faster than FP16 on desktop and mobile GPUs. *(confidence: high)* [[245](../source/src-frantar-2022-gptq.md), [246](../source/src-lin-2023-awq.md)]
- inZOI (early access March 2025) ships an on-device SLM through which typed prompts influence Zois' actions and thoughts; an August 2025 update made Smart Zois observe surroundings and react to events better and align actions with inner thoughts. *(confidence: high)* [[138](../source/src-steam-2025-inzoi.md), [247](../source/src-nvidia-2025-gamescom-ace.md)]
- KRAFTON ran a public PUBG Ally beta (Ally Duo, 17 June to 1 July 2026) in which an AI teammate takes voice instructions via an on-device small language model built on NVIDIA ACE with speech-to-text and text-to-speech. *(confidence: high)* [[248](../source/src-krafton-2026-pubg-ally-beta.md)]
- NVIDIA's in-game inference SDK requires an RTX 30-series class GPU or newer with at least 8 GB of VRAM (12 GB recommended), and some plugins need RTX 40-series. *(confidence: high)* [[249](../source/src-nvidia-2026-nvigi-core.md)]
- Hidden Door reports that a 1.7B model tuned on real play beat a 120B general model on one of its core narrative tasks. *(confidence: low)* [[175](../source/src-hiddendoor-2026-homepage.md)]

## Sources

- [LLM Pruning and Distillation in Practice: The Minitron Approach](../source/src-sreenivas-2024-minitron.md)
- [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](../source/src-frantar-2022-gptq.md)
- [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration](../source/src-lin-2023-awq.md)
- [NVIDIA ACE autonomous game characters: PUBG Ally, inZOI Smart Zoi, NARAKA AI teammate](../source/src-nvidia-2025-ace-companions.md)
- [Gamescom 2025: DLSS 4 and RTX game announcements](../source/src-nvidia-2025-gamescom-ace.md)
- [NVIDIA ACE for Games](../source/src-nvidia-2026-ace-developer-page.md)
- [NVIGI-Core: NVIDIA In-Game Inferencing SDK core](../source/src-nvidia-2026-nvigi-core.md)
- [inZOI on Steam](../source/src-steam-2025-inzoi.md)
- [inZOI](../source/src-wikipedia-inzoi.md)
- [KRAFTON Introduces PUBG Ally Beta Test](../source/src-krafton-2026-pubg-ally-beta.md)
- [Hidden Door](../source/src-hiddendoor-2026-homepage.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`.
