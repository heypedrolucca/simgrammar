# Episode 6. What AI shipped

Target runtime about 13 minutes: about 1,390 words of narration at 135 words a minute, plus a beat of picture-only footage per scene. Covers book chapter 7. Footage: Suck Up!, AI Dungeon, Microsoft Flight Simulator (2020), inZOI, Where Winds Meet, Whispers from the Star, Gran Turismo 7, Townscaper, Infinite Craft, all captured by us; stills and published clips from the GameNGen, Genie 3, and WHAMM announcements, used as short quotations with credit. Publisher video policies are tracked in `media/rights.yaml` and must be checked before release. Every number below is filled in from the dataset when the script is built, and the sentences that interpret numbers carry the same checks as the book.

## 1. Cold open (0:00 to 0:36)

**Picture.** Suck Up! A cartoon street at night. The player, a vampire in a delivery-driver disguise, knocks. A resident opens the door a crack. Subtitles show the player's spoken pitch and the resident's spoken reply: she isn't expecting a parcel. The door shuts. Cut to the same door, a new disguise. This time she steps aside.

**Voice.** You're a vampire, and you can't go in until someone invites you. So you knock, and you talk, out loud, into a real microphone. Nobody wrote the resident's answer. A language model wrote it, from a personality the developers gave her and the words you just said [@src-steam-2026-suck-up].

## 2. Title (0:36 to 0:46)

**Picture.** Title card over the closed door.

**On screen.** What AI shipped. Episode 6.

## 3. When the model is the game (0:46 to 2:04)

**Picture.** AI Dungeon, a text screen. The player types an action; a paragraph appears. Several turns later the player mentions a silver key. The story ignores it. The player opens the memory box and types the key in.

**Voice.** Suck Up! goes back to AI Dungeon, from 2019. You type what you do, and a language model writes what happens next: GPT-2 at launch, GPT-3 for the premium model a year later [@src-wikipedia-ai-dungeon]. There's no inventory behind the text, and no world state at all. A fact lasts as long as it stays in the model's context window. Pick up a key, play for an hour, and the story forgets you have it. The fix the game gives you is a memory box where you write the key down yourself.

**Voice.** The dataset counts both games as boundary cases. Nothing in either is simulated outside the model's text. They show what a game looks like when the model is the whole game. Most games have a simulation to protect, and AI has been allowed into them in a few specific places.

## 4. How shipped is shipped (2:04 to 3:02)

**Picture.** A four-step ladder: research, prototype, shipped in one game, shipped as a norm. Technique names drop onto the rungs, most of them landing on the bottom two.

**On screen.** {{stat:n_technique_shipped_mainstream}} norm. {{stat:n_technique_shipped_niche}} in at least one game. {{stat:n_technique_prototype}} prototypes. {{stat:n_technique_research}} research.

**Voice.** The dataset holds {{count:technique}} AI and math techniques, each a dated result that changes at least one game mechanic, and it judges each one by how far it has got in games, which is a harder test than how far it has got in AI. Constrained decoding, which forces a model's answer into a fixed format, is everywhere in software. In shipped game code it's rare, so here it counts as research.{{assert:field.constrained-decoding.maturity == research}} By that test, {{stat:n_technique_shipped_mainstream}} technique has become normal in games, {{stat:n_technique_shipped_niche}} have shipped in at least one game, and the rest are prototypes and papers.{{assert:n_technique_shipped_mainstream == 1}}{{assert:n_technique_shipped < n_technique_research}}

## 5. The one that's normal (3:02 to 4:06)

**Picture.** Microsoft Flight Simulator, a low pass over a city. A split screen: rendered frames on the left, generated frames marked in between on the right.

**Voice.** The one that's normal is neural rendering. Upscaling rebuilds a sharp image from a smaller one, and frame generation predicts whole frames between the ones the game actually drew. By January 2026, more than 250 titles supported multi-frame generation [@src-nvidia-2026-dlss-4-5], including Microsoft Flight Simulator [@src-pcgamingwiki-2026-msfs-2020].{{assert:field.neural-rendering-shaders.maturity == shipped-mainstream}}

**Voice.** A generated frame sits between two frames the game computed, and the simulation never learns it exists. The rules, the saves, and the multiplayer code don't change, which is why a studio can add it late, and why the dataset records it as keeping the game reproducible.{{assert:field.neural-rendering-shaders.determinism_impact == preserves}} When it went wrong, with DLSS 5 in September 2026, the complaints were about faces and art direction [@src-wikipedia-deep-learning-super-sampling]. 

## 6. Places, objects, and motion (4:06 to 5:15)

