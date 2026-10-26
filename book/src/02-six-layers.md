# Chapter 2. Six layers

Zone a block of houses in [[simcity-1989|SimCity]], run a power line to it, and for a while nothing happens. Then small houses appear, then more, and then the block stops growing and the houses nearest the industrial strip begin to empty. The game explains itself with maps. Open the crime map and a red patch sits over the empty houses; open land value and the same area is dark. Crime in SimCity is computed for each cell as 128 minus land value plus population density minus the police effect, held between 0 and 250, and land value falls with distance from the city's center and with the pollution your industry writes into a map of its own [@src-hopkins-2008-micropolis]. The game recomputes these maps in passes, and a zone grows when its local score plus a city-wide demand valve passes a random test.

The six rules in that paragraph do six different jobs. The maps, the zones, and the treasury hold the city's state. The crime formula and the spread of pollution change it. Pollution lowering land value connects one system to another. Painting zones and setting the tax rate take in what the player wants. The maps on screen show the player what the simulation is doing. Disasters and the year-end budget decide when the player has to pay attention and what a mistake costs.

Every simulation game does these six jobs, and nearly every mechanic in the dataset does mostly one of them:

1. **Substrate:** what exists, and how it is stored.
2. **Dynamics:** the rules that change it.
3. **Coupling:** where one system reads or writes another's state.
4. **Control:** how the player's intent gets in.
5. **Legibility:** how the state gets out to the player.
6. **Pacing and stakes:** when the player must look, and what can be lost.

A game's character comes from which layers it spends on.

## Substrate: what exists

A simulation has to store its world somehow, and the choice fixes what the game can afford. Aggregate stocks, such as a treasury or a population count, are cheap and faceless. Individual agents, such as a colonist with needs, are expensive and legible: the player can follow one. Fields on a grid, such as pollution or temperature, cost in proportion to the map's area. Networks of roads, pipes, or friendships cost in proportion to their links. Continuous bodies, such as a wing or a chassis, cost in proportion to contacts and how small the time step is. Each mechanic record names the kinds of state it holds, and a mechanic can hold more than one.

{{table:mechanics-by-substrate}}

The 1989 SimCity stores its citizens as numbers in map cells. [[simcity-2013|SimCity (2013)]] replaced the statistical maps with its GlassBox engine, in which agents carry workers, power, water, and goods between buildings, so that a traffic jam is the visible sum of commuting agents [@src-cifaldi-2012-glassbox-engine]. Players could now follow a single citizen home; chapter 5 describes what they found.

## Dynamics: how it changes

Rules that change state form loops. A reinforcing loop amplifies itself: more citizens pay more taxes, which build more services, which attract more citizens. A balancing loop resists change: more traffic lowers land value, which slows growth, which eases traffic. Each mechanic record names its dominant polarity. Of the {{stat:n_mechanic}} mechanics, {{stat:n_mechanics_feedback_balancing}} are mainly balancing, {{stat:n_mechanics_feedback_reinforcing}} mainly reinforcing, and {{stat:n_mechanics_feedback_both}} run both ways depending on state. The remaining {{stat:n_mechanics_feedback_none}} have no loop of their own: pause buttons, overlays, and the other controls and displays that sit on top of the simulation.{{assert:n_mechanics_feedback_none > n_mechanics_feedback_balancing}}

[[factorio|Factorio]] pairs the two kinds on purpose. Production is the reinforcing loop: more machines make more science packs, research unlocks better machines, and the factory grows. Pollution is the balancing one. Machines emit pollution into chunks of 32 by 32 tiles; a chunk holding more than 15 units passes 2 percent of it to each neighbor every 64 ticks; enemy nests that absorb it send attack groups, and an evolution factor that rises with time, total pollution, and destroyed nests unlocks larger enemies [@src-factoriowiki-2026-pollution; @src-factoriowiki-2026-enemies]. Difficulty in a game like this is the relative strength of the two loops.

A reinforcing loop can also run downhill. A mood break leaves bad memories in the agents who witness it, which lowers their mood and raises their own chance of breaking, so in a colony sim one bad raid can start a slide that ends the colony.

## Coupling: how systems touch

A game can have many systems and still feel thin if they never touch. Systems couple through shared stocks, shared space, and shared agents.

Shared stocks are the simplest. Factorio's power grid connects every machine, and when generation falls short the grid shares power evenly, so every machine in the factory slows by the same proportion [@src-factoriowiki-2026-electric-system]. Shared space works through neighbors: in SimCity, industry lowers the land value of the houses beside it. Shared agents work through bodies and minds: in RimWorld the same cook hauls, eats, grieves, and fights, so a death in a raid reaches the kitchen.

[[oxygen-not-included|Oxygen Not Included]] couples much of its world through one rule for heat. Every tile in its asteroid holds one element with a mass and a temperature, and every 0.2 seconds each tile exchanges heat with its neighbors by conduction [@src-oxygennotincludedwiki-2026-thermal-conductivity]. Insulation, melting, boiling, and machines that overheat all follow from that rule rather than from scripts written for each building. Machines also emit what they do not use: a natural gas generator makes 800 watts and, with them, polluted water and carbon dioxide [@src-oniwiki-2026-natural-gas-generator]. The long game is closing those loops so that one machine's waste becomes another's input.

[[dwarf-fortress|Dwarf Fortress]] is the catalog's largest decomposition, at {{derived:dwarf-fortress.mechanic_count}} mechanics,{{assert:game_most_mechanics == dwarf-fortress}} and its parts are coupled tightly. A dwarf seized by a strange mood takes over a workshop to make a named artifact and goes insane if the materials are missing, which turns the production system into a source of stories.

