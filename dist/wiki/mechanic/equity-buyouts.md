# Equity and buyouts

*Mechanic* · `equity-buyouts` · status: **sourced**

Companies issue shares whose price tracks performance, and players buy them for profit or accumulate a majority to take control of rivals.

| field | value |
|---|---|
| aliases | stock market, shares, hostile takeover |
| family | Economy & finance |
| substrate | Aggregate stocks, Rule system |
| math basis | Game theory, Mechanism design / auctions |
| feedback | Reinforcing (positive) |
| player interface | Orders, Parameter |
| legibility | 3 |
| emergence potential | 3 |
| authoring cost | 1 |
| compute cost | 1 |
| tuning difficulty | 4 |
| ai leverage | 2 |
| maturity | Established |
| core count *(computed)* | 2 |
| earliest game *(computed)* | [Railroad Tycoon](../game/railroad-tycoon.md) |
| earliest year *(computed)* | 1990 |
| prevalence *(computed)* | 4 |
| prevalence share *(computed)* | 0.023 |
| subgenre spread *(computed)* | 2 |
| technique count *(computed)* | 0 |
| technique exposure *(computed)* | 0.0 |

## Definition

Owns each company's share count, share price, and ownership table. Share price is recomputed from company value (cash, assets, earnings, debt) and moved by trading pressure, so purchases raise it and sales lower it. Players buy and sell shares in their own and rival companies for dividends or gains. Crossing an ownership threshold, usually a majority, transfers control: the target is merged, its assets absorbed, or its owner eliminated. Railroad Tycoon (1990) starts each railroad with $1 million split between equity and a loan and lets players trade shares in themselves and rivals in a miniature stock market. Offworld Trading Company (2016) makes buyouts the win condition: a player who loses majority control of their own company is eliminated, and the game warns a player when a rival can afford to buy them out without telling the rival. Capitalism (1995) makes being bought out by a competitor a loss, and Transport Tycoon sells rival company shares in 25% blocks.

## Player Experience

Reading a rival's balance sheet as a target. The player buys a rival's stock while it is cheap, defends their own float by buying back shares, and feels dread when a competitor's cash nears the price of a takeover. Endgames become races to accumulate cash.

## Design Levers

- share price formula (book value, earnings multiple, dividend yield, recent trading pressure)
- price impact per share bought or sold
- control thresholds and their consequences (merger, elimination, board control)
- restrictions on buying, such as minimum company age or share blocks
- dividends and buybacks as defensive tools
- visibility of who owns what and warnings before a takeover

## Failure Modes

- A leading player can buy out weaker rivals early, ending the game before economic play matters.
- AI companies that do not defend their float become free takeover targets.
- Share prices driven only by book value can be gamed by moving cash into assets before a buyout.

## Dynamics

- Owning shares of rivals turns their success into the player's dividends, softening competition into partial alliance.
- Late-game cash races emerge as players hoard money for buyouts instead of investing in production.
- Buying back one's own stock converts operating profit into takeover defense, starving expansion.

## Open Questions

- Can learned or LLM-driven investor agents produce believable sentiment (bubbles, panics) without a hand-tuned price formula?
- What takeover thresholds keep buyouts a threat without ending multiplayer games early?

## Relations

**synergy**

- [Rival firms](../mechanic/rival-firms.md): Buyouts give competition a decisive end state (Offworld Trading Company, Capitalism).

## Backlinks (computed)

**used by:** [Capitalism](../game/capitalism.md), [Offworld Trading Company](../game/offworld-trading-company.md), [Railroad Tycoon](../game/railroad-tycoon.md), [Transport Tycoon](../game/transport-tycoon.md)

## Sources

- [Railroad Tycoon (video game)](../source/src-wikipedia-railroad-tycoon.md)
- [Offworld Trading Company](../source/src-wikipedia-offworld-trading-company.md)
- [Capitalism (video game)](../source/src-wikipedia-capitalism-video-game.md)

---
Provenance: created in run `2026-10-24-taxonomy-m2`.
