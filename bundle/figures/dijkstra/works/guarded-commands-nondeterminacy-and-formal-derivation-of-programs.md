---
type: work
title: "Guarded Commands, Nondeterminacy and Formal Derivation of Programs"
figure: dijkstra
description: Introduces the guarded-command language and the weakest-precondition predicate transformer as a way to derive programs from their specifications rather than write them first and verify them after. Nondeterminism is treated as a deliberate design feature rather than a bug, since it prevents a proof from accidentally depending on some incidental property of a particular implementation. The paper walks through worked derivations, including a program to compute a maximum and a version of Euclid's algorithm, to show the method in practice.
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
year: 1975
url: https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD472.html
extraction: complete
access: public
host: institutional
tags: [work]
---

# Guarded Commands, Nondeterminacy and Formal Derivation of Programs

**Venue/year:** Communications of the ACM 18(8), August 1975, pp. 453-457.
**Source:** https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD472.html — live page, EWD472 transcription at the E.W. Dijkstra Archive, UT Austin.

## Lessons
- [Work backwards from what must be true at the end, and let the proof obligations write the code](../lessons/let-the-proof-lead-the-program.md)
- [Leave choices the problem does not force unmade: nondeterminacy exposes the essential program](../lessons/nondeterminacy-strips-the-incidental.md)
