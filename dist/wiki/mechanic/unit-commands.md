# Unit commands

*Mechanic* · `unit-commands` · status: **asserted**

The player issues direct orders to specific units or agents, overriding their autonomous behavior.

| field | value |
|---|---|
| aliases | direct orders, drafting, move and attack orders |
| family | Control & automation |
| substrate | Agent-based, Rule system |
| math basis | Graph search, Scheduling |
| feedback | None |
| player interface | Orders |
| legibility | 4 |
| emergence potential | 2 |
| authoring cost | 2 |
| compute cost | 2 |
| tuning difficulty | 2 |
| ai leverage | 3 |
| maturity | Classic |
| core count *(computed)* | 4 |
| earliest game *(computed)* | [Utopia](../game/utopia.md) |
| earliest year *(computed)* | 1982 |
| prevalence *(computed)* | 17 |
| prevalence share *(computed)* | 0.098 |
| subgenre spread *(computed)* | 11 |
| technique count *(computed)* | 3 |
| technique exposure *(computed)* | 1.562 |

## Definition

The player selects one or more units and gives explicit orders (move here, attack this, use that, stay, guard) that take precedence over the units' autonomous decision making. State owned: per-unit order queue and override flag. Update rule: when an order is present, the unit's action selection is bypassed or constrained to executing it; on completion or cancellation, autonomy resumes. Orders can be queued and may be refused if impossible. In simulation games it often sits beside autonomy: RimWorld's drafting switches a colonist from autonomous work to direct control for combat; The Sims lets the player queue actions for a Sim who otherwise acts on free will; Dwarf Fortress squads take orders while civilians do not. Strategy games make it the default control mode.

## Player Experience

When autonomy fails or stakes are high, the player takes the wheel. Drafting colonists into a defensive line or forcing a Sim to bed is precise and reassuring, but heavy use turns agents into puppets and the player into a micromanager.

## Design Levers

- scope: any unit, only military units, or only drafted units
- how long overrides last and how autonomy resumes
- order queue length and shift-queue support
- whether units can refuse or delay orders based on morale or needs
- group orders and formations
- what autonomous behavior continues under orders, such as eating or fleeing

## Failure Modes

- Orders are needed constantly because autonomy is weak, turning play into micromanagement.
- Drafted or ordered agents ignore needs and starve or collapse, producing deaths players blame on the interface.
- Unclear return-to-autonomy rules leave units idle after an order completes.

## Dynamics

- A dual mode emerges: autonomy in peace and direct command in crisis, giving play a rhythm of calm and intensity.
- The cost of micromanagement pushes players to improve autonomy-affecting systems such as priorities and schedules.
- Override on one agent shifts load to others, revealing hidden dependencies in job systems.

## Open Questions

- Can units interpret high-level natural-language orders (hold the bridge until the medic arrives) and decompose them, and how should they report failure?
- When agents have language-model reasoning, how should they negotiate or refuse orders without frustrating the player?

## Backlinks (computed)

**affected by:** [Generalist instructable game agents (SIMA)](../technique/generalist-game-agents.md), [On-device small language models for characters](../technique/on-device-language-models.md), [Realtime speech-to-speech and expressive TTS for characters](../technique/realtime-voice-models.md)

**involved in:** [Intent-level orders](../opportunity/intent-level-orders.md)

**used by:** [Anno 117: Pax Romana](../game/anno-117.md), [Arma 3](../game/arma-3.md), [Command: Modern Operations](../game/command-modern-operations.md), [Dwarf Fortress](../game/dwarf-fortress.md), [From Dust](../game/from-dust.md), [FTL: Faster Than Light](../game/ftl.md), [Kenshi](../game/kenshi.md), [Manor Lords](../game/manor-lords.md), [Mindustry](../game/mindustry.md), [Populous](../game/populous.md), [Project Hospital](../game/project-hospital.md), [Railroad Tycoon](../game/railroad-tycoon.md), [SimAnt](../game/simant.md), [Songs of Syx](../game/songs-of-syx.md), [Space Haven](../game/space-haven.md), [Spore](../game/spore.md), [Utopia](../game/utopia.md)

---
Provenance: created in run `2026-10-24-taxonomy-m6`.
