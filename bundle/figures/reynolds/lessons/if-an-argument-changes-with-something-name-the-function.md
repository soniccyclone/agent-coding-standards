---
type: lesson
title: "If an argument's value moves with something else, name the function it secretly is"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# If an argument's value moves with something else, name the function it secretly is

**Lesson:** Some arguments are not values at all. If an argument is re-consulted each time it is used, and what it yields depends on a variable that the receiving component is itself driving, then what was handed over is a function — one whose input is that variable — and the component's whole purpose is to evaluate it at a series of points. Until you say that out loud you cannot state anything about the component, because every claim you try to write mentions the argument at a moment, and the interesting facts are about all the moments together.

So introduce a name for the function and record, as a condition on the call, that the argument agrees with that function applied to the driving variable. The name never appears in the executable text; it exists purely so the specification has something to quantify and accumulate over. With it in hand, the loop invariant becomes sayable — the accumulated result equals the function summed over the portion already visited — and the postcondition becomes a statement about the function over the whole range rather than about a value that no longer exists. Without it, the same invariant has a hole in it exactly where the changing quantity should go.

The general instruction is to look at every parameter and ask what it varies with. A parameter that varies with nothing is a value and needs no such treatment. A parameter that varies with the clock, or with a counter the callee owns, or with which element is currently being processed, is a function of that thing, and the honest interface says so. This is worth doing even where the language is offering you the dependency implicitly and for free, because the implicitness is precisely what makes such arguments notorious: the mechanism that lets a caller supply behaviour by supplying an expression is powerful, and the price of the power is that nothing in the text shows what the expression depends on until you write the dependency down yourself.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.3.10's second example, the summing procedure using Jensen's device, which introduces a ghost identifier of procedural type to express the value of the expression parameter as a function of the index parameter, states their relationship as a static parameter assumption, and uses it to write the loop invariant as the running total equalling that function summed over the already-processed interval, with the corresponding postcondition over the whole interval; together with Section 3.1.5's presentation of the device itself, which turns repeated evaluation of a by-name argument from a hazard into the mechanism that makes the procedure general.
