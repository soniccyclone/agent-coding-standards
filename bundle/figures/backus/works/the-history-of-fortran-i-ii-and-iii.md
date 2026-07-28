---
type: work
title: "The History of FORTRAN I, II, and III"
figure: backus
description: Backus's own retrospective, delivered at the first History of Programming Languages conference, on how and why FORTRAN was designed the way it was. He explains the team's central bet — that a compiler could generate machine code efficient enough to make high-level, math-like notation acceptable to programmers who otherwise trusted only hand-written assembly — and walks through the optimization techniques built to make good on that bet, plus what changed across FORTRAN I, II, and III. It is a first-person account of the engineering trade-offs behind the first widely adopted high-level language.
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
year: 1978
url: https://softwarepreservation.computerhistory.org/FORTRAN/paper/p165-backus.pdf
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# The History of FORTRAN I, II, and III

**Venue/year:** ACM SIGPLAN History of Programming Languages Conference (HOPL I), Los Angeles, 1978; SIGPLAN Notices 13(8), pp. 165-180. Reprinted in R. Wexelblat (ed.), History of Programming Languages, Academic Press, 1981, pp. 25-45.
**Source:** https://softwarepreservation.computerhistory.org/FORTRAN/paper/p165-backus.pdf — live page (HTTP 200, application/pdf), preprint copy hosted by the Computer History Museum's Software Preservation Group.
**Host:** third-party-rehost — Computer History Museum preservation archive, not ACM's paywalled DL copy.

## Lessons
- [An abstraction is rented against whatever overhead the current hardware still hides](../lessons/abstraction-is-rented-against-the-overhead-the-hardware-hides.md)
- [Solve the problem against an unlimited resource, then treat scarcity as a separate stage](../lessons/solve-against-an-idealized-resource-then-map-scarcity-separately.md)
- [Cut the feature that is hard to specify, awkward to implement, and barely more powerful than its simpler form](../lessons/cut-the-feature-that-loses-on-all-three-counts.md)
- [Give up the expectation that output resembles input, and whole-program optimization becomes available](../lessons/give-up-local-correspondence-to-optimize-the-whole.md)
- [When the right static decision depends on unknowable dynamics, estimate the dynamics instead of assuming them away](../lessons/estimate-the-dynamics-you-cannot-prove.md)
- [Raising the level of notation relocates error rather than removing it, so make the new level's errors mechanically visible](../lessons/raising-the-notation-relocates-error-it-does-not-remove-it.md)
- [Audit the machine model a language commits you to before comparing its features](../lessons/audit-the-machine-model-a-language-commits-you-to-before-its-features.md)
- [Growth without added power is evidence that the framework cannot be extended from inside it](../lessons/growth-without-power-means-the-framework-cannot-extend-itself.md)
