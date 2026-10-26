# Chapter 8. Where AI lands

You start with four tiles: water, fire, wind, and earth. Drag one onto another and a new tile appears with a name and an emoji. Drag that onto something else. Most pairs you try have been tried before by someone, somewhere, and the answer comes back from a database that every player of [[infinite-craft|Infinite Craft]] shares, so you get the same result anyone else would.

After a while you combine two things nobody has combined. This time the database has no entry, and the game asks a language model: a Llama model writes a name for the result, at most twenty tokens long, and picks an emoji. The game stores the answer, and your screen marks the new tile as a First Discovery. From then on every player who drops those two tiles together gets your result [@src-wikipedia-infinite-craft].

Infinite Craft is the clearest case in the dataset of a model deciding a game rule in a shipped game, and it works because the decision is made once. The technique record, LLM-adjudicated state transitions, describes the cache as turning a stochastic model into a growing deterministic rule table, with cost bounded by the number of new pairs.{{assert:field.llm-rule-adjudication.determinism_impact == mitigable}} It also helps that the mechanic has no right answer. When researchers asked GPT-4 to predict the next state of 31 text games across 76,369 transitions, it got the whole state right at most 59.9 percent of the time, and at most 49.7 percent for changes the environment caused on its own [@src-wang-2024-text-world-simulators]. A combination in Infinite Craft only has to be plausible once and consistent afterwards. A model asked to run a city's water table would have to be right.

## Seven ways to change a mechanic

Every technique in the dataset is linked to the mechanics it changes by an `affects` edge, and each edge records one of seven effects. A technique can replace a mechanic's substrate, keeping its role in play while swapping how it works, as when a language model replaces the scoring formula that picks a character's next action. It can deepen a mechanic with more fidelity, scale, or variety; enable a form that was not possible before; cut the authoring cost of the content the mechanic consumes; explain the mechanic's state to the player; tune or balance it; or run it faster.

{{table:effect-distribution}}

Across {{stat:n_affects_edges}} edges, deepening is the most common effect, at {{stat:n_effect_deepens}} edges, and explaining is the rarest, at {{stat:n_effect_explains}}.{{assert:top_effect == Deepens}}{{assert:rarest_effect == Explains}} Only {{stat:n_explains_techniques}} techniques explain anything. Three of the explaining edges come from one prototype, language-model explanation of state, which turns an agent's thought log into a short account of why it acted, condenses a long chain of modifiers into a ranked list of causes, or annotates a graph with the events that moved it.{{assert:field.llm-explanation-of-state.maturity == prototype}} {{stat:n_effect_explains_shipped}} explaining edge comes from a technique that has shipped: generative agents keep their memories, plans, and reflections as text, so a player or designer can read them or ask the character why it did something.{{assert:n_effect_explains_shipped == 1}}

The imbalance follows research effort. Generating content and replacing substrates attract most of the work, while explaining a running simulation to the person playing it attracts little, although the parts it needs (retrieval over a structured log, constrained generation, summarization) all exist. Chapter 5 described legibility as the cost that deep systems pay, and the dataset finds few techniques aimed at paying it.

## Counting exposure

To compare families of mechanics, the dataset sums each mechanic's edges into a *technique exposure*. Each edge counts for more when the technique has shipped than when it is a research result, and for more when it replaces or enables a mechanic than when it only tunes or speeds it up; the weights are written down in the rubrics file. A family's exposure is the sum over its mechanics. The measure says where the set of techniques points, weighted by how close each one is to a game. It does not say what will happen next.

{{viz:technique-flows}}

In total, exposure concentrates in four families: narrative and generation, agents and behavior, control and automation, and physics and materials.{{assert:top_exposed_family == Narrative & generation}}{{assert:rank.family-summary.agents-behavior <= 4}}{{assert:rank.family-summary.control-automation <= 4}}{{assert:rank.family-summary.physics-materials <= 4}} These are the families where content is expensive to write (events, dialogue, characters) or behavior is expensive to compute (bodies, vehicles, crowds).

Divided by the number of mechanics in each family, the order changes. {{stat:top_mean_exposed_family}} still leads and world generation comes second, while agents and physics drop out of the top three: their totals partly reflected how many mechanics they hold.{{assert:top_mean_exposed_family == Narrative & generation}}{{assert:rank.family-mean-exposure.world-generation <= 2}}{{assert:rank.family-mean-exposure.agents-behavior > 3}}{{assert:rank.family-mean-exposure.physics-materials > 3}}

## The economic core

At the other end sit the families most simulation games are built from. Per mechanic, resources, logistics, economy, and population all fall in the lower half of the families, and resources and logistics sit near the bottom.{{assert:rank.family-mean-exposure.resources-production >= 16}}{{assert:rank.family-mean-exposure.logistics-networks >= 16}}{{assert:rank.family-mean-exposure.economy-finance > 10}}{{assert:rank.family-mean-exposure.population-lineage > 10}} Operation and procedure, the family of checklists, surface tools, and repair, has no technique attached at all.{{assert:least_exposed_family == Operation & procedure}}{{assert:n_family_zero_exposure_operation_procedure == n_family_mechanics_operation_procedure}}

