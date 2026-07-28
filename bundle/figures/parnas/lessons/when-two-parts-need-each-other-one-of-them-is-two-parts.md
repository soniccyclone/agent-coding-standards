---
type: lesson
title: "When two parts seem to need each other, one of them is really two parts"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# When two parts seem to need each other, one of them is really two parts

Mutual dependence looks like proof that the acyclic ideal is naive: here are two components that would each be visibly better off leaning on the other, so the rule must bend. Parnas reads the same situation as a message about decomposition. If A would benefit from B and B would benefit from A, then one of them is not a single thing — slice it, let A rest on the lower half, and let the upper half rest on A. The cycle disappears not by relaxing the constraint but by admitting that the original boundary was wrong, and the usual outcome is a design that started with a few strata and ends with many, because each such discovery adds one.

The same diagnostic reading applies to duplication. Finding yourself about to implement similar functionality in two places — one version that handles a fixed-size structure cheaply, another that lets the structure grow — is not evidence that structured design forces redundancy. Parnas treats the urge as a signal that he has made an error in his own thinking, and the repair is ordering rather than extraction: put the operations that create and destroy the structure above the operations that merely use it, and the duplication evaporates because the expensive general case is no longer a peer of the cheap common one.

What licenses this reading is that dependency, unlike invocation, is something you are allowed to refuse. Parnas gates each one on a small set of conditions that must all hold: the dependent must be genuinely simpler for taking the dependency; the thing depended on must not be significantly complicated by being forbidden the reverse edge; there must be some worthwhile configuration containing the lower part without the upper; and there must be no worthwhile configuration containing the upper part without the lower. That last pair is the interesting bit, because it makes the value of possible reduced configurations, not local convenience, the arbiter of whether one component may lean on another.

A programmer who internalizes this stops treating structural friction as a cost of doing business. A cycle in the dependency graph, a component that resists being placed anywhere, an itch to copy a routine — each becomes a prompt to re-cut rather than a thing to work around. The discipline is uncomfortable because it means reopening boundaries you already thought were settled, and Parnas's own account of it is that splitting happens repeatedly, mostly because you began by assuming a stratum and a unit of hidden knowledge were the same object.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — The conditions governing when one program may depend on another, the "sandwiching" resolution that follows them, and the later remark on duplication as evidence of a mistake in the designer's own reasoning.
