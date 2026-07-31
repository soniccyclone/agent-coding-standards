---
type: lesson
title: "Find the floor before mapping the slope, because extra resource can buy exactly nothing"
figure: stearns
works: [hierarchies-of-memory-limited-computations]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Find the floor before mapping the slope, because extra resource can buy exactly nothing

**Lesson:** The relationship between resource and capability is usually assumed to be smooth and increasing, and it usually is not. What the analysis of storage-bounded machines exposes is a curve in two regimes separated by a discontinuity. Below a threshold, a budget can grow without bound and still purchase literally nothing beyond what a fixed finite budget already bought — a budget that grows, say, slower than the logarithm of the logarithm of the input length is, in capability terms, indistinguishable from a constant. Above the threshold the behaviour inverts completely: the faintest increase in the growth rate of the budget yields genuinely new capability, so the region is not a ladder with rungs but a continuum densely packed with distinct levels. Two regimes, one dead and one infinitely fine, meeting at a jump.

The consequence for how to spend attention is direct. Locating the discontinuity is worth more than characterising either regime, because it is the only fact that tells you whether investment can pay at all. Inside the dead zone the correct move is never incremental — no amount of additional budget helps, and the only way out is a structural change that moves the threshold, which is a different kind of decision made by different people. Above it, incremental investment is not just helpful but unusually well rewarded, since arbitrarily small increases separate arbitrarily many capability levels; here the useful question stops being whether to spend and becomes how finely you can measure what you got.

So the diagnostic order is: threshold first, curve second. Given any resource knob, ask whether there is a floor below which turning it accomplishes nothing, and find it before optimising anything. The symptom of an undiagnosed dead zone is a long history of increases that produced no measurable improvement, followed by an argument about measurement rather than about structure. The symptom of an undiagnosed dense regime is the opposite mistake — treating capability as coming in a few discrete tiers and therefore rounding your budget to the nearest tier, when in fact every increment was available to you and each one was worth something.

**Source:** [Hierarchies of Memory Limited Computations](../works/hierarchies-of-memory-limited-computations.md) — the minimal-growth results showing that below each model's threshold an unbounded budget still yields only the capability of a fixed finite one, the opening of the limit-theorems section naming the discontinuity between the two regimes, and the hierarchy theorems establishing that above the threshold the slightest increase in limiting growth defines a genuinely new capability level.
