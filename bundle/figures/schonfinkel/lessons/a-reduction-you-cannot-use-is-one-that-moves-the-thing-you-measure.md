---
type: lesson
title: "A reduction you cannot use is one that moves the thing you measure"
figure: schonfinkel
works: [entscheidungsproblem-der-mathematischen-logik]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# A reduction you cannot use is one that moves the thing you measure

Partway through the argument the authors need to get rid of relations taking three or more arguments, and a suitable theorem already exists: Löwenheim had shown that any question of validity can be transformed into one where only two-argument relations occur. They decline to use it, and the footnote explaining why is the most portable paragraph in the paper. That transformation increases the number of quantifiers standing in front of the formula — and the number and order of those quantifiers is precisely the parameter their whole classification is indexed on. A reduction that changes the coordinate you are classifying by throws you out of the class you were studying. It is a valid theorem and a useless tool here.

So they build a replacement from scratch: a construction that eliminates high-arity relations while leaving the quantifier prefix untouched, at the cost of some fiddly work with an auxiliary expression that is forced true when its two arguments coincide and freely choosable otherwise. More effort than citing the existing result, and the only version that is admissible. The general principle is that a reduction has two obligations, not one. It must preserve the answer, and it must preserve every quantity your surrounding argument is stratified by. Almost all discussion of reductions covers the first obligation and forgets the second, which is why the second is the one that quietly invalidates work.

The same trap sits in ordinary engineering under different names. A refactor that preserves behavior while changing allocation counts is worthless inside a proof about memory ceilings. A rewrite that preserves output but adds a round trip cannot be used to argue about latency bounds. A benchmark harness that normalizes input in a way that changes cache footprint is measuring something other than what you claimed. In each case the transformation is correct in the dimension people usually check, and destructive in the dimension the current argument depends on.

The habit to build is to state, before adopting any transformation, which invariants the surrounding argument rests on, and then verify the transformation against that list rather than against correctness alone. When an off-the-shelf reduction fails the list, the answer is not to relax the claim and hope; it is to construct one that respects the invariant, accepting that it will be uglier than the published version. The ugliness is the cost of staying inside the class you are actually reasoning about.

**Source:** [Zum Entscheidungsproblem der mathematischen Logik](../works/entscheidungsproblem-der-mathematischen-logik.md) — section 3, the elimination of function symbols with more than two arguments, and the footnote rejecting Löwenheim's existing reduction to binary relations on the grounds that it multiplies the leading quantifiers and so alters the formula type under study.
