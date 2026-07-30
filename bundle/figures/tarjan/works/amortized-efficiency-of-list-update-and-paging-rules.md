---
type: work
title: "Amortized Efficiency of List Update and Paging Rules"
figure: tarjan
description: Uses amortized analysis to compare online heuristics for two classic problems: maintaining a linear list under move-to-front-style reordering, and choosing which page to evict from a fixed-size cache. Sleator and Tarjan show move-to-front is within a constant factor of the optimal offline list-maintenance strategy, and that the paging rule it corresponds to, least-recently-used, is within a bounded factor of the optimal offline eviction rule (Belady's algorithm) as a function of cache size. The paper is an early and influential instance of what later got named competitive analysis, applying amortized-cost reasoning to online decision-making under uncertainty.
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
year: 1985
url: https://www.cs.cmu.edu/afs/cs/user/sleator/www/papers/amortized-efficiency.pdf
survey_pages: 7
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: self-archived
extraction: complete
tags: [work]
---

# Amortized Efficiency of List Update and Paging Rules

**Author(s):** Daniel D. Sleator, Robert E. Tarjan
**Venue/year:** Communications of the ACM 28(2), 1985, pp. 202-208.
**Source:** https://www.cs.cmu.edu/afs/cs/user/sleator/www/papers/amortized-efficiency.pdf — live page, self-archived by co-author Daniel Sleator on his CMU faculty site; verified by extracting the embedded text stream (self-organizing-lists / access-delete discussion matches the published paper's content).

## Lessons
- [Choose the cost measure before the algorithm, because the measure decides the answer](../lessons/choose-the-cost-measure-before-the-algorithm.md)
- [To prove you beat every rival, run the rival inside the proof and make disagreement the ledger](../lessons/to-beat-every-rival-run-the-rival-in-the-proof.md)
- [A cost model that permits arbitrage is the wrong model, and pricing it right prunes the strategy space](../lessons/a-cost-model-that-permits-arbitrage-is-the-wrong-model.md)
- [Price out what foresight is worth; when the ratio will not close, buy slack instead](../lessons/price-out-foresight-then-buy-slack-instead.md)
