---
type: lesson
title: "Weigh a reuse's dependency price against copying"
figure: pike
works: [go-at-google]
axes: [primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Weigh a reuse's dependency price against copying

**Lesson:** Avoiding duplication is taught as an unconditional good, which hides the fact that every reuse is a purchase. What you pay is a permanent edge in the dependency graph: everything that component drags in comes with it, its build time is now your build time, its release schedule constrains yours, and its failures become failures your users see. When the thing borrowed is a few lines of conversion or a small predicate, the price of the edge dwarfs the price of the duplication — and unlike duplication, the edge cannot be undone by anyone downstream.

So the comparison to make is not "duplicated or not" but the cost of the edge against the cost of maintaining two small copies. In the low layers of a system this calculation resolves toward copying far more often than instinct suggests, because those layers are what everything else sits on, and any weight added there is multiplied across every consumer. The result of taking it seriously is a foundation that is genuinely light, at the price of a handful of small routines existing in more than one place.

The obvious objection is drift: a copy can quietly stop agreeing with the authority it was taken from. That objection is answered by testing against the authority rather than by depending on it. A local implementation whose agreement with the canonical definition is checked automatically gives you the correctness that the dependency was supposed to guarantee, without the coupling. Correctness came from the check, not from sharing the code — recognizing that is what makes the trade safe instead of reckless.

A team that thinks this way puts a visible tripwire on new dependencies at its foundations, so that adding one is a deliberate decision someone has to argue for rather than an unnoticed import. They also learn to read a proposed dependency by its closure rather than by its interface, since what arrives is everything behind it, not the one function that motivated the request.

**Source:** [Go at Google: Language Design in the Service of Software Engineering](../works/go-at-google.md) — the closing part of the dependency discussion, where standard-library design deliberately duplicates small routines to keep low-level packages free of heavy dependencies, with tests standing in for the dropped coupling.
