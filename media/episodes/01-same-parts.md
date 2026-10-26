# Episode 1. Every simulation game is made of the same parts

Target runtime about 9 minutes: about 890 words of narration at 135 words a minute, plus a beat of picture-only footage per scene. Covers book chapters 1 and 2. Footage: RimWorld, Dwarf Fortress, SimCity (1989), Factorio, Oxygen Not Included, The Sims, Frostpunk, all captured by us; a still of Façade. Publisher video policies are tracked in `media/rights.yaml` and must be checked before release. Every number below is filled in from the dataset when the script is built, and the sentences that interpret numbers carry the same checks as the book.

## 1. Cold open (0:00 to 0:52)

**Picture.** RimWorld, a small colony at dusk. A raid letter. A short fight at the door; one colonist falls. Cut to three days later: the cook drops her work and walks out into the fields. The player clicks her. The needs tab fills the screen, every mood effect a line with a number and a timer.

**Voice.** Three days after the raid, the cook walks off the job. Click on her and RimWorld tells you why, line by line. Her son died in the fight: minus twenty, for thirty days. The fine meal that was holding her up has worn off. Her mood has been under the break line since the funeral, and today the game rolled the dice [@src-rimworldwiki-2026-thoughts; @src-rimworldwiki-2026-mental-break].

**Voice.** Nobody scripted that. Five separate rules made it happen, and every simulation game is built out of rules like them.

## 2. Title (0:52 to 1:02)

**Picture.** Title card over the game-by-mechanic grid, out of focus.

**On screen.** Every simulation game is made of the same parts. Episode 1.

## 3. RimWorld, in parts (1:02 to 2:24)

**Picture.** The paused colony. RimWorld's core mechanics peel off the screen as labelled cards: storyteller, needs, mood breaks, memories, work priorities, injuries by body part, threat that grows with wealth.

**Voice.** We've broken {{stat:n_game}} simulation games into their parts. RimWorld comes apart into {{derived:rimworld.mechanic_count}} of them, and {{derived:rimworld.core_count}} are core, meaning it would be a different game without them.{{assert:derived.rimworld.core_count == 7}}

**Voice.** The storyteller picks the raid, and spends a threat budget that grows with your wealth. Needs run down and feed mood. Every mood effect is written into memory with a value and an expiry. Mood below a threshold rolls for a breakdown. Bodies are trees of parts that bleed and scar. You rank the jobs, and colonists pick their own work.

**Picture.** Four stamps land on the storyteller card.

**On screen.** Nameable. One job. Tunable. Removable.

**Voice.** A part only counts if it passes four tests. Another designer would recognize it. It does one job. It has levers. And a game could drop it and still run. The storyteller passes: Left 4 Dead's director is the same idea, its levers are the event list and the length of the quiet stretches, and Dwarf Fortress runs without one [@src-booth-2009-ai-systems-l4d].

## 4. Rare parts (2:24 to 3:25)

**Picture.** Each core card flies to its column in the grid. Most columns are thin.

**Voice.** Now look at how many other games use each part. The storyteller is in {{derived:storyteller-director.prevalence}} catalog games. Mood breaks in {{derived:mood-breakdown.prevalence}}. Injuries by body part in {{derived:injury-body-model.prevalence}}.{{assert:derived.storyteller-director.prevalence <= 5}}{{assert:derived.mood-breakdown.prevalence <= 10}}{{assert:derived.injury-body-model.prevalence <= 10}} Only needs that decay are common, shared by {{derived:needs-decay.prevalence}} games going back to Little Computer People in 1985.{{assert:derived.needs-decay.prevalence > 20}}{{assert:derived.needs-decay.earliest_game == little-computer-people}}

**Picture.** Arrows from three columns back to one row: Dwarf Fortress, 2006. Then a still of Façade: two characters at a dinner party.

**Voice.** Three of those rare parts first show up in the catalog in one game, Dwarf Fortress, in 2006: mood breaks, bodies made of parts, and danger that grows with wealth.{{assert:derived.mood-breakdown.earliest_game == dwarf-fortress}}{{assert:derived.injury-body-model.earliest_game == dwarf-fortress}}{{assert:derived.adaptive-threat-scaling.earliest_game == dwarf-fortress}} The earliest storyteller in the catalog comes from Façade, a 2005 interactive drama where a drama manager steers an argument between a married couple toward one of three endings.{{assert:derived.storyteller-director.earliest_game == facade}}

## 5. The grid (3:25 to 4:10)

**Picture.** The game-by-mechanic grid fills in row by row, oldest game at the top, a year counter ticking in the corner.

**Voice.** Do that for every game in the catalog. {{stat:n_game}} games, from {{stat:year_min}} to {{stat:year_max}}, broken into a shared vocabulary of {{stat:n_mechanic}} mechanics. Each row is a game. Each column is a mechanic. A dark mark means the part is core.

**On screen.** {{stat:n_game}} games. {{stat:n_mechanic}} mechanics. {{stat:n_uses_edges}} uses.

**Voice.** The average game uses about {{stat:mean_mechanics_per_game}} parts. Only {{stat:n_mechanics_single_game}} mechanics belong to a single game, so almost everything in the vocabulary was worth building more than once.{{assert:n_mechanics_single_game <= 5}}

