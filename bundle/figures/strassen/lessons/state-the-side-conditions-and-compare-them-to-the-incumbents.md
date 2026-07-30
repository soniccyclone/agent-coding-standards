---
type: lesson
title: "State a faster method's side conditions up front, and compare them against the incumbent's rather than against perfection"
figure: strassen
works: [gaussian-elimination-is-not-optimal]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# State a faster method's side conditions up front, and compare them against the incumbent's rather than against perfection

**Lesson:** A faster construction almost always applies under conditions narrower than the problem's own statement — it needs the intermediate quantities it forms along the way to be well defined, which is a stronger requirement than the input merely being a legitimate instance. The obligation is to name that gap explicitly, at the point where the method is introduced, rather than leaving it to be discovered by whoever first feeds it an input that satisfies the problem but not the recursion. A precondition that lives only in the author's head is a defect in the result, not a detail of the implementation, because the correctness claim being advertised is quietly about a smaller domain than the one readers will assume.

The second half of the discipline is choosing the right comparison. An extra assumption looks damning against an idealized method that has none, and the idealized method usually does not exist: the standard approach being displaced typically carries an assumption of exactly the same character, tolerated only because familiarity has made it invisible. So the honest evaluation asks whether the new requirement is stronger than what the incumbent already demanded, not whether it is stronger than nothing. Frequently the answer is that both need the same kind of hypothesis, which converts an apparent disadvantage into a non-difference and lets the actual trade-off — the cost — be judged on its own.

Both halves generalize past algorithms to any substitution of one mechanism for another. Write down what the new thing assumes; write down what the old thing assumed; subtract. What remains is the real change in obligations that callers take on, and it is usually much smaller than a naive reading suggests and much larger than an enthusiastic one admits. Skipping the subtraction is how a system acquires a fast path whose applicability nobody can characterize, which is worse than having no fast path, because it must then be trusted rather than checked.

**Source:** [Gaussian Elimination is not Optimal](../works/gaussian-elimination-is-not-optimal.md) — the remark preceding the inversion algorithms, which states that invertibility of the matrix is not sufficient and that all divisions arising in the recursion must be legitimate, immediately noting that Gaussian elimination requires an assumption of the same kind.
