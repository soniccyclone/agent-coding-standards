---
type: lesson
title: "To generalise over sizes, compare with an ordering rather than an equivalence"
figure: mcmillan
works: [symbolic-model-checking-an-approach-to-the-state-explosion-problem]
axes: [expressiveness, verifiability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# To generalise over sizes, compare with an ordering rather than an equivalence

Having verified a protocol for a fixed number of participants, the natural question is whether that number was enough to stand for any number. Earlier attempts answered it by exhibiting an equivalence between the small configuration and the large one, and the thesis shows why that route is cramped. If your comparison relation must preserve *every* property expressible in your logic, then it preserves negations too, and preserving a property and its negation in both directions collapses the relation into mutual indistinguishability. You end up able to relate only systems that are already interchangeable — useless, because adding participants genuinely changes a system.

The fix is to give up symmetry deliberately, in two coordinated moves. Restrict attention to the fragment of the logic that talks only about what happens on all executions, dropping the ability to assert that some execution exists; then the appropriate relation is one-directional — the larger thing is more constrained than the smaller — and it is reflexive and transitive without being an equivalence. That is enough for an induction: show the composition operators respect the ordering, show one candidate absorbs itself plus one more participant, and every size follows. The general framing the thesis offers is that you should choose the class of properties you want preserved *first* and let the ordering be defined by that choice, rather than picking a familiar relation and discovering afterwards which properties survive.

The technique for finding the candidate is the counterintuitive part and the most portable. You start from the concrete component and make it *less* determinate — adding permitted behaviours until it can account for anything two of them could do between them. Each failed attempt returns a specific behaviour the candidate cannot produce, and you widen it to admit that. The fixed point of this widening is the inductive hypothesis. The thing you end up reasoning about is thus strictly vaguer than the real component, and that vagueness is precisely what lets one of it stand in for arbitrarily many.

There is an honest cost, and the thesis states it. Because the ordering only preserves all-executions properties, the existence claims — such as "a participant can always eventually proceed," which is how deadlock freedom was expressed — are not carried across. Getting those would demand the symmetric relation whose collapse forced this design in the first place. That is the shape of the trade: one-directional comparison buys generalisation over size and spends the ability to conclude that something remains possible. Knowing which half of your requirements survive an abstraction is part of using it.

**Source:** [Symbolic Model Checking: An Approach to the State Explosion Problem](../works/symbolic-model-checking-an-approach-to-the-state-explosion-problem.md) — the induction chapter: the argument that preserving the whole logic degenerates into indistinguishability, the substitution rules over a pre-order, and the counterexample-driven widening of a component into a usable invariant.
