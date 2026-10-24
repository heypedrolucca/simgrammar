## 7. The technique landscape, 2019 to 2026

### 7.1 What is in the set

{{table:techniques-by-category}}

A technique enters the dataset only as a dated, citable result that changes at least one mechanic (CONTRACT.md, I12). Maturity and technology readiness are judged for deployment *in games*, not for AI in general: [[constrained-decoding]] is routine in software engineering but rare in shipped game runtimes, so it is scored as research for this purpose.

{{table:techniques-by-maturity}}

Of {{count:technique}} techniques, {{stat:n_technique_shipped_mainstream}} is shipped as a genre norm{{assert:n_technique_shipped_mainstream == 1}}, {{stat:n_technique_shipped_niche}} are shipped in at least one commercial game, {{stat:n_technique_prototype}} exist as public prototypes, and {{stat:n_technique_research}} are research only. The shipped ones cluster in three places: rendering and assets ([[neural-rendering-shaders]], [[satellite-world-reconstruction]], [[text-to-3d-assets]], [[learned-motion-synthesis]]), language characters ([[generative-agents]], [[on-device-language-models]], [[realtime-voice-models]], [[llm-game-master]], [[llm-rule-adjudication]]), and older search and learning methods ([[monte-carlo-tree-search]], [[wave-function-collapse]], [[deep-rl-npc-policies]], [[automated-playtesting]]). Almost nothing that touches the authoritative simulation state of a simulation game has shipped.

### 7.2 Adoption and reception

Generative AI has moved from novelty to a measurable share of releases. Disclosures on Steam rose from about a thousand games in April 2024 [@src-totallyhuman-2024-steam-genai-count] to 7,818 Steam titles, a little under a fifth of 2025 releases, by July 2025 [@src-totallyhuman-2025-steam-genai-count], and an estimate in November 2025 put games with disclosures at roughly 8 percent of the store with about 660 million dollars in combined gross [@src-totallyhuman-2025-steam-ai-revenue]. Most disclosures concern pre-generated visual assets rather than runtime systems. Valve's survey distinguishes pre-generated from live-generated content and requires the latter to describe its guardrails [@src-valve-2026-steamworks-content-survey].

Developer sentiment moved the other way. In GDC's 2026 survey, 36 percent of respondents used generative AI at work, while the share who believe it harms the industry rose to 52 percent from 30 percent a year earlier [@src-gdc-2025-state-of-industry; @src-gdc-2026-state-of-industry]. Player reception has been mixed in visible cases: [[inzoi]] sold strongly at launch and drew negative reviews after announcing generative features [@src-wikipedia-inzoi]; ARC Raiders was criticized for synthetic voice lines, some of which were later re-recorded by actors [@src-wikipedia-arc-raiders].

Runtime language characters did ship. On-device small language models power companions and simulated people in PUBG Ally, inZOI's Smart Zoi, and NARAKA's teammate [@src-nvidia-2025-ace-companions; @src-krafton-2026-pubg-ally-beta]; [[where-winds-meet]] discloses live NPC text and voice chat [@src-steam-2025-where-winds-meet]. The cost of realtime speech fell by about a fifth between the 2024 and 2025 versions of one leading API [@src-openai-2024-realtime-api; @src-openai-2025-gpt-realtime], and specialized text-to-speech vendors price in cents per minute [@src-inworld-2026-tts-1-5]. Cost remains the stated wall for frame-generating world models: the consumer Genie product caps each world at sixty seconds of play [@src-techcrunch-2026-project-genie].

Among rendering techniques, neural upscaling and frame generation are the one area where learned models are a norm, with hundreds of supported titles [@src-nvidia-2026-dlss-4-5]. They never touch simulation state, which is why they could spread.

### 7.3 Seven clusters

**Frame-generating world models.** [[diffusion-game-engines]], [[genie-world-models]], [[muse-wham]], and [[open-interactive-video-models]] learn to predict the next frame from recent frames and player input, so the model is the engine. They produce convincing short interactions and fail at what simulation games need most: exact persistent state, long memory, and inspectable causes. Their realistic near-term role is ideation, previsualization, and non-authoritative views (§9).

**3D, rendering, and assets.** [[gaussian-splatting]], [[generated-3d-worlds]], [[text-to-3d-assets]], [[neural-rendering-shaders]], [[real-time-video-restyling]], and [[satellite-world-reconstruction]] cut the authoring cost of what the simulation is drawn with, leaving rules untouched. They are the most mature and the least controversial technically; their risks are provenance and reception.

**Motion.** [[learned-motion-synthesis]] has shipped in sports and life games; [[physics-based-character-control]] remains research. Both matter to simulation games because canned animation is how most agents' internal states are (poorly) displayed.

**Language agents and dialogue.** [[generative-agents]], [[llm-agent-societies]], [[human-behavior-simulation-models]], [[on-device-language-models]], [[constrained-decoding]], [[realtime-voice-models]], [[llm-game-master]], [[llm-explanation-of-state]], and [[llm-rule-adjudication]] change who decides what agents do and say, who narrates, and who explains. They relax the authoring and believability ceilings at a cost in determinism and consistency.

**Planning and game theory.** [[monte-carlo-tree-search]], [[model-based-planning-muzero]], [[imperfect-information-solvers]], [[cicero-strategic-dialogue]], [[deep-rl-npc-policies]], and [[mean-field-games]] produce strong opponents and equilibrium-consistent populations. Their game deployments are few because strength is rarely the design goal; believable and tunable opponents are.

**Design automation.** [[wave-function-collapse]], [[quality-diversity-search]], [[learned-level-generation]], [[automated-rule-generation]], [[automated-playtesting]], [[open-ended-environment-generation]], [[voyager-skill-libraries]], [[generalist-game-agents]], and [[alphaevolve-algorithm-discovery]] work on the developer's side: generating content and rules, finding exploits, and estimating difficulty. They preserve determinism because they run offline.

**Simulation science.** [[massively-parallel-simulation]], [[differentiable-simulation]], [[graph-network-simulators]], [[subspace-neural-physics]], [[ml-weather-models]], [[neural-cellular-automata]], [[continuous-alife-and-asal]], and [[simulation-based-inference]] come from robotics, physics, climate, and artificial life. They relax the compute ceiling and make calibration possible, and they are the least connected to game development today: an operational ML weather model runs at about a thousandth of the energy of the physics model it complements [@src-ecmwf-2025-aifs-operational], yet none of these techniques is confirmed at runtime in a catalog game.


### 7.4 Landscape

{{table:technique-landscape}}
