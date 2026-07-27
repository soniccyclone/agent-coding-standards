---
type: lesson
title: "To find out which level a construct really lives on, strip the language until it can no longer describe itself"
figure: steele
works: [the-revised-report-on-scheme]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# To find out which level a construct really lives on, strip the language until it can no longer describe itself

**Lesson:** A language that can represent its own programs as ordinary data invites a specific confusion: the machinery that transforms program text starts to look like just another set of functions, differing only in taking their arguments unevaluated. The report attacks this with a thought experiment worth stealing. Imagine the same language with its program-representing data types removed — numbers and arithmetic remain, but nothing capable of holding a program. The control constructs still work; programs can still be written. But now ask what processes those constructs. Whatever handles the conditional or the binding form must manipulate the *text* of a program, and the stripped language has no way to represent text. So the processor cannot be a procedure of that language at all. It has to be written in something else.

The point survives the return trip. Put the program-representing data types back, and the processor becomes expressible in the language — but it has not changed level, it has merely become possible for the language to serve as its own metalanguage. That coincidence is the source of enormous power and of the confusion, because implementations then store both kinds of definition in the same place with a flag distinguishing them, and the shared storage gets mistaken for shared nature. The report's position is that using the trick is fine and thinking in it is not: the implementation may be as clever as it likes, but a syntactic transformer and a function are different kinds of thing, and the reason is that one operates on descriptions of computations and the other on the values those computations consume.

The impoverishment move generalizes well past language design. When you cannot tell whether something belongs inside a system or one level above it, subtract from the system until the question forces itself: remove the capability that lets the system talk about itself, and see what stops being expressible. Whatever still has to work, and can no longer be written inside, was never inside. The same test explains why a build system written in the language it builds, a configuration format that is also a program, or a test framework that reflects over the code under test each carry a level distinction that no amount of syntactic uniformity erases.

A programmer who holds this distinction is careful about a particular failure: reasoning about compile-time machinery with runtime intuitions. They expect the two levels to have different notions of when things happen, what is in scope, and what a name refers to — and they notice that the report itself demonstrates the hazard, defining the language's multi-armed conditional using the host language's own similarly-named form and having to point out that the definition is not circular because the two live on different levels.

**Source:** [The Revised Report on Scheme: A Dialect of LISP](../works/the-revised-report-on-scheme.md) — the note defending the implementation trick for special forms, which builds the arithmetic-only toy dialect to argue that syntactic processors are metalanguage objects, together with the pair of macro definitions that define the conditional twice at different levels.
