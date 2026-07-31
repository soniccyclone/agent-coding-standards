---
type: lesson
title: "Relating one name to another is a spectrum of distinct commitments, not a single operation called assignment"
figure: kay
works: [the-reactive-engine]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Relating one name to another is a spectrum of distinct commitments, not a single operation called assignment

**Lesson:** Most notations offer one or two ways to connect one name to another and call the matter settled, which conceals that there are at least five genuinely different relationships and that choosing among them is a semantic decision the programmer should be making deliberately. The connection can duplicate the structure, so that later changes to one side are invisible to the other. It can share the structure, so that changes to the contents are seen by both but a rebinding of the original is not. It can refer to the original name, so that even a rebinding is followed. It can carry the name itself as a symbol, so that whatever that name means at the moment of use is what is obtained. Or it can evaluate first and connect to the result. These differ in exactly which future changes propagate, and every real program depends on getting that right, yet the distinction is usually left to be inferred from whether a thing happens to be a scalar or a structure.

The reason to make the spectrum explicit rather than picking a convention is that the choices differ along a second axis too: how much evaluation has happened. Between the unevaluated form and the final value there is a range of partial results, each of which is a legitimate thing to bind, and useful behavior lives at the intermediate points — a connection that carries an unfinished computation which completes on demand, or a shared structure with a slot left open so that many logical duplicates can exist without duplicating anything. That last case is where the pragmatic stakes appear: two schemes that are semantically indistinguishable can differ by orders of magnitude in what they cost, and when the requirement is many nearly-identical things, only the parameterized-sharing form is buildable at all. A notation with one connective forces its users to reconstruct these distinctions out of whatever it does offer, and they will get them wrong, silently.

The transferable habit is to ask, at every place where one thing is defined in terms of another, which of these you actually mean, and to satisfy yourself that the notation lets you say it. When the honest answer is that you need the meaning to depend on what is done to the connection later, that is not an exotic requirement to be designed around; it is evidence that the granularity of the notation is wrong, and the fix belongs at that level rather than in the program.

**Source:** [The Reactive Engine](../works/the-reactive-engine.md) — the section on abstraction and attributes, which sets out copying, instancing, equivalencing, binding a name as a symbol, and binding after evaluation as five distinct relationships between two names, works through what each implies when the original is subsequently modified or rebound, notes that evaluation admits intermediate degrees so that a partially evaluated form may itself be bound, and observes that interposing a parameter in a shared structure is semantically equivalent to copying but pragmatically the only option when many near-duplicates are needed in little space.
