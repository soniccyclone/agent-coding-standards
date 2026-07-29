---
type: lesson
title: "Put a cheap approximate filter in front of the expensive procedure, and size its accuracy by the cost it saves"
figure: turing
works: [the-applications-of-probability-to-cryptography]
axes: [parallelizability, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Put a cheap approximate filter in front of the expensive procedure, and size its accuracy by the cost it saves

**Lesson:** When the expensive step of a process must be run once per candidate and most candidates are wrong, the total cost is set almost entirely by how many wrong candidates reach the expensive step. That makes the highest-leverage thing you can build not a faster expensive step but a fast, deliberately imperfect test that rejects most of the wrong candidates first. The screening test does not have to be correct. It has to be much cheaper than what it guards and it has to be wrong in a direction you understand, because a filter that occasionally passes junk merely wastes some of the expensive step, while a filter that occasionally rejects a real answer destroys the whole process silently.

The subtle part is knowing how much effort to put into the filter, and the answer comes from an explicit comparison of the two costs rather than from a desire for accuracy. If the expensive step takes hours and the filter takes a minute, spending effort to make the filter more precise is nearly free and obviously worth it; if the filter creeps up towards the cost of the thing it screens, it has stopped being a filter and become a second implementation. So the design question is always stated as a ratio, and the accuracy target for the approximation is derived from that ratio, not chosen for its own sake. This is also why it pays to work out several candidate methods for the same estimate — a brute-force empirical measurement, an exhaustive enumeration over a small space, a closed-form derivation — and then pick among them on cost rather than on elegance. The methods agree on the answer; they differ enormously in what they demand of the executor.

For a programmer this reframes optimization work. Before making the hot path faster, ask what fraction of the calls into it should never have arrived, and whether a coarse predicate can eliminate them: a bloom filter before a disk seek, a bounding-box check before exact geometry, a cheap type or shape check before a full unification, a quick plausibility score before a full verification pass. Two things must then be written down and kept honest — the measured cost ratio that justified the filter, and the direction of its errors. A filter deployed without either becomes an unexplained fast path that someone later breaks by tightening it into correctness it was never supposed to have.

**Source:** [The Applications of Probability to Cryptography](../works/the-applications-of-probability-to-cryptography.md) — the letter-subtractor section, which enumerates several alternative ways to obtain the same distribution and chooses among them on effort, then justifies scoring candidate guesses cheaply by contrasting that cost against the lengthy catalogue search each surviving candidate would otherwise trigger.
