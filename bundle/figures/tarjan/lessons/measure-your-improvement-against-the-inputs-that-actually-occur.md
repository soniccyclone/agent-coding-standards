---
type: lesson
title: "Measure the improvement against inputs that actually occur, and publish the result even when it goes against you"
figure: tarjan
works: [a-data-structure-for-dynamic-trees]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Measure the improvement against inputs that actually occur, and publish the result even when it goes against you

**Lesson:** The paper's central claim is an asymptotic improvement on the fastest known method for a well-studied problem. The authors then report that they implemented it, raced it against the method it supposedly beats, and lost by roughly a factor of two on everything except graphs deliberately constructed to be bad for the rival — and they explain why: the rival's pathological inputs are a vanishing fraction of the inputs anyone generates, so the rival almost never pays the cost that the new method is designed to eliminate. An asymptotic win is a statement about the tail of the input distribution. If your traffic does not live in that tail, the constant factor is the entire story, and a structure with more fields, more pointer chasing, and more bookkeeping per step will lose despite being provably better.

The reasoning generalizes into a discipline about what an optimization is actually being asked to do. Before adopting an asymptotically superior method, characterize the inputs the system really sees and ask whether they trigger the behavior being optimized away. If they do not, you are buying insurance, and insurance should be priced as insurance rather than as speed: the question becomes whether an adversary can steer you into the tail, or whether a rare slow case would violate a real obligation, not whether the exponent is smaller. Both answers are legitimate reasons to pay. What is not legitimate is adopting the better bound and reporting it as a speedup, because the measurement will not agree and someone will eventually make that measurement.

The methodological half of this is the harder half: the authors ran the experiment that could embarrass their own result, and put its outcome in the paper next to the theorem. A theoretical result and a measurement that contradicts its practical reading are not in conflict — they are two different facts, and suppressing the second does not make the first more true, it only guarantees that the first gets misapplied. The same posture appears elsewhere in the same paper, where a variant that achieves a stronger guarantee is labeled by its own authors as likely slower in practice and mainly of theoretical interest. Reporting the limits of your result alongside the result is what makes it usable, and the appetite to run the test that might go against you is a better predictor of trustworthy engineering than any amount of proof.

**Source:** [A Data Structure for Dynamic Trees](../works/a-data-structure-for-dynamic-trees.md) — the closing remarks reporting an implementation of the maximum-flow application, its measured loss by a small constant factor to the older method it asymptotically beats, the explanation that only a small fraction of randomly generated graphs make the older method perform poorly, the call for further empirical work on the other applications, and the earlier statement that the worst-case variant is more complicated, likely slower in practice, and mainly of theoretical interest.
