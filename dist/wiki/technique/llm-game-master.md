# LLM game master and narrative director

*Technique* · `llm-game-master` · status: **sourced**

A language model that adjudicates player and NPC intentions, decides outcomes, generates events and quests, and narrates them, either free-form or checked against a typed world state and canon.

| field | value |
|---|---|
| aliases | AI game master, AI Dungeon, Concordia Game Master, story engine, AI narrator |
| category | LLM narrative & dialogue |
| year | 2019 |
| maturity | Shipped (niche) |
| trl | 8 |
| runtime | Server real-time |
| determinism impact | Breaks |
| horizon | Now |
| risks | Determinism, Consistency / hallucination, Content safety, Controllability, Compute cost, Evaluation difficulty |
| builds on |  |
| deployed in | [AI Dungeon](../game/ai-dungeon.md) |
| affects count *(computed)* | 6 |

## Summary

A language model that adjudicates player and NPC intentions, decides outcomes, generates events and quests, and narrates them, either free-form or checked against a typed world state and canon.

## Mechanism

The player types an intent; the system assembles a prompt from recent story, pinned memories, and setting notes and asks the model to continue the story, as AI Dungeon has since 2019. Grounded variants split the job: actors state intended actions in language, a Game Master component checks plausibility against rules and state, decides what happens, writes state changes, and only then narrates (Concordia). Hidden Door runs intent through plan, canon check, and world-state update steps over a typed, auditable world model, using many small tuned models for about 100 narrative tasks; its example blocks Dracula from entering a house uninvited. Research systems generate setting, items, and NPCs from designer criteria and use the model to validate free-text input against the story (PANGeA), or assist a human Dungeon Master (CALYPSO).

## Limitations

- Long-session consistency: models forget or contradict earlier facts unless state is externalized into memory or a typed world model.
- Accommodation bias: models rarely say no, which removes challenge and lets players talk past any obstacle.
- Content moderation is hard: AI Dungeon's filter both missed and over-blocked, and Steam requires guardrail disclosure for live-generated content.
- Latency of several to 15 seconds per turn frustrated players in a GPT-4 study; multi-step grounded pipelines add calls per turn.
- Every turn is an inference cost for the life of the service, which pushes products to subscriptions or small tuned models.

## Sources

- src-wikipedia-ai-dungeon
- src-vezhnevets-2023-concordia
- src-vezhnevets-2025-multi-actor-game-engine
- src-deepmind-2026-concordia-repo
- src-hiddendoor-2026-homepage
- src-hiddendoor-2026-blog-index
- src-peng-2024-player-driven-emergence
- src-buongiorno-2024-pangea
- src-zhu-2023-calypso
- src-gallotta-2024-llms-games-survey
- src-valve-2026-steamworks-content-survey
- src-valve-2024-ai-content-on-steam
- src-totallyhuman-2024-steam-genai-count
- src-totallyhuman-2025-steam-genai-count
- src-totallyhuman-2025-steam-ai-revenue

## Relations

**affects**

- [Storyteller director](../mechanic/storyteller-director.md) (Enables new form): The director can author an event in language for the exact current state, check it against canon and rules, and narrate it, instead of choosing among a finite catalog of pre-written incidents by a pacing budget.
- [Triggered event chains](../mechanic/triggered-event-chains.md) (Replaces substrate): Follow-up beats are generated from story state and player intent rather than scheduled by authored templates with trigger predicates, while the player still experiences multi-step chains.
- [Villager requests](../mechanic/villager-requests.md) (Deepens): Characters can ask for things tied to the specific story so far, not only fetch templates with filled slots; ungrounded models invent quests that do not exist, so requests must be checked against state.
- [Generative content on demand](../mechanic/generative-content.md) (Deepens): Story continuation from Do, Say, Story, and See inputs makes the whole narrative generated content; grounded engines turn it into typed state changes.
- [Natural-language interaction](../mechanic/natural-language-interaction.md) (Deepens): Any typed action is adjudicated for plausibility and consequence rather than matched against a parser's verb list, so unanticipated approaches produce new narrative paths (53 emergent nodes in one 28-player study).
- [Procedural characters](../mechanic/procedural-characters.md) (Cuts authoring cost): NPCs with backstories, goals, and personality are generated from designer criteria and voiced in dialogue, removing per-character writing.

**deployed in**

- [AI Dungeon](../game/ai-dungeon.md)

## Backlinks (computed)

**applied in:** [Content-elastic event systems](../opportunity/content-elastic-events.md), [Drama-aware storyteller](../opportunity/drama-aware-storyteller.md), [Generated inspection shifts](../opportunity/generated-inspection-shifts.md), [Illustrated chronicles](../opportunity/illustrated-chronicles.md), [Placement that tells stories](../opportunity/placement-that-tells-stories.md)

## Claims

