---
type: lesson
title: "Check whether a clever encoding is secretly parasitic on the evaluation rule you were about to change"
figure: sussman
works: [scheme-an-interpreter-for-extended-lambda-calculus]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Check whether a clever encoding is secretly parasitic on the evaluation rule you were about to change

**Lesson:** Encodings that eliminate a construct are collected as trophies, because each one shrinks the set of things the core has to know about. The danger is that an encoding is a claim relative to a set of background rules, and the rules usually go unstated — so the trophy quietly becomes a dependency. The standard case is choice. Represent the two truth values as functions that select one of their two arguments and a conditional is no longer needed: apply the value to the alternatives and it picks. That construction is airtight under a discipline where arguments reach a function unevaluated, and it collapses entirely under a discipline where arguments are evaluated first, since then both alternatives run before the selection happens and the rejected one takes effect anyway. Nothing about the encoding announces this dependence. It reads as a fact about representing booleans, when it is actually a fact about the evaluator.

The consequence is that a construct's eliminability must be re-derived, not inherited, whenever the surrounding regime changes — and the re-derivation sometimes fails. Choice is the case where it fails permanently, since selecting among alternatives means declining to compute the ones not selected, so any regime that evaluates everything eagerly must carve out at least one construct exempt from its own rule. That exemption is not a wart to be apologized for; it is where the design's actual content sits. An evaluator advertised as uniform is really a uniform rule plus an enumerated list of exceptions, and the list is short enough to read, so read it. A designer who cannot state their exceptions has not simplified their language, only their description of it.

The general habit is to treat every "X is definable in terms of Y" claim as carrying an invisible clause naming the conditions under which the definition holds, and to make that clause visible before relying on it. Reducibility results are the load-bearing walls of a minimal design, and a wall whose supporting assumption you have changed underneath it is worse than no wall, because you will keep behaving as though it holds. The check is cheap: for each encoding you depend on, ask which property of the surrounding machinery makes it work, and then ask whether anything in the current design still guarantees that property.

**Source:** [Scheme: An Interpreter for Extended Lambda Calculus](../works/scheme-an-interpreter-for-extended-lambda-calculus.md) — the reduction-order discussion in the implementation-issues section, which shows the selector-function representation of truth values working under normal order, notes that the trick depends implicitly on the order of evaluation and fails under call-by-value and in general under any other order, and concludes that a practical interpreter must therefore mix the two disciplines by making the conditional an operator exempt from eager argument evaluation.
