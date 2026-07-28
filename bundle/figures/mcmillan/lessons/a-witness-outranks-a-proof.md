---
type: lesson
title: "A concrete witness outranks a proof, because it does not inherit your assumptions"
figure: mcmillan
works: [symbolic-model-checking-an-approach-to-the-state-explosion-problem]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# A concrete witness outranks a proof, because it does not inherit your assumptions

The thesis states plainly, in the middle of its industrial case study, that a counterexample may be worth more than a proof of correctness. The reasoning is epistemic rather than practical. A positive result is conditional on three things being right: that the abstraction faithfully represents the real system, that the requirement was stated correctly, and that the set of requirements is complete. Every one of those is a human judgement outside the checker's reach, and none of them is verified by the checker succeeding. A trace exhibiting a bad outcome carries none of that baggage — it is a specific sequence you can walk through, hand to a designer, and confirm against the real artefact.

The case study makes the asymmetry vivid. A deadlock was found at a depth of thirteen steps, arising from a read and a write crossing in transit between clusters, and the thesis estimates the time random simulation would need to stumble into it: somewhere between a couple of years and tens of millennia. That estimate is the second half of the lesson. The probability of sampling your way onto a particular ordering of events decays exponentially in the number of events that must line up, so for any failure whose trigger is a long coordinated sequence, sampling is not a weaker tool than exhaustive analysis — it is structurally the wrong kind of tool, and buying more of it does not close the gap.

The value of witnesses turns out to compound in a way proofs do not. Because a failed check hands back a trace, the whole workflow becomes a loop: guess a description or an invariant, get told concretely where the guess is wrong, repair, repeat. The thesis's induction chapter runs exactly this loop, arriving at a usable inductive hypothesis by reading successive counterexamples and generalising in response to each. Without the witnesses, "your guess is wrong" would be all the feedback available, and the loop would not converge. The thesis also notes the by-product: understanding a protocol well enough to state its invariant tends to make the protocol simpler, so the reasoning pays back into the design.

The engineering conclusion is to prefer, wherever you can build it, the tool that hands back a reproducer over the one that returns a verdict — and to distrust green results in proportion to how much modelling stands between your artefact and the thing being checked. Where failures require long coordinated sequences, stop scaling the sampling and change the method.

**Source:** [Symbolic Model Checking: An Approach to the State Explosion Problem](../works/symbolic-model-checking-an-approach-to-the-state-explosion-problem.md) — the cache-consistency case study, where the deadlock counterexample is presented alongside the argument that counterexamples are more valuable than correctness proofs and the estimate of how long random simulation would need.
