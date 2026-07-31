---
type: lesson
title: "Define an unbounded object by all its finite views plus the requirement that they agree"
figure: kolmogorov
works: [grundbegriffe-der-wahrscheinlichkeitsrechnung]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Define an unbounded object by all its finite views plus the requirement that they agree

**Lesson:** Kolmogorov needs to put probabilities on spaces where a single outcome has infinitely many coordinates — a whole trajectory, a whole function — and no one can write such an assignment down directly. His result is that you never have to. Supply the finite views: for each finite selection of coordinates, a distribution over just those. Impose exactly two compatibility requirements — that permuting the coordinates permutes the answer correspondingly, and that a smaller selection's distribution is recovered from a larger one by discarding the extra coordinates — and the object on the infinite space exists, is unique, and satisfies everything the axioms demand. Nothing further is needed, and nothing further is permitted to be needed.

Two payoffs sit inside that. The first is a specification technique: an object too large to describe can be pinned down completely by the family of its bounded observations, provided every pair of overlapping observations is *required* to agree. The consistency of the views is not evidence about the object, it constitutes the object. The second is the freedom this hands you in the other direction — because the finite views are the only input, you may design them freely and receive the infinite object as output, which is exactly how a family of independent variables with arbitrary prescribed distributions gets constructed rather than assumed.

The engineering analogue is anything whose full extent you cannot write down: the trace of a long-running process, the total behavior of a stream, the whole history of a replicated store. Do not attempt the totality. Say what any bounded window of it looks like, then state the overlap law: a window's meaning must not depend on which larger window you happened to observe it inside, nor on the order in which you enumerated it. If those laws hold, the whole behavior is determined, and — this is the operational point — every obligation you have taken on is checkable locally, which is the only kind of obligation that can be checked at all. If the laws fail, the failure is precisely diagnostic rather than merely inconvenient: some finite view's meaning depends on context you never declared, and that is a defect in the model itself, not a limitation of the method.

**Source:** [Grundbegriffe der Wahrscheinlichkeitsrechnung](../works/grundbegriffe-der-wahrscheinlichkeitsrechnung.md) — Chapter III, §4, where the finite-dimensional distributions are shown to determine the probability function on cylinder sets and hence on their Borel extension, and the fundamental theorem establishes that any system of finite-dimensional distributions satisfying the permutation and marginalization conditions defines such a probability function; applied in Chapter VI, §2 to construct a family of mutually independent variables with arbitrarily prescribed individual distributions.
