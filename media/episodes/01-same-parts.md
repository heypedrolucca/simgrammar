# Episode 1. Every simulation game is made of the same parts

Target runtime about 11 minutes: about 1,260 words of narration at 135 words a minute, plus a beat of picture-only footage per scene. Covers book chapters 1 and 2. Footage: RimWorld, SimCity (1989), Factorio, all captured by us; publisher video policies are tracked in `media/rights.yaml` and must be checked before release. Every number below is filled in from the dataset when the script is built, and the sentences that interpret numbers carry the same checks as the book.

## 1. Cold open (0:00 to 1:01)

**Picture.** RimWorld, late afternoon on a small colony. A letter slides in: raiders to the east. Three colonists in three places: hauling, sleeping, cooking. The game pauses. While paused, the player drafts two colonists, walks them to sandbags, wakes the third, assigns a rifle. Unpause. The fight begins and we cut away on the first shot.

**Voice.** This is the most important button in RimWorld, and nobody talks about it. The raid is coming, my colonists are scattered, and I stop time. Not to escape. To think. While the world is frozen, I give every order I need, and then I let it run.

**Voice.** That button has a name. So does the storyteller that sent the raid, the needs that put one colonist to sleep, and the mood that might make another walk off the job in the middle of the fight. RimWorld is a stack of named parts. So is every other simulation game. This series is about the parts.

## 2. Title (1:01 to 1:11)

**Picture.** Title card over the game-by-mechanic grid, out of focus.

**On screen.** Every simulation game is made of the same parts. Episode 1.

## 3. What a mechanic is (1:11 to 2:48)

**Picture.** RimWorld's mechanics peel off the paused screen as labelled cards and stack in two piles: core and supporting.

**Voice.** In the dataset behind this series, RimWorld breaks into {{derived:rimworld.mechanic_count}} mechanics. A mechanic is a rule-system that owns one kind of state and one rule for changing it. Of those, {{derived:rimworld.core_count}} are core: take any one away and it is a different game.{{assert:derived.rimworld.core_count == 7}}

**On screen.** Storyteller. Needs that decay. Mood breaks. Memories and thoughts. Work priorities. Bodies made of parts. Threat that grows with wealth.

**Voice.** A storyteller picks what happens and when. Needs run down and feed each colonist's mood. Push mood too low and a colonist breaks. Every mood effect is itemized, so you can read why it happened. You rank jobs; colonists choose. Injuries land on body parts. And the richer the colony gets, the bigger the raids.

**Voice.** The rest are supporting: crops, rooms, traits, fire, permanent death, and, near the bottom, the pause button.

**Picture.** Four stamps land on the pause card in turn.

**On screen.** Nameable. Atomic. Tunable. Removable.

**Voice.** To count as a mechanic, a part has to pass four tests. Another designer would recognize it. It does one job. It has levers you can turn. And a game could drop it and still run. The pause button passes all four. Its levers are how many speeds there are, whether you can give orders while paused, which events pause the game for you, and who controls speed in multiplayer.

## 4. The grid (2:48 to 3:56)

**Picture.** The game-by-mechanic grid fills in row by row, oldest game at the top. A counter in the corner ticks up years.

**Voice.** Now do that for every simulation game you can find. The dataset decomposes {{stat:n_game}} games, from {{stat:year_min}} to {{stat:year_max}}, into a shared vocabulary of {{stat:n_mechanic}} mechanics. Each row is a game. Each column is a mechanic. Each mark is one game using one mechanic, dark where it is core.

**On screen.** {{stat:n_game}} games. {{stat:n_mechanic}} mechanics. {{stat:n_uses_edges}} uses.

**Voice.** The average game uses {{stat:mean_mechanics_per_game}} mechanics. Almost every mechanic shows up in more than one game: only {{stat:n_mechanics_single_game}} belong to a single title.{{assert:n_mechanics_single_game <= 5}} When a rule-system exists, it exists because several designers found it worth building.

**Voice.** Read a row and you see one game's recipe. Read a column and you see a mechanic's career: where it started, and where it spread. A few columns are nearly full. Most are nearly empty.

## 5. The most common part (3:56 to 5:26)

**Picture.** One column lights up across the whole grid. The camera pulls back to show it running nearly top to bottom.

**Voice.** The fullest column is not a market or a factory or a model of crowds. It is the pause button. It appears in {{stat:most_prevalent_mechanic_share_pct}} percent of the catalog.{{assert:derived.variable-speed.prevalence_rank == 1}}{{assert:most_prevalent_mechanic_share_pct >= 40}}

**Picture.** A short bar chart builds from the grid: the six most used mechanics.

**Voice.** Next come free placement of buildings and objects, and support for mods.{{assert:derived.free-placement.prevalence_rank == 2}}{{assert:derived.modding-api.prevalence_rank == 3}} Only then do the mechanics that simulate something take over: tech trees, scenario goals, production chains.{{assert:derived.tech-tree.prevalence_rank <= 5}}{{assert:derived.production-chain.prevalence_rank <= 6}} The parts simulation games share most are not about the world being simulated. They are about the player living with it: when it runs, where things go, and who gets to change the rules.

**Picture.** The pause column again, almost all light marks, one dark one.

**Voice.** And the pause is almost never the point. It is core in {{derived:variable-speed.core_count}} of the {{derived:variable-speed.prevalence}} games that have it.{{assert:derived.variable-speed.core_count <= 2}} Nearly universal, almost never central. That is what infrastructure looks like.

**Voice.** It also has costs. Fast-forward runs every other system faster, so when late-game speed stutters, you are watching the simulation hit the limit of the machine. In multiplayer, someone has to decide how fast time goes. The smallest button in the game exposes the cost of everything else.

