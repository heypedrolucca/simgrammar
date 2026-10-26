# Chapter 1. Same parts

The raid comes at dusk. A letter in the corner of the screen says pirates have landed to the east. You stop the clock, draft the two colonists nearest the door, walk them to the sandbags, and let time run again. The fight takes less than a minute of game time. One pirate gets as far as the doorway before he goes down, and he takes the cook's son with him.

Three days later the cook puts down her knife and walks out of the kitchen. She ignores orders. She wanders past the stockpile and out through the fields while the stew she left burns. Open her needs tab and [[rimworld|RimWorld]] tells you why, one line at a time: her son died, worth −20 to her mood for thirty days; a lavish meal two days ago, worth +12, has since expired; a dozen smaller entries for her bed, her room, and the corpses nobody has hauled away [@src-rimworldwiki-2026-thoughts]. Her mood has sat below the first of three break thresholds, 35, 20, and 5 percent, since the funeral, and every hour below it carried a chance of a break. Today the roll came up [@src-rimworldwiki-2026-mental-break].

Nobody wrote that story. A storyteller chose the raid and its timing. The raid's size came from how rich the colony had grown. The shot that killed the son hit a named part of his body. His death wrote an entry into his mother's memory with a value and an expiry date, the entries summed to a mood, and the mood crossed a threshold that rolls for breakdowns. Each of those is a separate rule-system with its own state and its own update rule, and RimWorld's designer chose them for the stories they produce: he describes the game as a "story generator" [@src-wikipedia-rimworld].

An open dataset breaks {{stat:n_game}} simulation games into {{stat:n_mechanic}} named rule-systems like those, with the sources for each, and this book is built on it.

## RimWorld, in parts

The dataset lists {{derived:rimworld.mechanic_count}} mechanics in RimWorld. A mechanic, in this book, is a named rule-system that owns one kind of state and one rule for changing it. Each game marks some of its mechanics as core, meaning the game would be a different game without them. RimWorld has {{derived:rimworld.core_count}}:{{assert:derived.rimworld.core_count == 7}}

- a **storyteller** that picks incidents from a catalog, spending a threat budget derived from colony wealth and the time since the last major event;
- **needs** that run down (food, rest, recreation, comfort, beauty) and feed each colonist's mood;
- **mood breaks**, rolled while mood sits below thresholds that personality traits shift;
- **memories and thoughts**, every mood effect listed with its source and expiry;
- **work priorities**, a grid of colonists by job types where you rank each job from 1 to 4 and colonists choose for themselves;
- an **injury model** in which a body is a tree of parts that bleed, scar, get infected, and get replaced;
- **threat that scales with wealth**, so the richer the colony, the bigger the raids.

The other mechanics support those: crops and spoilage, rooms the game recognizes from their walls and furniture, traits, relationships, fire, permanent death, mod support, and the pause button you pressed when the letter arrived.

The definition has four tests, and a candidate has to pass all of them before it enters the taxonomy. A designer must be able to name it and recognize it in other games. It must be atomic: if it splits into two parts that real games use without each other, it is two mechanics. It must have at least two levers a designer can turn. And a game must be able to drop it and still run. The storyteller passes: Left 4 Dead's director and RimWorld's three storytellers are recognizably the same thing [@src-booth-2009-ai-systems-l4d], its levers include the incident catalog and the length of the quiet stretches, and a colony sim can run without one, as Dwarf Fortress does.

## Rare parts

Count how many other games in the catalog use each of RimWorld's core mechanics. The storyteller appears in {{derived:storyteller-director.prevalence}} catalog games, work priorities in {{derived:work-priorities.prevalence}}, the injury model in {{derived:injury-body-model.prevalence}}, mood breaks in {{derived:mood-breakdown.prevalence}}, scaling threat in {{derived:adaptive-threat-scaling.prevalence}}, and itemized memories in {{derived:memories-thoughts.prevalence}}.{{assert:derived.storyteller-director.prevalence <= 5}}{{assert:derived.work-priorities.prevalence <= 10}}{{assert:derived.injury-body-model.prevalence <= 10}}{{assert:derived.mood-breakdown.prevalence <= 10}}{{assert:derived.adaptive-threat-scaling.prevalence <= 10}}{{assert:derived.memories-thoughts.prevalence <= 10}} Six of the seven are rare. The seventh, needs that decay, is shared by {{derived:needs-decay.prevalence}} games, going back to [[little-computer-people|Little Computer People]] in 1985.{{assert:derived.needs-decay.prevalence > 20}}{{assert:derived.needs-decay.earliest_game == little-computer-people}}

The rare six have traceable origins. Three of them, mood breaks, bodies made of parts, and danger that grows with wealth, first appear in the catalog in the same game, [[dwarf-fortress|Dwarf Fortress]], released in 2006.{{assert:derived.mood-breakdown.earliest_game == dwarf-fortress}}{{assert:derived.injury-body-model.earliest_game == dwarf-fortress}}{{assert:derived.adaptive-threat-scaling.earliest_game == dwarf-fortress}} Dwarf Fortress is where the three arrived together in a colony sim, and RimWorld's record names it as an influence. The catalog's earliest storyteller is older and comes from somewhere else: [[facade|Façade]], a 2005 interactive drama in which a drama manager picks the next beat of an argument between a married couple, Grace and Trip, toward one of three endings.{{assert:derived.storyteller-director.earliest_game == facade}} RimWorld's core puts together a device the catalog first records in a narrative experiment, three systems that arrived together in Dwarf Fortress, and the needs of the life sims, all driven through a work grid.

