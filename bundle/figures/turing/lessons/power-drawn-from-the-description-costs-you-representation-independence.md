---
type: lesson
title: "Power drawn from how a thing is described costs you the right to treat equal things as interchangeable"
figure: turing
works: [systems-of-logic-based-on-ordinals]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Power drawn from how a thing is described costs you the right to treat equal things as interchangeable

**Lesson:** There is a tension at the heart of any system parameterized by descriptions of things rather than by the things themselves. Representation-independence is what makes a system comprehensible: two descriptions denoting the same value should be substitutable, so that reasoning about the system can be done in terms of values and nobody has to care which spelling arrived. But the extra strength a system gets from its parameter often comes from structure present in the description and absent from the value — from how the description was built, in what order, by which route. Take that structure away, and the strength goes with it. Keep it, and equal values stop behaving equally.

This is not a defect of a particular construction, it is a trade with a fixed price, and the useful move is to decide deliberately which side to buy. A system that insists on representation-independence gets clean substitution, a coherent semantics, and a hard ceiling on what it can achieve. A system that draws on the description gets more reach, and in exchange its behaviour is a function of syntax, meaning that any layer above it must expose descriptions rather than values and must document which syntactic details are load-bearing. What you cannot do is present a description-sensitive system as if it were value-based; that is where the confusing bugs live, because users reason by substitution and the system does not honour it.

For a programmer this shows up wherever an artifact is consumed as data rather than merely evaluated. Two functions with the same extension but different bodies get different optimizations, different inlining, different termination behaviour, and different results from any reflective query. Two logically equivalent schemas produce different query plans. Two equal keys with different construction histories hash apart. Two provably equivalent proofs discharge different obligations. The right response is not to pretend these coincide, and not to abandon the extra power, but to say explicitly at each interface whether it is denotational or descriptional — and to resist the temptation to expose an interface as value-based while its strength quietly depends on the shape of what was handed in.

**Source:** [Systems of Logic Based on Ordinals](../works/systems-of-logic-based-on-ordinals.md) — the completeness-questions section, whose central negative results show that a system whose strength grows with its parameter cannot also depend only on what that parameter denotes, generalized at the end of that section to essentially any reasonable notation.
