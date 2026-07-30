---
type: lesson
title: "The shortest description and the affordable one are different things, so carry the time budget in the definition"
figure: kolmogorov
works: [three-approaches-to-the-quantitative-definition-of-information]
axes: [hardware-affinity, cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# The shortest description and the affordable one are different things, so carry the time budget in the definition

**Lesson:** A measure of description length says nothing about how long the description takes to unfold. An object can have a tiny generator that only reaches it after a computation nobody will ever wait for, so "this thing is simple" and "this thing is cheap to obtain" are separate claims and the first does not imply the second. Anyone optimizing for minimal specification is silently trading a resource that the metric does not report — and the trade can be unbounded, because there is no ceiling on how much work a short program may do.

The repair is not to abandon minimality but to parameterize it. Ask for the shortest description obtainable subject to a stated bound on effort, and you get a family of measures indexed by what you are willing to spend. Relax the bound completely and you recover the pure size measure as the limiting case, which is the correct relationship between them: unbounded minimality is the idealization at the end of a real spectrum, not the practical point on it. Every serious use of the metric names its own budget.

The engineering form of this shows up wherever compression, generalization, or factoring is treated as an unqualified good. Data folded into a rule must be unfolded at read time. Duplication collapsed into a parameterized abstraction is re-expanded at every call. A configuration reduced to a generator is a computation someone pays for at startup. None of these is wrong, and each is wrong when done past the point the budget allows, which is invisible to a metric that counts only size. Keep both numbers in view — how small can the statement of this be, and what does it cost to run — and treat any argument that cites one while ignoring the other as incomplete, whichever side it is arguing for.

**Source:** [Three Approaches to the Quantitative Definition of Information](../works/three-approaches-to-the-quantitative-definition-of-information.md) — §4, which names the neglect of a program's difficulty as the important disadvantage of the §3 construction, notes that objects of very small complexity can be recoverable by short programs only through computations of thoroughly unreal duration, and sketches a complexity relative to a permissible difficulty of which the earlier measure is the unconstrained minimum.
