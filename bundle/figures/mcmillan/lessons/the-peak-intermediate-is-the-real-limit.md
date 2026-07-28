---
type: lesson
title: "Never assemble the object you only need to interrogate; the peak intermediate is your real limit"
figure: mcmillan
works: [symbolic-model-checking-for-sequential-circuit-verification]
axes: [hardware-affinity, primitive-count]
subdomains: [formal-methods-and-verification, algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Never assemble the object you only need to interrogate; the peak intermediate is your real limit

Two habits in this paper reinforce each other. The first is a refusal to build things: a circuit's step relation is left as a *list* of small per-component pieces that are notionally combined but never actually combined, and the query that would have consumed the combined object is instead pushed through the list piece by piece. Where the combining operator distributes over the query, this is straightforward; where it does not, the authors find a weaker manoeuvre — pull each piece in one at a time and discard variables as soon as no remaining piece mentions them — that achieves the same end. Likewise the central set-image operation is done in a single traversal that never forms the intermediate product it is conceptually a projection of.

The second habit explains why the first matters so much: the authors state plainly that what caps the problem size is the number of nodes in the *intermediate* results, not in the final one. This is the sentence that reorganises how you think about resource use. A pipeline of operations does not cost what its output costs; it costs what its worst moment costs. Two implementations producing byte-identical answers can differ by orders of magnitude in whether they run at all, and the difference is entirely in transients that never appear in the result.

The consequences are counterintuitive in both directions, and the paper is honest about both. One of its speedups *increases* total memory while cutting time, because it makes the objects fed into the expensive step smaller even though more objects exist. Conversely, merging pieces of the step relation sometimes shrinks the stored representation and sometimes raises the asymptotic cost — the same knob helps or hurts depending on where the peak happens to sit. There is no single quantity called "efficiency" here; there is a time cost, a stored cost, and a peak transient cost, and they move independently.

A programmer who takes this seriously instruments peak usage rather than final size, and treats "materialise the joined thing, then query it" as a decision that needs justifying rather than the obvious implementation. When an operator distributes over the structure they are avoiding, they distribute it; when it does not, they look for a rewriting that lets them shed state early instead of accepting the monolith. And they stop reasoning about performance as one number, because a change that improves one of the three costs routinely worsens another.

**Source:** [Symbolic Model Checking for Sequential Circuit Verification](../works/symbolic-model-checking-for-sequential-circuit-verification.md) — the sections on partitioned step relations and the single-pass image computation, plus the remark in the pipeline experiments identifying intermediate node counts as the binding constraint.