Resources and production is the clearest case. It is the most used family in the catalog,{{assert:most_used_family == Resources & production}} and of its {{stat:n_family_mechanics_resources_production}} mechanics, {{stat:n_family_zero_exposure_resources_production}} have no technique in the set pointed at them.{{assert:n_family_zero_exposure_resources_production >= 10}} The two that do are hand crafting, which Infinite Craft's cached combinations turn into an open-ended recipe space, and machine boosting, where a research method searches module layouts for the dominant configurations that flatten a player's choices.{{assert:derived.hand-crafting.technique_exposure > 0}}{{assert:derived.machine-boosting.technique_exposure > 0}} Production chains, extraction, storage, spoilage, crops, and power have nothing.{{assert:derived.production-chain.technique_exposure == 0}}{{assert:derived.resource-extraction.technique_exposure == 0}}{{assert:derived.storage-capacity.technique_exposure == 0}}{{assert:derived.spoilage.technique_exposure == 0}}{{assert:derived.crop-cultivation.technique_exposure == 0}}{{assert:derived.power-grid.technique_exposure == 0}}

Logistics fares only slightly better. Of its {{stat:n_family_mechanics_logistics_networks}} mechanics, {{stat:n_family_zero_exposure_logistics_networks}} have no technique, and every edge that reaches the family comes from research: mean-field games that would let drivers anticipate congestion instead of reacting to it, GPU simulation that points at agent-level traffic at much larger counts, and calibration methods that fit a traffic model to observed counts.{{assert:field.mean-field-games.maturity == research}}{{assert:field.massively-parallel-simulation.maturity == research}}{{assert:field.simulation-based-inference.maturity == research}} In economy and finance, the one shipped technique with an edge is tree search, which can let rival firms choose prices and expansions by rolling the market forward.{{assert:field.monte-carlo-tree-search.maturity == shipped-niche}}

Chapter 1 noted that most of the ten most used mechanics have no technique attached. Across the whole vocabulary, {{stat:n_mechanics_zero_exposure}} mechanics are affected by no technique in the set, and they account for {{stat:pct_uses_on_zero_exposure}} percent of every game-to-mechanic use in the catalog.{{assert:pct_uses_on_zero_exposure >= 40}}

Part of this is sensible. A production chain is cheap to compute and, by the rater's scores, about as easy to read as the average mechanic; there is less for a learned model to fix. Part of it is a gap. Economies are where simulation games break: a price or loan loophole turns the economy into an exploit, recipe graphs have to be authored and balanced by hand, and scenarios have to be tested against strategies no designer tried. Those are tuning and authoring problems, and tuning methods exist. Agent-based playtesting has shipped in production pipelines, and search that keeps the best design for each niche of a space is an established research method.{{assert:field.automated-playtesting.maturity == shipped-niche}}{{assert:field.quality-diversity-search.maturity == research}}

## The most exposed mechanics

{{table:most-exposed-mechanics}}

Generative content and procedural terrain lead the ranking, because many techniques generate content or worlds.{{assert:rank.most-exposed-mechanics.generative-content <= 2}}{{assert:rank.most-exposed-mechanics.procedural-terrain <= 2}} Utility action selection, the scoring that picks a character's next action from its needs, comes third:{{assert:rank.most-exposed-mechanics.utility-action-selection == 3}} language models, planners, and learned policies all offer to replace it, and inZOI's Smart Zois are the shipped case, a small local model choosing among the game's own actions. Rigid-body physics and direct avatar control follow,{{assert:rank.most-exposed-mechanics.rigid-body-physics <= 6}}{{assert:rank.most-exposed-mechanics.direct-avatar <= 6}} exposed mainly to frame-generating world models such as Genie, which replace both with learned prediction and carry over the consistency limits chapter 7 described.

Generative content is used by {{derived:generative-content.prevalence}} catalog games, almost all of them AI-native titles, and is affected by {{derived:generative-content.technique_count}} techniques.{{assert:derived.generative-content.prevalence < 10}} The most exposed mechanic in the set is one of the least used, which is another way of saying that exposure measures where research looks.

## Judgment against evidence

Every mechanic also carries a judged score for AI leverage: how much, in the rater's reading, current techniques could change it. Leverage and exposure correlate at ρ = {{stat:rho_ai_leverage_exposure}}.{{assert:rho_ai_leverage_exposure >= 0.3}} That number is a consistency check and not independent agreement. The same model rater scored leverage, wrote the `affects` edges, and judged each technique's maturity, so a correlation between them shows the rater was consistent with itself. A second, calibrated rater is the remedy, and chapter 13 describes how one is being added.

Where the two disagree is more useful than where they agree. The leverage-gap table lists mechanics judged highly open to AI that no technique in the set touches.

{{table:leverage-gap}}

Mod support tops the list because it is the most widely used of them, at {{derived:modding-api.prevalence}} games.{{assert:rank.leverage-gap.modding-api == 1}}{{assert:derived.modding-api.technique_exposure == 0}} Romance and family systems, blueprints, creature care, product design, diagnosis, simulated history, and rule-checking inspection are each judged ready for substantial change and have no cited, game-specific technique.{{assert:derived.blueprints.technique_exposure == 0}}{{assert:derived.history-generation.technique_exposure == 0}}{{assert:derived.rule-checking-inspection.technique_exposure == 0}}{{assert:derived.creature-care.technique_exposure == 0}} Some are covered implicitly by general methods, such as code generation for mods or language models for romance dialogue, but the dataset admits a technique only as a dated result that changes a named mechanic, and none has been recorded.

## Exercise: aim a technique

Pick one mechanic from the leverage-gap table.

1. Write down the state it owns and the rule that updates it, from its record.
2. Choose one effect from the seven: replace, deepen, enable, cut authoring cost, explain, tune, or accelerate. Pick the one that would matter most to a player.
3. Name the smallest technique that could do it, and say whether its output would enter authoritative state or stay in presentation.
4. Describe the experiment that would show it worked, with a number a stranger could check.

Step 3 decides most of the risk. Chapter 9 turns from techniques to the mechanics themselves and looks for pairs of common parts that almost never appear in the same game.
