# Episode 8. Vacant lots

Target runtime about 12 minutes: about 1,290 words of narration at 135 words a minute, plus a beat of picture-only footage per scene. Covers book chapter 9. Footage: Cities: Skylines, Surviving Mars, SimCity (1989), Football Manager, SpaceChem, Factorio, Spore, Besiege, Banished, Captain of Industry, Workers & Resources: Soviet Republic, Crusader Kings III, Stellaris, Prison Architect, Kenshi, Against the Storm, Kerbal Space Program, all captured by us. Publisher video policies are tracked in `media/rights.yaml` and must be checked before release. Every number below is filled in from the dataset when the script is built, and the sentences that interpret numbers carry the same checks as the book.

## 1. Cold open (0:00 to 0:37)

**Picture.** Cities: Skylines. A tidy riverside district, built all at once. Time-lapse: decades pass. Hearses queue down the main road; skull icons float over house after house.

**Voice.** Everyone in this district moved in the same year. So they grew old the same year, and now they're dying the same week, faster than the hearses can collect them. Cities: Skylines shows you a deathcare problem. It has no way to show you a story about any of them.

## 2. Title (0:37 to 0:47)

**Picture.** Title card over the queue of hearses.

**On screen.** Vacant lots. Episode 8.

## 3. The missing story (0:47 to 2:13)

**Picture.** Two columns of game covers. On the left, games with building placement; it's long. On the right, games with triggered event chains; it's short. One cover slides into the middle: Surviving Mars.

**On screen.** Building placement: {{derived:free-placement.prevalence}} games. Event chains: {{derived:triggered-event-chains.prevalence}} games. Both: 1.

**Voice.** Placing buildings is in {{derived:free-placement.prevalence}} catalog games. Event chains, the machinery that lets Crusader Kings III follow a rival's illness with a succession crisis and then a war, are in {{derived:triggered-event-chains.prevalence}}. If the two were spread across games at random, several games would have both. One does: Surviving Mars, whose Mysteries lay authored storylines like plagues and AI revolts over a colony you build by hand.{{assert:cooccur.free-placement.triggered-event-chains == 1}}{{assert:rank.whitespace.free-placement.triggered-event-chains == 1}} Even there, the stories are about the colony as a whole, and nothing ties them to where a building stands. Picture the other version: a tavern built next to the temple, or a mill whose pond floods a farmer's field, firing a short event about the people it affects, with a choice and a consequence the game keeps track of. Frostpunk, Manor Lords, and Islanders each do a piece of it.

**Voice.** This episode is about pairs like that: two mechanics, each common, from different corners of the design, that almost never share a game.

## 4. Packages (2:13 to 3:34)

**Picture.** SimCity (1989). The land value overlay, then the traffic overlay, toggled back and forth over the same streets. Cut to Football Manager: a match engine highlight, then a board confidence screen.

**Voice.** Start with the opposite: pairs that turn up together far more often than chance. The strongest come in packages, inherited down a lineage. Sports management carries a match engine, a board that rates the manager, and contract talks.{{assert:rank.cooccurrence-top.attribute-match-engine.board-confidence <= 10}} Grand strategy carries war score and religious conversion.{{assert:rank.cooccurrence-top.culture-religion-conversion.war-score-peace <= 10}} City builders carry SimCity's land value and traffic.{{assert:rank.cooccurrence-top.land-value.traffic-congestion <= 15}} Flight sims pair aerodynamics with cockpit checklists. Online worlds pair a shared, persistent world with player-run corporations and guilds. The Sims pairs what a Sim wants with objects that advertise what they offer.{{assert:rank.cooccurrence-top.flight-aerodynamics.procedural-checklists <= 30}}{{assert:rank.cooccurrence-top.persistent-world.player-organizations <= 30}}{{assert:rank.cooccurrence-top.aspiration-wants.smart-objects <= 10}}

**Voice.** Packages hold together because each part makes the other matter. In SimCity, a block's value falls with pollution and crime and distance from the centre, and traffic writes pollution into the same map. So your road plan changes what the land is worth, and the land decides where the city grows next. Take either one away and the other loses its point.

## 5. The lots (3:34 to 5:21)

**Picture.** The vacant-lots figure builds: mechanic names down a staircase, lots filling in where rows meet columns. Dark lots, dashed lots, a few slashed ones.

**Voice.** The dataset looks for the opposite on purpose. It takes mechanics that each appear in at least {{stat:whitespace_min_games}} games, pairs them across different families, leaves out time controls, and leaves out pairs already recorded as being in tension. Then it keeps the pairs that share one game or none. {{stat:n_whitespace_pairs}} pairs pass.{{assert:n_whitespace_pairs >= 100}} The bar of {{stat:whitespace_min_games}} games was 8 percent of the catalog when it was set, and it's written down to be revisited as the catalog grows.

**Voice.** The tension list is worth hearing, because it's what designers already know about pairs that fight. Threat that grows with your wealth pulls against unlocks that reward growth. Characters with strong free will resist direct orders. Full-information overlays undercut fog of war. A shared online world can't be paused by one player. Generated content resists the authored conditions that event chains depend on. Those pairs are left out on purpose. What's left is emptiness without an explanation on record.

**Voice.** The chance baseline has a known weakness. It treats each mechanic as spread across games regardless of how many mechanics a game has, so pairs whose mechanics live in small games can look emptier than they are. A stricter baseline would shorten the list. Treat it as a list of candidates.

## 6. Workers who grow old (5:21 to 6:29)

**Picture.** Banished: a village in winter, a family's house, a child who grows into a worker across a time-lapse. Then Captain of Industry and Workers & Resources: trucks, conveyors, smelters, and no faces.

