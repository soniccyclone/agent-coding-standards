---
type: lesson
title: "When a quantity only matters up to a bounded factor, replace its operational definition with an algebraic one"
figure: strassen
works: [relative-bilinear-complexity-and-matrix-multiplication]
axes: [primitive-count, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# When a quantity only matters up to a bounded factor, replace its operational definition with an algebraic one

**Lesson:** Some central notions are painful to define honestly — what exactly counts as an algorithm, which operations are chargeable, what the machine model permits — and the pain is usually spent on distinctions that the eventual question cannot see. The move that dissolves this: notice that the quantity you actually care about is insensitive to a bounded factor, then find a purely structural invariant of the object that is provably within such a factor of the operational count, and define everything in terms of the invariant instead. The delicate model-theoretic questions do not get answered; they get routed around, because no statement you intend to make can distinguish the two definitions.

What is bought is not just brevity. An operational definition supports only operational reasoning — you can exhibit procedures and count their steps, and little else. A structural invariant of the object inherits every property the object's algebra already has: it behaves predictably under sums and products of objects, it is preserved by the natural morphisms, it can be bounded by geometric or combinatorial arguments that never mention computation at all. A whole body of existing mathematics becomes applicable to a question that was previously stated in a vocabulary nothing else spoke. That is the real conversion: from a definition that only you can reason about, to one that a hundred years of someone else's theorems can reason about.

The precondition is the honest part, and it must be checked rather than hoped. The substitution is legitimate exactly when the difference between the two measures is swallowed by the coarseness of the question — a constant factor when you are asking about growth rates, an additive term when you are asking about a limit. Where the question is finer than the gap, the operational definition is doing real work and cannot be discarded. So the discipline is to determine the resolution of your question first, and only then decide how much definitional precision you are entitled to throw away.

**Source:** [Relative Bilinear Complexity and Matrix Multiplication](../works/relative-bilinear-complexity-and-matrix-multiplication.md) — the introduction, which observes that the exponent has been defined without saying what an algorithm or a complexity measure is, argues that there is no need to, and substitutes the rank of a bilinear map (an invariant known to sit within a bounded factor of the nonscalar operation count) as the working definition.
