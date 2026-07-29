---
type: work
title: "Continuations: A Mathematical Semantics for Handling Full Jumps"
figure: strachey
description: Extends denotational semantics to cover unrestricted control transfers — arbitrary gotos, and by extension exceptions and coroutine-style transfers — which the earlier Scott-Strachey framework couldn't handle cleanly. The fix is to make "the rest of the computation" an explicit mathematical object, a continuation, that a jump can hand control to directly. This paper, written with Christopher Wadsworth, is the origin point for continuation-passing style as a semantic and later an implementation technique used throughout functional language design.
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
year: 1974
url: https://www.cs.ox.ac.uk/files/3233/PRG11.pdf
survey_pages: 31
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: institutional
tags: [work]
---

# Continuations: A Mathematical Semantics for Handling Full Jumps

**Author(s):** Christopher Strachey and Christopher P. Wadsworth
**Venue/year:** Oxford University Computing Laboratory, Programming Research Group, Technical Monograph PRG-11, 1974. Reprinted in Higher-Order and Symbolic Computation 13(1/2), 2000, pp. 135-152.
**Source:** https://www.cs.ox.ac.uk/files/3233/PRG11.pdf — official University of Oxford Department of Computer Science publications page (cs.ox.ac.uk/publications/publication3729-abstract.html links directly to this file); institutional host. Verified via HTTP 200 fetch.

## Lessons
- [Make the rest of the computation an argument](../lessons/make-the-rest-of-the-computation-an-argument.md)
- [Test a formalism against the feature you would ban](../lessons/test-a-formalism-against-the-feature-you-would-ban.md)
- [Say what happens and stay silent about the bookkeeping](../lessons/say-what-happens-and-stay-silent-about-the-bookkeeping.md)
- [Judge a semantics by the equalities it lets you prove](../lessons/judge-a-semantics-by-the-equalities-it-lets-you-prove.md)
