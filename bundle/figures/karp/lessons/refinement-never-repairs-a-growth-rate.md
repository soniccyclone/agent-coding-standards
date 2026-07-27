---
type: lesson
title: "Refinement never repairs a growth rate, and a working demo on small inputs is not evidence"
figure: karp
works: [combinatorics-complexity-and-randomness]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Refinement never repairs a growth rate, and a working demo on small inputs is not evidence

**Lesson:** Karp's first professional defeat is the most useful story in the lecture because it is the failure mode every engineer repeats. His group built a circuit synthesizer full of clever shortcuts and careful refinements, and underneath all of it the mechanism was still enumerating candidates in order of increasing cost. It solved toys and never got past toys. Every shortcut multiplied the workload by a constant fraction; the workload itself was multiplying by a factor per additional input variable, and the second effect wins by an unbounded margin. He notes the same arc played out across automatic theorem proving for two decades: an initial wave of excitement as small cases fell, then a slow reckoning with what the growth curve was always going to do.

The structural reason this trap is so effective is that the small-input region is exactly where the difference between growth rates is invisible. Any two curves can be made to look alike near the origin, so the demo works, the reviews are enthusiastic, and the fatal property of the design is undetectable by the only evidence anyone has gathered. Faster hardware does not save you either, since a generation of hardware improvement buys a constant factor and an exponential mechanism consumes constant factors as though they were nothing. This is why the fix is never more optimization and never better machines. Even the more sophisticated later approaches to the same problem, Karp points out, reduced the growth without eliminating it, so they moved the wall further out rather than removing it.

What this asks of a programmer is to identify the growth rate of the core mechanism before spending any effort on its constants, and to treat performance on small inputs as carrying essentially no information about performance at scale. Measure across a range of sizes and look at the shape, not the numbers. When the shape is wrong, the honest options are to change the mechanism, to change the problem being solved, or to accept a smaller answer than exact; polishing is not on the list. And when the growth is intrinsic to the problem rather than to your approach, which is the possibility the rest of Karp's work exists to establish, then no amount of design talent is the missing ingredient and continuing to look for it is the expensive mistake.

**Source:** [Combinatorics, Complexity, and Randomness](../works/combinatorics-complexity-and-randomness.md) — the opening account of the IBM circuit synthesis program whose refinements never overcame its enumerative core, the parallel drawn to automatic theorem proving, and the later observation that improved tour-solving methods reduced but never removed exponential growth.
