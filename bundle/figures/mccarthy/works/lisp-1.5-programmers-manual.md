---
type: work
title: "LISP 1.5 Programmer's Manual"
figure: mccarthy
description: The first complete reference manual for a working Lisp implementation, covering the reader/printer, the full set of primitive and library functions, property lists, the FUNARG mechanism, and the compiler. It's the document that took Lisp from McCarthy's 1960 paper design to a language other people could actually sit down and program in on the IBM 7090. Co-written with the MIT team that built the implementation, it fixed conventions (like dynamic binding of free variables) that later proved consequential enough to require Scheme to walk back.
subdomains: [programming-languages-and-semantics]
year: 1962
url: https://softwarepreservation.computerhistory.org/LISP/book/LISP%201.5%20Programmers%20Manual.pdf
survey_pages: 116
survey_text_layer: full
survey_fetch_mb: 5
access: public
host: third-party-rehost
tags: [work]
---

# LISP 1.5 Programmer's Manual

**Author(s):** John McCarthy, with Paul W. Abrahams, Daniel J. Edwards, Timothy P. Hart, and Michael I. Levin.
**Venue/year:** MIT Computation Center and Research Laboratory of Electronics, 1962; also published by MIT Press.
**Source:** https://softwarepreservation.computerhistory.org/LISP/book/LISP%201.5%20Programmers%20Manual.pdf — live PDF, hosted by the Software Preservation Group at the Computer History Museum, posted with permission of MIT Press. Confirmed 200 OK. (Also mirrored, same scan, at archive.org/details/lisp15programmer00john.)

## Lessons
- [Keep one calling discipline for everything, and carry the deviations as named classifications rather than as special syntax](../lessons/keep-one-calling-discipline-and-carry-the-exceptions-as-names.md)
- [Publish a ladder of models at increasing fidelity, and state which one is allowed to answer which question](../lessons/publish-a-fidelity-ladder-and-say-which-model-is-authoritative.md)
- [When an abstraction cannot be uniformly cheap, expose its cost tiers as declarations rather than picking one price and hiding it](../lessons/make-the-cost-tier-a-declaration-instead-of-a-hidden-uniform-choice.md)
- [Define liveness as reachability from a declared set of roots, and the correctness burden collapses to whether you named every root](../lessons/define-liveness-as-reachability-from-a-declared-root-set.md)
- [Introduce a destructive operation as the twin of a pure one, specified by the equation it still satisfies and the equation it breaks](../lessons/specify-a-destructive-operation-by-the-equation-it-keeps-and-the-one-it-breaks.md)
- [In a self-hosted system the fast artifact is a cache, so name the high-level definitions as the only place a change may enter](../lessons/the-fast-artifact-is-a-cache-changes-enter-through-the-definitions.md)
