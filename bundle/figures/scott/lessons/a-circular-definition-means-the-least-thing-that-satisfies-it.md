---
type: lesson
title: "When a definition is circular, its meaning is the least thing that satisfies it"
figure: scott
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# When a definition is circular, its meaning is the least thing that satisfies it

**Lesson:** A definition that refers to the thing being defined does not, on its own, pick out a unique object. Once you have arranged for solutions to exist at all, you typically find several: the equation constrains its solutions without determining one. This is the moment where accounts of recursion usually go vague — they describe an unrolling process and let the reader's intuition supply the rest. The precise answer is that a circular definition denotes the *least* of its solutions under the ordering by information content: the object that satisfies the equation while committing to nothing the equation did not force. Everything the definition entails is present; everything else is left undefined rather than invented.

This selection principle earns its place on several grounds at once. It is canonical, so the meaning of a recursive definition is a fact rather than a choice made per case. It matches what a machine actually does, since unrolling the definition only ever produces the consequences the definition entails and never manufactures an answer for an input it fails to reach — a larger solution would be claiming behavior the program does not have. And it is constructive in the sense that matters: the least solution is available uniformly, as the value of one operator applied to the function the equation describes, so recursion stops being a special syntactic phenomenon and becomes ordinary application of a single primitive. That operator itself behaves well enough to be used inside larger expressions without breaking the properties everything else relies on, which is what keeps a system of mutually recursive definitions from needing a separate theory.

The transferable move is to notice that "underdetermined" and "ambiguous" are not the same thing. When a specification admits many models, look for an ordering on the models under which one of them is distinguished by adding nothing of its own, and adopt that as the meaning. You get determinacy without arbitrariness, and — more valuable — you get a statable relationship between the specification and every other solution, which is what turns "the implementation does something reasonable here" into a claim that can be proved or refuted. The same reading applies to any self-referential structure a system has to interpret: mutually recursive definitions, configuration that refers to itself, protocols whose meaning depends on their own outputs. Do not ask what the loop settles on; ask what the smallest fixed point is.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the treatment of a recursively declared command whose functional equation has a least solution, the argument that monotone maps on complete lattices have least fixed points, the packaging of least-fixed-point formation as a single operator that is itself continuous, and the interpretation of simultaneous recursive declarations as the least solution to a system of equations with the principal declared name selected out of the resulting tuple.
