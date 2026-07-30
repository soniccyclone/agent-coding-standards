---
type: lesson
title: "Keep the notation and the thing it denotes apart, because equivalence is a question about meanings"
figure: scott
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Keep the notation and the thing it denotes apart, because equivalence is a question about meanings

**Lesson:** The cleanest illustration of what a semantics is for is the gap between numerals and numbers. Numerals are strings in a particular notation; numbers are abstract objects the strings are about. The distinction looks pedantic until you notice what depends on it. Many different notations convey the same concepts, and within one notation many different expressions denote the same thing — and deciding *which* expressions are interchangeable is not something syntax can settle, because the answer depends on what the expressions mean. You need the objects, not just the strings, even to state the claim that two programs are equivalent, let alone to prove it.

What makes the confusion so easy to fall into is a canonical naming system. When every object has exactly one preferred spelling, the reduced spellings sit in one-to-one correspondence with the objects, and it becomes almost irresistible to treat the spelling *as* the object. For a while nothing goes wrong, since the notationally bound thinker and the clear-headed one give the same answers. The tell shows up in method rather than results: someone who has fused notation with concept feels obliged to specify every operation as a manipulation of symbols, because symbols are the only things they believe are really there. And the moment the domain admits no complete canonical notation, or you want the same account to cover several structures with different normal forms, the fused view has nothing left to stand on.

Two working consequences. First, the definition that maps expressions to meanings is not circular busywork even when it looks like it merely restates the obvious — its content is the explication of exactly what the notation contributes, which is often a genuine and clever invention that the underlying concepts do not imply. Second, whenever you catch yourself reasoning about a system entirely in terms of transformations on its text, ask what the text denotes and whether the transformation is justified at that level. Rewriting rules that happen to be right are worth less than rewriting rules you can prove are right, and the proof has to happen where the meanings live.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the introductory contrast between numerals and numbers, the argument that explaining equivalences of expressions is too important to leave to syntax, the diagnosis of the notationally bound thinker who must specify everything by symbol manipulation, and the observation that a positional notation is a discovery of language not implied by the concepts it names.
