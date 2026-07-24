---
type: work
title: "Self-Stabilizing Systems in Spite of Distributed Control"
figure: dijkstra
description: Poses and solves the problem of a distributed system built from identical finite-state machines arranged in a ring, none of which has global knowledge, that must converge to a single legal configuration from any arbitrary starting state within a bounded number of steps. Dijkstra gives three variant solutions (using four, three, and finally fewer states) and treats this convergence-from-anywhere property as a form of fault tolerance distinct from anything achievable by a centrally controlled system. The paper is short but founded the entire field now called self-stabilization in distributed computing.
subdomains: [distributed-systems-and-concurrency]
year: 1974
url: https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD426.html
access: public
host: institutional
tags: [work]
---

# Self-Stabilizing Systems in Spite of Distributed Control

**Venue/year:** Communications of the ACM 17(11), November 1974, pp. 643-644.
**Source:** https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD426.html — live page, EWD426 transcription at the E.W. Dijkstra Archive, UT Austin.

## Lessons
- [Design distributed rules so the legitimate states are an attractor, not a fortress](../lessons/make-the-legal-state-an-attractor.md)
