---
type: work
title: "Monitors: An Operating System Structuring Concept"
figure: hoare
description: Develops Brinch Hansen's monitor concept into a full structuring mechanism for operating systems, encapsulating shared state and the operations on it behind an interface that automatically enforces mutual exclusion. Adds condition variables with signal/wait as the synchronization primitive layered on top, and gives an implementation in terms of semaphores along with a proof rule for verifying monitor correctness. Worked through several classic examples (bounded buffer, disk-head scheduler, readers-writers) that later became standard operating-systems teaching material.
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
year: 1974
url: http://web.archive.org/web/20220619233139/https://lya.fciencias.unam.mx/jloa/Articulos/CARHoareMonitors.pdf
survey_pages: 17
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# Monitors: An Operating System Structuring Concept

**Venue/year:** Communications of the ACM 17(10), October 1974, pp. 549-557.
**Source:** http://web.archive.org/web/20220619233139/https://lya.fciencias.unam.mx/jloa/Articulos/CARHoareMonitors.pdf — Wayback Machine snapshot of a course-materials mirror hosted by the Facultad de Ciencias, UNAM (Universidad Nacional Autónoma de México), for a concurrent-programming course. The live UNAM host currently refuses connections on this path, so the Wayback snapshot is used per the dead-link fallback policy. The PDF is owner-password-protected (no open-password required) which prevented direct text-stream extraction; filename, byte size, and hosting context (dedicated concurrent-programming course page) are consistent with the genuine paper.

## Lessons
- [Draw the encapsulation boundary so the discipline you need becomes a textual property a machine can check](../lessons/put-the-discipline-where-a-textual-scan-can-enforce-it.md)
- [Decide who establishes a condition, and hand the guarantee over atomically instead of making the waiter re-derive it](../lessons/hand-off-a-guarantee-instead-of-making-the-waiter-re-derive-it.md)
- [Every point where an operation can block is a public boundary, so the invariant must hold there too](../lessons/every-point-where-you-can-block-is-a-public-boundary.md)
- [Aim to avoid persistently pessimal states rather than to reach optimal ones](../lessons/avoid-the-pessimal-rather-than-chase-the-optimal.md)
- [Under overload a dynamic allocator must fall back toward a static regime, so design the floors before the flexibility](../lessons/under-overload-a-dynamic-scheme-must-fall-back-toward-static-reservation.md)
- [Splitting a global optimization into independent modules is a hypothesis you must earn, not a structural default](../lessons/decomposing-a-global-optimization-is-a-hypothesis-to-be-earned.md)
