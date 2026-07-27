---
type: lesson
title: "Bound every search you can, and know exactly which single one you cannot"
figure: godel
works: [on-formally-undecidable-propositions]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Bound every search you can, and know exactly which single one you cannot

**Lesson:** The forty-odd definitions that carry the 1931 argument are built with a conspicuous discipline: wherever a quantifier or a minimization appears, it comes with an explicit bound tying the search to a range computable from the arguments. Gödel remarks, in a footnote, that these bounds usually make no difference at all to *what* is being defined — the same relation would be picked out without them. They are there to guarantee something else: that the relation is decidable, that for any concrete arguments a finite step-by-step evaluation settles it. Every notion in the ladder inherits that property from the ones below it, because the closure operations he establishes first — substitution, boolean combination, bounded quantification, bounded search for a least witness — all preserve it. And then, at the very top, exactly one definition breaks the pattern: "there exists a derivation of this" quantifies over derivations with no bound available, and Gödel flags it as the sole member of the list that cannot be claimed decidable.

That is the whole architecture of the paper in one observation, and it generalizes cleanly. Two predicates can pick out the same set while differing completely in computational character, and the difference is whether the search space is bounded by the input. Bounded search is a loop you can cost, run, and trust to terminate; unbounded search is a semi-decision procedure that answers yes eventually and never answers no. A system built entirely from the first kind is verifiable by evaluation. A system with the second kind mixed in throughout is verifiable nowhere, because you can no longer tell which questions terminate.

The engineering consequence is to keep the two kinds apart and to know precisely where the boundary sits. Build the total, cost-bounded machinery as a large layer of primitives that compose without leaving the class, and confine open-ended search — the solver call, the retry loop, the fixpoint iteration with no a priori bound, the network request with no deadline — to identified places you can name out loud. Then the properties you want hold everywhere except at those places, and the places are few enough to reason about individually. The failure mode is the opposite habit: sprinkling unbounded operations through a codebase until no function's termination or cost can be argued locally, and then being surprised that nothing about the system is checkable. Adding the bound often costs nothing semantically, which is exactly why it is cheap to insist on.

**Source:** [On Formally Undecidable Propositions of Principia Mathematica and Related Systems I](../works/on-formally-undecidable-propositions.md) — the closure propositions on computable relations preceding the definition ladder, the footnote explaining that the bounds attached to each quantifier exist to preserve computability rather than to change the concept, and the closing remark singling out derivability as the one definition not claimed to be computable.
