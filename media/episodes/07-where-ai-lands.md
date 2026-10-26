# Episode 7. Where AI lands

Target runtime about 14 minutes: about 1,500 words of narration at 135 words a minute, plus a beat of picture-only footage per scene. Covers book chapter 8. Footage: Infinite Craft, RimWorld, Crusader Kings III, Victoria 3, Dwarf Fortress, inZOI, The Sims, Factorio, all captured by us; a still from the DIAMOND paper's Counter-Strike model, credited. Publisher video policies are tracked in `media/rights.yaml` and must be checked before release. Every number below is filled in from the dataset when the script is built, and the sentences that interpret numbers carry the same checks as the book.

## 1. Cold open (0:00 to 0:00)

**Picture.** Infinite Craft. Four tiles: water, fire, wind, earth. The cursor drags one onto another; a new tile pops out. Faster now, combination after combination. Then one combination pauses for a beat, a new tile appears, and a badge flashes: First Discovery.

**Voice.** Every pair you try in Infinite Craft has an answer stored in a database every player shares. Until you try a pair nobody's tried. Then a language model names the result, the game saves it, and from that moment everyone who makes that pair gets your answer [@src-wikipedia-infinite-craft].

## 2. Title (0:00 to 0:00)

**Picture.** Title card over a wall of tiles.

**On screen.** Where AI lands. Episode 7.

## 3. A rule decided once (0:00 to 0:00)

**Picture.** A diagram: a pair of tiles goes into a lookup box. Hit: the stored answer comes back. Miss: an arrow to a model, then back into the box, which now holds one more row.

**Voice.** That's the clearest case in the dataset of a language model deciding a rule in a shipped game, and it works because the decision only happens once. The cache turns an unpredictable model into a rule table that grows with play and gives everyone the same result.{{assert:field.llm-rule-adjudication.determinism_impact == mitigable}}

**Voice.** It also helps that a combination has no right answer. When researchers asked GPT-4 to predict the next state of text games, across 76,369 transitions, it got the whole state right at most 59.9 percent of the time [@src-wang-2024-text-world-simulators]. An Infinite Craft tile only has to be plausible once. A model asked to run a city's water table would have to be right every tick.

## 4. Seven kinds of change (0:00 to 0:00)

**Picture.** Seven quick clips, each labelled with one effect: a Zoi crossing a room on a model's decision, "replaces"; a GT Sophy car on the limit, "deepens"; a teammate following a spoken order, "enables"; a scene appearing from a typed prompt, "cuts authoring"; a tooltip, "explains"; a bot running a test level, "tunes"; a flight sim at a higher frame rate, "accelerates."

**Voice.** Every technique in the dataset is linked to each mechanic it changes, and every link says how. It can replace how a mechanic works, deepen it, enable a new version, cut the cost of making its content, explain it to the player, tune it, or run it faster. Across {{stat:n_affects_edges}} links, the most common is deepening. The rarest is explaining: {{stat:n_effect_explains}} links, from {{stat:n_explains_techniques}} techniques, and only {{stat:n_effect_explains_shipped}} of those links comes from something that has shipped.{{assert:top_effect == Deepens}}{{assert:rarest_effect == Explains}}{{assert:n_effect_explains_shipped == 1}}

## 5. Explanation by hand (0:00 to 0:00)

**Picture.** RimWorld's needs tab, every thought listed with a number and a timer. Victoria 3: a tooltip, then a tooltip inside the tooltip, then another. Dwarf Fortress: a dwarf throwing a tantrum, with nothing on screen saying why.

**Voice.** Games that explain themselves do it by hand. RimWorld lists every thought behind a colonist's mood, with its value and when it expires. In Crusader Kings III and Victoria 3 you can hover any number to see what produced it, then hover a term inside that tooltip to open another one. Dwarf Fortress keeps each dwarf's stress as a hidden number between minus and plus a million. You see the tantrum. You don't see the account.{{assert:derived.causal-tooltips.prevalence <= 5}}

**Voice.** A model that reads the simulation's own modifier lists and event log could give any game the Paradox treatment, as long as it reports what the simulation computed instead of guessing. The technique that does this is still a prototype.{{assert:field.llm-explanation-of-state.maturity == prototype}}

## 6. Counting exposure (0:00 to 0:00)

**Picture.** The technique-flows figure builds: techniques on the left, effects in the middle, mechanic families on the right, ribbons running between them. Four families on the right collect most of the ribbons.

