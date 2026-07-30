---
type: lesson
title: "Paired operations are rarely duals: check which direction your invariant survives"
figure: vardi
works: [on-the-semantics-of-updates-in-databases]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, foundations-of-computation]
tags: [lesson]
---
# Paired operations are rarely duals: check which direction your invariant survives

**Lesson:** Add and remove, grow and shrink, acquire and release, subscribe and unsubscribe — the symmetry of the naming invites you to expect symmetric reasoning, and the expectation is usually wrong. What breaks the symmetry is that the invariant you care about is typically preserved in one direction and not the other. Consistency is the clean case: any subset of a consistent collection is still consistent, while a superset may not be. That single asymmetry propagates all the way into how the two operations can be analyzed. Judging a removal is tractable because you can restrict attention to what was taken away and know the remainder is still sound; judging an addition is not, because accommodating the new item can force removals elsewhere, and no amount of looking at what was added tells you which.

Vardi and his coauthors demonstrate the failure of the tempting symmetric treatment rather than just asserting it, and the manner of the demonstration is the reusable part: they take the symmetric rule, follow it to its logical endpoint, and exhibit the absurd outcome it implies — insisting on adding nothing beyond the new item forces you to discard everything that does not already follow from it. A rule that produces a degenerate result at its extreme is not a rule with an unfortunate corner case; it is a rule that was never measuring what you wanted, and finding its extreme is how you discover that cheaply.

The habit is therefore twofold. When designing a pair of inverse-looking operations, name the property you are protecting and ask which direction of change automatically preserves it — that direction is the easy one, and its ease will mislead you about the other. And when you propose any preference rule for choosing among acceptable outcomes, immediately compute what it recommends in the most extreme case you can construct. Both checks cost minutes and both catch a class of error that survives ordinary testing indefinitely, because the symmetric intuition keeps making the wrong behaviour look correct.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — section two's treatment of insertion versus deletion: the lemma showing a minimal deletion can always be witnessed by a subset of the original, the explicit attribution of the discrepancy to consistency being preserved under subsets but not supersets, the counterexample where accommodating a new fact forces a choice of which existing fact to drop, and the second lemma showing that minimizing additions first collapses the state to the consequences of the new fact alone.