**Picture.** Flight Simulator's camera pulls up from a street to a whole region, every roof and tree in place. Then inZOI: a photo dragged into a menu becomes a 3D lamp in a living room.

**Voice.** Other techniques change what a simulation is drawn with, mostly before you press play. Microsoft Flight Simulator rebuilt the planet from map imagery: machine learning picked out buildings, trees, and terrain, and procedural rules turned them into about one and a half billion buildings [@src-wikipedia-microsoft-flight-simulator-2020]. That happened once, offline, so every player sees the same town.{{assert:field.satellite-world-reconstruction.determinism_impact == preserves}} In inZOI, players turn a photo into a 3D object [@src-steam-2025-inzoi]. A generated object has to be saved to be seen again, because asking twice gives you a different chair.{{assert:field.text-to-3d-assets.determinism_impact == mitigable}}

**Voice.** This is also where most of the store's AI sits. By July 2025, about 7 percent of Steam's titles disclosed generative AI, and visual assets came up in about 60 percent of those disclosures [@src-totallyhuman-2025-steam-genai-count].

## 7. Characters that talk (5:15 to 7:15)

**Picture.** inZOI: the player types a thought into a prompt box, and a Zoi changes course across the room. Where Winds Meet: a player speaks to a market trader, who answers. Whispers from the Star: Stella on a video call, waiting for an answer.

**Voice.** Characters that talk did ship, in a handful of games. In inZOI, a small language model running on your own graphics card lets typed prompts steer what a Zoi thinks and does [@src-steam-2025-inzoi]. It picks from inZOI's own actions, with the game's animations and rules, and replaces the formula that used to choose the next one.{{assert:field.on-device-language-models.maturity == shipped-niche}} Where Winds Meet answers free-text and voice chat with a live model [@src-steam-2025-where-winds-meet], while its quests and combat stay written by hand. Whispers from the Star is one stranded astronaut, voiced live, whose survival depends on what you tell her [@src-steam-2026-whispers-from-the-star]. And in June 2026, KRAFTON ran a two-week beta of PUBG Ally, a teammate that takes spoken orders through a model on your own machine [@src-krafton-2026-pubg-ally-beta].

**Voice.** Voice got cheaper and the models got smaller. Small models got small enough that a two-billion-parameter one fits in about one and a half gigabytes of video memory, beside the game's own graphics [@src-sreenivas-2024-minitron; @src-nvidia-2025-ace-companions]. And voice got cheaper fast. One leading realtime speech service cut its audio prices from 100 and 200 dollars per million tokens in October 2024 to 32 and 64 dollars ten months later [@src-openai-2024-realtime-api; @src-openai-2025-gpt-realtime]. The cost shows up elsewhere. A local model can be seeded and run the same way twice. A voice model or a full language-model character can't: the same words can get a different answer, and a replay has to store what was said.{{assert:field.on-device-language-models.determinism_impact == mitigable}}{{assert:field.realtime-voice-models.determinism_impact == breaks}}{{assert:field.generative-agents.determinism_impact == breaks}}

## 8. Opponents (7:15 to 8:30)

**Picture.** Gran Turismo 7. A GT Sophy car takes the inside line into a hairpin and holds it. Menu shots: Race Together, then Quick Race with Sophy as a permanent rival.

**Voice.** The oldest shipped techniques in the set are aimed at opponents. Monte Carlo tree search, from 2006, plans by playing many quick games forward from the current position; Total War: Rome II used it for campaign decisions [@src-kocsis-2006-uct; @src-wikipedia-monte-carlo-tree-search]. Gran Turismo Sophy learned to drive with deep reinforcement learning on many copies of the Gran Turismo simulator, with a reward that encodes racing's sportsmanship rules, and in 2022 it beat four of the world's best Gran Turismo drivers head to head [@src-wurman-2022-gt-sophy]. It reached players as a limited event in February 2023 [@src-polyphony-2023-gt-sophy-race-together] and became a permanent rival that November [@src-polyphony-2023-gt-sophy-2].{{assert:field.deep-rl-npc-policies.maturity == shipped-niche}} It drives the same tire and suspension model you do. What took the time was making a strong driver fair, tunable to your level, and small enough to ship one update at a time.

## 9. Tools that never reach you (8:30 to 9:27)

**Picture.** Townscaper: a click on the water adds a block, and arches, stairs, and roofs rearrange around it. Then a spreadsheet of level difficulty estimates with a column of agent pass rates.

