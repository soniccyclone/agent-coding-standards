---
type: lesson
title: "State your ignorance as precisely as your knowledge, and map which unknown carries the others"
figure: stearns
works: [on-the-computational-complexity-of-algorithms]
axes: [cognitive-load, verifiability]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# State your ignorance as precisely as your knowledge, and map which unknown carries the others

**Lesson:** A body of results has two boundaries: the conditions under which a positive answer is known, and the conditions under which a negative one is. Between them lies a gap, and the discipline is to write that gap down as sharply as the two theorems that bound it — as an explicit region of the parameter space, not as a vague admission that more work is needed. Doing so converts an absence into an object other people can attack. It also forces honesty about the shape of the ignorance: whether the gap is a small technical annoyance or a wide band containing the cases anyone would actually care about. Stating a belief about which way the gap resolves, clearly labelled as belief, is part of the same discipline, because a conjecture is a target and a silence is not.

The higher-value move is to map how the unknowns depend on each other. When the argument that establishes the headline result routes through a technical lemma, the strength of the result is limited by the strength of that lemma, and saying so out loud converts two apparently separate open problems into one: any improvement to the lemma automatically improves the headline. That is enormously useful information for allocating effort, because it identifies the load-bearing unknown among a list of interesting ones. It also predicts which line of attack cannot possibly work — if the current technique is bounded by the lemma, no amount of polishing the technique closes the gap, and the honest statement is that a different approach will be needed.

There is a third kind of ignorance worth naming, which is when your framework cannot yet even express a concept you were assuming it had. A framework built to certify that something is achievable within a budget does not, by itself, let you say that a budget is the cost of a problem rather than merely an achievable bound for it; expressing that requires defining a separate collection and then admitting you do not know whether it is ever nonempty. Discovering that you cannot say the thing you thought you were saying is a more important result than most theorems, and burying it is how a field acquires vocabulary it cannot cash.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the problems-and-open-questions section, which states the gap between the containment corollary and the separation theorem as an explicit limit condition together with the authors' stated inclination about how it resolves and their judgement that a better approach will be required; notes that improving the single-band simulation would automatically improve the separation theorem; and defines the collection of sequences for which a given bound is a genuine lower bound while asking whether it is ever nonempty.
