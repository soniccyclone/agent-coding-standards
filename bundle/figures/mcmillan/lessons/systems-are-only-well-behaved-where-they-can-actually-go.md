---
type: lesson
title: "Systems are only well behaved where they can actually go"
figure: mcmillan
works: [symbolic-model-checking-an-approach-to-the-state-explosion-problem]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Systems are only well behaved where they can actually go

One of the thesis's most useful observations arrives as a surprise in the middle of an experiment. A round-robin arbiter, structurally simple, was verified quickly for most of its requirements but one property doubled in cost with each cell added. The cause turned out to be that the property's meaning, expressed over *all* configurations, embeds a rotation comparison between two bit vectors — and rotation is one of the known functions for which no variable order gives a compact decision diagram. But the arbiter can never actually be in most of those configurations. Its token vector always holds exactly one token, so the rotation question never arises in reality. Computing the reachable configurations first and confining every later step to them made the cost polynomial.

The generalisation the thesis draws is that engineered artefacts tend to be tame in the region reachable from their starting state and arbitrarily nasty outside it. This should not be surprising once stated: the designer only ever reasoned about reachable behaviour, so that is the only region where the invariants that make the thing comprehensible actually hold. Any analysis that quantifies over the whole configuration space is therefore analysing a much wilder object than the one that exists, and paying for the difference.

There is a chicken-and-egg trap here that the thesis names and escapes. Restricting to reachable configurations requires knowing them, and computing them requires the step relation over the full space — the very thing you were trying to avoid representing. The way out is to stop treating the step relation as one static object and instead re-derive it at each round, accurate only over the newly-discovered frontier. That reframing turns a global object you cannot afford into a sequence of local ones you can, and it works because each round only ever asks about the states it just found.

The habit worth taking is to treat reachability as a first-class precondition on analysis rather than an optimisation. Before concluding a problem is intractable, ask whether the intractability lives in configurations the system can enter — profile against reachable state, type away the unreachable rather than defending against it, and be suspicious of any worst case whose witness your system cannot construct. And when the reachable set is itself expensive to obtain, look for the incremental formulation that only ever needs the part of the machinery touching what you have already found.

**Source:** [Symbolic Model Checking: An Approach to the State Explosion Problem](../works/symbolic-model-checking-an-approach-to-the-state-explosion-problem.md) — the synchronous arbiter experiment where a fairness property provoked exponential blowup over all configurations, the resulting decision to compute reachable configurations first, and the frontier-restricted step relation introduced for the asynchronous mutual-exclusion example.
