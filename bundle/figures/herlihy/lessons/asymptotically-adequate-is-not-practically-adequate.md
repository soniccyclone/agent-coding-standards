---
type: lesson
title: "A guarantee that is sound in the step-counting model can be the wrong engineering choice; go measure"
figure: herlihy
works: [a-methodology-for-implementing-highly-concurrent-data-objects]
axes: [hardware-affinity, parallelizability]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, algorithms-and-complexity]
tags: [lesson]
---

# A guarantee that is sound in the step-counting model can be the wrong engineering choice; go measure

**Lesson:** Theory about concurrency counts steps taken by participants. Hardware charges for something the step count cannot see: traffic on the interconnect. That gap is not a detail, it inverts conclusions. A lock-free protocol and a spin lock both let exactly one participant make progress at a time, so by step counting they should be comparable — but the participants waiting on a lock spin on a cached copy and generate no traffic at all, while the participants retrying an optimistic update all keep hammering shared memory. Measured on a real multiprocessor, the naive lock-free version loses to the crude spin lock badly, for a reason no amount of theory would have surfaced. Adding randomized backoff between retries reverses the outcome. Neither the loss nor the reversal was predictable from the model in which the protocol was proved correct.

The second measured surprise is more uncomfortable, because it concerns the guarantee itself. Upgrading from "somebody always progresses" to "everybody always progresses" is a strictly stronger promise, and getting it requires participants to publish their pending requests and execute each other's work, which means every operation now scans and copies per-participant bookkeeping. The measured overhead of that bookkeeping is substantial, and the starvation it deterministically prevents was already almost entirely eliminated by the randomized backoff added for unrelated reasons. So the honest recommendation is that a probabilistic remedy may be the better buy than the deterministic guarantee — a conclusion available only by building both. The step-counting model can tell you a guarantee is achievable; it cannot tell you the guarantee is worth its price, and the strongest available guarantee is not automatically the right one.

What this asks of a programmer is unglamorous and rare: build the prototype, measure it against the incumbent technique on real hardware, and publish the comparison including the parts that lose. The paper's own measurements show the sophisticated spin lock still ahead by roughly a factor of two when every participant has a dedicated processor and nothing ever stalls — and it says so, while noting that this is precisely the scenario in which the costs of avoiding waiting are visible and the benefits are not. Choosing your benchmark to be maximally unfavorable to your own proposal, and then reporting the number, is what makes a performance claim mean anything. The corresponding failure mode is to compare against a straw incumbent; the same backoff that rescued the new technique also improves the old one, and only comparing tuned against tuned tells you anything.

**Source:** [A Methodology for Implementing Highly Concurrent Data Objects](../works/a-methodology-for-implementing-highly-concurrent-data-objects.md) — the prototype benchmark on a shared priority queue, the memory-contention explanation for why the naive protocol loses to a spin lock, the effect of exponential backoff on both throughput and starvation, the measured overhead of the operation-combining technique with its concluding preference for the probabilistic remedy, and the stated choice to benchmark under conditions where delay never occurs.
