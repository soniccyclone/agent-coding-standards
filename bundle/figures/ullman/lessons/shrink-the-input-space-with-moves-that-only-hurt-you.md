---
type: lesson
title: "Shrink the input space with moves that only hurt you"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Shrink the input space with moves that only hurt you

**Lesson:** Proving that a procedure always attains some fraction of the ideal means quantifying over every input it could ever receive, and that space is normally too unstructured to argue about directly. There is a preprocessing move that makes it tractable and that is easy to miss because it happens in one sentence. Before touching the procedure, find transformations of the input that leave the ideal result unchanged while making your own procedure's result no better. Every input maps under such a transformation to a cleaner input on which your worst-case ratio is at least as bad. So the worst case must live inside the transformed family, and you can prove the bound there and inherit it everywhere.

The chapter uses the move twice in a row on the same proof. Requests that the ideal allocator declines to serve are deleted, since deleting them cannot reduce the ideal's revenue and may reduce yours. Unspent portions of budgets are shaved away, since the ideal was not using them and shrinking a budget can only constrain you further. Two sentences, and an arbitrary sequence of requests against arbitrary budgets has become a sequence in which every request is served by the ideal and every budget is exactly exhausted, which is a structure regular enough to reason about with a case split and a counting argument.

The direction of the inequality is the whole trick and is worth stating carefully, because getting it backwards produces a proof of nothing. The transformation must be neutral or favourable for the competitor you are being measured against, and neutral or unfavourable for you. Then the ratio on the transformed input lower-bounds the ratio on the original. A transformation that helps you, however natural it looks, proves only that you do well on inputs you have quietly cleaned up. It is worth writing the two directions down explicitly for each move rather than trusting the intuition that the change is harmless, because "harmless" is exactly the word that hides an asymmetry.

The habit generalises past competitive analysis to anywhere a claim is universally quantified over messy inputs: fuzzing corpora, invariants under refactoring, capacity arguments, tests that must hold for all configurations. Look for a normalisation whose error runs in the safe direction, apply it until the remaining family has visible structure, and argue there. The alternative, arguing over the raw space, usually means arguing over examples, which settles ceilings but never floors.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 8's lower-bound proof for the Balance algorithm, which first discards queries the optimum leaves unassigned on the grounds that removing them cannot help Balance, then reduces budgets the optimum does not fully consume by the same reasoning, before analysing the resulting canonical case.
