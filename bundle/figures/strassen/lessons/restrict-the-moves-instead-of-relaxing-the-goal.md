---
type: lesson
title: "When the general relation is out of reach, restrict the allowed moves rather than relax the goal"
figure: strassen
works: [relative-bilinear-complexity-and-matrix-multiplication]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# When the general relation is out of reach, restrict the allowed moves rather than relax the goal

**Lesson:** You define the right comparison — can this object be transformed into that one, can this configuration reach that one — and then discover you cannot decide it. Two responses are available and they are not equally good. The tempting one is to weaken what you are trying to prove: ask for an approximate answer, a heuristic, a probabilistic guarantee. The better one is to keep the question exactly as stated and shrink the set of transformations you are willing to consider. Allow only maps of some rigid shape — permutations and scalings rather than arbitrary invertible maps — and the reachability relation collapses from a question about orbit closures in an algebraic variety into a question about whether a system of linear inequalities on a finite index set has a solution. Nothing about the goal was compromised, because reachability under fewer moves implies reachability under more: every fact the restricted relation certifies is a true fact about the unrestricted one. You have traded completeness for decidability, and completeness is the cheaper thing to lose, because an incomplete method that answers is worth more than a complete one that hangs.

What makes the trade pay is choosing the restriction so that the resulting search lands in a class where both outcomes are certifiable. Reducing to linear inequalities is not merely convenient; it means that when a witness exists you can exhibit it, and when none exists duality hands you a dual object that proves none exists. A search procedure whose failures are silent is nearly useless for building theory, because you can never tell "no such transformation" from "I did not find one." Arrange the restriction so that impossibility has a short certificate too, and the negative results become as usable as the positive ones. That is a design criterion for the restriction, not an accident of it.

The residual obligation is to keep the two relations distinguished in your own head and in your notation, and to know which direction of implication you are entitled to. Anything you prove with the restricted moves transfers upward; nothing you fail to prove transfers at all, so a negative result under the restriction is a statement about your toolkit and must never be reported as a statement about the problem. Practically, this is the discipline behind every sound-but-incomplete analysis: a type system, a decidable fragment of a logic, a model checker over a finite abstraction. Each one narrows the moves rather than the question, and each is worth having precisely because its answers, when they come, are answers about the real system.

**Source:** [Relative Bilinear Complexity and Matrix Multiplication](../works/relative-bilinear-complexity-and-matrix-multiplication.md) — section 6, which restricts the transformation group to monomial maps, obtains a purely combinatorial criterion for the resulting degeneration order in terms of weight vectors on the support, notes that the restricted order implies the general one, and observes that non-existence of the weights is itself certified by a dual object via linear-programming duality.
