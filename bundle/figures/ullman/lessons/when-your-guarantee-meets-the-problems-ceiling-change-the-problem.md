---
type: lesson
title: "When your guarantee meets the problem's ceiling, stop tuning and change the problem"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# When your guarantee meets the problem's ceiling, stop tuning and change the problem

**Lesson:** Two very different numbers get compared at the end of an analysis and it is easy to conflate them. One is what your procedure is guaranteed to achieve. The other is what no procedure of that kind can exceed, for any amount of cleverness, on the problem as stated. When those two numbers coincide, something specific has happened: the remaining shortfall has been reclassified from a defect in your design into a property of the problem. Further work on the procedure is not merely likely to be unproductive, it is provably unproductive, and the correct response is to stop and go looking for a stated constraint to remove.

The chapter arrives at exactly that configuration. The improved allocation rule attains a particular fraction of the ideal, and the same fraction is the maximum attainable by any on-line procedure for the problem as defined. What follows immediately is not another allocation rule. It is a change to the problem statement: relax the requirement that the procedure know nothing about the future, by feeding it historical arrival frequencies, so it can stop hedging against futures that will not occur. That relaxation moves the ceiling, because the impossibility result was proved against procedures with no distributional knowledge, and the new procedure is not one of those.

The general instruction is to treat an impossibility result as a map of which assumption is expensive rather than as a wall. Every such result was proved by quantifying over a class of designs, and that class was pinned down by a small number of structural commitments: that decisions are irrevocable, that nothing is known about the distribution, that there is one pass, that memory is bounded, that parties cannot communicate. The productive question after a matching bound is which commitment is carrying the cost, and whether the real deployment actually has to honour it. Often it does not, and the assumption was inherited from how the problem was first written down rather than from anything in the situation.

The discipline this buys is knowing when to stop. Without the ceiling, effort on a procedure has no natural termination and teams keep tuning because tuning always feels like it might work. With it, the effort relocates to a different and usually more valuable question, which is what you are allowed to know or to defer that you had assumed you were not.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 8's statement that the generalized Balance algorithm attains a competitive ratio of one minus one over e together with the assertion that no on-line algorithm for the adwords problem as described can exceed it, followed immediately by the final observations that use historical query frequency to relax the algorithm's hedging.
