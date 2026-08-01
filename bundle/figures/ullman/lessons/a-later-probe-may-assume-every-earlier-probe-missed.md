---
type: lesson
title: "A later probe may assume every earlier probe missed"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# A later probe may assume every earlier probe missed

**Lesson:** When a search is a disjunction — several probes, and finding the target in any one of them is enough — the probes are usually treated as independent and each is made as thorough as it would have to be if it were the only one. That is a needless expense. The probes run in some order, and if an earlier probe had found the target the search would already be over. So every later probe is entitled to assume the target was not where the earlier ones looked. That assumption is a genuine constraint on what the target can look like, and it shrinks the region the later probe has to cover.

The effect compounds. The first probe must consider the widest range of possibilities. The second may exclude everything the first would have caught, so its range is narrower. By the third or fourth, the surviving possibilities can be a small handful, and the total work across the whole disjunction is a fraction of what independent probes would have cost. The bookkeeping to obtain this is a short inequality relating what the earlier probes covered to what remains, computed once at design time rather than maintained at run time. Nothing is remembered between probes; the pruning comes from a fact about the order, not from a data structure.

The precondition to check is that finding the target once is sufficient, which is the defining property of a disjunctive search but is easy to lose. If the task is to enumerate all the ways in which two things match, or to count matches, or to score them, then a later probe may not skip what an earlier one covered, because those occurrences are part of the answer rather than redundant confirmations of it. The same distinction decides whether a duplicate result is a saving or a bug, and it is worth stating explicitly when the search is written, since the code for the two cases is nearly identical and the difference lives entirely in what the caller does with the output.

The general prompt: whenever you see a fixed set of alternative lookups performed in sequence, ask what each one may assume from the failure of its predecessors. Ordered case analysis in a matcher, a fallback chain across caches, a retry ladder over replicas, and a series of increasingly expensive parsers all have the same structure, and in each the later stages are frequently written to handle inputs the earlier stages provably already absorbed. Removing that redundancy costs nothing at run time and is invisible unless somebody thinks about the order as carrying information.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's position-based index for high-similarity matching, where a probe string's prefix symbols are looked up in buckets keyed by symbol and position, and the bound on which positions must be searched is derived from the observation that a candidate need only be discovered once, so any candidate that would have been found in an earlier bucket may be assumed absent, which restricts the admissible positions to a small range that shrinks as the search advances.
