---
type: figure
title: C.J. Date
description: b. 1941, independent. The field's most rigorous popularizer and codifier of relational theory for fifty years.
status: accepted
layer: design-thought
subdomains: [databases-and-data-management]
tags: [figure, accepted]
---

# C.J. Date

**Dates:** b. 1941. Independent author, lecturer, and consultant; worked at IBM Hursley 1967-83, frequently collaborating with Codd early on.

## Why a candidate
Not an originator but the field's most rigorous popularizer and codifier of relational theory — pushed the "reason from primitives, not convention" standard into textbooks and practice for fifty years, including sharp critiques of SQL's own deviations from the relational model.

## Top 10 most influential works
Output is almost entirely commercial books — no open copies found, flagged as a real access constraint:
1. *An Introduction to Database Systems* (1975, 8th ed. 2003) — `public`, see `works/an-introduction-to-database-systems.md`
2. *Databases, Types, and the Relational Model: The Third Manifesto* (1995, with Darwen) — `public`, see `works/databases-types-and-the-relational-model-the-third-manifesto.md`
3. *A Guide to the SQL Standard* (1987, with Darwen) — `paywalled`
4. *Relational Database: Selected Writings* (1986) — `paywalled`
5. *Database Design and Relational Theory* (2012) — `paywalled`
6. *SQL and Relational Theory* (2009) — `paywalled`
7. "What First Normal Form Really Means" (essay, various reprints) — `paywalled`

## Phase 3 access flag
Verified 2026-07-24. Date's output is genuinely book-bound: of the 7-item top list,
5 remain unavailable after actively checking for public copies (not just trusting the
Phase 1 guess):

- *A Guide to the SQL Standard*, *Relational Database: Selected Writings*, and
  *Database Design and Relational Theory* — only Internet Archive controlled-digital-lending
  ("borrow") copies found, which is a DRM'd access gate, not public per the rules for this pass.
- *SQL and Relational Theory* — same Internet Archive borrow-only situation; a full copy also
  turned up in a personal GitHub repo of dumped copyrighted PDFs (not a course mirror or
  preservation nonprofit — reads as plain piracy warehousing rather than a legitimate
  third-party rehost), so excluded rather than cited.
- "What First Normal Form Really Means" — dbdebunk.com (which Date has written for) sells its
  papers via a PUBS page rather than hosting them free; no self-archived or reprinted free copy
  found elsewhere. Resolved from `uncertain` to `paywalled`.

Two items resolved to genuinely public sources, both now `work` files:

- *An Introduction to Database Systems* (8th ed., 2003) — full PDF live on a college's public
  course-materials directory (`third-party-rehost`).
- *Databases, Types, and the Relational Model: The Third Manifesto* (3rd ed., 2006, with Darwen)
  — self-archived by co-author Hugh Darwen on his own University of Warwick homepage
  (`self-archived`), alongside the original 1995 SIGMOD Record manifesto paper and several other
  free Third Manifesto-related essays and papers (not pulled in here — this pass stayed close to
  the existing top-10 rather than sweeping that whole page).

## Lessons
Date's contribution is a method for holding a design accountable to a theory, and every lesson here
is some form of that. He treats any distinction that is logical in character as load-bearing and any
that is merely syntactic as cheap, which makes vocabulary an engineering tool rather than a
courtesy: value against variable, type against variable, model against physical realization. From
that last split he derives independence from change as a proportionality rather than a benefit — a
system keeps exactly as much of it as it kept implementation concepts out of its abstract machine —
and he pairs it with the less obvious complement that hiding everything is also a failure, since a
type reachable only through operators someone anticipated cannot answer an unanticipated question;
what must be published is a complete logical representation, possibly several, none of them a
commitment about storage. His reading of stored data as a body of asserted, exhaustive claims turns
several perennial design arguments into decidable ones, and supplies the economy at the centre of
his thinking: things you can name plus assertions about them are both necessary and jointly
sufficient, so every additional way of representing the same information multiplies the operator
surface without extending reach. The same accounting powers his refusals — positional access,
absent values, address-valued fields, and the conflation of a variable with a type each fail either
the interpretability test or the operator-count test — and it powers his one positive strategy for
growth: find the axis the core is already silent on and fill it, demanding of every proposed feature
a general reduction to existing operators or an admission that the core is being changed. Two
practical corollaries recur. Closure over a data type buys a single expression language that serves
retrieval, update scope, constraints, derived views, locking, and authorization at once, and is
rewritable because it is algebraic; and the grain of an operator set decides who owns the access
path, since a request phrased over whole collections carries no traversal plan for the caller to
freeze. Underneath all of it is a stance about where authority lives. Principles outlast products,
so the practitioner's leverage comes from learning the small durable model and using it to audit
whatever tool is in front of them; and the same relocation applies reflexively, which is why Date
regards his own earlier text as corrigible and attaches his opinions to arguments that can overturn
them.
