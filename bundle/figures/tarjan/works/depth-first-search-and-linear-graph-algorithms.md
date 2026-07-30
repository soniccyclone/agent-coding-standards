---
type: work
title: "Depth-First Search and Linear Graph Algorithms"
figure: tarjan
description: Formalizes depth-first search as a rigorous algorithmic technique rather than an informal backtracking heuristic, then uses it to derive linear-time algorithms for finding strongly connected components of a directed graph and biconnected components of an undirected graph. Both algorithms run in time bounded by a linear function of vertices plus edges, which was a sharp improvement over prior approaches. It's the paper that made DFS a first-class tool for provable complexity bounds rather than just a search strategy.
subdomains: [algorithms-and-complexity]
year: 1972
url: https://sites.cs.ucsb.edu/~gilbert/cs240a/old/cs240aSpr2011/slides/TarjanDFS.pdf
survey_pages: 15
survey_text_layer: full
survey_fetch_mb: 4
access: public
host: third-party-rehost
extraction: complete
tags: [work]
---

# Depth-First Search and Linear Graph Algorithms

**Venue/year:** SIAM Journal on Computing, Vol. 1, No. 2, June 1972, pp. 146-160.
**Source:** https://sites.cs.ucsb.edu/~gilbert/cs240a/old/cs240aSpr2011/slides/TarjanDFS.pdf — full scan of the SIAM paper, hosted as course reading material on a UC Santa Barbara CS course site; verified by extracting the embedded text stream (abstract and opening section confirmed to match the published paper).

## Lessons
- [Constrain the order you explore in and you buy an invariant, not just a search](../lessons/constrain-the-traversal-order-to-buy-an-invariant.md)
- [Replace a global test with a per-node summary that flows upward](../lessons/replace-a-global-test-with-a-summary-that-flows-upward.md)
- [Don't make the repair step cheaper; order the work so nothing needs repairing](../lessons/do-not-speed-up-the-repair-step-order-the-work-so-nothing-needs-repair.md)
- [When a technique's guarantee weakens in a harder setting, inventory the new cases instead of abandoning it](../lessons/when-a-guarantee-weakens-inventory-the-new-cases.md)
- [Separate the canonical answer from the representation artifact, then prove the answer indifferent to it](../lessons/prove-the-answer-independent-of-the-representation-you-happened-to-pick.md)
- [Find the floor before you climb, so you know when optimizing is finished](../lessons/find-the-floor-so-you-know-when-to-stop-optimizing.md)
