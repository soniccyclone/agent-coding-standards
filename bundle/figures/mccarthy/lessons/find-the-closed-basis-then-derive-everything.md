---
type: lesson
title: "Look for the handful of operations that generate everything, then earn the rest by derivation instead of decree"
figure: mccarthy
works: [recursive-functions-of-symbolic-expressions, a-micro-manual-for-lisp]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Look for the handful of operations that generate everything, then earn the rest by derivation instead of decree

**Lesson:** A language can be specified as a list of features, or it can be specified as a basis: a few irreducible operations on a single data class, plus a few ways of combining them, from which every further capability is *defined* rather than added. The second discipline is enormously more powerful, and its power is measurable — with a way to take a structure apart, a way to build one up, a test for atomicity, an equality test on atoms, and a means of quoting, plus composition, conditional selection, and self-reference, the full class of computable functions is already reachable. Everything after that point — list append, association lookup, substitution, structural equality, mapping a function over a list — is a definition, not an extension to the language.

The reason to insist on this is that the two kinds of vocabulary have completely different costs. A primitive must be implemented, documented, kept consistent with every other primitive, and reasoned about separately in any proof about the language; a derived function inherits its meaning from the basis for free and cannot introduce a new semantic surprise. So the primitive set is where all the irreducible complexity of a language lives, and shrinking it is not aesthetic tidiness but a reduction of the total number of independent facts anyone — implementer, prover, or reader — has to hold. It is also how you discover that features you thought were fundamental are not: the boolean connectives, the abbreviations for repeated structural access, even the list notation itself, turn out to be sugar over the same few operations.

Two things follow for the practitioner. First, when adding capability to a system, the default question is whether it can be defined in terms of what already exists; only when the answer is genuinely no does it belong in the basis, and that admission should feel expensive. Second, the basis must be *found*, not merely chosen — McCarthy's own account is that the design arrived at its representation through repeated simplification, not by initial fiat. Expect the minimal basis of your own domain to emerge only after you have built enough on top of a larger one to see which parts were never pulling their weight.

**Source:** [Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I](../works/recursive-functions-of-symbolic-expressions.md) — the introduction of the five elementary functions and predicates, the claim that conditional expressions plus recursive definition over them reach all computable functions, and the subsequent stretch where useful list utilities are simply defined rather than declared. Also [A Micro-Manual for Lisp — Not the Whole Truth](../works/a-micro-manual-for-lisp.md), which compresses the same basis to the point where the whole of it fits on a page.
