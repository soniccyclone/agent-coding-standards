---
type: lesson
title: "Judge a parallel design by its utilization on the problems you did not have in mind"
figure: wilkes
works: [computers-then-and-now]
axes: [parallelizability, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Judge a parallel design by its utilization on the problems you did not have in mind

**Lesson:** Adding parallel capacity does not by itself add power; power arrives only if the added capacity stays busy. The figure of merit is therefore the fraction of the machinery doing useful work, averaged over the workload you will actually meet — and the trap is that highly parallel arrangements tend to hold that fraction high only on the problems their designer was thinking about. Off that set the fraction collapses, often far enough that a plainer design with less capacity finishes sooner. So a parallel design evaluated on its intended workload is not evaluated at all. The measurement that means something is the one taken on problems chosen without reference to the design.

The honest conclusion from this is that parallelism at scale is bought with generality, and a designer should decide in advance how much generality they are willing to spend rather than discovering the loss later. This inverts the usual instinct that a more capable machine should be at least as good at everything: specialization toward particular problem shapes is not a defect of a highly parallel design, it is the price, and pretending otherwise produces systems marketed as general and usable only on their demonstration cases. Compare against the historical benchmark for the failure mode — a machine containing an enormous amount of apparatus of which only a fraction was ever in use on the average problem, which is exactly what low utilization across an unforeseen workload looks like from the outside.

There is a further caution about cost arguments in this shape. When the case for a parallel design rests on the falling price of its components, check whether the same price fall benefits the conventional alternative too. If it does, the cost trend is not an argument for the design at all — it is an argument for building more of whatever you were already building, and the parallel design still has to win on utilization.

**Source:** [Computers Then and Now](../works/computers-then-and-now.md) — the next-breakthrough section's treatment of hardware utilization as the binding constraint on parallel systems, its point that such systems are efficient mainly on their designer's own problems, the resulting acceptance of greater specialization, the ENIAC comparison, and the note that falling component cost would help conventional processors equally.
