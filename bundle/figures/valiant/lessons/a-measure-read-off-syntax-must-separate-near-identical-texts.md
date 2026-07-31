---
type: lesson
title: "Two expressions can be one symbol apart and worlds apart in cost, which condemns every measure read off their shape"
figure: valiant
works: [the-complexity-of-computing-the-permanent]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Two expressions can be one symbol apart and worlds apart in cost, which condemns every measure read off their shape

**Lesson:** The most seductive route to a lower bound, or to any judgement about how expensive something will be, is to score the text: assign difficulty to an expression from features you can see in it — how many terms, how deep the nesting, which operators appear — and let the score stand in for the cost. The approach works in restricted settings and fails in general, and the reason it fails can be exhibited by a single pair. Take the defining formula for the determinant and change the sign convention on its terms so they are all positive. The two formulas are the same size, the same depth, over the same variables, differing in nothing a syntactic measure can name. One has been computed efficiently since the nineteenth century; for the other, no method better than exponential is known, and it is complete for a class of counting problems believed intractable.

The consequence for anybody hoping to bound difficulty from structure is sharp and worth stating as a test: whatever measure you propose must, to be of any use, assign wildly different values to that pair. If it cannot, it is not measuring what you think it is, no matter how well it correlates on the examples you tried. This is not a comment about the difficulty of proving lower bounds; it is a comment about the shape any successful proof must have, and it retires a whole family of attempts before they are made.

The pattern transfers to every proxy metric anyone uses on programs. Line counts, expression complexity, control-flow graph statistics, coupling scores — all are functions of the artifact's shape, and the question to ask of each is whether two artifacts differing in one symbol can behave arbitrarily differently under the property you care about. In a discrete system they usually can, so a shape-derived metric can serve as a cheap heuristic but cannot serve as evidence. It also cuts the other way: if you want a measure that genuinely tracks a semantic property, you have to find features that the property's discontinuities are visible in, which usually means computing something about behavior rather than reading something off the source. Being able to name the minimal pair that defeats your metric is the fastest way to learn what your metric is worth.

**Source:** [The Complexity of Computing the Permanent](../works/the-complexity-of-computing-the-permanent.md) — the closing paragraphs of the introduction, which observe that the permanent and determinant are the only known pair of functions whose algebraic expressions are so similar while their complexities differ so greatly, and draw the methodological consequence that any complexity measure assigned to intermediate results by syntactic criteria would need to distinguish expressions resembling each other that closely.
