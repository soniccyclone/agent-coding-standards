---
type: lesson
title: "Defend an awkward definition by recovering it from an unrelated angle"
figure: milner
works: [algebraic-laws-for-nondeterminism-and-concurrency]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# Defend an awkward definition by recovering it from an unrelated angle

**Lesson:** Some definitions cannot be justified by inspection. The one at the centre of this paper — a relation defined as the limit of a decreasing chain of approximations, each demanding that every step of one system be matched by a step of the other into the next approximation — is admitted to be complicated, and no amount of staring at it establishes that it captures the right idea. The move made in response is not to simplify it but to arrive at it a second time from somewhere else: identify a system with the set of properties it enjoys, where properties are formulas built from ordinary logical connectives plus one modality per kind of interaction, and define two systems to be the same when they satisfy exactly the same formulas. That relation is then proved to be the first one. Two definitions with nothing in common in their construction landing on the same relation is the argument that the relation is not an artifact of either.

The second characterization pays off practically as well as rhetorically, and this is what makes the technique worth copying. To show two systems are not interchangeable under the original definition you must argue about an infinite chain of approximations; under the logical characterization you exhibit a single formula that one satisfies and the other does not. A distinguishing witness is finite, checkable, and diagnostic — it tells you what the difference is, not merely that there is one. Anyone who has debugged a failing equivalence knows the gap between those two things.

The same apparatus then serves as a measuring instrument. Deleting connectives from the property language yields characterizations of progressively coarser relations: without negation you get the classical automata-theoretic notion that identifies a machine with the set of interaction sequences it admits, and it is immediately visible why that notion is too weak — deadlock is a statement about the absence of a possibility, and you cannot say it without negation. The paper also takes the trouble to prove the approximation chain strictly decreasing, so no finite stage suffices. That is a check worth imitating: if your elaborate limit construction quietly stabilizes early, you built something more complicated than you needed.

The transferable habit is to distrust a definition you can only motivate by narrating it, and to look for a second, independently plausible formulation that should agree. When the two agree, you have evidence. When they diverge, the divergence is the most informative thing you will learn that week.

**Source:** [Algebraic Laws for Nondeterminism and Concurrency](../works/algebraic-laws-for-nondeterminism-and-concurrency.md) — the section giving the modal-logic characterization, explicitly introduced to justify a complicated definition, together with the theorems relating sublanguages lacking negation or conjunction to weaker equivalences and the examples establishing strictness of the approximation hierarchies.
