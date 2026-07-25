---
type: lesson
title: "Of two equivalent definitions, the one needing fewer auxiliary concepts is the right one"
figure: boyce
works: [recent-investigations-in-relational-data-base-systems]
axes: [primitive-count, verifiability]
subdomains: [databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# Of two equivalent definitions, the one needing fewer auxiliary concepts is the right one

**Lesson:** Logical equivalence does not make two definitions equal. A definition is also an interface: every auxiliary concept it invokes — a privileged attribute class, a distinguished key, a chain of derived dependency notions — is a dependency that everything built on the definition inherits. Restating the same property purely in terms of one primitive relation (here, functional dependence between attribute sets) removes distinctions that were doing no real work, and the payoff is concrete: the algorithms that operate on the definition get simpler, the proofs about it get shorter, and edge cases that only existed because of the scaffolding vanish. The classification of attributes into special categories turned out to be arbitrary — an artifact of how the idea was first found, not of what the idea is.

The working heuristic: when a definition you rely on needs a taxonomy of special cases to state, suspect the taxonomy before suspecting the domain. Try to re-derive the property using only the most primitive relation in play, quantified uniformly over everything. If the restatement succeeds and is provably equivalent, adopt it and let the old formulation go, however historically entrenched — the simpler statement is closer to the actual structure being described, and the tooling built on it will show the difference.

This is normalization theory's own lesson applied reflexively to itself: the original normal-form definitions were correct but carried incidental structure, and tightening them was as real a contribution as inventing them. A programmer who thinks this way revisits their invariants and type definitions after the fact, asking not "is this right?" but "is this stated in terms of anything it doesn't need?"

**Source:** [Recent Investigations in Relational Data Base Systems](../works/recent-investigations-in-relational-data-base-systems.md) — the normalization section, where the Boyce-Codd restatement of third normal form is presented and its advantage argued in terms of the concepts it no longer references and the resulting simplification of the normalizing algorithm.
