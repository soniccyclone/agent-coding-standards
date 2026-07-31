---
type: lesson
title: "Two optimizations that each win do not compose into a win"
figure: wirth
works: [algorithms-and-data-structures]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Two optimizations that each win do not compose into a win

**Lesson:** Two independent improvements to the same operation invite an obvious third move: take the better of the two at each step, since each is justified by an argument that no smaller step could be correct, so the larger is safe. The arithmetic of the gains does not follow the arithmetic of the safety argument. Each improvement carries setup, per-step bookkeeping and a share of the code, and combining them adds those costs while the benefits largely overlap — the situations in which the first one helps are, more often than not, situations in which the second also helps, so you pay twice and collect roughly once. There is no general reason to expect the combination to beat the better constituent, and the burden of proof is on whoever wants it, not on whoever declines it.

The sharper version of the point is about where each improvement's benefit is concentrated. An improvement whose gain is conditioned on an event tells you what to measure: how often does that event happen on the inputs you actually have. One of these two methods only gains ground when a failed attempt was preceded by a substantial partial success, and partial successes are rare in ordinary data — so its impressive worst-case guarantee buys almost nothing in the average case, which is where the combination was supposed to collect. Do this analysis for each constituent before combining anything, because it usually reveals that one of them is contributing a constant factor of overhead in exchange for protection against an input you will never receive.

The disposition to carry away is the willingness to stop at a version you can justify and say plainly that you do not know whether the more sophisticated one is better. Uncertainty about the sign of a change is itself a decisive reason not to make it, since the complexity is certain and the gain is not, and a system accumulates permanent cost from every such change while collecting only the gains that turned out to be real. The test that catches this early: for a proposed combination, name the input on which it beats both constituents, and estimate how much of your traffic looks like that. If you cannot name one, you have a more complicated program and nothing else.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — the opening of section 1.9.3, which observes that the Knuth-Morris-Pratt scheme yields genuine benefits only when a mismatch was preceded by a partial match, that matches occur much more seldom than mismatches, and that the gain in normal text searching is therefore marginal; and the section's closing discussion of the authors' suggestion to combine the two shift strategies and take the larger step, which is declined on the grounds that the additional complexity of generating two tables and of the search itself does not seem to yield any appreciable efficiency gain, that the overhead is larger, and that this casts uncertainty on whether the sophisticated extension is an improvement or a deterioration.
