---
type: lesson
title: "Optimal means nothing until you name the resource, and the winner on one resource can be absurd on another"
figure: fischer
works: [a-lower-bound-for-the-time-to-assure-interactive-consistency]
axes: [parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---

# Optimal means nothing until you name the resource, and the winner on one resource can be absurd on another

**Lesson:** In a distributed setting, "how long does this take" splits into resources that do not trade off smoothly against each other. Latency is counted in rounds of mutual waiting. Bandwidth is counted in how much has to move. Storage is counted in what each participant must retain to interpret what arrives next. A bound proven against one of these says nothing about the others, and an algorithm that provably cannot be beaten on rounds can require an amount of traffic that grows so fast in the number of tolerated faults that nobody would ever run it. Matching a lower bound is therefore evidence about one dimension of a design, not a verdict on the design.

This matters because the round count is the metric that is easiest to prove things about and the least likely to be what hurts you. Rounds are a clean combinatorial quantity; message volume and per-participant state are messier, so the literature and the folklore both drift toward the clean one. The honest posture is to hold the resources apart in your head, state which one a given result constrains, and treat the remaining ones as open — which is exactly what it means to leave, as an explicit open question, whether the round-optimal scheme's traffic can be brought down to something polynomial while keeping the round count.

The habit this produces is small and useful: before optimizing, write down the resource vector you care about and which component actually binds in your deployment. A latency-bound service and a bandwidth-bound one want different algorithms even when both are solving the identical coordination problem, and a result proving one of them cannot improve tells the other nothing at all. It also keeps you honest when reading benchmarks and bounds alike — an unqualified claim of optimality is a claim with a hidden argument, and the hidden argument is usually the choice of metric.

**Source:** [A Lower Bound for the Time to Assure Interactive Consistency](../works/a-lower-bound-for-the-time-to-assure-interactive-consistency.md) — the framing of rounds as the sole complexity measure of interest for the bound, and the closing open question observing that the round-minimal scheme moves an amount of data exponential in the fault bound and asking for a communication-efficient alternative.
