---
type: lesson
title: "Eliminating the intermediate can destroy the structure that made it cheap"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Eliminating the intermediate can destroy the structure that made it cheap

**Lesson:** Substituting one definition into another to remove an intermediate quantity is the standard move for making a description simpler, and it is frequently a performance disaster. The composed form is mathematically equivalent and often shorter to write, but composition does not preserve the properties that made the original pieces efficient. Sparseness is the clearest case: two structures that each touch very few positions compose into one that touches far more, so the fused form does strictly more work than the two-step form it replaced. The simplification was real at the level of notation and false at the level of execution.

This matters because the instinct it contradicts is a good instinct in most other contexts. Fewer intermediates usually means less allocation, fewer passes, better locality — fusion is a standard optimisation precisely because it usually wins. What distinguishes the cases is whether the intermediate was doing structural work. If the intermediate is just a buffer holding values on their way somewhere else, eliminating it is free. If the intermediate has a shape — it is small, it is sparse, it is sorted, it is bounded in a way neither of its neighbours is — then it is a chokepoint that keeps the pipeline narrow, and removing it lets the width of the two ends multiply. Ask what the intermediate's shape is before deciding it is redundant.

The general form is that equivalence of results is a much weaker relation than interchangeability. Two expressions can denote the same value while having entirely different cost profiles, and any rewrite justified purely by the equality is unjustified operationally. This cuts both ways and is worth holding symmetrically: sometimes the fused form is the fast one and the staged form wastes memory bandwidth; the point is not that staging is better but that the algebra cannot tell you which, so you have to reason about the structure separately. A rewrite rule licensed by mathematics needs a second, independent argument about representation before it is licensed by engineering.

The practical discipline is small: whenever you simplify a composition on paper, write down what each eliminated intermediate looked like, and check that the direct form does not have to materialise something wider than everything it replaced. That check takes a minute and catches the case where an obviously nicer formulation is quietly quadratic.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the hubs-and-authorities section of the link-analysis chapter, where the two mutually recursive definitions can be substituted into each other to give a single self-contained equation for each score, but the composed operator is much less sparse than the link structure it was built from, so the alternating two-step iteration is retained in practice.
