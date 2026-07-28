---
type: figure
title: Kristen Nygaard
description: 1926-2002, Norwegian Computing Center/Oslo. Co-created Simula with Dahl, designed to model interacting entities. Turing Award 2001.
status: accepted
layer: both
subdomains: [programming-environments-and-object-systems]
tags: [figure, accepted]
---

# Kristen Nygaard

**Dates:** 1926-2002. Norwegian computer scientist, social scientist, and later politician.

## Why a candidate
Co-designed Simula's class/object mechanism specifically to model *interacting* entities (originally for discrete-event simulation), embedding message-like interaction and encapsulation as the organizing abstraction rather than a bolt-on — the founding act of treating objects as a standalone way of thinking about systems.

## Top 10 most influential works
Heavy overlap with Dahl's bibliography (see [dahl](../dahl/index.md)) — same core: SIMULA 67 (1968, public), Development of SIMULA (1978, paywalled), Class and Subclass Declarations (1967, uncertain). Distinct additions:
1. "Program Development as a Social Activity" (1986, IFIP, later "social systems" turn) — `paywalled`/`uncertain`
2. "How Many Choices Do You Make — and Which?" (1986, Turing-lecture-adjacent essay) — `uncertain`

Distinct solo contribution smaller than Dahl's — flagged honestly.

## Phase 3 access flag
Two of the five top-10 items resolved to genuinely unavailable after direct
checks, Wayback fallback, Unpaywall/Crossref DOI lookups, and a search of
Nygaard's own self-archived-PDF folder (which turned up only one PDF total —
see below):

- **"Class and Subclass Declarations"** (Dahl & Nygaard, in Buxton, ed.,
  *Simulation Programming Languages*, IFIP Working Conference at Lysebu,
  Oslo, May 1967, published North-Holland 1968, pp. 158-174) — the paper
  that first specifies class/subclass as language declarations, i.e. the
  literal origin of the mechanism cited in this figure's "why a candidate"
  case. No open copy anywhere: the original North-Holland proceedings volume
  is an out-of-print paywalled book; both later reprints (Broy & Denert,
  eds., *Pioneers and Their Contributions to Software Engineering*, Springer
  2001, DOI 10.1007/978-3-642-48354-7_8; and *Software Pioneers*, Springer
  2002, DOI 10.1007/978-3-642-59412-0_7) are closed per Unpaywall; the
  "Software Pioneers" conference companion site (softwarepioneers.org) that
  might once have hosted a free copy is now a domain-squatted WordPress spam
  blog with no Wayback trace of the original content; Nygaard's own
  self-archived-PDF folder (heim.ifi.uio.no/~kristen/PDF_MAPPE/) contains
  exactly one research PDF total (the IFIP 86 paper below) — this isn't in
  it. This is a real gap: it's the founding artifact, and the corpus can
  only cite it by title, not link to it.

- **"How Many Choices Do We Make? How Many Are Difficult?"** (Nygaard,
  1992, in Floyd, Züllighoven, Budde, Keil-Slawik, eds., *Software
  Development and Reality Construction*, Springer, pp. 52-59) — note this
  corrects both the title and year guessed in the Phase 1 pass ("How Many
  Choices Do You Make — and Which?", 1986); the real title, year, and venue
  come from Nygaard's own "Selected Publications" bibliography page
  (archived from his University of Oslo homepage, see source note on the
  IFIP 86 work file). Closed per Unpaywall (DOI
  10.1007/978-3-642-76817-0_7, Springer), no self-archived copy on his
  homepage. Less central than the Class/Subclass gap — the stub already
  flags this line of Nygaard's solo work as thinner than the Dahl overlap —
  but it does mean the "social activity" turn is now represented by only
  one work file (the 1986 IFIP paper) instead of two.

"The Development of the SIMULA Languages" (1978 HOPL retrospective,
Nygaard & Dahl) was already marked `paywalled` in the Phase 1 pass and
stays that way after rechecking: closed on Unpaywall across all three ACM
DOI variants indexed for it (10.1145/800025.1198392,
10.1145/800025.808391, 10.1145/960118.808391), no repository copy. Not
flagged above since it wasn't a surprise and the SIMULA 67 language report
itself (public, see works/) already carries the core technical claim.

## Lessons
Nygaard's two surviving accessible works pull in the same direction from
opposite ends of the stack. In the Simula 67 report the recurring move is
economy of mechanism: the object arrives not as a new primitive but as an
existing construct with two accidental restrictions lifted, justified
explicitly by how few concepts a person can hold at once; concurrency is
reduced to suspend-and-resume with every scheduling policy pushed into
ordinary declarations above it; domain specialization becomes an operation
inside the one language, tested by defining the language's own set-handling,
simulation, and I/O facilities with it; and safety is handled by declaring
what a reference may denote, rejecting what is provably wrong, and converting
the undecidable remainder into a defined runtime failure rather than a silent
one. The 1986 lecture then turns the same skepticism on the designer. A
system is not something the world contains but something a person elects to
see, with a purpose and a discarded set of properties; the major programming
styles are lenses to switch between rather than paradigms to win with;
whoever supplies the vocabulary of a design has already settled it, and
declining to state your assumptions enlists you in the ambient ones; and the
properties of a running program are largely fixed at levels above the
program, in how the work was organized and what the organization knew. Read
together, they teach a programmer to spend primitives sparingly, to keep
mechanism separate from policy, and to hold the model itself as a revisable
choice with an author rather than as a description of how things are.

