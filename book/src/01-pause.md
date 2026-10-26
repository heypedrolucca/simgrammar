# Chapter 1. Pause

The raid arrives at dusk. A letter slides onto the screen: a band of pirates has landed to the east. Your colonists are where you left them. One is hauling steel to the stockpile, one is asleep after a double shift, and one is in the kitchen, halfway through a meal that will now go cold. You press the space bar.

Nothing moves. The pirates stand frozen at the edge of the map. The cook's knife hangs over the cutting board. And yet you keep working. You draft the hauler and the cook and march them, still paused, to the sandbags by the door. You wake the sleeper and tell her to take the rifle off the shelf. You set the doctor to stand by the infirmary. Only when every order is queued do you let time run again, and the world lurches forward into the fight you just planned.

[[rimworld|RimWorld]] runs at sixty simulation ticks every real second at normal speed, and its speed buttons multiply that by three or six; a fourth speed, fifteen times normal, exists only in development mode [@src-rimworldwiki-2026-time]. None of that matters in the moment above. What matters is that the game lets you stop it. A real-time simulation, one where things keep happening whether you are ready or not, becomes for a few seconds a turn-based game, and you get to think.

I started cataloguing simulation games because of moments like this one. Not the fight, but the pause before it: the realization that this small control, which no one would list among the things that make RimWorld special, decides how the whole game feels. If a pause button can carry that much weight, then the parts of a game that nobody talks about deserve names too. This book is about those parts, and about an open dataset that names them: {{stat:n_game}} simulation games broken into {{stat:n_mechanic}} named mechanics, with the sources for each.

## The unit is the mechanic

Ask a player what RimWorld is and you will hear a genre: a colony sim. Ask its designer and you will hear a purpose. The game was built to be a "story generator" run by computer "storytellers" that decide what happens to your colony and when [@src-wikipedia-rimworld]. Neither answer tells you what RimWorld is made of.

The dataset behind this book answers that question with a list. It breaks RimWorld into {{derived:rimworld.mechanic_count}} mechanics, each one a named rule-system that owns one kind of state and one rule for changing it. Of these, {{derived:rimworld.core_count}} are core, meaning the game would not be itself without them:{{assert:derived.rimworld.core_count == 7}}

- a **storyteller** that chooses incidents from a catalog and paces them by a budget of threat;
- **needs** that decay over time (food, rest, recreation, comfort, beauty) and feed each colonist's mood;
- **mood breaks**, so that a colonist pushed below a threshold set by their traits stops obeying and has a mental break;
- **memories and thoughts**, every mood effect itemized with a source and an expiry, which is how the game explains a breakdown after the fact;
- **work priorities**, a grid of jobs by colonists in which you rank what each person should do while they choose for themselves;
- an **injury model** in which a body is a tree of parts that bleed, scar, get infected, and get replaced;
- **threat that scales with success**, so that the richer your colony grows, the larger the raids it draws.

The rest are supporting mechanics: crops and spoilage, rooms the game recognizes by their walls and furniture, personality traits, relationships, fire that spreads, permanent death, and, near the bottom of the list, the pause button. Supporting does not mean minor. It means the mechanic serves the core ones rather than defining the game. Remove the storyteller and you have a different game. Remove the pause button and every system is still there, but the game turns from a test of planning into a test of reaction speed: a different experience built from the same parts.

In this book a mechanic has a strict definition. A candidate has to pass four tests before it enters the taxonomy. It must be **nameable**: a designer would recognize it in other games. It must be **atomic**: it owns one kind of state and one update rule, and if it splits into two parts that appear without each other in real games, it is two mechanics. It must be **tunable**: it has at least two levers a designer can turn. And it must be **removable**: a game could drop it and still run. The pause button passes all four. Its levers are the number of speeds, whether you can give orders while paused, which events pause the game automatically, and what happens to speed in multiplayer.

## A catalog of compositions

RimWorld is one game. The claim of this book is that every simulation game is a composition of the same kind of parts, and that the parts recur.

To test it, the dataset decomposes {{stat:n_game}} games, from {{stat:year_min}} to {{stat:year_max}}, into a shared vocabulary of {{stat:n_mechanic}} mechanics. Each game lists the mechanics it uses and marks which are core; each use carries a note on how that game implements it. Across the catalog there are {{stat:n_uses_edges}} such uses. The average game is built from {{stat:mean_mechanics_per_game}} mechanics, and the median game from {{stat:median_mechanics_per_game}}.

The vocabulary is shared in a strong sense. Almost no mechanic belongs to one game: only {{stat:n_mechanics_single_game}} of the {{stat:n_mechanic}} appear in a single title.{{assert:n_mechanics_single_game <= 5}} When a mechanic exists, it exists because several games found it worth building.

The figure below draws every use at once. Each row is a game, ordered by year; each column is a mechanic, grouped by family; each mark is a game using a mechanic, filled where the mechanic is core.

