---
type: figure
title: Serge Abiteboul
description: b. 1953, INRIA/Collège de France. Wrote the standard rigorous logical treatment of the relational model, freely available.
status: accepted
layer: design-thought
subdomains: [databases-and-data-management]
tags: [figure, accepted]
---

# Serge Abiteboul

**Dates:** b. 1953. INRIA senior researcher, Collège de France professor; PhD under Seymour Ginsburg.

## Why a candidate
*Foundations of Databases* is the standard rigorous logical treatment of the relational model plus Datalog and complexity — a textbook built entirely from formal primitives, and it's freely available, which matters for a corpus meant to be actually used. Notably strong public-source accessibility for this candidate.

## Top 10 most influential works
1. *Foundations of Databases* (1995, with Hull, Vianu) — `public` (full text self-archived free at webdam.inria.fr/Alice/, confirmed)
2. *Web Data Management* (2011, with Manolescu, Rigaux, Rousset, Senellart) — `public` (free online edition via WebDam project)
3. *Data on the Web* (1999, with Buneman, Suciu) — `paywalled`
4. "Datalog Extensions for Database Queries and Updates" (1991, JCSS) — `uncertain`
5. Various database-theory papers hosted at webdam.inria.fr — `public`

## Lessons
Abiteboul's thread through all four works is that the interface is where the
thinking happens, and that its content is measurable. An abstraction only
exists if some invariance forbids the layer above from observing what it
hides, and the power that invariance costs can be priced exactly: refuse to
expose an ordering and a trivial count becomes unstateable, hand the ordering
back and the language snaps onto a complexity class. The same discipline
applied to restriction turns guarantees you would otherwise prove per program
into theorems about the language, whether the guarantee is termination,
decidable optimization, or parallel execution, and each restriction comes with
a stated list of what it forecloses. Once an interface is explicit it also
becomes the instrument of comparison, which is why views recur as the tool for
making unlike systems commensurable and unlike sources integrable, and why
the weaker, one-directional form of a mapping is preferred whenever the
parties are autonomous. Against all that formal leverage he is consistently
unwilling to let expressive equivalence settle a design question: proving one
notation can simulate another is the point at which he argues for keeping
both, because an encoding preserves behavior and destroys intent. The
underlying object of study is the class of computations rather than any
notation for it, so scheduling choices, where control lives, whether fresh
values can be minted, and whether structure travels inside the data are all
recognized as semantic commitments rather than implementation details.
