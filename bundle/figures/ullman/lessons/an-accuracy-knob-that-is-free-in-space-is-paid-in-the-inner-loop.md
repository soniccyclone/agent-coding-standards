---
type: lesson
title: "An accuracy knob that looks free in the space budget is paid in the inner loop"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# An accuracy knob that looks free in the space budget is paid in the inner loop

**Lesson:** Approximate algorithms usually come with a parameter that trades accuracy against resources, and the published analysis usually prices that parameter in whichever resource the algorithm was designed to economise. When the state per unit of the parameter is a single counter, the space price is so low that the analysis concludes you could turn the knob up absurdly far. That conclusion is a statement about one resource and gets read as a statement about feasibility. It is not: the same parameter typically also multiplies the work done on every arriving item, and items are the thing there are billions of. Fixed state times a large parameter is nothing; per-item work times a large parameter times the arrival rate is the whole machine.

The general form is worth naming because it is easy to check. Every parameter has a footprint in at least two places, one charged once and one charged per unit of input, and analyses habitually report the first. So for any knob you are about to turn, ask separately what it does to the state you hold and what it does to the work you do per element, and price the second against your arrival rate rather than against your memory. A knob whose analysis says more is strictly better is precisely the knob whose real cost lives somewhere the analysis did not look — if there were no cost, the parameter would not be a parameter.

This is not a criticism of the analyses. Space is what makes a streaming algorithm publishable and space is the interesting bound, so it is properly the headline. But adopting a published algorithm means re-deriving its cost in the resource your own system is actually short of, which is frequently cycles in a hot loop, or cache residency, or the tail latency contributed by a per-item computation that is cheap on average. The re-derivation is arithmetic and takes minutes; skipping it is how a system ends up with a parameter set to a value chosen because it was free in the wrong currency.

The habit generalises past streaming to every place a quality dial exists. More replicas, more probes, more retries, more sampled traces, more validation rules, more hash functions: each is nearly free in the resource its advocate is thinking about and each lands on the per-request path. The useful question at review time is not what does this cost, but what does this cost per unit of the thing we have the most of.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 4's space-requirements discussion of distinct-element counting, which observes that one integer per hash function permits millions of hash functions for a single stream and then notes that in practice the time to compute those hash values for each arriving element is the more significant limitation.