**Voice.** Aging lives in {{derived:lifecycle-aging.prevalence}} games. Production chains live in {{derived:production-chain.prevalence}}. No catalog game has both.{{assert:cooccur.lifecycle-aging.production-chain == 0}} Banished comes closest from one side: every worker was born in the town, ages, and dies, so a decision you made years ago shows up as a labour shortage today. But its families gather, farm, and stockpile without anything the dataset records as a production chain. From the other side, Captain of Industry and Workers & Resources run deep industrial economies whose workers never age or retire.

**Voice.** Put them together and a factory's bottleneck could be a missing mentor as easily as a missing machine. The demographic wave that fills Cities: Skylines with hearses would show up, years later, as a production line running short-handed.

## 7. Shared designs (6:29 to 7:31)

**Picture.** SpaceChem: a solution finishes, and three histograms rise showing where it ranks against everyone else's. Factorio: a player copies a blueprint string out of the game. Spore: a creature browser, thousands of player-made animals.

**Voice.** Content sharing, where players upload what they build and others browse, rate, and import it, is in {{derived:content-sharing.prevalence}} games, mostly sandboxes, life sims, and contraption builders. The one production game with it is SpaceChem, which plots your solution against everyone else's.{{assert:cooccur.content-sharing.production-chain == 1}} Factorio players do trade layouts, as blueprint strings pasted between games, and the dataset files that under blueprints. What no production game has built is the shared catalog that Spore made for creatures: a place where a factory layout is published, remixed, and ranked. Part of a lot's emptiness can come from where the vocabulary draws its lines, and this is one of those cases.

## 8. Research by people (7:31 to 8:29)

**Picture.** Crusader Kings III: a court screen full of faces and opinions. Stellaris: three research cards, each with a scientist's portrait and traits.

**Voice.** Tech trees are in {{derived:tech-tree.prevalence}} games. Relationships between named characters are in {{derived:relationship-values.prevalence}}. They share exactly one, Crusader Kings III.{{assert:cooccur.relationship-values.tech-tree == 1}} Stellaris gets partway: its research cards are weighted by the traits of the scientist leading each field. Game Dev Tycoon hires designers and programmers with their own stats, but its research points come from a separate pool. Everywhere else, research is a currency you spend on a graph. Run it through a few named scientists who collaborate, compete, and hold grudges, who publish, poach each other, and defect to rivals, and breakthroughs become events with names attached.

## 9. Lots already built (8:29 to 9:39)

**Picture.** Prison Architect: a guard walks past a generator room; a shared prison downloads; an Escape Mode prisoner slips out. Kenshi: a squad member with a missing arm hauls ore. Against the Storm: a new map unfolds for a new settlement.

**Voice.** Some games already stand on lots nobody else has built. Prison Architect is the only catalog game that hires staff one by one and also wires a power grid, and the only one that pairs a budget with shared player creations: you can download someone's prison and try to break out of it.{{assert:cooccur.staff-hiring.power-grid == 1}}{{assert:cooccur.budget-treasury.content-sharing == 1}} Kenshi is the only one where production chains meet permanent death.{{assert:cooccur.permadeath.production-chain == 1}} Against the Storm is the only one that sets scenario goals on generated maps: each settlement is a new map, won by filling a reputation gauge before the Queen's patience runs out.{{assert:cooccur.procedural-terrain.scenario-objectives == 1}} A lot with one building on it still counts as vacant here, and it might be the more useful kind, because somebody has already shown it can stand.

## 10. Lots that might stay empty (9:39 to 10:49)

**Picture.** Kerbal Space Program: a rocket assembled part by part in the hangar, then flown by hand off the pad.

**Voice.** Not every vacant lot deserves a building. Hands-on skill, like flying and driving, and placing buildings share no game at all.{{assert:cooccur.embodied-skill-control.free-placement == 0}} Most flight and racing sims have no use for a town. The lot next door is built: Kerbal Space Program and Besiege have you assemble a machine from parts and then fly or drive it yourself.{{assert:cooccur.modular-assembly.embodied-skill-control >= 3}} What nobody has made is the version where you build the place, the track or the airfield, and then drive it.

**Voice.** Other empty pairs are two lineages that haven't met. Permanent death lives in colony sims, survival games, and virtual pets; scenario goals live in tycoon, management, and puzzle games; the two never share a game.{{assert:cooccur.permadeath.scenario-objectives == 0}} A city treasury and growing crops never share one either.{{assert:cooccur.budget-treasury.crop-cultivation == 0}}

## 11. How a lot closes (10:49 to 11:59)

**Picture.** A pull request on screen adding one game record. The build reruns; a sentence in the book turns red; it's rewritten.

**Voice.** The catalog is a sample. It leans toward games well documented in English, and a game outside it may already combine any of these pairs. That's the cheapest way to close a lot: add the game, with its sources. The table recomputes, and any sentence in this series that depended on the gap fails its check until someone rewrites it.

**Voice.** And a lot is worth building when the two mechanics change each other. Traffic and land value do, in SimCity. Placement and events would, if the events changed what you build next. Aging and production would, if the age of the workforce set the factory's output years later. Two mechanics that never touch each other's state just put two games on one menu.

## 12. Close (11:59 to 12:26)

**Picture.** The vacant-lots plan again, a handful of dashed lots outlined in colour.

**Voice.** Next episode turns the largest gaps, the missing techniques, and the five ceilings into {{count:opportunity}} bets, each with an experiment and a prediction with a date on it.

**On screen.** The dataset, the sources, and the book: sim.yohei.me
