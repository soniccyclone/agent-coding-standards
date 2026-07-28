---
type: work
title: "Distributed Processes: A Concurrent Programming Concept"
figure: brinch-hansen
description: Proposes a programming model for networks of processes that share no memory and communicate only by direct procedure calls into each other (an early rendezvous-style remote-call mechanism), rather than by monitors or shared variables. It's Brinch Hansen's move from the shared-memory monitor world of Concurrent Pascal into distributed, message-based systems, and it prefigures later remote-procedure-call and rendezvous constructs (including Ada's tasking model). The paper works through the design with example programs rather than staying purely abstract.
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
year: 1978
url: http://www.brinch-hansen.net/papers/1978a.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# Distributed Processes: A Concurrent Programming Concept

**Venue/year:** Communications of the ACM 21(11), November 1978, pp. 934-941.
**Source:** http://www.brinch-hansen.net/papers/1978a.pdf — author's self-archived papers site (brinch-hansen.net/papers), verified resolving 2026-07-24. Note: the site's HTTPS certificate is currently expired; the HTTP URL above resolves cleanly.

## Lessons
- [Count your special-case rules: a pile of ad hoc restrictions means the underlying concept has not been found yet](../lessons/count-your-special-case-rules.md)
- [Dependency among components is a graph, not a tree, so state it in the source and forbid the cycles](../lessons/dependency-is-a-graph-not-a-tree.md)
- [Look for the concept that erases a boundary, because whatever sits on either side then becomes substitutable](../lessons/erase-the-boundary-to-gain-substitutability.md)
- [Trade generality for tractability on purpose, and keep a ledger of what the trade cost you](../lessons/trade-generality-for-tractability-on-purpose.md)
