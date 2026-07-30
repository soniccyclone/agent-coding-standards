---
type: lesson
title: "Let a solution be approximate when the error is repaid by scale"
figure: strassen
works: [relative-bilinear-complexity-and-matrix-multiplication]
axes: [primitive-count, expressiveness]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Let a solution be approximate when the error is repaid by scale

**Lesson:** The demand that a construction be exact is usually inherited rather than examined, and it can be the binding constraint. Relax it: admit any object that can be approached with arbitrary precision by cheap objects, even if no cheap object hits it exactly. This defines a strictly more permissive measure, and constructions that were impossible at the exact price become available at the approximate one. The move is only sound if the slack is recoverable, and the recovery argument is the whole content: when the object is used recursively, the approximation error appears as a factor that grows polynomially in the depth of the recursion while the useful part grows exponentially, so taking the depth to infinity drives the penalty to nothing in the exponent. The relaxed measure then bounds the same asymptotic quantity as the exact one. You paid a price that vanishes under the very repetition that motivated the whole exercise.

Two disciplines make this a method rather than a wish. First, the relaxation must be defined precisely enough to prove things about, not left as an informal "close enough" — here that means a definite algebraic account of what an approximating family is and what it costs to remove the approximation, so the penalty term is an object you can carry through the algebra rather than a hand wave. Second, the relaxed measure must inherit the structural laws of the exact one: behaviour under sums, under products, under the transformations you plan to apply. Without inheritance you have a smaller number that no longer connects to anything, which is worse than the honest large number you started with.

The general shape is worth recognizing outside algebra. Wherever a system's guarantee is only meaningful in aggregate, insisting on the guarantee at every individual step overpays. A cache that is occasionally wrong, a counter that is approximate, a consensus that converges rather than decides — each can be the right primitive if you can show the deviation is bounded and that the bound is amortized away by the scale at which the thing is actually used. The question to ask is never "is this exact," but "at the scale where this runs, what does the inexactness cost, and does that cost shrink or grow with the workload." When it shrinks, exactness was a luxury constraint, and dropping it is where the real gains live.

**Source:** [Relative Bilinear Complexity and Matrix Multiplication](../works/relative-bilinear-complexity-and-matrix-multiplication.md) — the introduction's account of border rank, defined so that an object counts as cheap when it lies in the closure of the cheap ones, together with the observation that the exponent bound derived from exact constructions carries over verbatim to the approximate ones; and section 5, where the cost of removing an approximation is shown to be a factor polynomial in the truncation depth, which is why it disappears from the exponent.
