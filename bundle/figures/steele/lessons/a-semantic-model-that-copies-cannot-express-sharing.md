---
type: lesson
title: "A model that works by copying can never express sharing, so its blind spots tell you which features are really primitive"
figure: steele
works: [scheme-an-interpreter-for-extended-lambda-calculus]
axes: [expressiveness, parallelizability, verifiability]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# A model that works by copying can never express sharing, so its blind spots tell you which features are really primitive

**Lesson:** Substitution is a complete account of the applicative part of a language: replace the parameter with the argument everywhere it occurs and keep rewriting. But substitution proceeds by making copies, and two copies of a value are not one value that two parties can observe changing. So the entire family of features that depend on identity rather than content — assignment, a mutable cell, a semaphore, any coordination between processes — falls outside what the model can describe, not because the model is unfinished but because of what it does. When the same language is instead explained via an environment that maps names to storage locations, sharing appears for free: every occurrence of a name reaches the same location, so a primitive that overwrites a location is meaningful, and the whole notion of state becomes definable.

This is a general diagnostic. When a feature resists expression in your chosen formalism, the useful move is to ask what structural commitment of the formalism is blocking it, because that answer tells you whether the feature is a derived convenience or a genuinely new primitive. This work draws exactly that line: mutation and process synchronization are recognized as additions that the calculus cannot absorb, and they are added deliberately, as an acknowledged extension, rather than smuggled in as if they were more of the same. Notably, the argument also runs the other way — the work observes that concurrency's *scheduling* can be modeled by choosing nondeterministically which expression to rewrite next, while *synchronization* still cannot, which separates two things usually lumped together.

There is a further consequence about how to build coordination primitives. Once you have shared locations whose reads and writes are indivisible, you technically have enough to synchronize anything, and the work says so plainly — and then says that the resulting programs are impenetrable, so the implementor owes the user something more tractable. Expressive adequacy is not the same as usability; a primitive set can be sufficient in principle and still be the wrong thing to ship. The programmer who internalizes this stops treating "it can be encoded" as the end of the design conversation, and stops being surprised that purely functional reasoning goes quiet exactly where concurrency and identity begin.

**Source:** [Scheme: An Interpreter for Extended Lambda Calculus](../works/scheme-an-interpreter-for-extended-lambda-calculus.md) — the extensions discussion at the end of the implementation-issues section, which explains why side effects and process synchronization escape substitution semantics and what environments provide instead.
