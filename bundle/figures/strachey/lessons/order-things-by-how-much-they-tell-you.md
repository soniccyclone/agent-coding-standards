---
type: lesson
title: "Order things by how much they tell you"
figure: strachey
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Order things by how much they tell you

A self-referential definition — a loop written as a command that mentions itself, a recursive procedure, a stream defined in terms of its own tail — looks at first like a question with no answer. Read as an equation between ordinary total functions it frequently has none. The productive response is not to declare the construct illegitimate but to notice that the wrong comparison was being used. Once objects are ranked by how much they commit to rather than by how close they are to each other, the equation acquires solutions, and among them a canonical one: the answer that commits to nothing it wasn't forced to commit to.

The ordering itself is the insight, and it is easy to misread. It does not say one object is nearly another; it says one is a less finished version of the other, specifying strictly less while contradicting nothing already specified. Improvement means filling in, never revising. That reading is what forces the accompanying discipline on operations: any function worth admitting has to respect the ordering, because a computation given more information should not produce a worse-informed result. Monotonicity stops being a technical hypothesis and becomes the statement that computation accumulates knowledge rather than trading it.

What follows is a way of thinking about recursion that has nothing to do with tracing execution. You stop asking what a recursive definition does, step by step, and ask instead which object it pins down — specifically, the least-committed object consistent with the equation. That reframing is what makes recursive definitions provable rather than merely runnable, and it generalises: the same construction gives meaning to recursively defined data, mutually recursive systems of definitions, and definitions whose unfolding never terminates.

A programmer who holds this view treats "is it defined?" as a question about information content rather than about termination, is comfortable with definitions that describe an object rather than a procedure, and reaches for a least-commitment reading whenever a specification appears circular. It also gives a working test for a bad abstraction: an operation that can throw away or contradict information it has already been given cannot be part of a well-founded recursive story.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the lattices-and-fixed-points section, which introduces the approximation relation, insists on its reading as partial specification rather than nearness, and derives from it both the monotonicity requirement on functions and the existence of least solutions.
