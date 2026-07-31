---
type: lesson
title: "Find the form every term reduces to: it is what makes the laws few and the implementation direct"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [primitive-count, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Find the form every term reduces to: it is what makes the laws few and the implementation direct

**Lesson:** Once a notation has a handful of constructs, the useful question is whether every expression in it can be rewritten into a single shape. When the answer is yes, three things become cheap at once. Equality gets a decision procedure: two expressions denote the same thing exactly when their normal forms match component by component, so proofs of identity become structural comparisons instead of arguments. The law set collapses, because a law stated about the one form covers everything, and the degenerate constructs — the do-nothing, the single-step — are recovered as parameter values rather than needing laws of their own. And the implementation stops being a case analysis over the syntax and becomes a direct realization of the form itself.

The last point is worth dwelling on, because a good normal form usually tells you what the thing *is*. If every term reduces to "here is the set of things available now, and for each of them, here is what remains afterwards," then the object being defined is precisely a function from available things to continuations, and an implementation in any language with functions as values is a transcription rather than a design. Something that resists reduction to such a form is a signal in the other direction: either the construct is genuinely more powerful than the rest and you should know that explicitly, or the notation has accumulated a feature that is not pulling its weight.

Two dividends follow that are easy to overlook. The executable version of the normal form is immediately an exploration tool — show what is currently available, accept one of them, show what is available next — which lets a design be tried by hand long before anything is built, and which surfaces states offering nothing at all as an observable fact rather than a deduction. And unbounded, recursively-defined objects fit without special handling, provided each is guaranteed to commit to a step before recurring, since that guarantee is exactly what lets a recursive definition be unfolded one level into the normal form on demand. The normal form does not need to be finite; it needs to be reachable one step at a time.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the laws and implementation sections of the chapter on processes, where the first law equates two processes exactly when their initial menus coincide and their continuations agree for each item, yielding the inequalities and commutativity of choice as corollaries; and the following section, which observes that every process expressible so far can be written as a menu set together with a function from each item to subsequent behaviour, with the empty and singleton menus covering the stopped and prefixed cases, unfolds guarded recursions into that form, and renders it directly as a function in a functional language along with a menu-listing routine and an interactive explorer driven by keyboard input.