{{viz:matrix}}

Read the grid along a row and you see one game's composition. Read it down a column and you see a mechanic's career: where it first appeared, how it spread, and which kinds of games took it up. Most of this book is an argument about what the grid shows. The first thing it shows is that some columns are nearly full and most are nearly empty.

## The most common mechanic

The most widely used mechanic in the catalog is not a market, a production chain, or a model of crowds. It is the pause button, which the taxonomy names {{stat:most_prevalent_mechanic}}, present in {{stat:most_prevalent_mechanic_share_pct}} percent of games.{{assert:derived.variable-speed.prevalence_rank == 1}}{{assert:most_prevalent_mechanic_share_pct >= 40}} Close behind it come free placement of buildings and objects, and support for player modifications.{{assert:derived.free-placement.prevalence_rank == 2}}{{assert:derived.modding-api.prevalence_rank == 3}} Only after these three do the mechanics that simulate something take over: technology trees, scenario objectives, production chains.{{assert:derived.tech-tree.prevalence_rank <= 5}}{{assert:derived.production-chain.prevalence_rank <= 6}}

That result runs against how simulation games are usually described. The head of the distribution is not about the world being simulated. It is about the player's relationship to the simulation: when it runs, where things go, and who is allowed to change the rules. The parts that games share most are the parts that let a person live with a system that does not wait for them.

The pause button is also almost never the point. It is core in only {{derived:variable-speed.core_count}} of the {{derived:variable-speed.prevalence}} games that have it;{{assert:derived.variable-speed.core_count <= 2}} everywhere else it is supporting. That combination, nearly universal and almost never central, describes infrastructure. Players rarely name the pause button as the reason they bought a game, and almost nobody would buy a complex simulation without it.

The record for the mechanic says what it does in a single sentence: the player trades attention against elapsed game time. A real-time simulation produces events faster than a person can respond to all of them, and slower than a person wants during the dull stretches. Pause handles the first problem and fast-forward the second. Between them they create a two-tempo pattern of play that anyone who has waited for crops to grow will recognize: stop the world to plan, then race through the waiting.

That pattern has costs, and the record lists them as failure modes. At high speeds a game can quietly fall behind the multiplier it shows, because the machine cannot run the simulation that fast, so late-game fast-forward feels broken. Larger time steps at high speed can destabilize physics or produce different outcomes from normal speed. Fast-forward can also carry the player straight past an event they would have wanted to stop for, which is why so many games pause themselves when something important happens. And in multiplayer, players with different tolerances for waiting have to agree on a speed, which is why many games hand control to the host or put it to a vote. A control that looks trivial turns out to expose the compute cost of every other system in the game. When fast-forward stutters, you are watching the simulation hit its ceiling.

## A short history of stopping time