**Voice.** Two more techniques shipped where players mostly can't see them. Agent playtesting runs a build with trained bots before release: a network that learned from logged Candy Crush moves predicted how hard new levels would be for people [@src-gudmundsson-2018-human-like-playtesting], and EA used search agents to balance careers in The Sims Mobile [@src-zhao-2019-winning-isnt-everything]. Wave-function collapse, a constraint solver that fills a grid tile by tile, builds levels in Bad North and Caves of Qud, and in Townscaper it reruns every time you click [@src-gumin-2016-wavefunctioncollapse]. Both give the same answer every time from the same seed.{{assert:field.automated-playtesting.determinism_impact == preserves}}{{assert:field.wave-function-collapse.determinism_impact == preserves}}

## 10. What writes into the simulation (9:27 to 11:20)

**Picture.** The shipped techniques as cards, sorted into two piles: "changes what you see and hear" and "changes the game's state." The second pile has three cards: cached rules, characters that act, opponents. Then clips from world-model demos: a DOOM corridor generated frame by frame; a Genie 3 world where a character walks through a wall.

**Voice.** Only a few shipped techniques change the game's state, the part your save file and a replay depend on. A model's answer can be cached as a rule, which Infinite Craft does, and the next episode starts there.{{assert:field.llm-rule-adjudication.maturity == shipped-niche}} Language-model characters choose actions in inZOI and a few AI-native games. And trained or search-based opponents drive cars and armies. The {{stat:n_technique_shipped}} shipped techniques reach mechanics that make up {{stat:pct_uses_touched_by_shipped}} percent of what catalog games use.{{assert:pct_uses_touched_by_shipped < 50}}

**Voice.** Nothing learned has replaced a game's physics or its world in a catalog game. The models that would replace the engine itself are prototypes. GameNGen ran DOOM at 20 frames a second on one TPU, and its authors say it can't make new games [@src-valevski-2024-gamengen]. When Google opened Genie 3 to subscribers, each world allowed sixty seconds of play, a limit DeepMind put down to compute, and a reviewer watched characters walk through walls [@src-techcrunch-2026-project-genie]. Microsoft's Quake II demo ran at about ten frames a second, with health counters that couldn't be trusted [@src-microsoft-2025-whamm].{{assert:field.genie-world-models.maturity == prototype}}{{assert:field.diffusion-game-engines.maturity == prototype}}

**Voice.** These models keep the game's state as pixels. Health, position, the layout of the map exist only in the frames they remember, so whatever scrolls out of memory can come back different. A simulation game needs the cow in the field on day one to be the same cow on day three hundred.

## 11. Replays (11:20 to 12:00)

**Picture.** A replay timeline scrubbing back and forth. Model calls appear on it as small flags, each flag holding a stored answer.

**On screen.** Can run during play: {{stat:n_technique_runtime}}. Break replays: {{stat:n_technique_runtime_breaks}}. Fixable by logging or seeding: {{stat:n_technique_runtime_mitigable}}. Safe: {{stat:n_technique_runtime_preserves}}.

**Voice.** Of the {{stat:n_technique_runtime}} techniques that can run while you play, {{stat:n_technique_runtime_breaks}} make a game impossible to replay exactly, and {{stat:n_technique_runtime_mitigable}} can be made reproducible.{{assert:n_technique_runtime_breaks < n_technique_runtime_mitigable}} The fix is the one Infinite Craft uses: ask the model once, store the answer, and treat the stored answer as the rule. A replay reads the record and never asks again.

## 12. How it was received (12:00 to 12:58)

**Picture.** Survey charts from GDC 2025 and 2026, two bars side by side. inZOI's Steam review graph dipping in May 2025.

**Voice.** Developers' use of generative AI held steady while their opinion of it fell. In GDC's surveys, 36 percent reported using it in both 2025 and 2026, and the share who think it harms the industry went from 30 to 52 percent [@src-gdc-2025-state-of-industry; @src-gdc-2026-state-of-industry]. inZOI drew negative reviews after announcing generative features [@src-wikipedia-inzoi], and ARC Raiders re-recorded some synthetic voice lines with actors [@src-wikipedia-arc-raiders]. AI Dungeon had met the other side of the problem earlier: its 2021 content filter flagged innocent stories, and human moderators read the flagged private ones, which brought a wave of angry reviews [@src-wikipedia-ai-dungeon].

## 13. Close (12:58 to 13:26)

**Picture.** The two piles of cards again. The "changes the game's state" pile is pushed forward; Infinite Craft's card is on top.

**Voice.** Next episode counts every technique in the set, shipped or not, against every mechanic, and starts with the one shipped game that lets a language model write its rules.

**On screen.** The dataset, the sources, and the book: sim.yohei.me
