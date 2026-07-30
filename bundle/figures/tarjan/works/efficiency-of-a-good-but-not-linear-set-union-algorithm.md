---
type: work
title: "Efficiency of a Good But Not Linear Set Union Algorithm"
figure: tarjan
description: Analyzes the union-find data structure under union-by-weight and path compression, proving that a sequence of m finds and n-1 unions takes time related to the inverse Ackermann function rather than being truly linear. This is the paper that pins down just how close to linear "almost linear" amortized cost can get, and it became the standard reference bound cited whenever union-find complexity comes up. The version linked here is the 1974 UC Berkeley technical report that preceded the 1975 JACM publication.
subdomains: [algorithms-and-complexity]
year: 1974
url: https://www2.eecs.berkeley.edu/Pubs/TechRpts/1974/Archive/ERL-m-434.pdf
survey_pages: 27
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: institutional
extraction: complete
tags: [work]
---

# Efficiency of a Good But Not Linear Set Union Algorithm

**Venue/year:** UC Berkeley Electronics Research Laboratory technical report UCB/ERL M434, 1974; journal version in Journal of the ACM 22(2), 1975, pp. 215-225.
**Source:** https://www2.eecs.berkeley.edu/Pubs/TechRpts/1974/Archive/ERL-m-434.pdf — live page, UC Berkeley EECS technical reports archive; verified by extracting the embedded text stream (union-rule and collapsing-find discussion matches the published paper's content).

## Lessons
- [Simple code does not imply simple analysis, and the complicated rival is usually the worse choice](../lessons/simple-code-does-not-mean-simple-analysis.md)
- [Evaluate mitigations in combination, and prefer ones that cover different failure modes](../lessons/measure-mitigations-in-combination-not-one-at-a-time.md)
- [Hoist one kind of operation to the front and re-encode the interleaving as a constraint](../lessons/hoist-the-interleaving-out-and-re-encode-it-as-a-constraint.md)
- [Split the cost into classes with different arguments, leave the granularity free, and tune it last](../lessons/split-the-cost-into-classes-and-leave-the-granularity-free.md)
- [A worst case only counts if it is reachable through legal operations and pays for its own setup](../lessons/a-worst-case-must-be-reachable-and-pay-for-itself.md)
- [Find the regime where the bad bound actually bites, because outside it the cheap analysis holds](../lessons/find-the-regime-where-the-bad-bound-actually-bites.md)
