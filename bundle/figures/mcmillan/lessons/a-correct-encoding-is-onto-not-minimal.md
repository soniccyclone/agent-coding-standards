---
type: lesson
title: "A correct encoding is onto, not minimal"
figure: mcmillan
works: [symbolic-model-checking-10-20-states-and-beyond]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# A correct encoding is onto, not minimal

The checking engine in this paper is built for exactly one domain: the two-element Boolean one. Everything else — any finite set of values a real model might range over — is reached by translation. You supply a map from bit vectors onto your values, every relation in the original model is redefined over vectors, and a preservation result says the translated question holds of the translated model precisely when the original held of the original. The engine is never generalised. The generality lives entirely in the translation and in the theorem that the translation does not lose anything.

That is a familiar and underused architecture — a small core plus a front end that compiles into it, where the compiler's obligation is a preservation statement rather than a promise of good behaviour. The part worth dwelling on is what the obligation actually demands, because it is much weaker than the requirement most people impose on themselves. The map has to cover every value; it does not have to be one-to-one. A value may have several names. The width has to be at least enough to distinguish the values in principle, but wider is explicitly permitted and nothing in the correctness argument objects.

Programmers reflexively minimise here. Given a set of things to encode, we count them, take the logarithm, and pack. That instinct comes from a period when the bits themselves were the scarce resource, and it silently converts a *lower* bound into a target. The paper's construction shows what the slack is for: the encoding choice, together with the ordering of the resulting bits, is named as having a substantial effect on how well the whole method runs. Once minimality is off the table, the encoding becomes a free parameter to spend on making the operations you actually perform cheap — redundant tags that turn a case analysis into a mask, one-hot layouts that make a disjunction a single test, padding that keeps related fields adjacent, extra bits that let an invariant be checked locally instead of derived.

There is a diagnostic hiding in the same construction. The authors observe that for digital circuits this whole apparatus is vacuous, because the state was already in the target form — the translation layer costs nothing precisely where it is not needed. That is the sign of a well-chosen core: the intended primary case compiles to itself, and only the outlying cases pay. If your core requires elaborate translation even for the thing you built it for, you picked the wrong core.

The practice: separate the question "does this representation lose information the downstream computation needs" from the question "is this representation small," answer the first with an argument and the second with a measurement, and never let the first be settled by the second. The encoding with a spare bit in it is frequently the faster one, and it is no less correct.

**Source:** [Symbolic Model Checking: 10^20 States and Beyond](../works/symbolic-model-checking-10-20-states-and-beyond.md) — the section reducing model checking over an arbitrary finite domain to the Boolean case: the encoding function required to be surjective but not injective, the permitted use of more than the minimum number of bits, the homomorphism argument that truth is preserved, and the closing remark that encoding and ordering choices substantially affect efficiency while being trivial for circuits.