**Voice.** Add the links up, counting a shipped technique for more than a paper, and you get a measure of where the field is pointed. The dataset calls it exposure. In total, it piles up in four families: narrative, agents, control, and physics.{{assert:top_exposed_family == Narrative & generation}}{{assert:rank.family-summary.agents-behavior <= 4}}{{assert:rank.family-summary.control-automation <= 4}}{{assert:rank.family-summary.physics-materials <= 4}} Those are the places where content is expensive to write, like events and dialogue, or behavior is expensive to compute, like bodies and crowds.

## 7. What they'd change (0:00 to 0:00)

**Picture.** Crusader Kings III: an event window about a rival's illness, then a second event weeks later about a succession dispute. The Sims: a Sim choosing between a fridge, a bed, and a TV, each with a score floating above it. A DIAMOND-generated frame of Counter-Strike: a player hanging in mid-air.

**Voice.** In narrative, the change is from choosing to writing. Crusader Kings III's stories come from authored event templates that fire when conditions hold and schedule a follow-up weeks later. A language-model game master would write the next event for the exact state of your game instead.{{assert:field.llm-game-master.maturity == shipped-niche}} Authored chains repeat once you've seen them all. Generated ones agree to things a human game master would refuse, and invent quests that don't exist [@src-gallotta-2024-llms-games-survey].

**Voice.** In agents, the change is from scoring to asking. Most simulated characters pick their next action by giving each option a score from their needs and taking the best. Language-model characters replace the score with a prompt, and inZOI ships a small version of that. In physics, nearly every proposal replaces the engine with video prediction, and nothing in that line has shipped. One research model of Counter-Strike let the player jump again and again in mid-air, which the real game doesn't allow [@src-alonso-2024-diamond].{{assert:field.open-interactive-video-models.maturity == prototype}}

## 8. The economic core (0:00 to 0:00)

**Picture.** Factorio. A long production line; one furnace far upstream sits idle while the player inspects an assembler at the end of the line. The family-exposure bars rearranged per mechanic, resources and logistics at the bottom.

**On screen.** Resources and production: {{stat:n_family_mechanics_resources_production}} mechanics, {{stat:n_family_zero_exposure_resources_production}} with no technique.

**Voice.** Now look at the families most simulation games are built from. Resources and production is the most used family in the catalog, and of its {{stat:n_family_mechanics_resources_production}} mechanics, {{stat:n_family_zero_exposure_resources_production}} have no technique in the dataset pointed at them.{{assert:most_used_family == Resources & production}}{{assert:n_family_zero_exposure_resources_production >= 10}} Production chains, extraction, storage, crops: nothing.{{assert:derived.production-chain.technique_exposure == 0}} Every link into logistics comes from research. Per mechanic, the economic families sit near the bottom of the table, and checklists and repair sit at zero.{{assert:rank.family-mean-exposure.resources-production >= 16}}{{assert:rank.family-mean-exposure.logistics-networks >= 16}}{{assert:least_exposed_family == Operation & procedure}}

**Voice.** The production chain's own record lists the problems a technique could take on. A single optimal ratio, once solved, turns play into copying calculator output. And starvation far upstream is hard to diagnose, so players blame the wrong building. The first is a design problem that search could expose before release. The second is an explanation problem. The simulation already knows which furnace is idle, and why.

## 9. Judgment against evidence (0:00 to 0:00)

**Picture.** A scatter of mechanics: judged AI leverage on one axis, exposure on the other. A handful of points sit high on judgment and flat on exposure, labelled: mod support, simulated history, blueprints, creature care.

**Voice.** Every mechanic also carries a judged score for how much AI could change it. Judgment and exposure line up at a correlation of {{stat:rho_ai_leverage_exposure}}.{{assert:rho_ai_leverage_exposure >= 0.3}} That's a consistency check, not a second opinion: the same model rater scored the judgment, wrote the links, and rated each technique's maturity.

**Voice.** The gaps are more useful. Mod support is used by {{derived:modding-api.prevalence}} catalog games, is judged highly open to AI, and has no technique attached.{{assert:derived.modding-api.technique_exposure == 0}} Simulated history, the centuries Dwarf Fortress runs before your fortress begins, is in the same position.{{assert:derived.history-generation.technique_exposure == 0}} A general-purpose model can write mod code today. The dataset waits for someone to publish or ship that use for a named mechanic.

## 10. Close (0:00 to 0:00)

**Picture.** The family bars again, the economic core dark at the bottom. Cut to a city at night with no events on screen.

**Voice.** Next episode looks for a different kind of gap: pairs of common mechanics that almost never appear in the same game, starting with a city builder that never tells a story.

**On screen.** The dataset, the sources, and the book: sim.yohei.me