## 6. The most common parts (4:10 to 5:02)

**Picture.** The grid narrows to its fullest columns. Five light up in turn, each over a two-second clip: a paused raid, a building dropped on a lot, a mod list, a research screen, a scenario goal. Then a sixth: ore riding a belt into a furnace.

**Voice.** The five most common parts are the pause button, placing buildings, mod support, a tech tree, and scenario goals.{{assert:derived.variable-speed.prevalence_rank == 1}}{{assert:derived.free-placement.prevalence_rank == 2}}{{assert:derived.modding-api.prevalence_rank == 3}}{{assert:derived.tech-tree.prevalence_rank <= 5}}{{assert:derived.scenario-objectives.prevalence_rank <= 5}} None of them simulates anything. They handle the player: when the world runs, where things go, who can change the rules. Production chains come sixth, the first part on the list that models something in the world.{{assert:derived.production-chain.prevalence_rank == 6}}

**Voice.** The pause button is in {{stat:most_prevalent_mechanic_share_pct}} percent of catalog games, and core in exactly one: Universe Sandbox, where running a solar system faster can change how it ends.{{assert:derived.variable-speed.core_count == 1}}

## 7. Where identity lives (5:02 to 5:37)

**Picture.** Two histograms build side by side: the parts games call core, and the parts they call supporting, by how many games use each.

**Voice.** RimWorld's pattern holds across the catalog. The parts a game calls core are used by a median of {{stat:median_prevalence_core_uses}} catalog games. The parts it calls supporting, by {{stat:median_prevalence_supporting_uses}}.{{assert:median_prevalence_core_uses < median_prevalence_supporting_uses}} And {{stat:pct_games_with_rare_core}} percent of games have at least one core part that no more than {{stat:rare_max_games}} games share.{{assert:pct_games_with_rare_core >= 75}}

## 8. Six jobs (5:37 to 7:19)

**Picture.** SimCity, 1989. A block of houses stalls next to an industrial strip. The crime map washes over it, then land value.

**Voice.** The parts also do different jobs. In SimCity, crime in each cell is a formula: 128, minus land value, plus density, minus police [@src-hopkins-2008-micropolis]. The maps hold the city's state. The formulas change it. Pollution dragging down land value connects one system to another. Zoning brings in what you want. The overlays show you what is going on. And disasters and the yearly budget decide when you have to pay attention.

**On screen.** Substrate. Dynamics. Coupling. Control. Legibility. Pacing and stakes.

**Picture.** Factorio: a factory grows; a pollution cloud spreads chunk by chunk; biters leave their nests.

**Voice.** Factorio runs two loops against each other. Production feeds itself: more machines, more research, more machines. Pollution pushes back. It spreads from chunk to chunk, the nests that soak it up send attacks, and the enemies evolve as your total pollution climbs [@src-factoriowiki-2026-pollution; @src-factoriowiki-2026-enemies].

**Picture.** Oxygen Not Included: a temperature overlay; heat creeps out of a generator room into the base.

**Voice.** Oxygen Not Included couples almost everything through one rule. Every tile holds an element with a mass and a temperature, and every fifth of a second it trades heat with its neighbours [@src-oxygennotincludedwiki-2026-thermal-conductivity]. Insulation, boiling, and overheating machines all fall out of that.

**Picture.** The Sims: a Sim heads to the fridge on its own; the bills sit unpaid until the player clicks.

**Voice.** The Sims chooses where your control stops. Sims feed themselves, but paying bills and finding a job need you [@src-wikipedia-the-sims]. Frostpunk shows pacing: the temperature falls on a schedule toward a storm you know is coming [@src-wikipedia-frostpunk].

## 9. Where genres spend (7:19 to 8:12)

**Picture.** A table builds row by row: each subgenre, and the three families of parts it uses most.

**Voice.** Count where each genre spends its parts and the genres separate. Life sims put about a third into agents and behavior.{{assert:top_family_life_sim == agents-behavior}}{{assert:top_family_pct_life_sim >= 30}} Factory games lead with production.{{assert:top_family_factory_automation == resources-production}} Programming games lead with control.{{assert:top_family_programming_sim == control-automation}} Vehicle sims lead with careers and missions, ahead of the physics.{{assert:top_family_vehicle_sim == progression-goals}} And the AI-native games, the ones built on language models, lead with social relations.{{assert:top_family_ai_native == social-relations}}

**Voice.** Most combinations of these parts have never been tried. Of the {{stat:n_possible_pairs}} possible pairs of mechanics, {{stat:pair_coverage_pct}} percent have ever shared a game.{{assert:pair_coverage_pct < 50}} Later episodes go looking in the gaps.

## 10. Close (8:12 to 9:00)

**Picture.** A blank grid row with a cursor over it.

**Voice.** Try it on a game you love. List its parts, mark the ones it couldn't live without, and look up how many other games use each one. The ones that make it special will probably be rare.

**On screen.** The dataset, the paper, and every source: sim.yohei.me.

**Voice.** Everything in this video comes from an open dataset, and every number on screen is checked against it each time it's built. Next episode: where these parts came from, and how few games invented most of them.
