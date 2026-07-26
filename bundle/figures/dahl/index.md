---
type: figure
title: Ole-Johan Dahl
description: 1931-2002, Norwegian Computing Center/Oslo. Co-created Simula with Nygaard - the literal origin of encapsulation-as-design-primitive. Turing Award 2001.
status: accepted
layer: both
subdomains: [programming-environments-and-object-systems]
tags: [figure, accepted]
---

# Ole-Johan Dahl

**Dates:** 1931-2002. Norwegian computer scientist at the Norwegian Computing Center and later University of Oslo.

## Why a candidate
Simula introduced class, subclass, object, and virtual method as first-class language constructs — the literal origin of encapsulation-as-design-primitive that the whole OO lineage descends from, predating Smalltalk by years.

## Top 10 most influential works
Core artifacts are the language definition and the 1978 HOPL retrospective; individually-authored bibliography beyond these is thin:
1. "SIMULA 67 Common Base Language" (1968, with Myhrhaug, Nygaard) — `public` (softwarepreservation.org)
2. "Class and Subclass Declarations" (1967, with Nygaard) — `uncertain`
3. "The Development of the SIMULA Languages" (1978, with Nygaard, ACM HOPL) — `paywalled`
4. *Structured Programming* (1972, with Dijkstra, Hoare) — `paywalled`
5. "Abstract Types Specified as Classes" (1970s tech reports, with Nygaard) — `uncertain`

## Lessons

Dahl's work teaches that a new way of programming is most cheaply reached by
removing an artificial constraint from a construct you already understand
rather than by inventing machinery: the object is the ALGOL block instance
with the requirement to die in nesting order lifted, and subclassing is
defined as a textual merge of two such blocks, so inheritance inherits the
block's scope rules instead of needing its own. That economy is in service of
reasoning, not elegance. The stated motive for the whole class mechanism is
that a program which misreads storage has consequences no one can derive
inside the language, so the language's job is to keep every legal program's
behavior expressible in the terms its author thinks in, and the way the
rigidity of earlier checked-record schemes was escaped was by giving the set
of classes an order and testing inclusion rather than by weakening the check.
The same instinct governs the smaller decisions: a general layer names what it
does not define and keeps control around what fills the gap so specializations
cannot get the protocol wrong; "undefined" is treated as an openly deferred
decision, with the warning that a plausible default for a case you never
understood erases the only evidence of its existence; and the grain of the
object model is set by measured storage behavior, with any convenience whose
cost is invisible to its user rejected outright. On top of that sits a view of
what languages are for. Concurrency belongs to the description rather than the
execution, with switch points named in the text and the pending-work order
kept as data a program can read, so an interleaved system stays reproducible
and each entity's whole life can be read top to bottom in one place. And the
right end state for a general language is to be a substrate that domain
vocabularies extend from the inside, so that working in a specialized area
feels like working in a language that knows your problem rather than calling
someone else's code. The decomposition itself has a criterion, not a taste:
promote the entities that already hold the information the behavior consults,
and let the prominent-but-ignorant ones fall back to being resources.
