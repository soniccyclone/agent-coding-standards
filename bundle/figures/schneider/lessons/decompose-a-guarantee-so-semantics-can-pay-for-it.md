---
type: lesson
title: "Split a guarantee into independently weakenable parts, then let the application's semantics pay for less of each"
figure: schneider
works: [implementing-fault-tolerant-services-using-the-state-machine-approach-a-tutorial]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Split a guarantee into independently weakenable parts, then let the application's semantics pay for less of each

A general theory's real gift is rarely the general algorithm it hands you. It is the factoring — the decomposition of one expensive monolithic guarantee into named parts that can be argued about, and crucially weakened, one at a time. Requiring that all copies of a service process an identical sequence of operations is a single requirement with a single high price. Split it into two: every copy must receive every operation, and every copy must process what it receives in a common relative order. Nothing has been made cheaper yet. What has changed is that there are now two separate places to go looking for a discount, and the two turn out to be governed by entirely different facts about the system.

The discounts, once you look, are specific and mundane. An operation that reads without modifying anything does not need to reach every copy at all — one trustworthy answer is as good as many, since a read leaves no divergence behind. Operations that commute do not need a common order — the copies converge regardless of the sequence they see. Both discounts come from knowledge about what the operations *mean*, knowledge the general protocol was deliberately built not to require. The general protocol is the price of ignorance about your own workload. It is the correct starting point and almost never the correct endpoint.

Note the asymmetry that makes the decomposition the right one rather than an arbitrary one: each part lands cleanly on a different actor. Reaching every copy is something the requester's side must arrange; agreeing on order is something the copies must arrange among themselves. A factoring whose parts align with the boundaries that already exist in the system gives you two problems each owned by one place, rather than two problems that both need coordinating everywhere. Factorings that cut across the existing seams are technically valid and practically useless.

The habit worth taking: when a requirement is expensive, do not immediately look for a faster implementation of it. Look first for the conjunction it really is, name the conjuncts, and then ask of each conjunct separately whether this particular application actually needs it in full strength. Most of the large wins in a distributed system come from discovering that one of the conjuncts was never needed for half the traffic — a discovery that is invisible while the requirement remains a single word.

**Source:** [Implementing Fault-Tolerant Services Using the State Machine Approach: A Tutorial](../works/implementing-fault-tolerant-services-using-the-state-machine-approach-a-tutorial.md) — the section that decomposes replica coordination into its two constituent requirements, together with the immediately following discussion of the two standard weakenings and the remark on why that particular partition is the natural one.
