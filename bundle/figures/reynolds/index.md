---
type: figure
title: John C. Reynolds
description: 1935-2013, Syracuse/CMU. Independently discovered System F; showed a language's meaning can be given as an interpreter written in a simpler one.
status: accepted
layer: both
subdomains: [programming-languages-and-semantics]
tags: [figure, accepted]
---

# John C. Reynolds

**Dates:** 1935-2013. American computer scientist, Syracuse/CMU professor.

## Why a candidate
Independently discovered the polymorphic lambda calculus (System F) via "Towards a Theory of Type Structure," formalized continuations, and showed via "definitional interpreters" that a language's meaning can be given as a small interpreter written in an even simpler one — reduction to primitives as method.

## Top 10 most influential works
1. "Definitional Interpreters for Higher-Order Programming Languages" (1972, reprinted 1998) — `public` (self-archived via Wadler's homepage)
2. "Separation Logic: A Logic for Shared Mutable Data Structures" (2002, LICS) — `public` (widely self-archived, incl. own CMU page)
3. "Towards a Theory of Type Structure" (1974) — `uncertain`/`paywalled`
4. "Types, Abstraction, and Parametric Polymorphism" (1983, establishes parametricity) — `uncertain`/`paywalled`
5. "The Discoveries of Continuations" (1993) — `uncertain`/`paywalled`
6. "Theories of Programming Languages" (1998, textbook) — `paywalled`
7. "The Craft of Programming" (1981) — `paywalled`

## Lessons
Reynolds explains a thing in something strictly weaker than itself, and treats every place that attempt fails as the finding. A definition that explains functions with functions, or borrows its host's evaluation order, has stated nothing and forwards the reader's misconceptions into the subject, so his test for any model is which properties it states and which it merely inherits. The instinct runs all the way down: discharge a proof step from the weakest property that suffices rather than unfolding an ugly definition, and model an abstraction in the weakest universe that supports it. The complementary move is reification. State diffused through control flow, the pending remainder of a computation or the ownership of a piece of storage, can be relied on but never manipulated; make it an ordinary value and the special-purpose control constructs collapse into one. He runs such transformations blind, driven by syntax alone, interpreting the output afterwards, which turns closures, environments and stack frames from design choices you defend into consequences you check. He prices power before spending it: every construct added is paid for out of some theorem, and he wants to know which one first. A discipline earns its keep by an invariance it guarantees rather than by the mistakes it happens to catch, and its strength lies in what it forbids, sometimes in a capability left out of the language so the ad hoc version is unsayable. Where an argument will not close he confines the debt to one labelled hole and proceeds. Naming is not clerical: an unnamed technique will not survive its first setting. And the formal apparatus is worth mastering mostly for calibration, so you know when the informal argument is enough.
