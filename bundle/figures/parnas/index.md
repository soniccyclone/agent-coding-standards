---
type: figure
title: David Parnas
description: b. 1941, CMU/Maryland/McMaster. Rigorous treatment of coupling and information hiding as decomposition criteria.
status: accepted
layer: implementation-mapping
subdomains: [software-engineering-and-architecture]
tags: [figure, accepted]
---

# David Parnas

**Dates:** b. 1941. Held professorships at Carnegie Mellon, University of Maryland, and McMaster University; consulted for the US Naval Research Laboratory.

## Why a candidate
"On the Criteria To Be Used in Decomposing Systems into Modules" is arguably the single most direct rigorous treatment of coupling and information hiding as decomposition criteria — the paper the vetting philosophy's language most directly points to. Strongest fit in this subdomain against the primitive-count/rigor standard.

## Top 10 most influential works
1. "On the Criteria To Be Used in Decomposing Systems into Modules" (1972, CACM) — `public` (KiltHub, CMU's institutional repository — the MSU/k-nut.eu mirrors from the Phase 1 pass were superseded by this stronger source)
2. "On the Design and Development of Program Families" (1976, IEEE TSE) — `public` (the MSU mirror noted in Phase 1 turned out to be a PowerPoint deck, not the paper; used a Wayback snapshot of a UW course mirror instead — the live copy is now login-gated)
3. "Software Aging" (1994, ICSE) — `public` (Drexel course mirror)
4. "A Technique for Software Module Specification with Examples" (1972, CACM) — `public` (laputan.org self-hosted paper archive)
5. "The Modular Structure of Complex Systems" (1985, with Clements, Weiss) — `public` (MSU course mirror)
6. "Designing Software for Ease of Extension and Contraction" (1979, IEEE TSE) — `public` (MIT OpenCourseWare, 16.355J)
7. "Active Design Reviews: Principles and Practices" (1985/1987) — `public` (Internet Archive mirror of DTIC tech report ADA163188)
8. "On a 'Buzzword': Hierarchical Structure" (1974, IFIP) — `paywalled`, no public copy found (see Phase 3 access flag below)

## Phase 3 access flag

"On a 'Buzzword': Hierarchical Structure" (IFIP Congress '74, North-Holland,
pp. 336-339) has no free copy anywhere checked: not on ACM DL or Springer
(both paywalled — it was reprinted as Ch. 8 of the 2001 Broy/Denert
*Software Pioneers* volume), not on CiteSeerX, not on Internet Archive, not
on MIT OpenCourseWare, and McMaster's own SQRL bibliography page for Parnas
(cas.mcmaster.ca/sqrl/DLP.publications.html, checked via a 2007 Wayback
snapshot since the live page 403s) lists it as a citation only, with no
attached PDF. This matters somewhat for the "why a candidate" case — it's
Parnas's earliest attempt to pin down what "hierarchical structure" actually
means as a design term, precursor to the module-guide work in "The Modular
Structure of Complex Systems" — but it's not the paper the vetting
philosophy points to (that's "On the Criteria..."), so its absence doesn't
weaken the core case. Excluded from the `works/` directory per the
public-sources-only rule.

## Lessons

Parnas's whole body of work turns on one substitution: stop describing what a
system does and start describing what each of its parts is permitted to know.
Every structural virtue he argues for follows from that move. Boundaries get
drawn along the decisions likely to be revised rather than along the order in
which processing happens, because the flowchart's joints are not the places
change arrives. A part is then an assignment of responsibility for concealing
something, not a chunk of the running program, and its interface is the set of
claims its clients are allowed to rely on — which makes a true but unnecessary
promise a design error, makes the "uses" relation a statement about correctness
rather than a call graph, and makes any knowledge that reaches a client outside
the specification a leak to be closed. He is consistently more interested in
what a design forbids than in what it enables: judge it by the programs it has
ruled out, by which exceptions to its own rules each change forces, by the width
of a level you can still argue is complete. Where lesser treatments would stop
at the principle, he pushes on the parts that resist it — the criterion that
goes fuzzy and needs a named arbiter, the technique that inverts once the system
outgrows the tutorial example, the two parts that appear to need each other and
are therefore miscounted, the ordering of decisions that no amount of cleverness
lets you back out of. The later work carries the same logic into process:
specifications are objects to be tested before any code exists, documentation is
worth what its timing allows rather than what it contains, redundancy is the
precondition of detecting anything at all, scrutiny held collectively is held by
nobody, and a question phrased so it can be answered without doing the work is
not a check. The through-line is a refusal to let plausibility substitute for a
demonstration — including, pointedly, when the thing being taken on faith is
your own design discipline working.
