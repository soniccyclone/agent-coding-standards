---
type: work
title: "Notes on Structured Programming"
figure: dijkstra
description: A long, discursive essay written as private notes on how to compose large programs so their correctness can actually be checked, rather than merely tested. It works through correctness proofs, stepwise program composition, and the handling of program "families" as a way of taming complexity before it accumulates. Together with two companion essays by Dahl and Hoare it was published as the book "Structured Programming," a founding document of the discipline.
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
year: 1969-1970
url: https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html
extraction: complete
access: public
host: institutional
tags: [work]
---

# Notes on Structured Programming

**Venue/year:** Written August 1969 as private "letters to myself"; second edition April 1970. Later published as part of Dahl, Dijkstra & Hoare, "Structured Programming" (Academic Press, 1972).
**Source:** https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html — live page, EWD249 transcription at the E.W. Dijkstra Archive, UT Austin.

## Lessons
- [Confidence in a program can only come from its structure, never from sampling its behavior](../lessons/correctness-comes-from-structure-not-testing.md)
- [Compose programs one decision at a time, and treat every program as a member of a family](../lessons/take-one-design-decision-at-a-time.md)
- [Treat your own working memory as the binding resource and design down to it](../lessons/program-within-the-limits-of-your-head.md)
- [Structure a system as a stack of complete machines, each one abstracting a physical resource out of existence](../lessons/build-systems-as-layers-of-complete-machines.md)
- [Pick control structures that keep the written program and the running process in lockstep](../lessons/shorten-the-gap-between-text-and-computation.md)
