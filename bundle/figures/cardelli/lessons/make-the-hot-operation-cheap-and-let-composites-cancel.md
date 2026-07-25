---
type: lesson
title: "Identify the operation your programs perform constantly, make it cheap, and factor it so common sequences cancel"
figure: cardelli
works: [the-functional-abstract-machine]
axes: [hardware-affinity, expressiveness]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# Identify the operation your programs perform constantly, make it cheap, and factor it so common sequences cancel

**Lesson:** Every style of programming has one operation it performs far more often than any other, and in a language built around functions that operation is application. The design decision worth copying is not any particular trick but the ranking: pick the dominant operation, set a concrete target for its cost by comparing it against something known to be cheap, and then treat any proposed feature that would slow it down as disqualified regardless of other merits. Stated that baldly it sounds obvious, and it is routinely violated by systems that accumulate conveniences each of which taxes the hot path a little, arriving at an implementation where the most common thing is the most expensive thing and nobody can point at the decision that caused it.

The subtler move is in the factoring. Rather than providing application as one indivisible instruction, it is split into separate steps for saving the caller's context, entering the callee, and restoring afterwards. Splitting looks like it costs more, and pays off because two of the steps are inverses: in a chain of applications the restore and save between adjacent calls annihilate, and when a call is the last thing a routine does the whole save-and-return apparatus collapses into a jump. The consequence is that expressing iteration as recursion carries no penalty in stack growth, so the language's natural idiom stops being a performance liability. The general principle is that an intermediate vocabulary should be factored at the joints where composites cancel algebraically, since the cancellation is what a simple local optimizer can find; a monolithic operation hides those joints and leaves nothing to cancel.

Two supporting choices come with this. Special cases are omitted from the instruction set on the grounds that they can be recognized while assembling, which keeps the machine small in the dimension that matters without giving up the fast paths. And features acknowledged to be less efficient, mutable structures and their effect on reclamation, are named as such instead of being quietly presented as equals, so that a programmer choosing them knows what is being paid.

**Source:** [The Functional Abstract Machine](../works/the-functional-abstract-machine.md) — the introduction's cost target for application and its refusal of techniques that would slow it, the control operations section where application is split into separately named steps whose inverses cancel across curried calls and collapse into a jump for final calls, and the compilation hints showing the resulting sequences.
