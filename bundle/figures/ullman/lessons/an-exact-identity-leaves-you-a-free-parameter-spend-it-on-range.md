---
type: lesson
title: "An exact identity leaves you a free parameter — spend it on staying in range"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# An exact identity leaves you a free parameter — spend it on staying in range

**Lesson:** Two expressions that are provably equal as mathematics are not interchangeable as computations. The equality guarantees identical answers under exact arithmetic; the machine does not do exact arithmetic, and the two forms can differ enormously in how far their intermediate values wander from the range the representation handles well. So an algebraic identity is not merely a fact to be noted — it is a degree of freedom handed to the implementer, and the question to ask of it is which member of the equivalent family keeps every intermediate quantity somewhere the hardware is accurate.

The specific danger is an intermediate that is much larger or much smaller than the final answer. A well-scaled result computed through an intermediate that overflows, underflows, or has to be summed alongside quantities many orders of magnitude away from it, is not well-scaled at all; the precision was lost in the middle and no amount of care at the end recovers it. That is why identities that let you subtract a common offset, factor out a common scale, or reorder a sum are disproportionately valuable: they act only on the intermediates, leaving the answer untouched by construction, which means applying them can never be wrong and can only be an improvement.

Two habits follow. First, when an identity contains a symbol you are free to choose, do not leave it at the obvious value — solve for the choice that bounds the intermediates, which is usually something derived from the data rather than a constant. Picking the offset from the largest quantity actually present, so that everything else lands below it, is the recurring shape of the trick. Second, once such a form is known, it belongs inside whatever routine everyone calls, not in the notes of the person who worked it out. The whole point is that a caller who reasons in mathematics rather than in floating point should not have to know: the safe form and the naive form are indistinguishable at the interface, so the library owes its users the safe one.

Read broadly, this is the case for treating numerical behaviour as part of an operation's contract rather than as a quality of the input. An operation that is accurate only when its arguments happen to be well conditioned has an unstated precondition, and unstated preconditions on numerical range are close to unenforceable in practice — nobody checks, and the failure is a plausible-looking wrong answer rather than an exception.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the accuracy-of-softmax-calculation aside in the neural-nets chapter, which observes that summing exponentials of widely spread values mixes very large and very small floating-point numbers, notes that subtracting any constant from every exponent leaves the normalised result unchanged, chooses that constant to be the maximum so all the exponentiated terms fall between zero and one, and remarks that deep-learning frameworks generally build this form into the operation itself.
