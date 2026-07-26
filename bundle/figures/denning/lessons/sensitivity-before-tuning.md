---
type: lesson
title: "Differentiate before you tune: a large hardware ratio can leave no safe operating margin at all"
figure: denning
works: [thrashing-its-causes-and-prevention]
axes: [hardware-affinity, parallelizability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Differentiate before you tune: a large hardware ratio can leave no safe operating margin at all

**Lesson:** The most transferable thing in this paper is a derivative, not a policy. Useful work per unit of elapsed time is a simple function of two things: how often you miss, and how much a miss costs relative to a hit. Write that function down and differentiate it with respect to the miss rate. In the comfortable regime, where the miss rate times the miss cost is still well under one, the whole miss cost shows up undamped in the slope: one unit of added miss rate subtracts roughly a full miss-cost worth of efficiency. When a miss costs four orders of magnitude more than a hit — which is what a mechanical storage device against electronic memory amounted to, and what a network round trip against local memory amounts to now — efficiency near the good operating point is not merely sensitive to the miss rate. It is a cliff face. Only once the product has grown past one does the denominator start to soften the slope, and by then the good operating point is already behind you.

The consequence overturns an intuition strong enough that Denning bothers to name it. Adding one more unit of work to a nearly-full system feels like it should degrade service gradually, each arrival taking a proportional share. He shows the opposite by a small conceptual experiment: with a large enough speed gap, the one arrival past the limit takes aggregate throughput to nearly nothing, because the small increase in miss rate it forces on every resident program gets multiplied by the enormous miss cost. There is no gentle slope to ride down, which means there is no region in which a soft, reactive policy has time to work.

That is the design conclusion, and it is stronger than "be careful." Where the derivative is this steep, the policy has to be a hard bound computed in advance, not a feedback loop. A controller that notices degradation and reacts is too late by construction, because the collapse is faster than the observation that would trigger the correction. So admission must be refused ahead of time against a precomputed criterion — is there room for this unit's memory claim — and a reserve must be held back for claims that grow unexpectedly, because a system running exactly at its computed requirement has no room for the first surprise.

A programmer who has internalized this does one calculation before joining any argument about eviction rules: given the ratio between my hit path and my miss path, how much does throughput move per unit of miss rate? The number decides whether a soft policy is permissible at all. If it is a cliff, stop optimizing the rule and go build the admission bound.

**Source:** [Thrashing: Its Causes and Prevention](../works/thrashing-its-causes-and-prevention.md) — the steady-state efficiency derivation and its derivative, followed by the thought experiment introducing one program beyond saturation, and the section drawing the cures from that sensitivity.
