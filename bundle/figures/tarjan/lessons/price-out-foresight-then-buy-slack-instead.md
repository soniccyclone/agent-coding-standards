---
type: lesson
title: "Price out what foresight is worth; when the ratio will not close, buy slack instead"
figure: tarjan
works: [amortized-efficiency-of-list-update-and-paging-rules]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Price out what foresight is worth; when the ratio will not close, buy slack instead

**Lesson:** Before building machinery to predict future demand, it is worth asking what perfect prediction would even be worth. For the list-reordering problem the answer is a constant factor: a rule that reacts only to what has already happened stays within a small multiple of a strategy handed the complete future, so no amount of statistics-gathering, counting, or modelling can buy more than that. That is a licence to stop optimizing, and it explains an otherwise surprising practical finding — the rule that maintains per-item frequency counters, despite paying real time and space for its bookkeeping, is not reliably better than the rule that keeps no bookkeeping at all. When the reactive baseline is provably near the ceiling, prediction machinery is overhead with an upper bound on its possible reward.

For paging the same question gets the opposite answer, and the contrast is the actual lesson. Any online eviction policy can be driven by an adversarial request stream to fault on essentially every access while a policy that knows the future faults only a handful of times, and the size of the gap grows with the cache. Here foresight is genuinely worth a great deal, because eviction is a decision that cannot be partially hedged: unlike a list, where a badly placed item is merely somewhat expensive, a page is either resident or absent, and the cost function has a cliff at the cache boundary rather than a slope. Recognizing which of these two shapes your problem has tells you whether to invest in prediction or in a cheap reactive rule.

What to do when the ratio provably will not close is the most reusable move in the paper. Rather than concluding that the online case is hopeless, the comparison is restated with an extra parameter: least-recently-used eviction on a given cache comes within a chosen constant factor of an optimal clairvoyant policy running on a proportionally *smaller* cache. The unbounded quantity has been traded for a resource margin, which converts an impossibility result into an engineering recipe — foresight can be substituted for by slack, and the exchange rate is explicit. A designer who has this reflex, on hitting a proof that no strategy in their class can be within a constant of the best, asks what modest extra resource would restore the bound instead of abandoning the comparison, and stops treating clairvoyance as the only baseline worth measuring against.

**Source:** [Amortized Efficiency of List Update and Paging Rules](../works/amortized-efficiency-of-list-update-and-paging-rules.md) — the paging section's lower bound for all online policies against the clairvoyant optimum, the matching upper bound for least-recently-used and first-in-first-out, the counterexamples showing last-in-first-out and least-frequently-used fail it, and the closing remarks that restate the result as a bound against a smaller-memory optimum, read together with the earlier finding that frequency counting does not pay for itself in the list setting.
