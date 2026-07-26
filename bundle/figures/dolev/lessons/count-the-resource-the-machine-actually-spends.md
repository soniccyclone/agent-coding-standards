---
type: lesson
title: "A tight bound on one resource says nothing about the resource that decides feasibility"
figure: dolev
works: [polynomial-algorithms-for-multiple-processor-agreement]
axes: [hardware-affinity, parallelizability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# A tight bound on one resource says nothing about the resource that decides feasibility

**Lesson:** A field can converge on a cost measure, prove a matching lower bound for it, hit that bound, and remain nowhere near a usable artifact. Fault-tolerant agreement had settled on counting synchronized rounds of exchange. Protocols existed that met the round floor exactly, and the floor was known to be unimprovable, so by the accepted measure the problem was closed. Meanwhile every one of those protocols sent a number of messages that grew exponentially in the number of failures tolerated, which meant none of them could be run. Optimality in the measured dimension had concealed impracticality in the unmeasured one.

The correction is not to replace one scalar with another but to notice that a distributed computation spends at least two separable resources, and they trade against each other. Rounds are the latency of coordination: the number of times the whole system must wait for everyone before it can proceed, bounded below by the failure budget and immune to cleverness. Messages and bits are what the interconnect actually carries, and unlike rounds they are elastic. Once counted, the elasticity becomes visible as engineering room. Holding to the round floor while forcing message cost down to a polynomial is one design point. Accepting a small constant multiple of the round floor in exchange for a much smaller message count is another, and the honest way to present that work is as a trade rather than as an improvement, with the shape of the trade left open as a question nobody has answered.

The lesson for anyone designing under a resource constraint is to name every resource whose exhaustion could stop the system, not just the one the literature or the benchmark rewards. A proven lower bound is a statement about a dimension, not about the problem; running into one is a signal to check whether the binding constraint lies elsewhere. In distributed and parallel work specifically, the dimensions that go unmeasured are usually the physical ones: bytes on the wire, round trips, memory per participant. They are the dimensions that turn a theoretically settled design into something nobody deploys.

**Source:** [Polynomial Algorithms for Multiple Processor Agreement](../works/polynomial-algorithms-for-multiple-processor-agreement.md) — the framing that prior protocols all achieved the round floor at exponential message cost, the claim that reducing message cost is what first makes the problem feasible, and the closing question about the trade between rounds and messages.
