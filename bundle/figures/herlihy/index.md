---
type: figure
title: Maurice Herlihy
description: b. 1954, Brown. Formalized linearizability and proved the wait-free hierarchy - the sharpest known formal tool for classifying synchronization primitives. Turing Award 2023.
status: accepted
layer: implementation-mapping
subdomains: [distributed-systems-and-concurrency]
tags: [figure, accepted]
---

# Maurice Herlihy

**Dates:** b. 1954. An Wang Professor of Computer Science, Brown University.

## Why a candidate
Formalized linearizability as a correctness condition for concurrent objects and proved the wait-free hierarchy (consensus numbers) — the sharpest known formal tool for classifying what synchronization primitives can and cannot achieve under concurrent execution.

## Top 10 most influential works
1. "Wait-Free Synchronization" (1991, ACM TOPLAS) — `public` (self-archived at cs.brown.edu)
2. "Linearizability: A Correctness Condition for Concurrent Objects" (1990, with Wing) — `paywalled` (widely course-mirrored)
3. "Transactional Memory: Architectural Support for Lock-Free Data Structures" (1993, with Moss) — `paywalled`
4. "A Methodology for Implementing Highly Concurrent Data Objects" (1993) — `paywalled`
5. *The Art of Multiprocessor Programming* (2008, book with Shavit) — `paywalled`

## Lessons

Herlihy's body of work teaches a single discipline applied at four different
altitudes: name the property you actually need, in the weakest form that still
excludes the failure you fear, and then find where in the stack it can be
enforced most cheaply. At the specification altitude that means judging a
correctness condition by whether it can be established one object at a time —
a property that holds locally composes for free, while one that requires a
global argument has smuggled in a scheduler — and by reducing every question
about concurrent behavior to a question about the data type's ordinary
sequential meaning, with the honest admission that a pure safety condition can
forbid progress you wanted. At the guarantee altitude it means treating
progress as something the shared object owes each individual caller rather than
a courtesy callers extend to each other, then refusing to shop for such
guarantees by strength: unbundle a condition into its clauses, keep the one
that is load-bearing, and relocate the obligation you dropped into a
replaceable policy module rather than pretending it vanished. At the primitive
altitude it means measuring a mechanism by how much agreement it can
manufacture rather than how much it can compute, using that measure to prove
whole design spaces closed or unreachable, and — above the threshold where
power stops discriminating — choosing between adequate primitives by which one
directly answers the predicate your algorithm tests. At the implementation
altitude it means the mapping down to real hardware is itself the object of
study: reuse the invariant the machine already maintains instead of building a
parallel one, restructure data so a multi-field invariant fits the machine's
one-word atomic unit, count the bookkeeping traffic a coordination scheme adds
as a cost of the scheme rather than the problem, publish the bound of any
mechanism that has a physical limit, and measure on a real multiprocessor
because a guarantee that is sound in the step-counting model can still be the
wrong purchase. Two habits run through all of it: give the machine the
uniform, provable part of a hard problem and leave the human only the part
that needs domain understanding, so that human error costs performance instead
of correctness; and remember that optimistically executed work still runs, so
code that may be abandoned must be defined on states that could never legally
arise.