## 6. Rare parts make the game (5:26 to 6:52)

**Picture.** Back to RimWorld's core cards. Each one flies to its column in the grid, and each column is thin.

**Voice.** If the common parts make a game playable, the rare ones make it itself. RimWorld's storyteller appears in {{derived:storyteller-director.prevalence}} catalog games.{{assert:derived.storyteller-director.prevalence <= 5}} Work priorities in {{derived:work-priorities.prevalence}}. The injury model in {{derived:injury-body-model.prevalence}}. Mood breaks in {{derived:mood-breakdown.prevalence}}.{{assert:derived.work-priorities.prevalence <= 10}}{{assert:derived.injury-body-model.prevalence <= 10}}{{assert:derived.mood-breakdown.prevalence <= 10}} The one exception is needs that decay, which {{derived:needs-decay.prevalence}} games share, going back to Little Computer People in 1985.{{assert:derived.needs-decay.prevalence > 20}}{{assert:derived.needs-decay.earliest_game == little-computer-people}}

**Picture.** Arrows from three of RimWorld's columns back to a single row: Dwarf Fortress, 2006.

**Voice.** In the catalog, three of those rare parts first appear in the same game: Dwarf Fortress. Tabletop and mech games tracked damage by body location long before, but Dwarf Fortress is where the three arrived together in a colony sim.{{assert:derived.mood-breakdown.earliest_game == dwarf-fortress}}{{assert:derived.injury-body-model.earliest_game == dwarf-fortress}}{{assert:derived.adaptive-threat-scaling.earliest_game == dwarf-fortress}} Mood breaks, bodies made of parts, and danger that grows with your wealth. RimWorld did not copy a genre. It took three specific rule-systems and wired them to a storyteller.

**Voice.** That is the pattern this series keeps coming back to. A game's identity lives in a few uncommon parts and how they connect. Its playability lives in many common ones that players expect and rarely notice.

## 7. Six jobs every simulation does (6:52 to 9:13)

**Picture.** A stacked diagram of six layers builds from the bottom: substrate, dynamics, coupling, control, legibility, pacing.

**Voice.** The mechanics also sort into jobs. Every simulation game has to do six things. It has to hold some state: that is the substrate. It has to change that state: dynamics. Its systems have to touch: coupling. The player has to get intent in: control. The player has to see what is going on: legibility. And the game has to decide when the player looks and what a mistake costs: pacing and stakes.

**Picture.** SimCity, 1989. Zoned blocks, power lines, then the land value overlay washing over the map.

**Voice.** SimCity, from 1989, puts its weight on substrate and legibility. Its city is a set of coarse maps, land value, crime, pollution, traffic, recomputed in passes, plus demand for homes, shops, and industry. Its signature move is letting you see those maps. The overlays are not decoration. They are how a player understands a system that is too big to watch.

**Picture.** Factorio. A smelting column feeding belts into assemblers; the camera rides a belt into the factory.

**Voice.** Factorio puts its weight on dynamics and coupling. Ore becomes plates, plates become gears, gears become machines, and every one of those steps is a physical thing on a belt you have to route. Its pollution draws attacks, and the attacks grow as you do. That last part should sound familiar. It is the same mechanic as RimWorld's raids, which grow with the colony's wealth, in a game from a different genre.

**On screen.** Same part, two genres: threat that grows with success.

**Picture.** RimWorld again, the needs tab open on one colonist, thoughts listed with timers.

**Voice.** And RimWorld puts its weight on agents, coupling, and pacing. One colonist eats, sleeps, grieves, and fights, so everything touches everything through that colonist. The storyteller decides when you will be tested. The pause decides when you get to think.

**Picture.** The six-layer stack again, with three bars beside it showing where each game invests.

**Voice.** A compact description of any simulation game is where it invests across these six layers. City builders, factory games, colony sims, flight sims: they differ less in the parts they can choose from than in where they spend.

## 8. What has not been built (9:13 to 10:19)

**Picture.** The grid rearranges into a triangle of every possible pair of mechanics. Most cells are empty.

**Voice.** Here is the last thing the grid shows. {{stat:n_mechanic}} mechanics allow {{stat:n_possible_pairs}} possible pairs. Only {{stat:pair_coverage_pct}} percent of them appear together in even one game in the catalog.{{assert:pair_coverage_pct < 50}} Most combinations of known parts have never been tried.

**Voice.** Some of those gaps make no sense. A flight simulator has no use for free building placement. But some are open lots in a built-up neighbourhood, and later episodes walk through them. Names also sharpen the question everyone is asking about AI: not whether it will change games, but which parts. A language model that writes dialogue changes a different column from a learned physics model. Most of the research is landing on columns that few games use.{{assert:n_top10_prevalent_zero_exposure >= 5}}

## 9. Close (10:19 to 11:29)

**Picture.** A blank grid row with the viewer's cursor over it.

**Voice.** Here is the exercise. Take a simulation game you love and list its parts. Mark the ones it could not live without. Then look up how many other games use each one. I would bet the parts you think of as its signature are rarer than you guess, and the parts you never noticed are among the most common in the field.

**Voice.** And then take away the pause button and ask what breaks first. Usually it is the player.

**On screen.** The dataset, the paper, and every source: sim.yohei.me.

**Voice.** Everything in this video comes from an open dataset. Every number on screen is computed from it, and every claim is checked against it each time it is built. Next episode: most of the vocabulary of simulation games was written before 2000.{{assert:pct_mechanics_seen_by_2000 >= 50}} What happened after?
