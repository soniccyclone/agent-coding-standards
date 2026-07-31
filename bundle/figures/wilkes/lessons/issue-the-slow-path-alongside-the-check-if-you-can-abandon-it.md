---
type: lesson
title: "When a cheap check gates an expensive fallback, start both at once and abandon the loser — if abandoning leaves nothing behind"
figure: wilkes
works: [slave-memories-and-dynamic-storage-allocation]
axes: [hardware-affinity, parallelizability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# When a cheap check gates an expensive fallback, start both at once and abandon the loser — if abandoning leaves nothing behind

**Lesson:** The natural way to write a fast-path-with-fallback is a sequence: consult the cheap local structure, and if it cannot answer, go to the expensive authority. Written that way the expensive path always pays the check's latency as a prefix, even though nothing the check produces is an input to it. The dependency is not real. It is an artifact of having asked the question in one order. Issue the expensive request at the same instant you begin the check, and when the check succeeds, throw the request away. Misses then cost exactly the authority's latency instead of the authority plus the probe, and hits cost the probe plus some capacity burned at a tier that was not the bottleneck anyway. You have converted a latency problem into a throughput problem, which is the right direction whenever the fast tier is the one under pressure and the slow tier has headroom to waste.

The precondition is the whole lesson, and it is narrower than the technique's popularity suggests: the abandoned attempt must leave nothing observable behind. A read qualifies — a fetch that nobody looks at is indistinguishable from a fetch that never happened, modulo the bandwidth it consumed. A write does not. Neither does anything that allocates, charges, locks, sends, increments a counter someone else reads, or advances a cursor. Before speculating, name what the loser leaves behind; if the answer is anything at all, you are not racing two attempts, you are performing two operations and hoping one of them does not matter. This is exactly the mistake that turns hedged requests into duplicate side effects, and it hides well, because the design reads correctly in the case where the speculation wins.

Two consequences for how you specify layers. First, cancellability is a property of the lower interface, not of your policy — you can only abandon an in-flight request if the thing serving it will take an abort, so if you intend to speculate, that capability belongs in the requirements for the tier below rather than being discovered later. A layer that offers only fire-and-forget forecloses the optimization for everyone above it. Second, the same reasoning tells you when to decline: if the fast path hits nearly always, the speculation is pure waste at the slow tier, and if it nearly always misses, you should be questioning whether the fast tier earns its place instead of racing around it. The technique pays in the middle of the hit-rate range, which means the decision needs a measurement rather than a preference.

**Source:** [Slave Memories and Dynamic Storage Allocation](../works/slave-memories-and-dynamic-storage-allocation.md) — the note appended to the large-slave scheme's access sequence, observing that where the large core memory's own design allows it, an access to the large memory may be started simultaneously with the access to the fast memory and then cancelled should the fast memory turn out to hold the word.
