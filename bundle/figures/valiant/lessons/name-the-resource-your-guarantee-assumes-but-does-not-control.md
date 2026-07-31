---
type: lesson
title: "Name the resource your guarantee assumes but cannot control, then notice that starving it is itself a mechanism"
figure: valiant
works: [evolvability]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Name the resource your guarantee assumes but cannot control, then notice that starving it is itself a mechanism

**Lesson:** Every convergence claim divides its resources into two piles that are worth separating explicitly: the ones the process sets for itself, and the ones supplied from outside. The first pile is design. The second pile is assumption, and any guarantee that leans on it is conditional whether or not the condition is written down. So when you say a process reliably reaches its goal, the honest form of the statement names the externally furnished quantity and the threshold it must clear — how many observations per decision, how much throughput, how many replicas responding — and admits that below that threshold the guarantee is void rather than merely degraded. This is not pedantry about preconditions. The process cannot detect that it is below threshold, because detecting it would require the very measurement precision that is missing, so the failure is silent by construction.

The interesting turn is that the failure mode is useful. Shrink the externally supplied measurement budget and the process's comparisons become noisy; noisy comparisons misclassify losing moves as acceptable ones; and a process that occasionally accepts a real loss can leave a state that the reliable version could never leave. The knob that governs trustworthiness is therefore the same knob that governs escape, in opposite directions, and a schedule that varies it deliberately gets both — precise measurement while there is still gradient to climb, deliberate imprecision to break out and begin again somewhere else. Which means the capability you carefully excluded from the model by bounding one parameter reappears, legitimately, through a different one, and the model has to say so. What looked like a purity condition on the definition turns out to describe two operating regimes rather than a correct one and a broken one.

The habit worth carrying: for any adaptive loop, write down what determines the resolution of its feedback, ask who supplies it, and then ask what the loop does at both extremes of that quantity. Systems that behave one way under generous measurement and another way under scarce measurement are the normal case, not a pathology, and the transition between the two is where the surprises live. A loop tuned and validated in a high-resolution environment can be a substantially different loop in a thin one — still running, still reporting improvement, exploring instead of converging.

**Source:** [Evolvability](../works/evolvability.md) — the closing remark of section 3 that the population size, which bounds the number of experiences available per candidate, is the aspect outside the control of the evolution algorithm itself, so convergence is guaranteed only when that quantity is adequate; together with the variable-population variant described earlier in the same section, where a small sample makes low-performance mutations appear neutral or beneficial and thereby permits the reinitialization the main definition forbids, and section 6's observation that large populations serve reliable detection of small improvements while small ones serve the adoption of deleterious steps.
