# Brief: propose a missing mechanic

**Run kind:** whatever run you are in; the proposal goes in its `proposals` list. Only `taxonomy` runs create mechanics (E031), and those are maintainer-reviewed.

Propose a mechanic when a game you are cataloguing clearly has a rule-system the taxonomy lacks, and forcing the nearest existing mechanic would be wrong.

```yaml
proposals:
  - kind: new-mechanic
    target: <proposed-id>
    detail: >-
      One-line definition (the state it owns and its update rule). Admission test: nameable (two other games that
      have it), atomic (why it does not split), tunable (two levers), removable (a game could drop it). Games in the
      catalog that use it: <ids>. Nearest existing mechanics and why they do not fit: <ids>.
```

Also open a **Proposal** issue with the same text so a maintainer can triage it; an agent without GitHub access leaves that to its operator. Describe the rule-system in the game's `design_notes` meanwhile.
