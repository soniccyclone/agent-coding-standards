---
type: lesson
title: "Idle capacity in one resource is usually a symptom of scarcity in another"
figure: denning
works: [thrashing-its-causes-and-prevention]
axes: [hardware-affinity]
subdomains: [operating-systems-and-systems-programming]
tags: [lesson]
---
# Idle capacity in one resource is usually a symptom of scarcity in another

**Lesson:** Denning derives how much memory is required to keep a given number of processors busy, and then reads the relation in both directions. Too little memory shows up as processors sitting idle. Too few processors shows up as memory nobody is using. In neither case does the symptom appear at the resource that is actually short. He states it flatly as a general property of the configuration: a shortage in one resource inevitably announces itself as a surplus in another.

The reasoning is that resources along a path are consumed in ratios fixed by the workload and by hardware constants, so utilization figures are not independent readings — they are one underlying quantity observed from several angles. An underused resource is either genuinely overprovisioned or blocked behind something else, and those two situations produce identical utilization numbers. Only the relation between the resources distinguishes them, which means a per-resource dashboard cannot answer the question it appears to be answering.

The practical stakes are high because the naive reading leads to the worst available action. Idle processors invite adding more work; in a memory-overcommitted system that is precisely the move that collapses throughput, and it will look like it should have helped right up until it doesn't. The correct reading is that the idleness is a memory shortage speaking through the processor meter, and the responses are to add memory or reduce load. Diagnosing a symptom at the wrong resource does not merely waste effort — it points you at an intervention that deepens the actual problem.

So: never tune a resource because its own meter looks bad. Write down the relation that fixes the consumption ratios, identify which term is binding, and intervene there. The meter that looks healthy is often the one reporting the constraint.

**Source:** [Thrashing: Its Causes and Prevention](../works/thrashing-its-causes-and-prevention.md) — the section deriving the memory requirement for a given number of busy processors and the two numbered consequences drawn from that static balance relation.
