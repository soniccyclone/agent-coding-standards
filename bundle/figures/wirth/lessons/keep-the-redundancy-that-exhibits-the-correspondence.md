---
type: lesson
title: "Keep the redundancy that exhibits the correspondence to the algorithm you already trust"
figure: wirth
works: [algorithms-and-data-structures]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Keep the redundancy that exhibits the correspondence to the algorithm you already trust

**Lesson:** Most new algorithms are not new; they are an old one with a variable replaced by something richer. A scan that carries a single position becomes a bisection that carries a bracket, and the bracket plays exactly the role the position played — same invariant shape, same argument for termination, same reasoning about which elements have been ruled out. When that correspondence exists, it is the cheapest correctness argument available, because it lets you inherit the confidence you already have rather than construct a new proof from nothing. It is also fragile in a specific way: the correspondence lives in the *shape of the code*, so any edit that changes the shape without changing the meaning can destroy it silently. This is why an apparently free tidy-up — noticing that the same assignment appears at the top of the loop and at the bottom and hoisting one away — can be a bad trade. What it removes is not duplication; it is the visible evidence that this loop has the same skeleton as one you already believe.

So the discipline is to decide, deliberately, that a small redundancy is load-bearing, and then to leave it alone and say why. This runs against the instinct that any repetition is a defect to be factored out, and the instinct is right often enough that the exceptions have to be marked or the next reader will remove them. Marking is easy and the note is short: this assignment appears twice so that the loop reads as the same loop as the simpler method. That sentence is worth more than the instruction it costs, because it converts a future silent regression into a decision someone has to overrule.

The general habit is to look for the correspondence before you look for the optimization. When writing a harder version of something you already have, ask what in the new version stands in for what in the old, write the new version so that the substitution is legible, and only then consider changes that would obscure it — each one now visibly priced against the argument it costs you. The corollary is a diagnostic: if you cannot state what the correspondence is, you do not actually have an inherited proof, and you owe the new algorithm a fresh one. Discovering that early is much cheaper than discovering it after the code is in use.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 1.8.2's note of a fundamental structural similarity between binary search and the linear search of the preceding section, in which the single index of the linear search is played by the triple of left bound, midpoint and right bound, and the stated decision to resist the temptation of a minor optimization that would eliminate one of the two identical assignments to the midpoint, made in order to explicate the similarity and thereby better ensure the loop's correctness.
