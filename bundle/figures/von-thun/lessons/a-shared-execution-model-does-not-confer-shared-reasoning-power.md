---
type: lesson
title: "A shared execution model does not confer shared reasoning power"
figure: von-thun
works: [joy-forths-functional-cousin]
axes: [verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# A shared execution model does not confer shared reasoning power

Two systems can agree on their entire operational story and still differ
completely in what you are licensed to conclude about programs written in them.
Von Thun is explicit that the central semantic principle of Joy — that placing
programs next to each other means composing the functions they denote — holds
equally of the purely functional part of Forth. The stack discipline is the same,
the postfix reading is the same, the substitution rule for ordinary
side-by-side code is the same. And yet the second half of the rule, the one that
lets you swap a deferred program for an equivalent deferred program, has no
counterpart in Forth, because Forth has no principled mechanism for taking a
piece of held-back code and running it.

This holds because reasoning power comes from the availability of rules, not from
the behavior of executions. Two languages that run the same way can still differ
in whether a given rewrite is always valid, and a rewrite you cannot justify is a
rewrite you cannot use — in a proof, in a refactoring, or in a compiler. Deferred
code is the sharp case: the moment a program can be stored rather than run, you
have an opaque region where equivalence of meaning no longer implies
interchangeability, and you get that region back only by having a well-defined
way to reopen it. A language that lets you build up deferred code but offers no
disciplined way to make it active again has bought flexibility at the price of an
inference rule.

This is also why the distinction between convergent invention and deliberate
derivation is not merely historical. Arriving at a structure by taste gets you the
behavior; deriving it from a formal account gets you the behavior plus the
theorems, and the theorems are what let anyone other than the original author
manipulate the code with confidence. The extra work is not decoration — it is the
difference between a system you can only run and a system you can also reason
about.

A programmer who has internalized this stops reading feature comparisons as the
whole story and starts asking what each system lets them prove. When evaluating a
design, they look specifically for the opaque contexts — anything that captures
code or configuration for later — and ask whether there is a defined operation
that makes the captured thing active on known terms. Where there is not, they
expect to lose the ability to refactor safely across that boundary, and they plan
for that loss rather than discovering it.

**Source:** [Joy: Forth's Functional Cousin](../works/joy-forths-functional-cousin.md) — the mathematical-foundations section written for a Forth audience, which grants the concatenation-is-composition principle to Forth's functional fragment and then notes that Forth has no equivalent of the combinator mechanism licensing substitution inside quotations.
