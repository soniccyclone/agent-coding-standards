---
type: lesson
title: "Degrade each measurement if the savings buy you more of them"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, verifiability, parallelizability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Degrade each measurement if the savings buy you more of them

**Lesson:** When an estimate is built by averaging many independent trials, the accuracy of any single trial is not the quantity to protect. What matters is the accuracy of the average, and that depends on both the quality of each trial and how many of them you can afford. Those two move against each other, which turns a question that looks like a correctness question into an allocation question: given a fixed budget, is it better to run few careful trials or many sloppy ones? The answer is usually many sloppy ones, because error in an average falls with the count in a way that is hard to match by improving individual trials, and because a cheap trial is often only slightly worse than an expensive one.

The concrete form this takes is refusing to finish. A measurement defined as a scan for the first qualifying element can be truncated after a fixed fraction of the data, accepting that some subjects yield nothing at all within that window. Each surviving measurement is a little less informative and some are missing entirely, so a single estimate built this way is worse than the full-scan version. But the truncation cuts the work by a large constant factor, and reinvesting that factor in additional measurements more than repays the loss. The net effect is an estimate that is both more accurate and cheaper than the careful one, which is the outcome people assume is unavailable when they frame the choice as speed against quality.

Two conditions make the trade legitimate and both deserve checking before you take it. The truncation must not bias the estimator, only add variance: the abandoned trials have to be discarded honestly rather than scored as agreements or disagreements, since an arbitrary verdict imposed on a trial that observed nothing shifts the average in a fixed direction that no amount of averaging removes. And the savings must actually be reinvested. A team that truncates and pockets the time gets exactly the degradation with none of the compensation, and will reasonably conclude the technique does not work.

The general habit is to price accuracy per unit of work rather than per measurement. Ask what the cheapest primitive is that still carries some signal about the quantity you want, how many of them your budget buys, and what the aggregate error of that many looks like. That framing routinely selects a primitive that would be dismissed as too crude if it were being judged on its own, and it is the same reasoning that justifies sampling instead of scanning, sketching instead of counting, and short simulations run many times instead of one long one.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's section on speeding up minhashing, which examines only the first portion of the permuted rows, records a special undefined value for any set with nothing in that portion, argues that the loss in accuracy is small, and concludes that the time saved affords enough extra hash functions to end up more accurate than the original scheme as well as faster.
