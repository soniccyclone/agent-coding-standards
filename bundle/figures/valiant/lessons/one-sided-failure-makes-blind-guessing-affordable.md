---
type: lesson
title: "When failure is one-sided and checkable, an unknown parameter costs you retries rather than a redesign"
figure: valiant
works: [np-is-as-easy-as-detecting-unique-solutions]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# When failure is one-sided and checkable, an unknown parameter costs you retries rather than a redesign

**Lesson:** A procedure often needs a tuning value it cannot compute — the right scale, the right threshold, the right number of times to apply a transformation. The reflex is to go estimate it, which means building a whole second mechanism whose accuracy the first one now depends on. The cheaper route is available whenever the procedure's failures are one-sided: it may miss, but it never produces a false positive, and success is recognizable when it happens. Then you can simply pick the parameter blindly out of its range of candidates. Guessing wrong is not an error, only a wasted attempt, and the price of ignorance collapses from "design an estimator" to "run more attempts."

What makes this sound rather than sloppy is the way one-sided error behaves under repetition. If a single run can only err by failing to find something that exists, then independent runs compose by disjunction: any one success is conclusive, and the failure probability multiplies down. Consequently a success rate that looks embarrassing — one in a polynomial number of tries — is, up to a polynomial slowdown, indistinguishable from certainty, so classes of problems defined with a constant success threshold and with an inverse-polynomial one are the same class. That equivalence is the licence to be wasteful in exactly one currency. You may throw away almost all of your probability mass on blind choices, provided you never spend any of your soundness.

The design consequence is to spend early effort on the asymmetry rather than on the accuracy. Arrange the mechanism so that the direction it can be wrong in is the harmless one, and so that a caller can confirm a claimed success independently. Once those two are in place, unknown parameters stop being blockers: enumerate them, sample them, sweep them. The trade is visible and boring — a polynomial factor of extra work in exchange for deleting an entire estimation subsystem, along with the coupling and the calibration bugs it would have brought. The failure mode to watch for is a procedure that can also err the other way, because then repetition amplifies the wrong thing: more attempts increase the chance of a confident falsehood, and blind guessing becomes exactly as dangerous as it feels.

**Source:** [NP Is as Easy as Detecting Unique Solutions](../works/np-is-as-easy-as-detecting-unique-solutions.md) — the section 1 definition of randomized reducibility, whose two clauses require that a non-member never maps into the target while a member need only do so with inverse-polynomial probability, the accompanying remark that lowering the acceptance threshold from a constant to any inverse polynomial leaves the class unchanged, and the reduction of section 2, which chooses the number of adjoined constraints uniformly at random from the whole available range instead of computing it.
