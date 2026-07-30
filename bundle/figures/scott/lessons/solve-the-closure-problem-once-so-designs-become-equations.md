---
type: lesson
title: "Solve the closure problem once, and each specific design collapses into an equation"
figure: scott
works: [outline-of-a-mathematical-theory-of-computation]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Solve the closure problem once, and each specific design collapses into an equation

**Lesson:** Faced with a class of systems to describe, there are two places to put the effort. One is to describe each system: enumerate its kinds of thing, say how they interact, repeat for the next system. The other is to identify a small set of operations that build new descriptions from old ones — pairing, alternation, and the space of maps between two descriptions is a surprisingly sufficient set — prove that the class is closed under all of them, and prove that equations written with them have solutions. The second is much harder up front and it changes what describing an individual system costs. Once the closing work is done, a specific design is stated as an equation whose unknowns are its own kinds of thing, and the existence of the design is a corollary rather than a new investigation.

What that looks like in practice is worth being concrete about. The values of a language with stores, commands, procedures, and lists are pinned down by saying that a value is a number or a location or a list of values or a command or a procedure, where commands are maps from states to states, states are maps from locations to values, and procedures take a value and a state to a value and a state. Every one of those clauses refers to the thing being defined, directly or through two or three others. Written out, it is a mutually recursive system with no evident solution — and it needs no new argument, because it is an instance of the general fixed-point result already established for the constructors it uses. The design question has been separated cleanly from the existence question, and only the design question is left.

The transferable habit is to notice when repeated effort is being spent on the same shape of argument and to push that shape down into a closure result. The tell is a sequence of designs each of which requires its own proof that the pieces fit together at all; the fix is to isolate the combining forms, establish once that they compose and that self-reference under them is meaningful, and then let each design be written as a system of equations. The secondary benefit is a kind of honesty about scope: with the closure result in hand, adding a new kind of value to a design is visibly a small edit to an equation, so an argument about whether a language should support some feature stops being an argument about whether it is feasible and becomes an argument about whether it is wanted.

**Source:** [Outline of a Mathematical Theory of Computation](../works/outline-of-a-mathematical-theory-of-computation.md) — the construction-of-data-types section, which introduces product, sum, and function-space constructors, generalizes them to infinite sums giving finite lists, and obtains spaces satisfying recursive equations including a space isomorphic to its own function space; together with the conclusion, which defines stores, commands, and procedures in terms of those constructors and then writes the whole value space of a programming language as a single recursive equation, noting it is only slightly more complicated than the ones already solved.