- AI Dungeon 2 (December 2019) ran the full 1.5B-parameter GPT-2 and moved to GPT-3 in mid-2020, reaching over 100,000 players in its first week and 1.5 million by June 2020. *(confidence: high)* [[173](../source/src-wikipedia-ai-dungeon.md)]
- AI Dungeon's 2021 content filter, added to block sexual content involving minors, produced false positives on innocuous text and led human moderators to read flagged private stories, prompting review bombing. *(confidence: high)* [[173](../source/src-wikipedia-ai-dungeon.md)]
- In a 28-player study with five GPT-4 NPCs holding backstories, clues, and ordered goals, play produced 53 narrative nodes absent from the designers' graph; about 15 seconds of lag frustrated 40% of players and NPCs forgot earlier statements in 10% of reports. *(confidence: high)* [[171](../source/src-peng-2024-player-driven-emergence.md)]
- Hidden Door announced early access in August 2025 and offers licensed worlds such as Dracula; its engine checks every story turn against canon and rules before display and reports a tuned 1.7B model beating a 120B general model on one core task. *(confidence: medium)* [[174](../source/src-hiddendoor-2026-blog-index.md), [175](../source/src-hiddendoor-2026-homepage.md)]
- Concordia's Game Master converts agents' natural-language actions into outcomes and checks physical plausibility, and its 2025 design pattern classifies uses as Simulationist, Dramatist, or Evaluationist. *(confidence: high)* [[176](../source/src-vezhnevets-2023-concordia.md), [177](../source/src-vezhnevets-2025-multi-actor-game-engine.md), [149](../source/src-deepmind-2026-concordia-repo.md)]
- Surveyed LLM game masters tend to accommodate even bizarre player requests that human GMs would curb, and LLM NPCs can invent quests that do not exist in the game. *(confidence: medium)* [[135](../source/src-gallotta-2024-llms-games-survey.md)]
- Steam requires games with live-generated AI content to disclose it and describe guardrails against illegal output, and does not permit live-generated adult sexual content. *(confidence: high)* [[178](../source/src-valve-2026-steamworks-content-survey.md), [179](../source/src-valve-2024-ai-content-on-steam.md)]
- Dungeon Masters using CALYPSO presented some generated text almost directly and treated rougher output as ideas while keeping creative control. *(confidence: medium)* [[180](../source/src-zhu-2023-calypso.md)]
- PANGeA generated settings, key items, and Big Five personality-biased NPCs from designer criteria and used the model to keep free-text player input within the narrative, tested in a browser demo and a Unity game. *(confidence: medium)* [[181](../source/src-buongiorno-2024-pangea.md)]
- Steam generative AI disclosures rose from about 1,000 games in April 2024 to 7,818 (about 7% of the catalog, a little under 20% of 2025 releases) in July 2025 and 10,258 (about 8%) in November 2025; about 60% of disclosures concern visual assets, so live-generated runtime systems such as LLM narration are a small share. *(confidence: medium)* [[182](../source/src-totallyhuman-2024-steam-genai-count.md), [183](../source/src-totallyhuman-2025-steam-genai-count.md), [184](../source/src-totallyhuman-2025-steam-ai-revenue.md)]

## Sources

- [AI Dungeon](../source/src-wikipedia-ai-dungeon.md)
- [Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia](../source/src-vezhnevets-2023-concordia.md)
- [Multi-Actor Generative Artificial Intelligence as a Game Engine](../source/src-vezhnevets-2025-multi-actor-game-engine.md)
- [Concordia: a library for generative social simulation](../source/src-deepmind-2026-concordia-repo.md)
- [Hidden Door](../source/src-hiddendoor-2026-homepage.md)
- [Hidden Door blog](../source/src-hiddendoor-2026-blog-index.md)
- [Player-Driven Emergence in LLM-Driven Game Narrative](../source/src-peng-2024-player-driven-emergence.md)
- [PANGeA: Procedural Artificial Narrative using Generative AI for Turn-Based Video Games](../source/src-buongiorno-2024-pangea.md)
- [CALYPSO: LLMs as Dungeon Masters' Assistants](../source/src-zhu-2023-calypso.md)
- [Large Language Models and Games: A Survey and Roadmap](../source/src-gallotta-2024-llms-games-survey.md)
- [Steamworks Documentation: Content Survey (generative AI disclosure)](../source/src-valve-2026-steamworks-content-survey.md)
- [AI Content on Steam](../source/src-valve-2024-ai-content-on-steam.md)
- [The Surprising Number of Steam Games that Use GenAI](../source/src-totallyhuman-2024-steam-genai-count.md)
- [The NEW Surprising Number of Steam Games that Use GenAI](../source/src-totallyhuman-2025-steam-genai-count.md)
- [Games With AI Disclosures Have Grossed an Estimated $660M on Steam](../source/src-totallyhuman-2025-steam-ai-revenue.md)

---
Provenance: created in run `2026-10-24-techniques-llm-agents`; reviewed in `2026-10-24-review-fixes`.
