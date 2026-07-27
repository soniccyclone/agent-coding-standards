---
type: work
title: "Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems"
figure: karp
description: Edmonds and Karp show that choosing augmenting paths by shortest length (or by maximum residual capacity) in the Ford-Fulkerson labeling method bounds the number of iterations by a polynomial in the network size, independent of the edge capacities — fixing the pathological slow cases that plague naive max-flow implementations. The same paper extends the idea to the transportation problem and general minimum-cost flow. This is the paper behind what's now taught everywhere as the Edmonds-Karp algorithm, and it established polynomial-bounded augmenting-path selection as the standard fix for flow algorithms.
subdomains: [algorithms-and-complexity]
year: 1972
url: https://web.eecs.umich.edu/~pettie/matching/Edmonds-Karp-network-flow.pdf
survey_pages: 17
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: third-party-rehost
tags: [work]
---

# Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems

**Author(s):** Jack Edmonds and Richard M. Karp
**Venue/year:** Journal of the ACM 19(2), April 1972, pp. 248-264.
**Source:** https://web.eecs.umich.edu/~pettie/matching/Edmonds-Karp-network-flow.pdf — full-text copy hosted on Seth Pettie's (University of Michigan CS faculty, matching-algorithms researcher) personal research reference page; third-party rehost. Resolves HTTP 200 (the server's TLS chain is missing an intermediate certificate, so strict clients need `-k`/cert-tolerant fetch, but content is unaffected). Verified by decompressing the PDF's text streams directly: extracted text opens "Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems JACK EDMONDS University of Waterloo ... AND RICHARD M. KARP University of California, Berkeley", confirming this is the actual paper. The ACM Digital Library version (dl.acm.org/doi/10.1145/321694.321699) is paywalled.

## Lessons
- [Wherever a method says choose any, you have a family of algorithms and you will get its worst member](../lessons/an-unspecified-choice-is-where-the-pathology-hides.md)
- [Cost that scales with the magnitude of your numbers rather than the size of your data is exponential in disguise](../lessons/cost-must-scale-with-input-size-not-input-magnitude.md)
- [Solve a coarse version first, carry the answer forward, and pay for a repair step you can bound](../lessons/solve-it-coarsely-then-refine-with-a-bounded-repair.md)
- [Reshape the data to fit your cheap tool's preconditions instead of reaching for a more general tool](../lessons/restore-the-precondition-rather-than-generalize-the-tool.md)
