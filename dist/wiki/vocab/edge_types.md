# Vocabulary: edge_types

Every typed relation in the graph. Each edge is stored exactly once, on the `owner` side named here. Inverses are computed by the build and never stored. Symmetric edges are stored on the entity whose id sorts first.

| id | label | definition |
|---|---|---|
| `uses` | uses | A game uses a mechanic. Attributes role (mechanic_role) and note. |
| `influenced_by` | influenced by | A game's design draws on an earlier game. |
| `requires` | requires | A mechanic cannot function without another mechanic. |
| `specializes` | specializes | A mechanic is a narrower form of a parent mechanic. |
| `synergy` | synergy | Two mechanics amplify each other's dynamics when combined. |
| `tension` | tension | Two mechanics pull design in opposite directions; combining them needs a resolution. |
| `affects` | affects | A technique changes a mechanic. Attributes effect (effect vocab) and note. |
| `builds_on` | builds on | A technique depends on or extends an earlier technique. |
| `deployed_in` | deployed in | A technique is used in a specific game, shipped or prototype. |
| `involves` | involves | An opportunity reworks or combines a mechanic. |
| `applies` | applies | An opportunity depends on a technique. |
| `precedent` | precedent | A game partially demonstrates an opportunity. |
| `cites` | cites | An entity or claim relies on a source. |
