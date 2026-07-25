---
type: figure
title: John Backus
description: 1924-2007, IBM. Co-invented BNF; later argued for function-level programming built from a small algebra of combining forms rather than von Neumann assignment.
status: accepted
layer: design-thought
subdomains: [programming-languages-and-semantics]
tags: [figure, accepted]
---

# John Backus

**Dates:** 1924-2007. American computer scientist at IBM; led the original FORTRAN team; Turing Award 1977.

## Why a candidate
Co-invented Backus-Naur Form, the notation nearly every language's concrete syntax has been specified in since; later argued (Turing lecture) for function-level programming built from a small algebra of combining forms rather than von Neumann assignment statements — an explicit primitives-over-convention argument.

## Top 10 most influential works
Genuinely small, high-impact set:
1. "Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs" (1978 Turing lecture) — `public` (archive.org, multiple mirrors)
2. "The Syntax and Semantics of the Proposed International Algebraic Language..." (1959, IFIP, introduced what became BNF) — `uncertain`
3. "The History of FORTRAN I, II, and III" (1978, ACM HOPL I) — `uncertain`
4. "Report on the FORTRAN Automatic Coding System" (1954/1957, IBM internal report) — `uncertain`

## Lessons
Backus's thinking turns on the gap between what a notation lets you say and what the
machinery underneath will let you get away with saying. Formalize the class of legal
texts with a handful of recursive formation rules and keep that definition independent
of any character set, because the precision a specification owes is proportional to the
number of implementers who must agree unaided — but do not mistake having pinned down
the form for having pinned down the meaning, since the attempt at semantics is the
design review that finds what cannot be given a coherent meaning at all. On the
implementation side, expressive power is rented against whatever overhead the current
hardware still conceals, which makes the mapping down to mechanism the expensive half
of any language project: abandon the piecewise correspondence between source and output
to optimize across the whole program, solve against an idealized resource and treat
scarcity as its own later stage, estimate the runtime frequencies you cannot derive
rather than assuming them away, expect errors to relocate to the new level instead of
vanishing, and cut any feature that is simultaneously hard to specify, awkward to
compile, and barely stronger than its plain form. His late argument pushes the same
scrutiny onto the notation itself: every language smuggles in a machine model that caps
its power, a framework that grows without gaining strength is confessing it cannot
define new constructs from within, the width of a program's interface to its state
bounds which changes are even conceivable, and the way out is to state results over
whole values without naming them, using a small fixed vocabulary of combining
operators chosen for the algebraic laws they obey so that reasoning about programs
happens in the language of programs rather than in a logic that merely talks about
them.
