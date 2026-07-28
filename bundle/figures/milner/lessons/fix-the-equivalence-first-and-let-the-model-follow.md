---
type: lesson
title: "Fix what counts as indistinguishable first, and let the model be whatever that forces"
figure: milner
works: [algebraic-laws-for-nondeterminism-and-concurrency]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Fix what counts as indistinguishable first, and let the model be whatever that forces

**Lesson:** The standard order of business is to invent a mathematical structure that programs can be mapped into, and afterwards check that the structure is faithful — that it does not identify programs a user could tell apart, and does not separate programs no user could. This paper inverts the order, and the reason it gives is the honest one: for interacting programs there was no shortage of candidate structures, there were too many, several plausible variants of each, and the abundance itself was evidence that the choice was underdetermined. Nothing in the construction of a model tells you it is the right one. So the notion of indistinguishability is settled first, in purely operational terms — what an experimenter can do to a program and what happens next — and the model is then defined as the quotient, the collection of equivalence classes. Faithfulness stops being a property to verify and becomes true by construction.

The reason this works is that indistinguishability is the thing you actually have opinions about. You can argue about whether two systems should be interchangeable by describing a situation that would tell them apart, and such arguments are settleable. Nobody has comparable intuitions about whether a domain construction is the correct one; that question can only be adjudicated by reducing it to the first. Starting from the structure means the hard question gets deferred and then answered by whichever structure was already built.

The interesting wrinkle is that indistinguishability alone is not enough, because a relation can be respected by programs in isolation and violated once they sit inside a larger program. So the object of study becomes the largest relation contained in indistinguishability that survives being placed in any context, and the meaning of a program fragment is defined as its class under that. This is the step most designs skip: they check that two components behave alike on their own and conclude they are interchangeable, when the substitutability claim requires quantifying over every surrounding program.

A practitioner working this way starts a design by writing down when two implementations of a subsystem should be considered the same, and specifically what an adversarial client is allowed to notice — timing, partial results, the ability to deadlock. Whatever data structure or interface follows is then derived rather than chosen, and the question "is my abstraction leaky" has an answer instead of a debate.

**Source:** [Algebraic Laws for Nondeterminism and Concurrency](../works/algebraic-laws-for-nondeterminism-and-concurrency.md) — the introduction's critique of picking among the many available denotational models and needing full abstraction as an afterthought, and the following section's construction of equivalence from observation relations, its restriction to the largest congruence, and the definition of a program's meaning as its congruence class.
