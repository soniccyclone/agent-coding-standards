---
type: lesson
title: "When two problems are dual, work whichever side is cheaper each time"
figure: schonfinkel
works: [entscheidungsproblem-der-mathematischen-logik]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# When two problems are dual, work whichever side is cheaper each time

Two questions run through the paper: whether a formula comes out true under every interpretation, and whether some interpretation makes it true. They are interdefinable through negation, so a method for one yields a method for the other, and the authors say once at the start that results transfer between them the way theorems transfer in projective geometry. Having established the bridge, they stop treating the choice as fixed. The monotonicity theorem is proved on the satisfiability side, because there the construction extends a domain by folding new elements onto an existing one, which is easier to write than its mirror image. The decision criteria are developed on the validity side, because there the conjunctive normal form gives a criterion you can see by eye — a clause containing a symbol and its negation. Each subproblem is worked wherever it is cheapest, and the translation is invoked to move the result back.

They go further than switching sides; they switch the representation to match. Validity is read off conjunctive normal form, satisfiability off disjunctive, and the two normal forms are themselves duals of each other. Committing to validity as the target consequently forces an unusual bookkeeping convention — treating conjunction as the additive operation and disjunction as the multiplicative one, inverted from the customary reading — and they adopt it without apology because it is what makes the later algebraic manipulation of coefficients come out right. A duality is not just a fact about two problems; it is a permission to pick the coordinate system per step.

The trap the paper also documents is assuming the difficulty sits in the same place on both sides. Among the two-quantifier prefixes, the hard case for validity is existential before universal; under the dual question the hard case is the other one, universal before existential. Cost structure does not survive the translation even though truth does. So the classification you inherit from one formulation is only a classification of that formulation, and importing "this case is the easy one" across a duality is how you end up working the wrong case.

For a programmer the pattern is familiar wherever a problem has an equivalent complement: proving a property holds versus finding a counterexample, checking a whitelist versus a blacklist, computing a set versus its complement, solving a linear program versus its dual. The move is to establish the equivalence carefully once, then choose per subtask according to which side has the cheaper construction or the more mechanical test, and to re-derive rather than assume where the expensive cases live on the side you switched to.

**Source:** [Zum Entscheidungsproblem der mathematischen Logik](../works/entscheidungsproblem-der-mathematischen-logik.md) — section 1's statement of the duality between validity and satisfiability and the choice to prove only the satisfiability half of the monotonicity theorem, section 2's pairing of conjunctive normal form with validity and disjunctive with satisfiability along with the inverted sum/product convention, and the end of section 3 noting that the non-trivial prefix type is the dual one for satisfiability.
