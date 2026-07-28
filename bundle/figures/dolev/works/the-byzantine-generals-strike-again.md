---
type: work
title: "The Byzantine Generals Strike Again"
figure: dolev
description: Extends the original Lamport-Shostak-Pease Byzantine Generals formulation, which assumed every pair of processes could talk directly, to arbitrary (non-complete) network topologies. Establishes that a network needs 2t+1 vertex-connectivity for agreement to be reachable despite t Byzantine faults when messages have to travel over a general graph rather than a clique. A foundational result for running Byzantine agreement over realistic, sparsely-connected networks.
subdomains: [distributed-systems-and-concurrency]
year: 1982
url: https://www.cs.huji.ac.il/~dolev/pubs/byz-strike-again.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# The Byzantine Generals Strike Again

**Venue/year:** Journal of Algorithms 3(1), 1982, pp. 14-30
**Source:** https://www.cs.huji.ac.il/~dolev/pubs/byz-strike-again.pdf — self-archived PDF on Dolev's own HUJI publications page, live and directly downloadable (HTTP 200).

## Lessons
- [Fault tolerance is purchased with two separate redundancies, and no protocol can substitute for either](../lessons/tolerance-is-bought-with-population-and-with-independent-paths.md)
- [You will never learn who failed; scope correctness to a budget instead](../lessons/correctness-holds-inside-a-fault-budget.md)
- [The exact shape of the agreement you demand is the biggest lever you have, and its price is discontinuous](../lessons/the-shape-of-agreement-you-demand-is-the-largest-lever.md)
- [Let the failure budget do the filtering, so no step ever needs to know which inputs were lies](../lessons/build-operators-safe-against-any-budgeted-adversary.md)
- [What a participant cannot tell apart is the whole argument](../lessons/what-participants-cannot-distinguish-bounds-every-protocol.md)
