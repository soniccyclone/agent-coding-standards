---
type: figure
title: David Ungar
description: PhD Berkeley 1985, Stanford/Sun/IBM. Designed Self (prototypes, no classes) with Randall Smith - liveness itself as the design goal.
status: accepted
layer: implementation-mapping
subdomains: [programming-environments-and-object-systems]
tags: [figure, accepted]
---

# David Ungar

**Dates:** Active 1985-present (PhD UC Berkeley 1985 under David Patterson). Assistant professor at Stanford (1985-90), later distinguished engineer at Sun Microsystems and IBM Research.

## Why a candidate
Self pushed the "environment you explore live" philosophy further than Smalltalk by eliminating classes altogether in favor of prototypes and direct object cloning, explicitly arguing (with Smith) that concreteness and liveness were themselves the design goal, not merely implementation convenience.

## Top 10 most influential works
1. "Self: The Power of Simplicity" (1987, with Smith; revised 1991) — `public` (bibliography.selflanguage.org)
2. "The Design and Evaluation of a High-Performance Smalltalk System" (1986 PhD dissertation, MIT Press book) — `paywalled`
3. "Organizing Programs Without Classes" (1991, with Chambers, Chang, Hölzle) — `paywalled` (public mirrors circulate, not confirmed stable)
4. "Animorphic Self: Mixin-Based Inheritance and Efficient Implementation" (1995, OOPSLA) — `paywalled`
5. "Debugging and the Experience of Immediacy" (1997, CACM) — `paywalled`
6. "Programming as an Experience: The Inspiration for Self" (1998, ECOOP) — `paywalled`

## Phase 3 access flag

Item 4, "Animorphic Self: Mixin-Based Inheritance and Efficient Implementation" (1995,
OOPSLA), could not be verified as an actual publication. It does not appear in DBLP's
full list of Ungar's works, returns zero hits on Google Scholar and Semantic Scholar
under this exact title (with or without author names), and no OOPSLA '95 paper by this
title exists in the official Self bibliography (bibliography.selflanguage.org), which
otherwise lists every other Ungar/Self paper checked in this pass. This looks like
either a garbled or misattributed title from the Phase 1/2 pass rather than a real
paywalled-but-real work — it isn't just unavailable, it doesn't appear to exist under
this title/venue/year combination. Not central to the "why a candidate" case (that
rests on the liveness/prototypes argument covered by items 1, 3, and 6, all now
verified public), so this doesn't block the figure, but it's worth a second look if
someone can identify what the stub was actually referring to (candidates checked and
ruled out as not-a-match: Chambers & Ungar, "Making Pure Object-Oriented Languages
Practical," OOPSLA '91 — same authors/mixins territory but about compiler performance,
not inheritance model).

## Lessons

Ungar's work teaches that the experience of using a system is a technical
specification, and that taking it seriously constrains the language, the tools, and
the implementation in ways that are measurable rather than aesthetic. On the design
side that means removing distinctions rather than adding features — every construct
that bundles two decisions, every rule justified by one compelling example, every
mechanism whose seed object needs privileges the others lack is treated as a defect,
and the honest accounting is that the cut relocates cost into the environment rather
than erasing it. On the tools side it means pricing the programmer's attention and
memory the way one prices instructions, building diagnostics to run in the direction
reasoning actually runs (backward from symptom to cause), and being suspicious of any
stage that turns what you wrote into something else you are then obliged to debug. On
the implementation side it produces the most transferable habits: an optimization that
shows through is disqualified regardless of what it saves; a feature is priced by what
its absence would cost, in units that sum, which is how you discover that several of
your cleverest ideas earn nothing; whatever dimension your metric omits is where your
design will quietly spend; and the layer boundary itself is a variable, so the right
question about a bottleneck is often which layer should be doing this at all. Running
underneath all of it is a preference for measuring the population you are managing
before writing the algorithm that manages it — the lifetime distribution, the actual
frequency of the case you are about to bet on, the interruption as a person would
group it rather than as your instrument reports it. That is what makes his cost models
double as style guides: when the good structure is also the cheap one, programmers
adopt it without being asked.
