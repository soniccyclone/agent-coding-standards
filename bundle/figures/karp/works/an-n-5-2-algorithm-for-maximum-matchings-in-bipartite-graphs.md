---
type: work
title: "An n^5/2 Algorithm for Maximum Matchings in Bipartite Graphs"
figure: karp
description: Hopcroft and Karp give an algorithm that finds a maximum matching in a bipartite graph in O((m+n)*sqrt(n)) steps, beating the straightforward augmenting-path approach by repeatedly finding a maximal set of shortest, vertex-disjoint augmenting paths via combined BFS/DFS phases rather than one path at a time. The paper matters as an early, clean demonstration that careful amortized analysis of a graph algorithm's phase structure can shave a full polynomial factor off the obvious running time. The Hopcroft-Karp algorithm is still the standard textbook method for bipartite matching and underlies later work on general graph matching and network flow.
subdomains: [algorithms-and-complexity]
year: 1973
url: https://www.cs.princeton.edu/courses/archive/fall09/cos521/Handouts/Hopcroft.pdf
extraction: complete
survey_pages: 7
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# An n^5/2 Algorithm for Maximum Matchings in Bipartite Graphs

**Author(s):** John E. Hopcroft and Richard M. Karp
**Venue/year:** SIAM Journal on Computing 2(4), December 1973, pp. 225-231. (Earlier version: Proc. 12th Annual Symposium on Foundations of Computer Science, 1971, pp. 122-125.)
**Source:** https://www.cs.princeton.edu/courses/archive/fall09/cos521/Handouts/Hopcroft.pdf — full-text scan hosted on a Princeton course handout archive (COS 521); third-party rehost. HTTP 200, application/pdf. Verified by decompressing the PDF's text streams directly: the extracted text opens "SIAM J. COMPUT. Vol. 2, No. 4, December 1973 ... JOHN E. HOPCROFT AND RICHARD M. KARP", confirming this is the actual paper text, not a summary. The SIAM Journal on Computing version (epubs.siam.org) is paywalled.

## Lessons
- [Stop optimizing the single step; find the batch of non-interfering steps and bound how many batches there are](../lessons/batch-non-interfering-improvements-into-phases.md)
- [Derive the reasoning in the general setting and let only the implementation depend on your special case](../lessons/derive-in-the-general-setting-specialize-only-at-the-implementation.md)
- [Know whether your local check certifies a global property, because that decides if hill climbing is a proof or a guess](../lessons/when-no-local-improvement-exists-means-globally-optimal.md)
- [Design the search so every step permanently retires part of the input, and the cost bound becomes a census instead of a trace](../lessons/make-each-step-retire-input-permanently.md)
