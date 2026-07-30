---
type: lesson
title: "Two mechanisms maintained for different reasons that must agree somewhere give you a free oracle"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Two mechanisms maintained for different reasons that must agree somewhere give you a free oracle

**Lesson:** Systems often end up with two independent mechanisms that track overlapping facts for unrelated reasons — an incrementally maintained count and a periodic traversal, a cache and its backing store, a running total and a recomputation. The instinct is to treat this as redundancy to be eliminated. The better move is to find the point at which the two must necessarily agree and check it there. When the periodic traversal concludes that something is unreachable, its incrementally maintained count must be zero; if it is not, then either the traversal is wrong or the counting is wrong or the hardware lied, and you have learned that from a comparison that cost one test. Neither mechanism can validate itself, and no amount of care in either makes it self-checking; their independence is exactly what makes the comparison informative.

The value peaks during development of the harder mechanism, since a traversal-based algorithm running concurrently with mutation is the kind of code whose bugs produce no immediate symptom — the wrong answer looks like a correct answer until something much later goes wrong in a place with no connection to the cause. An agreement check converts a silent wrong answer into a loud one at the moment it is produced. So build the check while building the mechanism, at the point where the two computations meet, and leave it in.

The habit to cultivate is looking for redundant derivations rather than removing them. Any time you can compute a fact two ways with genuinely different machinery, you have an available assertion, and assertions of that kind are far stronger than the ones you invent by inspecting a single algorithm, because they do not depend on your understanding of either implementation being correct. Unifying the two mechanisms for elegance would be a real loss: it would remove the only witness either of them has.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 4's garbage collection section, which notes that at the end of a collection a valuable consistency check is available by verifying that the reference counts of the objects declared garbage are all zero, that a non-zero count indicates either a serious defect in the collector or a hardware error, and that this check was particularly useful while the collector was being debugged.
