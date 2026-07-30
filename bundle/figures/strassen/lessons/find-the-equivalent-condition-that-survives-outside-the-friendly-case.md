---
type: lesson
title: "Find the equivalent condition that survives outside the friendly case, then make it the definition"
figure: strassen
works: [relative-bilinear-complexity-and-matrix-multiplication]
axes: [expressiveness, verifiability]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Find the equivalent condition that survives outside the friendly case, then make it the definition

**Lesson:** Useful notions are often born inside a setting that supplies extra machinery, and the first definition anyone writes down leans on that machinery without noticing. A concept defined as "lies in the closure of the cheap objects" needs an ambient topology; one defined as "the limit of a family of approximations" needs limits to exist. The definition is then silently unavailable everywhere the machinery is missing, and the whole theory looks like it only applies to the special case. The repair is not to weaken the concept or to carry two parallel theories. It is to prove, inside the friendly setting where both are available, that the topological condition is equivalent to a condition stated purely in terms you have everywhere — a finite algebraic identity, a combinatorial inequality on the object's support — and then to adopt that second condition as the definition. In the friendly case nothing changes, because they agree; outside it, the concept now exists at all.

The equivalence proof is what earns the promotion, and it must go both ways. One direction is usually easy and worth little: any construction satisfying the concrete condition obviously produces an approximating family. The direction that matters is the hard one, showing that every limit whatsoever is witnessed by such a finite certificate — that nothing achievable by an unbounded limiting process escapes description by a bounded amount of algebra. Only when that holds are you entitled to say the general definition is the same concept rather than a lookalike, and the price of the translation is worth watching, because the certificate usually carries a parameter (how many terms, how deep the truncation) that the limiting formulation hid.

The habit generalizes past mathematics to any place a specification is written against the capabilities of the environment it was first developed in. A property expressed as "converges under repeated application" or "holds in the limit of infinite retries" is not implementable; a property expressed as a checkable condition on a finite trace is. When a definition resists porting to a setting you care about, the useful question is not how to smuggle the missing machinery in, but which finite, first-order fact about the object the machinery was being used to certify. That fact is the definition you should have written first, and it is usually more useful in the original setting too, because it is something you can exhibit rather than merely assert.

**Source:** [Relative Bilinear Complexity and Matrix Multiplication](../works/relative-bilinear-complexity-and-matrix-multiplication.md) — section 5, where degeneration, originally defined by Zariski closure over an algebraically closed field, is shown equivalent to a finite identity over a ring of truncated infinitesimals, and that characterization is explicitly adopted as the definition for arbitrary ground fields; and section 6, where the same promotion is performed for the monomial version of the order, whose replacement condition is purely combinatorial.