The pattern holds across the catalog. The mechanics games mark as core are used by a median of {{stat:median_prevalence_core_uses}} catalog games; the ones they mark as supporting, by a median of {{stat:median_prevalence_supporting_uses}}.{{assert:median_prevalence_core_uses < median_prevalence_supporting_uses}} And {{stat:pct_games_with_rare_core}} percent of games have at least one core mechanic that no more than {{stat:rare_max_games}} catalog games use.{{assert:pct_games_with_rare_core >= 75}}

## The grid

Do the same for every game in the catalog. The dataset decomposes {{stat:n_game}} games, from {{stat:year_min}} to {{stat:year_max}}, into a shared vocabulary of {{stat:n_mechanic}} mechanics. Each game lists the mechanics it uses, marks the core ones, and adds a note on how it implements each. Across the catalog there are {{stat:n_uses_edges}} such uses; the average game is built from {{stat:mean_mechanics_per_game}} mechanics, and the median game from {{stat:median_mechanics_per_game}}.

Almost every mechanic recurs. Only {{stat:n_mechanics_single_game}} of the {{stat:n_mechanic}} appear in a single title,{{assert:n_mechanics_single_game <= 5}} so a mechanic in this vocabulary is something several designers found worth building.

The figure draws every use at once. Each row is a game and each column a mechanic; each mark is a game using a mechanic, filled where the mechanic is core.

{{viz:matrix}}

A row is one game's recipe. A column is one mechanic's career: the year it first appears, how fast it spread, and which kinds of games took it up. A few columns are nearly full and most are nearly empty.

## The most common parts

The five mechanics that the most catalog games use are the pause button, building placement, mod support, a tech tree, and scenario goals.{{assert:derived.variable-speed.prevalence_rank == 1}}{{assert:derived.free-placement.prevalence_rank == 2}}{{assert:derived.modding-api.prevalence_rank == 3}}{{assert:derived.tech-tree.prevalence_rank <= 5}}{{assert:derived.scenario-objectives.prevalence_rank <= 5}} None of the five models anything in the world being simulated. They decide when the world runs, where the player puts things, who may change the rules, and what the player is working toward. Production chains come sixth and are the first mechanic on the list that models a process: ore into plates, plates into gears, grain into flour into bread.{{assert:derived.production-chain.prevalence_rank == 6}}

The pause button leads, present in {{stat:most_prevalent_mechanic_share_pct}} percent of catalog games.{{assert:most_prevalent_mechanic_share_pct >= 40}} The one game where it is core is [[universe-sandbox|Universe Sandbox]], a space sandbox where the speed you choose changes the result: the simulation runs from real time to years per second, larger time steps trade away accuracy, and a fast run of a solar system can end differently from a slow one.{{assert:derived.variable-speed.core_count == 1}} Real time with a pause is also the catalog's most common way to handle time, at {{stat:n_games_time_model_real_time_pausable}} games against {{stat:n_games_time_model_real_time}} in pure real time and {{stat:n_games_time_model_turn_based}} turn-based.{{assert:top_time_model == real-time-pausable}}{{assert:n_games_time_model_real_time < n_games_time_model_real_time_pausable}} Fast-forward runs every other system faster, so the late-game slowdown players complain about in colony and city games is the cost of every computed path and every growing crop, showing up as the top speed the machine can reach. Chapter 6 treats compute as one of five ceilings on what a mechanic can be.

Building placement is the exception among the five. It is core in {{derived:free-placement.core_count}} games,{{assert:derived.free-placement.core_count >= 10}} the city builders and construction games where placing things is most of what the player does. The other four are nearly always supporting parts. Mod support is core in {{derived:modding-api.core_count}} games: in [[garrys-mod|Garry's Mod]] community game modes became the main way people play, and [[arma-3|Arma 3]] gets much of its life from community scenarios and mods.{{assert:derived.modding-api.core_count <= 3}}

## What the names are for

Naming parts lets you compare games that look nothing alike. RimWorld and [[the-sims|The Sims]] sell to different players and get reviewed in different places. In the grid they share needs that decay, personality traits, relationships, skills, decoration that people respond to, and characters that choose their own next action by scoring what they need. A designer who knows that can borrow across the genre line deliberately, and chapter 4 shows that grouping games by their parts puts the two in the same family more often than not.{{assert:cocluster.rimworld.the-sims > 0.5}}

Names also show what has not been tried. A vocabulary of {{stat:n_mechanic}} mechanics allows {{stat:n_possible_pairs}} possible pairs, and only {{stat:pair_coverage_pct}} percent of those pairs occur together in even one catalog game.{{assert:pair_coverage_pct < 50}} Some combinations are empty because they make no sense; a flight simulator has no use for building placement. Others are empty because nobody has built them, and chapter 9 walks through the ones where both mechanics are common.

And names make questions about AI answerable. A language model that writes dialogue changes a different column of the grid from a learned physics model or a planner that routes a city's traffic. Part II traces each technique in the dataset to the mechanics it affects. Of the ten most widely used mechanics, {{stat:n_top10_prevalent_zero_exposure}} have no technique in the dataset pointed at them.{{assert:n_top10_prevalent_zero_exposure >= 5}}

## Exercise: decompose a game

Pick a simulation game you know well. It does not have to be in the catalog.

1. List its mechanics, using the catalog's names where they fit (the glossary at the back of the book, or the dataset online). Ten to fifteen is typical.
2. Mark the core ones, the mechanics without which it would be a different game. Most games have only a few.
3. For each core mechanic, guess how many catalog games use it, then look it up. The parts you think of as the game's signature are probably rarer than you guessed, and the parts you never think about are probably among the most common.
4. Remove one core mechanic and describe the game that is left. Then add one rare mechanic from another game's core and describe that game.

Chapter 2 sorts the vocabulary by the job each mechanic does: holding state, changing it, connecting systems, taking in the player's intent, showing what is happening, and deciding when the player has to look.
