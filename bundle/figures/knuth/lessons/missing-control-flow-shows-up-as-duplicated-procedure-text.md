---
type: lesson
title: "The primitives a notation lacks are visible as duplication in everything written in it"
figure: knuth
works: [ancient-babylonian-algorithms]
axes: [primitive-count, expressiveness]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# The primitives a notation lacks are visible as duplication in everything written in it

**Lesson:** Knuth's survey of the tablets finds essentially no branching and almost no looping across the whole surviving corpus, and the interesting part is what the scribes did instead. Where we would write a conditional, they wrote two complete procedures, one per case, differing only at the point where the case mattered — the same operation sequence twice, once specialized to a zero parameter. Where we would write a loop, they wrote the iterations out end to end: a compound-interest problem advances five years, then five more, then five more, doubling a running figure each time, until the term is reached. Nothing is hidden and nothing is wrong. The procedures are correct and complete. They are simply proportional in length to the number of cases and iterations rather than to the number of distinct ideas they contain.

This gives you a diagnostic that runs in the opposite direction from the usual one. Normally you evaluate a language by asking what it lets you say. Here you infer the language by looking at the shape of the redundancy in its texts: repeated near-identical passages are the negative image of an absent abstraction, and the axis along which the copies differ names the abstraction that is missing. The two nearly identical case procedures are a conditional the notation could not hold; the unrolled interest calculation is a loop the notation could not hold. Duplication is not a discipline failure in these texts — it is the only available encoding, and it is legible as such.

Knuth also traces why the branching primitive was unavailable, and the reason is upstream of control flow entirely. The tests we reach for first — is it zero, is it negative — were unaskable, because the number system contained neither zero nor negative quantities as objects. The set of predicates you can write is bounded by the set of values your data model admits, so a gap in the value domain propagates outward into a gap in the control structures, which propagates outward into structural duplication in the source. Three levels of consequence from one missing primitive.

The working conclusion for a programmer is to read repetition as a measurement rather than a mess. When the same shape appears three times in a codebase, the useful question is not "who copied this" but "what construct would have let this be written once, and why was it not reachable here" — sometimes the language genuinely lacks it, more often the data model in play does not represent the distinguishing state as a value you can dispatch on. Fixing the copies without fixing the value domain that forced them produces a different arrangement of the same duplication.

**Source:** [Ancient Babylonian Algorithms](../works/ancient-babylonian-algorithms.md) — the section on conditionals and iteration, which reports the near-total absence of both, the substitution of per-case procedures and fully written-out repetitions, and the connection to the missing zero and negative numbers.
