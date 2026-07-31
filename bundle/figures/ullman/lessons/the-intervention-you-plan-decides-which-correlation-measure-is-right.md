---
type: lesson
title: "The intervention you plan decides which correlation measure is the right one"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# The intervention you plan decides which correlation measure is the right one

**Lesson:** Two ways of scoring an association between a condition and an outcome look almost the same and answer different questions. The first is conditional: among cases where the condition held, how often did the outcome follow. The second subtracts a baseline: how much more often did the outcome follow than it would have anyway. Arguments about which is correct are unresolvable in the abstract, because correctness depends entirely on what you intend to do with the answer, and that is a fact about your plans rather than about the data.

If the planned action is blunt and cheap — do something that exposes more cases to the condition and take whatever outcomes follow — the conditional measure is sufficient, and the baseline correction is not merely unnecessary but misleading, since it will discard exactly the high-volume associations that make the blunt action pay. If the planned action is targeted or expensive — investigate a mechanism, run a trial, allocate scarce effort per case — then the conditional measure is dangerous on its own, because an outcome that is simply common everywhere will top the ranking while carrying no information, and you will spend your budget confirming that popular things are popular. There the baseline-corrected measure is the only one that ranks by anything you can act on.

The generalisation is that a metric is half of a pair whose other half is a decision procedure, and you cannot evaluate either alone. This resolves a lot of otherwise circular methodology disputes: the question "is this the right measure" is not answerable, while "does this measure rank candidates in the order in which our intervention pays off" is answerable and usually easy. It also explains why the same analysis serves one organisation and misleads another with identical data — different cost structures for acting mean different measures, and the second organisation copying the first's dashboard inherits a scoring function tuned to somebody else's economics.

The corollary worth carrying is that a negative deviation from baseline is as actionable as a positive one and is invisible to the uncorrected measure. Conditions that suppress an outcome are often the more useful discovery, since they identify substitution and interference rather than affinity, and any scoring scheme that only ranks by conditional frequency cannot express them at all.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the association-rules section of the frequent-itemsets chapter, which defines confidence, then defines interest as confidence minus the outcome's overall rate, argues confidence alone suffices for the promotional tactic it describes, and notes that strongly negative interest identifies substitutable products.
