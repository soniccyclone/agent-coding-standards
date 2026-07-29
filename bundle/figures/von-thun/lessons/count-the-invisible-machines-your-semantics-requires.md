---
type: lesson
title: "Count the invisible machines your semantics requires"
figure: von-thun
works: [joy-forths-functional-cousin]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Count the invisible machines your semantics requires

Everyone knows to ask whether a language has mutable state, because state is the
famous villain and its absence is the headline claim of functional programming.
Von Thun's classification is sharper than that, because it counts a second
hidden structure that the usual story leaves out. Imperative languages carry two
of them: a store mapping variables to current values, and an environment mapping
formal parameters to actuals at each call. Mainstream functional languages drop
the store and are then advertised as having nothing left — but they keep the
environment, because they are built on abstraction and application, and
application is precisely the act of extending an environment. A language built
on composition and quotation instead has neither.

The reason this distinction earns its keep is that both structures cost the same
kind of thing. Each is a piece of runtime apparatus that exists nowhere in the
program text, that you must simulate in your head to predict behavior, and that
any tool reasoning about the program must also model. When von Thun says
programs become easy to manipulate by hand and by other programs, he is
describing the direct consequence of there being nothing implicit to carry
along: equational reasoning on the text alone is sound because the text alone is
the whole story. A language whose meaning depends on an ambient binding
structure cannot offer that, no matter how pure its functions are.

The habit to build is to enumerate the implicit structures a design requires
before evaluating it, and to treat "no visible mechanism" as unproven rather
than proven. Name resolution, implicit context, dynamic scope, ambient
transactions, thread-local storage, dependency-injection containers, the
enclosing test fixture, an inherited configuration cascade — each is an
invisible machine, and each one added is a thing every reader and every tool has
to model. The count matters more than the elegance of any single one, since they
compose into the state you must hold in your head at a breakpoint.

A programmer who takes this seriously judges designs by what must be simulated
rather than by what must be typed. They notice that removing the most notorious
machine while keeping a quieter one buys less than the marketing suggests, and
they get suspicious when a system's behavior can only be explained by pointing
at something not present in the code. They also accept the trade honestly: doing
without an environment means the plumbing that the environment was handling has
to be expressed some other way, which is why this family of languages leans so
hard on operators for rearranging what is at hand.

**Source:** [Joy: Forth's Functional Cousin](../works/joy-forths-functional-cousin.md) — the section on doing without abstraction and environments, which lays out the four-way comparison between imperative languages, mainstream functional languages, Joy, and Forth in terms of which carry a state and which carry an environment.
