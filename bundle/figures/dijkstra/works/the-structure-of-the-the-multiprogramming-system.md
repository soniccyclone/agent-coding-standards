---
type: work
title: "The Structure of the 'THE'-Multiprogramming System"
figure: dijkstra
description: Describes the layered design of the THE operating system, where each level provides a complete abstraction over the ones below it (storage allocation, processor allocation, device handling, and so on) so the whole system's correctness could be argued level by level instead of all at once. This paper is where the idea of an OS as a hierarchy of abstraction layers, rather than a monolithic pile of code, gets its first serious working demonstration. It directly informed decades of subsequent kernel and system design.
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
year: 1968
url: https://www.cs.utexas.edu/~EWD/transcriptions/EWD01xx/EWD196.html
extraction: complete
access: public
host: institutional
tags: [work]
---

# The Structure of the 'THE'-Multiprogramming System

**Venue/year:** Communications of the ACM 11(5), May 1968, pp. 341-346.
**Source:** https://www.cs.utexas.edu/~EWD/transcriptions/EWD01xx/EWD196.html — live page, EWD196 transcription at the E.W. Dijkstra Archive, UT Austin.

## Lessons
- [Structure a system as a stack of complete machines, each one abstracting a physical resource out of existence](../lessons/build-systems-as-layers-of-complete-machines.md)
- [Confidence in a program can only come from its structure, never from sampling its behavior](../lessons/correctness-comes-from-structure-not-testing.md)
- [Make cooperating processes correct under every speed ratio, because timing assumptions are hidden coupling](../lessons/never-let-correctness-depend-on-timing.md)
