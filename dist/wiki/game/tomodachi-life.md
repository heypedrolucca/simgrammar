# Tomodachi Life

*Game* · `tomodachi-life` · status: **sourced**

A Nintendo 3DS life sim in which player-made Mii characters live in an island apartment building, form friendships, quarrels, and romances on their own, and ask the player to solve their problems.

| field | value |
|---|---|
| aliases | Tomodachi Collection: New Life |
| year | 2013 |
| developer | Nintendo SPD |
| platforms | Handheld |
| subgenre | Life sim |
| subgenre secondary | Social sim |
| sim domain | Social / interpersonal, Domestic / personal |
| player role | Caretaker |
| agency model | Caretaking interaction, Indirect incentive |
| time model | Real-world clock |
| sim scale | Settlement |
| fidelity | Stylized |
| perspective | Isometric |
| win structure | Open sandbox |
| failure model | None |
| narrative mode | Hybrid |
| multiplayer | Single-player, Async / shared content |
| modding | None |
| production tier | AA |
| agent count order | ~100 |
| emergence | 3 |
| influence | 2 |
| cluster *(computed)* | C04 |
| core count *(computed)* | 3 |
| mechanic count *(computed)* | 8 |

## Summary

A Nintendo 3DS life sim in which player-made Mii characters live in an island apartment building, form friendships, quarrels, and romances on their own, and ask the player to solve their problems.

## Core Loop

add Miis to the apartment -> Miis develop friendships, crushes, and quarrels -> they raise problems such as food, clothes, or advice -> solve problems to fill happiness and earn money -> level-up gifts and new island venues unlock -> couples marry and have children

## Design Notes

The player is an omnipotent observer who cannot control Miis directly and instead answers their requests, so most of the comedy comes from autonomous pairings and quarrels among Miis whose looks, names, voices, and personalities the player designed. Key relationship changes pass through player consent: the player approves a confession before it happens and resolves fights indirectly. The apartment holds up to 100 Miis, and a filled happiness meter levels a Mii up and earns it a present, so care is paced by a stream of small templated problems rather than decaying meters.

## Relations

**uses**

- [Relationship values](../mechanic/relationship-values.md) (core): Miis form friendships and conflicts on their own; pairs can grow closer, fall into fights, or break up, and the player intervenes only indirectly.
- [Romance and family](../mechanic/romance-family.md) (core): Opposite-gender friends of similar age may develop crushes; the player approves the confession, couples can marry and have a child who later moves in or leaves via StreetPass.
- [Villager requests](../mechanic/villager-requests.md) (core): Miis raise problems such as wanting a food or outfit, needing relationship advice, or asking for a minigame; solving them raises happiness and pays money.
- [Personality traits](../mechanic/personality-traits.md) (supporting): Each Mii receives a personality at creation that shapes its behavior.
- [Milestone unlocks](../mechanic/milestone-unlocks.md) (supporting): Adding Miis and completing objectives unlocks shops, an amusement park, a concert hall, a café, and other venues.
- [Content sharing](../mechanic/content-sharing.md) (supporting): Miis can be imported from Mii Maker or by scanning QR codes.
- [Asynchronous shared regions](../mechanic/async-shared-region.md) (supporting): StreetPass sends grown children to other players' islands.
- [Real-time clock](../mechanic/real-time-clock.md) (supporting): Island time follows the 3DS clock; at night the player can listen to sleeping Miis' dreams.

## Sources

- [Tomodachi Life](../source/src-wikipedia-tomodachi-life.md)

---
Provenance: created in run `2026-10-24-catalog-gc`.
