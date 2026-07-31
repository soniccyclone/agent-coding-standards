---
type: work
title: "Self-Adjusting Binary Search Trees"
figure: tarjan
description: Introduces the splay tree, a binary search tree with no explicit balance condition that instead restructures itself toward recently accessed nodes via a rotation scheme called splaying. Sleator and Tarjan prove an O(log n) amortized bound per operation without storing any balance information per node, and show splay trees match or beat several specialized balanced-tree schemes on particular access patterns. It's a foundational example of amortized analysis driving a data structure's design rather than just describing its cost after the fact.
subdomains: [algorithms-and-complexity]
year: 1985
url: https://www.cs.cmu.edu/~sleator/papers/self-adjusting.pdf
survey_pages: 35
survey_text_layer: full
survey_fetch_mb: 5
access: public
host: self-archived
extraction: complete
tags: [work]
---

# Self-Adjusting Binary Search Trees

**Author(s):** Daniel D. Sleator, Robert E. Tarjan
**Venue/year:** Journal of the ACM 32(3), 1985, pp. 652-686.
**Source:** https://www.cs.cmu.edu/~sleator/papers/self-adjusting.pdf — live page, self-archived by co-author Daniel Sleator on his CMU faculty site.

## Lessons
- [Keep the tuning parameter in the analysis, not in the algorithm, and a blind mechanism will satisfy every instantiation at once](../lessons/keep-the-tuning-parameter-in-the-analysis-not-the-algorithm.md)
- [Adaptivity turns reads into writes, and that is the bill you are actually paying](../lessons/adaptivity-turns-reads-into-writes-and-that-is-the-real-bill.md)
- [A heuristic cannot be simplified by inspection: two nearly identical rules can differ by an order of magnitude](../lessons/a-heuristic-cannot-be-simplified-by-inspection.md)
- [Specify in the form that proves easily, implement in the form that fuses the passes, and keep the equivalence explicit](../lessons/specify-in-the-form-that-proves-implement-in-the-form-that-fuses.md)
- [An adaptive process that is cheap overall must pass through states worth keeping, so you can stop adapting and harvest one](../lessons/an-adaptive-process-worth-running-passes-through-states-worth-keeping.md)
- [Trigger maintenance on the gap between predicted and observed cost, and reject any tuning rule that needs the answer up front](../lessons/trigger-maintenance-on-the-gap-between-predicted-and-observed-cost.md)
- [State the claim you cannot prove precisely enough for someone else to attack it](../lessons/state-the-claim-you-cannot-prove-precisely-enough-to-be-attacked.md)
