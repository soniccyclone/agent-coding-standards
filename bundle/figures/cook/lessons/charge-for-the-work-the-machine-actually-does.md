---
type: lesson
title: "Price each primitive operation at what the physical machine would really pay, or your analysis describes a machine that cannot exist"
figure: cook
works: [time-bounded-random-access-machines, an-overview-of-computational-complexity]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Price each primitive operation at what the physical machine would really pay, or your analysis describes a machine that cannot exist

**Lesson:** The convenient idealization is that a register holds any integer and every operation on it takes one time unit. This is not a simplification; it is a leak. Repeated doubling reaches numbers whose written form exceeds any storage that will ever be built, yet the idealized cost stays constant, so the model credits an algorithm with work no hardware performs. The correction is to charge for storing or moving a number in proportion to the length of its representation, which is precisely what a real machine with a fixed word size pays when it spreads a large value across many words. The cost function stops being an accounting convenience and starts being a claim about mechanism.

Getting this wrong is not a rounding error, it inverts conclusions. Given a model whose single step is powerful enough to reorganize its own storage, entire problems appear to become dramatically cheaper, and the only sane reading is that either the problem was easier than everyone thought or the model is cheating. Having no principled way to tell those apart is a diagnosis of the model, not of the problem. And the failure is worse for negative results than positive ones: an upper bound is at least anchored by an artifact you could run, whereas a lower bound is a claim about all possible programs and therefore depends on every idealization in the model's fine print. Quoting a lower bound without stating which operations are primitive and what was assumed about word length and storage says almost nothing.

Choosing the primitives themselves demands the same honesty. Addition earns a place as primitive; multiplication does not, because it is quickly reachable from addition and the algorithms under study do not need it as a given. The criteria applied are that the operation not be cheaply derivable from what is already there, and that the theory built on the resulting basis comes out clean rather than full of special cases. Both criteria are judgment calls, and treating them as judgment calls to be argued for openly is the difference between a model and a set of arbitrary conventions.

The transferable habit is to ask, of any abstraction that presents an operation as a single step, what that step costs when the value is large and what real component performs it. Costs hidden inside a primitive do not disappear; they reappear as the difference between a benchmark and production. The place to catch them is in the cost model, before any measurement is taken.

**Source:** [Time-Bounded Random Access Machines](../works/time-bounded-random-access-machines.md) — the introduction and machine definition, where each instruction's execution time is expressed through a length function on the numbers it touches, the logarithmic choice is justified by what a fixed-word-size machine would pay, and the case is made that idealizations about arithmetic primitives, storage, and word length must be stated explicitly when quoting general bounds. Also [An Overview of Computational Complexity](../works/an-overview-of-computational-complexity.md) — the discussion of what should count as a step, including the storage-modifying model whose surprisingly fast multiplication forces exactly this suspicion about model cheating.
