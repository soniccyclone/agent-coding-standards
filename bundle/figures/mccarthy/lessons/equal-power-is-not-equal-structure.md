---
type: lesson
title: "Two formalisms of identical power can still be unequal designs: judge a basis by which operations it makes elementary"
figure: mccarthy
works: [recursive-functions-of-symbolic-expressions, a-basis-for-a-mathematical-theory-of-computation]
axes: [primitive-count, expressiveness, hardware-affinity]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Two formalisms of identical power can still be unequal designs: judge a basis by which operations it makes elementary

**Lesson:** It is easy to prove that two computational formalisms reach the same set of functions, and easy to conclude wrongly that the choice between them is therefore taste. The 1960 paper makes the counter-case twice in a few pages. A variant built on flat character strings — take the first character, drop the first character, prefix a character — is shown to contain the nested-pair formalism mathematically, since you can write the pair operations inside it. But in that variant, pulling a subexpression out of a structure is no longer one step; it is a program. And when the pair formalism is compared to ordinary flowchart-style programming, the paper shows that any single-entry single-exit chart can be mechanically rewritten as a set of mutually recursive equations, so control flow carries no expressive power that recursion lacks. Same reachable behavior in all three cases; radically different notions of what counts as a single move.

What differs, and what actually matters, is which operations sit at the base of the tower. Whatever a formalism makes elementary is what its programs will be cheap and legible in, and whatever it makes derived is where its programs will accumulate scaffolding. The string variant buys uniformity — no character is privileged with structural meaning, so anything writable linearly can be computed over — at the price of making structural access expensive both to write and to run. That is a real trade, made on real axes, and it is invisible to any argument conducted purely in terms of computability class.

A programmer who internalizes this stops asking "can this be expressed?" and starts asking "what does this make a one-step operation, and is that the set of one-step operations my problem actually needs?" It reframes language and library selection as a question about the shape of your problem's primitive moves rather than about feature checklists. It also inoculates against a common rhetorical trap: someone demonstrating that their minimal system can encode yours has established equivalence of extension, not that the encoding is a design you should want to program in.

**Source:** [Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I](../works/recursive-functions-of-symbolic-expressions.md) — the late section presenting the string-based alternative formalism, with its explicit accounting of what that uniformity gains and what it costs, and the final section translating flowcharts into mutually recursive function definitions. Also [A Basis for a Mathematical Theory of Computation](../works/a-basis-for-a-mathematical-theory-of-computation.md), whose comparison with prior formalisms establishes that they all reach the same functions and then argues the choice among them still matters, because encoding control decisions as arithmetic in the data domain leaves the branching structure of an algorithm present only in simulated form.
