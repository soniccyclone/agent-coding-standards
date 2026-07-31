---
type: lesson
title: "The operators you provide decide what your variables can range over"
figure: scott
works: [data-types-as-lattices]
axes: [expressiveness, primitive-count, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# The operators you provide decide what your variables can range over

**Lesson:** Scott stops in the middle of a technical section to name a mistake, and attributes it to the two people who invented the notation he is working with: reading its variables as ranging over arbitrary functions. They cannot. The notation includes an operator that, given anything, returns a fixed point of it. The instant that operator is part of the language, nothing lacking a fixed point can be in range, because the operator would have to produce an object that does not exist. The domain was never a free choice made alongside the notation. It was determined by the notation, and the determination happened whether or not anyone noticed.

Generalize it and you have a rule for designing anything with operations in it — a language, a library, a set of combinators, a service interface. You are not making two independent choices, one about what the operations are and one about what the values can be. Every operation you export is an assertion that for each input a corresponding output exists, and everything that would falsify the assertion is thereby excluded from the domain. The failure mode is advertising more generality than you have: a parameter documented as accepting anything of some broad kind, while one powerful operator elsewhere in the same interface silently demands much more of it. Nothing in the signatures records the demand, so the constraint gets discovered by whoever first supplies a legitimate-looking value that has no fixed point, no identity, no bound, no default — whatever it is your strongest operator quietly assumed.

Two practical uses. When adding an operation to an existing interface, the question is not just whether you can implement it for the cases in hand; it is which cases you have now ruled out forever, because that is a change of meaning that leaves no trace in any type signature. And when a formalism is presented as extremely general, go find its most powerful operator and ask what must hold of every inhabitant for that operator to be total — the answer is usually a substantial unstated restriction. Scott's own framing is the honest version of this: he says the success of his model lies precisely in *not* admitting arbitrary functions, since only the well-behaved ones correspond to the objects he set out to study. Deliberate narrowness is where the fit came from, and it is worth stating out loud rather than letting readers infer a generality that was never there.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — the opening discussion of Section 7, where Scott sets out the tension between total and partial functions, observes that the model's success depends on admitting only continuous functions rather than arbitrary ones, states that treating lambda calculus variables as ranging over arbitrary functions is a mistake made by both Church and Curry, and gives the fixed-point operator as the reason attention must be restricted to functions that do have fixed points.
