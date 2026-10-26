# The film: Every Simulation Game Is Built From the Same Parts

One long cut of the twelve episodes, released with the book's first edition so the two point at each other. It is assembled from finished episodes plus three new pieces, so it costs editing time and no new production. Every episode stays up on its own.

## Assembly

- Each episode's title card is cut; the film has one title, after the opening.
- Each episode's closing scene is cut except episode 12's, which ends the film. Lines that point to the next episode go with them.
- Cold opens stay. Each one starts a chapter of the film on a moment in a game.
- The three new pieces below open the film and join its acts. Their numbers are filled from the dataset like the episodes', so the film's edition names one dataset version.
- Runtime is about 2 hours 15 minutes: the episodes' 140 minutes, less about 10 minutes of title cards and closes, plus about 5 minutes of new material.

| Act | Episodes | Bridge before it |
|---|---|---|
| I. The grammar | 1 to 5 | Opening |
| II. The machines arrive | 6 to 8 | Bridge one |
| III. Bets and checks | 9 to 12 | Bridge two |

## YouTube chapters

Recompute these from the episode timings when an episode changes; the times below are from this draft.

| Start | Chapter |
|---|---|
| 0:00 | Opening |
| 2:00 | 1. Every simulation game is made of the same parts |
| 10:02 | 2. Where the parts came from |
| 21:11 | 3. Families across genres |
| 32:10 | 4. Why deep systems are hard to read |
| 42:43 | 5. The five ceilings |
| 53:20 | Bridge: the machines arrive |
| 54:50 | 6. What AI shipped |
| 1:07:38 | 7. Where AI lands |
| 1:19:17 | 8. Vacant lots |
| 1:30:52 | Bridge: from gaps to bets |
| 1:32:07 | 9. Bets worth making |
| 1:43:28 | 10. What breaks |
| 1:53:31 | 11. Keeping score |
| 2:04:11 | 12. How this was made |

## 1. Opening (0:00 to 2:00)

**Picture.** A teletype prints a line of text in 1968: the steward's yearly report on a city's grain. The camera pulls back as the line becomes the first row of the catalog grid, and rows pour in beneath it, one per game, a year counter running in the corner up to {{stat:year_max}}.

**Voice.** In 1968, a program asked its player how many bushels of grain to feed the people. The dataset behind this film starts there and runs to this year: {{stat:n_game}} simulation games, broken into {{stat:n_mechanic}} named parts, every one with its sources.

**Picture.** The grid's five fullest columns light up, then RimWorld's row with its core columns, each nearly empty.

**Voice.** The five parts that turn up most often in those games model nothing in the world: a pause button, building placement, mod support, a tech tree, and scenario goals.{{assert:derived.variable-speed.prevalence_rank == 1}}{{assert:derived.free-placement.prevalence_rank == 2}}{{assert:derived.modding-api.prevalence_rank == 3}}{{assert:derived.tech-tree.prevalence_rank <= 5}}{{assert:derived.scenario-objectives.prevalence_rank <= 5}} The parts a game is known for are usually rare.{{assert:pct_games_with_rare_core >= 75}}

**Picture.** The technique-flow ribbons draw in from the right and land on a handful of columns; most of the grid stays unlit.

**Voice.** Research on AI in games lands on a few of those columns. {{stat:n_mechanics_zero_exposure}} mechanics, carrying {{stat:pct_uses_on_zero_exposure}} percent of every use in the catalog, have no technique in the dataset aimed at them, and the production chains and budgets that most simulation games run on are among them.{{assert:pct_uses_on_zero_exposure >= 40}}{{assert:derived.production-chain.technique_exposure == 0}}{{assert:derived.budget-treasury.technique_exposure == 0}}

**Picture.** A calendar strip scrolls forward; dates light up one by one, the first group bunched on a single day.

**Voice.** The dataset also makes {{stat:n_predictions}} bets about what comes next, each with a date on which it can be wrong. The first {{stat:n_predictions_first_date}} come due on {{stat:first_prediction_resolves}}.{{assert:n_predictions_open == n_predictions}}

**On screen.** Every Simulation Game Is Built From the Same Parts.

## 2. Bridge: the machines arrive (between episodes 5 and 6, about 1:30)

**Picture.** The five ceilings from episode 5 as five horizontal lines across the screen. Dots appear on a timeline beneath them, one per technique, each rising to the ceiling it presses on and colored by how far it has shipped.

**Voice.** Each of those ceilings has techniques pressing on it. The dataset records {{count:technique}} of them, each a dated result that changes at least one mechanic, and {{stat:n_technique_since_2023}} are dated 2023 or later.{{assert:n_technique_since_2023 > 20}} Language models, asset generators, and learned motion press on authoring cost. Neural rendering and learned surrogates for physics and weather press on compute. Language-model characters press on believability.

**Picture.** The determinism line darkens as a cluster of dots pushes down on it from above.

**Voice.** Determinism is the ceiling they mostly push the other way. Of the techniques that can run during play, {{stat:n_technique_runtime_breaks}} break reproducibility outright.{{assert:n_technique_runtime_breaks >= 5}}

**On screen.** {{count:technique}} techniques. Shipped in a game: {{stat:n_technique_shipped}}. A norm in shipped games: {{stat:n_technique_shipped_mainstream}}.

**Voice.** {{stat:n_technique_shipped}} have shipped in at least one game, and one has become a norm.{{assert:n_technique_shipped_mainstream == 1}} In 2019 a text adventure put a language model where the rules engine should be.

## 3. Bridge: from gaps to bets (between episodes 8 and 9, about 1:15)

**Picture.** The vacant-lots plan on the left half of the screen, the technique-flow ribbons on the right. Lines from both run to the middle and become the rows of one table.

**Voice.** The empty lots and the techniques meet in one list: {{count:opportunity}} bets, each a design that combines mechanics the catalog already has with a technique the dataset records. Each names the games that partly do it already, an experiment a small team could run, and a prediction with a date. By the dataset's reading, {{stat:n_opportunity_horizon_now}} could be built now.{{assert:n_opportunity_horizon_now >= 10}}

**Picture.** The table sorts itself by priority; the top rows glow, then every row's status cell reads "open".

**Voice.** None of them has been tested, and none of the predictions has come due.{{assert:n_predictions_open == n_predictions}} The first one starts with a factory that has stopped, and a player who can't tell why.
