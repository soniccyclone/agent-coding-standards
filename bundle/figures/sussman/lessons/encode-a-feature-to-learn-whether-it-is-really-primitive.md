---
type: lesson
title: "Try to encode a feature in your core, and let the locality of the encoding tell you whether it belongs there"
figure: sussman
works: [lambda-the-ultimate-imperative]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Try to encode a feature in your core, and let the locality of the encoding tell you whether it belongs there

**Lesson:** If your core language is universal, then every feature can be encoded in it, and that fact carries no information whatsoever. Reducibility-in-principle is the cheapest possible claim and settles no design question. The informative question is what the encoding *costs*: whether the translation of each construct is a local rewrite that leaves surrounding code untouched, whether the translated program is the same size as the original, and whether a reader can still see the original structure in the result. Loops, sequencing, jumps, variable assignment, dynamic scoping and call-by-name all pass that test — each becomes a small pattern of function application, binding and tail transfer, and the global shape of the program survives the rewrite. Two constructs fail it: non-local escape, and assignable references to arbitrary places inside data. Their encodings are pervasive rather than local, forcing every value in the program to be rebuilt as a pair of accessor procedures.

Read that failure as a measurement, not an embarrassment. When a feature's encoding stops being local, the honest conclusion is that the core mechanism does not actually subsume it, and if you want the feature you should install it as a primitive instead of pretending the encoding is an explanation. Locality of translation is therefore a usable criterion for what deserves a place in a small basis: a construct that dissolves into a local pattern was never a separate concept, and one that resists dissolution is a genuine addition to the vocabulary. This is a sharper test than counting primitives, because it distinguishes the features that were sugar all along from the ones doing real work.

The method generalizes past language design to any layered system. Whenever you are deciding whether to add an operation to an interface or build it out of what is already there, do not stop at "it's expressible." Write the expression and look at its shape: if callers can use the existing pieces with a small local idiom, the interface is already complete; if every caller must restructure its own data or thread something through code that has no interest in it, the interface is missing an operation. The size and locality of the workaround is the evidence, and it is available before you commit.

**Source:** [Lambda: The Ultimate Imperative](../works/lambda-the-ultimate-imperative.md) — the conclusions, where the authors dismiss universality as unsurprising and rest their case on the naturalness, locality and size-preservation of the translations, then single out escape expressions and general assignable references as the two cases whose non-local transformations indicate they are not subsumed and should be primitives.
