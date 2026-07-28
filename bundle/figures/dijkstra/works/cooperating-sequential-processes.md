---
type: work
title: "Cooperating Sequential Processes"
figure: dijkstra
description: A long set of lecture notes that lays out the core problems of concurrent programming from first principles: mutual exclusion, semaphores as a synchronization primitive, producer-consumer coordination via bounded buffers, and the deadlock ("deadly embrace") hazard. It's the text that introduced the dining philosophers problem as a teaching example for resource contention among cooperating processes. Much of the vocabulary later textbooks use to teach concurrency traces directly back to this document.
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
year: 1965-1968
url: https://www.cs.utexas.edu/~EWD/transcriptions/EWD01xx/EWD123.html
extraction: complete
access: public
host: institutional
tags: [work]
---

# Cooperating Sequential Processes

**Venue/year:** Written as course notes, fall 1965; published in F. Genuys (ed.), "Programming Languages: NATO Advanced Study Institute" (Academic Press, 1968).
**Source:** https://www.cs.utexas.edu/~EWD/transcriptions/EWD01xx/EWD123.html — live page, EWD123 transcription at the E.W. Dijkstra Archive, UT Austin.

## Lessons
- [Make cooperating processes correct under every speed ratio, because timing assumptions are hidden coupling](../lessons/never-let-correctness-depend-on-timing.md)
- [In concurrency, proving nothing bad happens is half a proof: demand progress against an adversarial schedule](../lessons/safety-without-progress-is-not-correctness.md)
- [When a simple requirement needs an intricate solution, the fault is in your primitives, so change them](../lessons/tortuous-solutions-indict-the-primitives.md)