The pause is older than the games this book is mostly about. The earliest catalog entry tagged with it is [[game-of-life|Conway's Game of Life]], from 1970,{{assert:derived.variable-speed.earliest_game == game-of-life}} a cellular automaton rather than a game in the usual sense. Its computer implementations let you step one generation at a time or let it run continuously, and later simulators jump far ahead in time. That is the whole mechanic in its simplest form: a world that updates by rule, and a person who decides when.

Commercial simulation games turned that control into a design choice. [[simcity-1989|SimCity]], in 1989, let the player pause the city and pick a speed, and the same arrangement runs through city builders, management games, and colony sims to this day. Paradox's grand strategy games, which simulate centuries of history day by day, offer a pause and several speeds. Flight simulators call the same thing time compression and use it to cross oceans.

The catalog's time models record how common the arrangement became. Real time with a pause is the most common way for a catalog game to handle time, ahead of pure real time and of turns: {{stat:n_games_time_model_real_time_pausable}} games, against {{stat:n_games_time_model_real_time}} and {{stat:n_games_time_model_turn_based}}.{{assert:top_time_model == real-time-pausable}}{{assert:n_games_time_model_real_time < n_games_time_model_real_time_pausable}} Turn-based games do not need a pause button, since their structure already is one. Games that run on a real-world clock, such as virtual pets that keep living while you are away, cannot have one at all, and they build their design around that refusal.

Two details from the history matter for the rest of this book. The first is that pausing does not stop the player. In RimWorld the player can still give orders while time is stopped, which means the pause is not an absence of play but a different kind of play: planning without pressure. Some games go further and pause automatically when something important happens, which quietly decides what the player will notice.

The second is that fast-forward made simulation performance a gameplay issue. In a game without speed controls, a slow simulation is a technical problem. In a game with them, it is a design constraint, because players will push the speed as high as it goes during quiet stretches and expect the world to keep up. The cost of every other mechanic in the game, every path a colonist computes and every crop that grows, shows up as the speed the player can actually reach. Chapter 6 treats compute as one of the five ceilings on what a mechanic can be. The pause button is where players feel that ceiling first.

## Rare parts make the game

If the common mechanics make a game playable, the rare ones make it itself. RimWorld shows this sharply.

Go back to its core mechanics and count how many other games in the catalog use each one. The storyteller appears in {{derived:storyteller-director.prevalence}} catalog games.{{assert:derived.storyteller-director.prevalence <= 5}} Work priorities appear in {{derived:work-priorities.prevalence}}, the injury model in {{derived:injury-body-model.prevalence}}, mood breaks in {{derived:mood-breakdown.prevalence}}, scaling threat in {{derived:adaptive-threat-scaling.prevalence}}, and itemized memories in {{derived:memories-thoughts.prevalence}}.{{assert:derived.work-priorities.prevalence <= 10}}{{assert:derived.injury-body-model.prevalence <= 10}}{{assert:derived.mood-breakdown.prevalence <= 10}}{{assert:derived.adaptive-threat-scaling.prevalence <= 10}}{{assert:derived.memories-thoughts.prevalence <= 10}} Six of the seven sit in the long, thin tail of the grid. The exception is needs that decay, which {{derived:needs-decay.prevalence}} games share,{{assert:derived.needs-decay.prevalence > 20}} from [[little-computer-people|Little Computer People]] in 1985 to [[the-sims|The Sims]] and beyond.{{assert:derived.needs-decay.earliest_game == little-computer-people}}

Within the catalog, three of the rare six first appear in the same game: [[dwarf-fortress|Dwarf Fortress]], in 2006. Each has older relatives outside simulation games: tabletop role-playing games and mech combat games tracked damage by body location long before. Dwarf Fortress is where the three arrived together in a colony simulation.{{assert:derived.mood-breakdown.earliest_game == dwarf-fortress}}{{assert:derived.injury-body-model.earliest_game == dwarf-fortress}}{{assert:derived.adaptive-threat-scaling.earliest_game == dwarf-fortress}} RimWorld's record lists Dwarf Fortress as an influence, and the grid shows what that influence consisted of. RimWorld did not copy a genre. It took three specific rule-systems, mood breaks, bodies made of parts, and danger that grows with wealth, and combined them with a storyteller, a work grid, and the needs every life sim has.

That is the general pattern this book will keep returning to. A game's identity lives in a small number of uncommon mechanics and in how they are wired together. Its playability lives in a larger number of common ones that players expect and rarely notice.

## Why name the parts

Naming mechanics would be a pedantic exercise if names did not change what you can do. They change three things.

First, names let you compare games that look nothing alike. RimWorld and [[the-sims|The Sims]] belong to different genres, sell to different players, and draw different reviews. In the grid they share needs that decay, personality traits, relationships, rooms judged by their beauty, and characters who choose their own next action by weighing what they need. A designer who knows that can borrow across the genre line on purpose.

Second, names let you see what has not been tried. A vocabulary of {{stat:n_mechanic}} mechanics allows {{stat:n_possible_pairs}} possible pairs. Only {{stat:pair_coverage_pct}} percent of those pairs occur together in even one catalog game.{{assert:pair_coverage_pct < 50}} Most combinations of known parts have never been built. Some are empty because they make no sense; a flight simulator has no use for free building placement. Others are empty because no one has got round to them yet, and later chapters argue that some of those are the clearest openings in the field.

Third, names let you ask precise questions about new technology. When people say that AI will change simulation games, the useful follow-up is: which mechanics? A language model that writes dialogue changes a different column of the grid from a learned physics model or a planner that runs a city's traffic. Part II of this book traces each technique to the mechanics it affects, and finds that the columns attracting the most research are not the ones most games are built from.{{assert:n_top10_prevalent_zero_exposure >= 5}}

## Exercise: decompose a game

Pick a real-time simulation game you know well. It does not have to be in the catalog.

1. List its mechanics using the catalog's names where they fit. Browse the mechanic glossary at the back of the book, or search the dataset online. Aim for ten to fifteen.
2. Mark the core ones: the mechanics without which the game would not be itself. Most games have only a few.
3. For each core mechanic, guess how many other games use it, then look it up. You will probably find that the mechanics you think of as the game's signature are rarer than you guessed, and the ones you barely noticed are among the most common in the field.
4. Now remove the pause button, or its equivalent, and play the game in your head. What breaks first? What would you have to add to make the game playable again? (If you picked a turn-based game, ask the reverse: what would break if its turns became continuous time?)

The answer to the last question is usually a second mechanic doing the pause's job in disguise: an automatic slowdown when danger appears, a planning phase between waves, a turn structure. Simulation games can do without a pause button. They cannot do without some way of letting a person think. The next chapter shows that this is one of six jobs every simulation game has to do, and that the mechanics sort into those jobs more cleanly than they sort into genres.
