---
type: work
title: "An Optimal Algorithm for On-line Bipartite Matching"
figure: karp
description: Karp, Vazirani, and Vazirani analyze the online bipartite matching problem, where one side of the graph arrives vertex-by-vertex and must be matched immediately without knowledge of future arrivals. They show that a simple randomized algorithm (RANKING, which fixes a random priority order on the offline vertices up front) beats the best possible deterministic algorithm, achieving the optimal 1-1/e competitive ratio against an adversarial input order. It's a foundational result in online/competitive analysis and the direct ancestor of the algorithms behind ad-allocation and matching-market systems.
subdomains: [algorithms-and-complexity]
year: 1990
url: https://people.eecs.berkeley.edu/~vazirani/pubs/online.pdf
extraction: complete
survey_pages: 7
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# An Optimal Algorithm for On-line Bipartite Matching

**Author(s):** Richard M. Karp, Umesh V. Vazirani, and Vijay V. Vazirani
**Venue/year:** Proceedings of the 22nd Annual ACM Symposium on Theory of Computing (STOC 1990), pp. 352-358.
**Source:** https://people.eecs.berkeley.edu/~vazirani/pubs/online.pdf — self-archived by co-author Umesh Vazirani on his UC Berkeley faculty page. HTTP 200, application/pdf. Verified by decompressing the PDF's text streams directly: extracted text opens "An Optimal Algorithm for On-line Bipartite Matching Richard M. Karp University of California at Berkeley & International Computer Science Institute Umesh V. Vazirani ... Vijay V. Vazirani Cornell University", confirming this is the actual paper. The ACM Digital Library version (dl.acm.org/doi/10.1145/100216.100262) is paywalled; this resolves the figure stub's `uncertain` flag with a legitimate author self-archive.

## Lessons
- [Where you inject randomness matters more than how much: one hidden commitment held consistently beats a fresh coin flip per decision](../lessons/commit-to-one-random-choice-instead-of-re-rolling-each-decision.md)
- [When decisions are irrevocable and the future is unknown, redefine quality as a ratio to an oracle, then prove the ceiling so you know when to stop trying](../lessons/judge-irrevocable-decisions-against-an-oracle-and-prove-the-ceiling.md)
- [Prove you dominate a deliberately crippled version of yourself, then study the crippled version instead](../lessons/analyze-a-crippled-version-you-can-prove-you-dominate.md)
- [If the uncertainty sits where you cannot reason about it, look for a symmetry that lets you move it somewhere you can](../lessons/find-the-symmetry-that-relocates-the-uncertainty.md)

Also contributes to (extracted primarily from *Combinatorics, Complexity, and Randomness*):
- [Make your own behavior unpredictable instead of assuming the inputs will be kind](../lessons/be-unpredictable-instead-of-assuming-the-world-is-kind.md)
