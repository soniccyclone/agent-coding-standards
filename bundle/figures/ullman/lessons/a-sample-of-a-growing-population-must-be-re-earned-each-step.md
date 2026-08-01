---
type: lesson
title: "A sample of a growing population must be re-earned at every step"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# A sample of a growing population must be re-earned at every step

**Lesson:** Drawing a sample is treated as a one-time act, and for a fixed population it is. For a population that keeps growing, a sample drawn once is a sample of whatever existed at the moment you drew it, and it becomes less representative every day without changing in any way you can see. It has the right size, the right schema, the right sampling method in its documentation, and a steadily worsening bias toward the past. The alternative that suggests itself — wait until enough has accumulated, then draw — trades that for having nothing to answer with during the period you most want answers. Both horns are real, and picking either one by default is how most long-lived samples get built.

The way out is to stop thinking of sampling as an act and state it as an invariant that must hold at every instant: after any number of arrivals, every element seen so far has equal probability of being in the sample. Then find the per-arrival update that preserves it. The update has a characteristic shape worth recognising, because it recurs whenever a distributional property is maintained online: admit the newcomer with exactly the probability the invariant demands at the new size, and let that same admission event evict an incumbent chosen uniformly, so that the dilution applied to everyone already present exactly compensates for the newcomer's share. The two effects are not separately tuned; solving for one determines the other. Writing down what the invariant must say after the next arrival and solving for the admission probability is a general recipe, not a trick specific to this algorithm.

What makes this worth generalising is how ordinary the failure is outside streaming algorithms. Training sets assembled once and reused, benchmark corpora, the fixed set of canary accounts, the sampled traces feeding a dashboard, the manually curated test fixtures — all are samples of a population that has since grown, all keep their size and their name, and none announce that they now describe a prefix. The bias is toward whatever the world looked like at collection time, which is precisely the period the system was already tuned for, so the sample confirms rather than challenges.

The cheap institutional version of the fix does not require the algorithm. It requires that any retained sample carry the population size it was drawn against, and that anything consuming it compare that against the current size. When the ratio has moved by an order of magnitude, the sample is describing a different population and should be redrawn or continuously maintained. A sample without that number attached cannot be audited at all, since the one fact that determines whether it is still valid was never recorded.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 4's treatment of moment estimation on infinite streams, which observes that fixing the sampled positions once biases toward early positions while delaying the choice leaves too few variables to estimate with, and then maintains uniformity inductively by admitting each new position with probability proportional to the sample size over the new stream length and evicting a uniformly chosen incumbent.
