---
type: lesson
title: "Turn the question around: besides what an object costs to build, ask what can be extracted from it"
figure: strassen
works: [relative-bilinear-complexity-and-matrix-multiplication]
axes: [expressiveness, primitive-count]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Turn the question around: besides what an object costs to build, ask what can be extracted from it

**Lesson:** Once cost is expressed as a comparison — this object lies below that many copies of the unit — the inequality can simply be read the other way, giving a second quantity that had no name before: how many independent copies of the unit can be recovered from inside the object. One number is the price of the thing, the other is what the thing is worth if you cash it in, both denominated in the same currency, and they are not equal. The lower quantity is bounded above by the upper one, and the gap between them is exactly the object's inefficiency as a container of useful structure.

The reason this dual is worth naming is that it turns out to be the constructive half of the theory. Upper bounds on cost are proved by exhibiting a procedure; but progress often stalls there, and what unblocks it is knowing how much usable structure a large object contains, because that is what licenses using the object as raw material for something else. An object that is expensive to build may still be rich to mine, and richness is the property you need when the plan is to acquire the object once and extract from it repeatedly. Asking only about price systematically hides that.

The habit generalizes past complexity. Whenever a quantity is defined as an extremum over a relation, reversing the relation defines a companion quantity for free, and the companion is frequently the one that answers the question you were actually stuck on. Before inventing a new measure, check whether the measure you already have has an unexamined mirror image. The mirror inherits the whole theory — monotonicity, behaviour under combination, the same proof techniques — so the cost of naming it is nearly zero and the payoff is a second, independent handle on the same object.

**Source:** [Relative Bilinear Complexity and Matrix Multiplication](../works/relative-bilinear-complexity-and-matrix-multiplication.md) — section 6, where the subrank and border subrank are introduced by explicitly exchanging the sides of the inequalities that define rank and border rank, with the accompanying remark that one measures the price of an object and the other its value in the same units, and the resulting lower bound on how much diagonal structure a matrix multiplication tensor contains.
