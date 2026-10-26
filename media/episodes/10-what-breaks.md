# Episode 10. What breaks

Target runtime about 12 minutes: about 1,210 words of narration at 135 words a minute, plus a beat of picture-only footage per scene. Covers book chapter 11. Footage: Factorio, Infinite Craft, Townscaper, all captured by us; the desync and the event log are animated diagrams; research results appear as charts and quoted figures, not as clips from the papers. Publisher video policies are tracked in `media/rights.yaml` and must be checked before release. Every number below is filled in from the dataset when the script is built, and the sentences that interpret numbers carry the same checks as the book.

## 1. Cold open (0:00 to 0:46)

**Picture.** Animated diagram: two monitors side by side showing the same strategy map, an enemy cavalry unit in the middle. A small clock icon over each labelled "AI thinking time". On the left monitor the cavalry turns north; on the right it holds. Two checksums appear under the screens, different. A dialog box: "Desync".

**Voice.** Two players, one computer opponent, and a game that keeps both machines in step by sending only orders. The opponent gets a fixed slice of time to think before each move. One machine is faster, so in the same slice it thinks further, and on one move it picks something different. For a few seconds the two worlds look fine. Then they compare notes, and the match is over.

## 2. Title (0:46 to 0:56)

**Picture.** Title card over the desync dialog, out of focus.

**On screen.** What breaks. Episode 10.

## 3. The fix was one line (0:56 to 2:03)

**Picture.** The dataset's record for Monte Carlo tree search, scrolling to its limitations. One line highlights.

**Voice.** The opponent in that match plans with Monte Carlo tree search, and the dataset's record for the technique lists exactly this failure: a search that stops by the clock returns different moves on different hardware, which breaks replays and lockstep multiplayer. The fix is to count playouts instead of milliseconds and seed the random numbers. Then every machine computes the same move, which is why the record calls the technique mitigable.{{assert:field.monte-carlo-tree-search.determinism_impact == mitigable}}

**Voice.** That's the shape of most of this episode. Simulation games need some things most software doesn't: the same inputs have to make the same world, everything a player sees is evidence about how the game works, and one purchase has to pay for hundreds of hours.

## 4. Same inputs, same world (2:03 to 4:00)

**Picture.** Factorio multiplayer: two players' views of the same factory, belts moving in perfect step. Overlay: a replay file icon, a bug report icon, a leaderboard, a save file.

**Voice.** Factorio's record notes that items move in fixed, discrete steps, and that's what lets its multiplayer run identical worlds on every machine. The same property gives you replays, bug reports a developer can reproduce, leaderboards you can trust, and saves that load into the world you saved.

**On screen.** Techniques that can run during play: {{stat:n_technique_runtime}}. Break reproducibility outright: {{stat:n_technique_runtime_breaks}}. Can be made reproducible: {{stat:n_technique_runtime_mitigable}}. Leave it intact: {{stat:n_technique_runtime_preserves}}.

**Voice.** Of the techniques in the dataset that can run while you play, {{stat:n_technique_runtime_breaks}} break that property outright.{{assert:n_technique_runtime_breaks < n_technique_runtime_mitigable}} Frame-generating world models, language-model game masters, societies of language agents, realtime voice: each samples its output, and its output decides what happens next.{{assert:field.genie-world-models.determinism_impact == breaks}}{{assert:field.llm-game-master.determinism_impact == breaks}}{{assert:field.realtime-voice-models.determinism_impact == breaks}}

**Picture.** A diagram: a model's answer drops into a cache, and two players' screens read the same entry.

**Voice.** Others can be pinned down. Infinite Craft, from episode 7, stores each answer the first time a model gives it, so every player after that gets the same one.{{assert:field.llm-rule-adjudication.determinism_impact == mitigable}}

**Picture.** Townscaper: a player clicks along a waterline and houses, arches, and stairs assemble themselves.

**Voice.** And some never touch the problem. Townscaper fits its houses together with a deterministic algorithm, wave function collapse, so the same clicks always build the same town.{{assert:field.wave-function-collapse.determinism_impact == preserves}} Neural upscaling and frame generation never touch the simulation at all; they work on the picture after the game has decided everything. That's part of why they're the one learned technique that has become normal in games, and the dataset marks them as leaving reproducibility intact.{{assert:field.neural-rendering-shaders.maturity == shipped-mainstream}}{{assert:field.neural-rendering-shaders.determinism_impact == preserves}} Of the {{stat:n_predictions}} bets in the last episode, {{stat:n_opportunity_applies_breaking}} lean on at least one technique that breaks reproducibility, so each of those needs a plan for it.{{assert:n_opportunity_applies_breaking < n_predictions}}

## 5. Contradiction (4:00 to 5:19)

**Picture.** A diagram of a first-person view where the player icon jumps, then jumps again in mid-air.

**Voice.** A gap in a simulation is survivable. A contradiction teaches the player something false. Episode 7 showed a language model getting the state of a text game wrong close to half the time. A diffusion model trained on Counter-Strike footage lets the player jump again in mid-air, which the real game never allows [@src-alonso-2024-diamond]. In one playtest, players reported language-model characters forgetting what they had said earlier in one report out of ten [@src-peng-2024-player-driven-emergence].

**Voice.** So there's a place where a language model is safe and a place where it isn't. Asked to predict what the simulation will do, it's wrong often enough to mislead. Asked to describe what the simulation did, from a log of events the simulation computed, it has the answer in front of it.

