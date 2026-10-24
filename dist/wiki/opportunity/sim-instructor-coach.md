# Simulator instructor coaching

*Opportunity* · `sim-instructor-coach` · status: **asserted**

Flight, driving, and procedure sims with a voice instructor that watches inputs and state, explains mistakes, and adapts lessons in real time.

| field | value |
|---|---|
| opportunity type | Mechanic upgrade |
| involves | [Procedural checklists](../mechanic/procedural-checklists.md), [Embodied skill control](../mechanic/embodied-skill-control.md), [Flight aerodynamics](../mechanic/flight-aerodynamics.md), [Vehicle dynamics](../mechanic/vehicle-dynamics.md), [Diagnose and repair](../mechanic/diagnose-repair.md) |
| applies | [Realtime speech-to-speech and expressive TTS for characters](../technique/realtime-voice-models.md), [LLM explanation of simulation state](../technique/llm-explanation-of-state.md), [On-device small language models for characters](../technique/on-device-language-models.md) |
| precedent | [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md), [iRacing](../game/iracing.md), [DCS World](../game/dcs-world.md), [X-Plane](../game/x-plane.md), [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md) |
| novelty | 2 |
| feasibility | 4 |
| impact | 3 |
| horizon | Now |
| falsifiable signal | {'prediction': 'A major flight or racing simulator will ship an AI voice instructor that comments on live telemetry.', 'resolve_by': '2027-12-31', 'criteria': 'Official feature in Microsoft Flight Simulator, X-Plane, DCS, iRacing, Gran Turismo, or a peer title.'} |
| priority *(computed)* | 3.059 |

## Thesis

Vehicle and job simulators teach through checklists and failure. Professional training uses instructors who watch and talk. Realtime voice models, state-grounded explanation, and player modeling make an instructor that comments on what the player is actually doing, with references to the simulator's telemetry, feasible in consumer sims. The same tool serves professional training and lowers the entry barrier for the most intimidating subgenres.

## Design Sketch

During a landing, the instructor says 'airspeed 12 knots fast, reduce power' based on telemetry, then debriefs with a timeline of deviations. Lessons adapt to repeated errors. The player can ask questions mid-flight by voice.

## Key Risks

- Wrong advice in safety-relevant domains if transferred to real training.
- Voice latency during time-critical maneuvers.
- Instructor chatter annoys experienced players.

## Validation Experiment

Add a telemetry-grounded voice instructor to a flight sim landing lesson; compare novice landing success after five attempts with and without the instructor. Success: at least 25 percent higher success with no increase in reported frustration.

## Falsifiable signal

- **Prediction:** A major flight or racing simulator will ship an AI voice instructor that comments on live telemetry.
- **Resolve by:** 2027-12-31
- **Criteria:** Official feature in Microsoft Flight Simulator, X-Plane, DCS, iRacing, Gran Turismo, or a peer title.

## Relations

**applies**

- [Realtime speech-to-speech and expressive TTS for characters](../technique/realtime-voice-models.md)
- [LLM explanation of simulation state](../technique/llm-explanation-of-state.md)
- [On-device small language models for characters](../technique/on-device-language-models.md)

**involves**

- [Procedural checklists](../mechanic/procedural-checklists.md)
- [Embodied skill control](../mechanic/embodied-skill-control.md)
- [Flight aerodynamics](../mechanic/flight-aerodynamics.md)
- [Vehicle dynamics](../mechanic/vehicle-dynamics.md)
- [Diagnose and repair](../mechanic/diagnose-repair.md)

**precedent**

- [Microsoft Flight Simulator 2024](../game/microsoft-flight-simulator-2024.md)
- [iRacing](../game/iracing.md)
- [DCS World](../game/dcs-world.md)
- [X-Plane](../game/x-plane.md)
- [Euro Truck Simulator 2](../game/euro-truck-simulator-2.md)

---
Provenance: created in run `2026-10-24-synthesis`.
