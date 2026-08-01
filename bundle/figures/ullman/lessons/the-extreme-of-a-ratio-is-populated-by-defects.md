---
type: lesson
title: "The extreme of a ratio is populated by defects, so put a floor under support"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# The extreme of a ratio is populated by defects, so put a floor under support

**Lesson:** Comparing an observed rate against a baseline rate is the standard way to find what distinguishes one population from another, and the standard way for it to fail is arithmetic rather than statistical. The measure is a quotient, so its extreme values are produced by tiny denominators, and the items with tiny denominators are disproportionately the ones that should not be in your data at all. A misspelling appears three times in the world and twice inside your sample; its lift is enormous and its meaning is nil. Sort by the ratio and the head of the list is a catalogue of typos, encoding accidents, test records and one-off identifiers, ranked confidently above every real finding.

The right response is a minimum count on the raw occurrences, applied before the ratio is computed, and it is worth understanding why the fix goes there rather than in a smarter statistic. Sophisticated corrections for small samples exist and do help, but they answer a different question: they ask how confident you can be that the observed lift is real, assuming the item is real. The problem here is upstream of that. The item itself is an artifact, and no amount of correct inference about an artifact's rate produces anything useful. A support floor is a crude gate on data quality wearing the costume of a statistical adjustment, and treating it as the former makes it easier to set — you are asking how many independent occurrences it takes before you believe a thing exists, not what significance level you want.

The floor has a real cost and it should be chosen with the cost in view. Genuinely rare and genuinely diagnostic items sit just above the artifacts, and a floor set high enough to be comfortable will discard them. That trade is usually worth taking, because the failure modes are not symmetric: a false positive at the top of a ranked list is read, believed, and acted on, while a false negative is merely absent. But it means the floor is a knob to be revisited when your corpus grows, not a constant, since the count that separates artifact from rarity scales with how much data you have.

The general habit is to be suspicious of the extremes of any derived measure with a small quantity in the denominator, and to ask what population is being selected for by being extreme rather than what phenomenon is being detected. Rates per user with one event, conversion per impression on a page seen twice, error rates on endpoints called once an hour, speedups measured on the shortest benchmark: in every case the top of the list is selected for smallness, and smallness in real datasets correlates with brokenness. The check costs one line and one threshold, and it is what stands between a ranked list of insights and a ranked list of your own data-entry mistakes.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the passage in chapter 5 on inferring topics from words, which proposes identifying terms that appear far more often in a topic sample than in the background frequency of the whole Web, then cautions against extremely rare words whose relative frequency is high, observes such a word is probably a misspelling that landed in one or a few sampled pages, and prescribes a floor on the number of appearances before a word may be treated as characteristic.