## 6. Opaque replacements (5:19 to 6:10)

**Picture.** Victoria 3-style nested tooltips (diagram), each number opening into its causes. Then the same panel replaced by a single grey box labelled "learned policy", with nothing to open.

**Voice.** Deep simulations already fight to be understood. Designers built a whole family of mechanics, overlays, inspectors, tooltips, chronicles, whose only job is to explain the rest. A learned component can undo that work. A trained policy can run traffic or set a rival's prices well and still give no reason for anything it does. The dataset lists legibility as a risk on {{stat:n_technique_risk_legibility}} techniques.{{assert:n_technique_risk_legibility >= 5}} The cheapest remedy is the same every time: write down what the component decided, and on what inputs.

## 7. The bill (6:10 to 7:32)

**Picture.** A stack of coins grows beside a clock labelled "player-hours". Then a timer counting down from sixty seconds over a blurred generated world.

**Voice.** Most simulation games are bought once and played for a very long time, and a feature that calls a model every few seconds turns each of those hours into a cost. The 25-agent town behind the generative agents paper cost thousands of dollars in model credits [@src-park-2023-generative-agents]. When Google opened its Genie 3 world model to subscribers, each world was capped at sixty seconds because of limited compute [@src-techcrunch-2026-project-genie].

**Voice.** At the other end, a two-billion-parameter character model can be squeezed into about one and a half gigabytes of graphics memory, beside the game's own rendering [@src-sreenivas-2024-minitron; @src-nvidia-2025-ace-companions]. Running it on the player's machine moves the cost to their hardware, though NVIDIA's in-game inference kit still asks for at least an RTX 30-series card with eight gigabytes [@src-nvidia-2026-nvigi-core]. In between, caching helps: a later study cut the tokens for that same 25-agent town to under half by replaying stored plans [@src-yu-2024-affordable-generative-agents].

## 8. Steering and checking (7:32 to 8:22)

**Picture.** The risk table from the dataset builds as a bar chart, longest bar at the top.

**Voice.** The risk the dataset records most often across its techniques is {{stat:top_technique_risk}}: the designer can't reliably make the technique do what the design needs.{{assert:top_technique_risk == controllability}} It's on {{stat:n_technique_risk_controllability}} of them. Language-model game masters tend to go along with requests a human game master would refuse [@src-gallotta-2024-llms-games-survey]. Close behind comes evaluation: when a system can produce endless variations, nobody can check them all.{{assert:n_technique_risk_evaluation >= 15}} Automated playtests can say a generated event is valid and balanced. They can't say it's any good.

## 9. Trust (8:22 to 9:29)

**Picture.** Plain text cards, one per fact, over a dark background.

**Voice.** Players and the people who make games have their own reasons for caution. In 2021, AI Dungeon's new content filter flagged innocent stories, human moderators read players' private stories, and players review-bombed the game [@src-wikipedia-ai-dungeon]. The video game actors' strike that ran from July 2024 to July 2025 ended with rules requiring consent for AI voice replicas [@src-wikipedia-artificial-intelligence-in-video-games]. Steam now asks developers whether their AI content was made before release or is generated while you play, and asks the second kind to describe their guardrails [@src-valve-2026-steamworks-content-survey]. The bets that explain a game or let players write more of it replace nobody's work. The bets that replace writing, voices, or art carry the whole weight of those questions.

## 10. A log as the fix (9:29 to 10:52)

**Picture.** The desync diagram from the cold open again. This time the opponent's move is computed once, written as a line in a scrolling log, and sent to both monitors. The checksums match. Then the same log feeds three small panels: a replay, a "why?" answer with links, and a forked timeline.

**Voice.** One design answers most of this at once. Record every change to the game as an event, including the changes a model decided, and treat the log as the source of truth.{{assert:rank.opportunities-ranked.event-sourced-sim-runtime <= 5}} In the desynced match, the opponent's move would have been decided once and sent to both machines. A replay reads the logged answer instead of asking the model again. A bug report carries the log. And the "why?" button from the last episode cites it.

**Voice.** A second tool limits what the model can write in the first place: constrained decoding only lets it produce output that fits a schema, so every action it proposes is one the engine can carry out. A hosted version followed a complex schema every time in testing, against under forty percent for an older model without it [@src-openai-2024-structured-outputs]. Strict formats cost some reasoning accuracy [@src-tam-2024-let-me-speak-freely], and the dataset hasn't found a shipped game that documents using it.{{assert:field.constrained-decoding.maturity == research}}

## 11. Close (10:52 to 11:37)

**Picture.** The two monitors from the cold open, in step, the match continuing.

**Voice.** The event-log bet carries its own prediction: an engine, a middleware vendor, or an open-source project ships a replay layer built for games with generative parts by the end of 2028.{{assert:field.event-sourced-sim-runtime.falsifiable_signal.resolve_by == 2028-12-31}} Until then, the techniques that leave the simulation reproducible, upscaling, cached rules, deterministic generators, are the ones already shipping.{{assert:field.llm-rule-adjudication.maturity == shipped-niche}}{{assert:field.wave-function-collapse.maturity == shipped-niche}} The next episode is about how predictions like that one get checked, and who's allowed to check them.

**On screen.** Every technique and its risks: sim.yohei.me