## Control: how intent enters

The player can act directly through an avatar or a unit, place and zone, set parameters such as a tax rate, issue orders that agents pick up, write programs, or speak. Each step away from direct action widens what this book calls the control gap: the designed distance between what the player wants and what happens. A gap too narrow and the game is a toy; too wide and the player is a spectator.

{{table:games-by-agency}}

[[the-sims|The Sims]] sets its gap deliberately. Sims with free will choose their own actions among what the objects around them offer, but paying bills, finding a job, exercising, and having children need explicit commands, so the player alternates between architect and caretaker [@src-wikipedia-the-sims]. [[spacechem|SpaceChem]] sits at the other extreme. The player programs two mechanical arms in a reactor ten cells wide and eight tall to grab, bond, and rotate atoms into molecules; execution is deterministic and visible, so a program either meets its quota or collides, and a finished solution is plotted against every other player's on histograms of cycles, reactors, and instructions [@src-wikipedia-spacechem].

## Legibility: how the state gets out

A simulation the player cannot read plays as noise. Simulation games answer with a family of mechanics that own no simulation state at all: overlays, inspectors, tooltips, dashboards, alerts, advisors, forecasts. SimCity's maps are one. RimWorld's itemized thoughts, from chapter 1, are another. Paradox's grand strategy games nest tooltips: hover over a number and it breaks into labeled modifiers, each of which can be hovered in turn, until every value decomposes into causes [@src-pcgamesn-2022-victoria-3-nested-tooltips].

The catalog undercounts this layer. Data overlays are tagged in only {{derived:data-overlays.prevalence}} catalog games, yet the mechanic's own definition names the info views of [[cities-skylines|Cities: Skylines]], and the Cities: Skylines record does not tag them. The dataset's records were written game by game, and interface mechanics were the easiest to leave out.

## Pacing and stakes: when to look and what is lost

The time model sets the basic rhythm: real time with a pause is the most common, ahead of pure real time and turns. Other mechanics shape attention within it.

A crisis countdown announces a future disaster and lets the remaining time structure the play. Temperature in [[frostpunk|Frostpunk]] falls on a schedule toward the Great Storm, which the main scenario must outlast; in [[plague-inc|Plague Inc.]] the world's cure research climbs as a percentage, and the game ends when it completes [@src-wikipedia-frostpunk; @src-wikipedia-plague-inc]. The countdown is core in {{derived:crisis-countdown.core_count}} catalog games.{{assert:derived.crisis-countdown.core_count >= 5}}

A real-time clock ties the game to the calendar. [[tamagotchi|Tamagotchi]], in 1996, aged its pet through life stages in real time, and Animal Crossing follows the console's clock, so shops close at night and holidays arrive on their real dates; players who change the console clock to skip a wait call it time travel [@src-wikipedia-tamagotchi; @src-wikipedia-animal-crossing].{{assert:derived.real-time-clock.earliest_game == tamagotchi}} A daily action budget makes the day itself scarce. [[stardew-valley|Stardew Valley]] gives the farmer 270 energy, charges it for each swing of a tool, and makes the farmer pass out at 2 a.m., which away from home costs a tenth of the farmer's gold, up to 1,000 [@src-stardewvalleywiki-2026-energy].

Stakes come from the failure model. About half of catalog games let the player recover from a setback; fewer restart from scratch, and a smaller group, RimWorld and Dwarf Fortress among them, can collapse in a cascade where one failure causes the next.{{assert:field.dwarf-fortress.failure_model == cascading-collapse}}{{assert:field.rimworld.failure_model == cascading-collapse}}

## Where genres spend

The dataset does not tag layers directly. The closest measure is which families of mechanics a subgenre's games use most, since most families sit mainly in one layer. The table lists, for each subgenre with enough games, the three families that take the largest share of its games' mechanic uses.

{{table:subgenre-spend}}

Life sims put about a third of their uses into agents and behavior and about a sixth into social relations.{{assert:top_family_life_sim == agents-behavior}}{{assert:top_family_pct_life_sim >= 30}} Colony sims also lead with agents, but resources and construction come next, because a colony has to feed and house itself.{{assert:top_family_colony_sim == agents-behavior}} Factory games lead with resources and production, followed by the logistics that move it.{{assert:top_family_factory_automation == resources-production}} Programming games lead with control.{{assert:top_family_programming_sim == control-automation}} Vehicle sims lead with progression and goals, ahead of the physics: careers, licenses, and missions are wrapped around the driving and flying.{{assert:top_family_vehicle_sim == progression-goals}} And the AI-native titles lead with social relations, the family where conversation with a language model lands.{{assert:top_family_ai_native == social-relations}}

City builders spread their uses most evenly. No family takes more than about one use in six, and construction, production, and economy take nearly equal shares.{{assert:top_family_pct_city_builder <= 17}}

## Exercise: profile a game by layer

Take the game you decomposed in chapter 1.

1. Assign each of its mechanics to the layer where it does most of its work.
2. Count the mechanics per layer. Note which layer has the most and which has none.
3. For the layer with the most, name one coupling: a place where a mechanic there reads or writes another mechanic's state.
4. For the thinnest layer, add one mechanic from another game in the catalog and describe what changes for the player.

Most of the mechanics in this chapter are old. SimCity's maps date from 1989, Tamagotchi's clock from 1996, and The Sims' objects that advertise what they offer from 2000. Chapter 3 dates every mechanic in the vocabulary by the first catalog game that uses it, and tests how much of the old vocabulary was invented early and how much is simply shared.
