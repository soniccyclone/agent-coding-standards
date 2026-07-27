---
type: figure
title: Jean-Yves Girard
description: b. 1947, CNRS Marseille. Independently discovered System F via proof theory; invented linear logic, making resource use explicit in logical primitives.
status: accepted
layer: design-thought
subdomains: [programming-languages-and-semantics]
tags: [figure, accepted]
---

# Jean-Yves Girard

**Dates:** b. 1947. French logician, CNRS researcher (Marseille).

## Why a candidate
Independently discovered System F (the polymorphic lambda calculus) via proof-theoretic means, and later invented linear logic, which refines the logical primitives underlying type systems by making resource use explicit — directly relevant to substructural type systems in later language design.

## Top 10 most influential works
Mostly uncertain accessibility:
1. "Proofs and Types" (1989, with Lafont & Taylor) — `public` (authors self-archived a free PDF, an exception to the book's nominal paywall)
2. "Interprétation fonctionnelle et élimination des coupures..." (1972 PhD thesis, introduces System F, in French) — `uncertain`
3. "Linear Logic" (1987, Theoretical Computer Science) — `uncertain`/`paywalled`
4. "The System F of Variable Types, Fifteen Years Later" (1986) — `uncertain`/`paywalled`

## Lessons
Girard's work teaches a single stubborn habit applied over and over: refuse to accept a construct as atomic, a notation as neutral, or an account as an explanation. The recurring move is to find the joint in something everyone treats as indivisible — function space factors into licensed reuse plus single use, conjunction and disjunction each split along whether they share their context, the silent permissions to copy and to discard turn out to be the most consequential rules in the system — and the recurring precondition is a semantics chosen because it disturbs you rather than because it certifies you. From that stance a set of design commitments follows. A result and the process that reaches it are different objects, so any formalism that identifies them has made cost, order, and timing unsayable; equality of computed functions is therefore the wrong yardstick and which algorithms you can express, at what price, is the right one. A component's contract should be exactly the set of connections it permits, no more and no less, which makes substitutability definitional rather than aspirational. New primitives are not free stipulations: there is an objective test for whether one respects the law that makes the whole system normalize, and constructs that fail it announce themselves by importing a parasitic parameter and then multiplying into dozens of special cases. What you may state and what you may check are separate questions, so state the invariant you actually need and discharge it by closure rather than weakening it to something cheap. Genericity carries a real obligation of uniformity, which is why definability at every instance licenses nothing about the generic case, and why the natural next generalization of a sound system is the place to attack with a classical paradox before building on it — an inconsistency, once derived, becomes a reusable instrument for proving other features impossible. And when a property is out of reach globally, decompose into finitely generated slices, prove it uniformly, and name the principle that lifts the family. Throughout there is an unusual willingness to price the costs out loud: which decomposition is more primitive is often undetermined, the symmetric notation people find liberating others find disorienting, one enclosure is irreducible, and the lifting step's expense grows with what you lift.
