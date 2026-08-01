---
type: lesson
title: "Truncation does not cure a divergence"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Truncation does not cure a divergence

**Lesson:** When an analysis shows that some quantity you were planning to average has an unbounded expectation, there is a standard rescue that sounds like engineering pragmatism and is not: point out that the representation is finite, so the quantity cannot actually be unbounded, and carry on. The rescue is formally valid and practically empty. What the divergence was telling you is that the quantity's mean is dominated by rare enormous values, and imposing a ceiling does not remove that domination, it merely relocates it — the mean is now finite and set by where you put the ceiling. You have replaced an answer that does not exist with an answer that is a fact about your word size.

That is the diagnostic worth extracting. If you can change a reported number substantially by changing an implementation limit that nobody chose for statistical reasons — the width of a hash value, a timeout, a maximum retry count, a clamp added to stop overflow warnings — then the number is an artifact of that limit. Notice that this failure is invisible in testing, because every individual run produces a plausible value; it shows up as an aggregate that will not settle down, or that settles onto different values in environments that differ only in some limit. The correct reading is that the estimator is unusable as specified, and the repair belongs in how estimates are combined, not in how large a value is permitted to get.

The deeper point is about what a bound is evidence of. A bound that exists because reality is finite tells you nothing about the shape of the distribution below it; a bound that exists because the quantity genuinely concentrates does. Only the second licenses averaging. Distinguishing them takes one question: is the largest value I could observe determined by the process I am measuring, or by the container I am measuring it into? Latency histograms truncated at a request timeout, ratios whose denominator can approach zero, exponentially transformed counts, and anything involving a maximum over samples all fail that question, and all get averaged anyway.

There is also a discipline of exposition here worth copying. The honest move is to state the divergence, then state the technicality that appears to remove it, then say explicitly that the technicality does not change the conclusion. Suppressing the technicality invites a reader to find it and discard the argument; stating it without resolving it invites a reader to think the problem went away. Analysis that names its own loopholes and closes them is what makes a caveat trustworthy, and it costs a sentence.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 4's treatment of combining distinct-element estimates, where the expected value of the estimator is shown to be infinite and the accompanying footnote concedes that finite-length hash values technically bound it while insisting the effect is not enough to rescue the average.
