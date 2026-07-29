---
type: lesson
title: "Start the likely case and check the assumption alongside it, rather than checking first"
figure: ungar
works: [design-and-evaluation-of-a-high-performance-smalltalk-system]
axes: [hardware-affinity, verifiability, parallelizability]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# Start the likely case and check the assumption alongside it, rather than checking first

**Lesson:** The default shape of a safe operation is validate, then act. That ordering makes the check a serial prefix on every execution, and when the check costs about as much as the operation, it doubles the price of the overwhelmingly common path in order to protect against a case that almost never arrives. The alternative is to reverse the dependency: begin the operation on the assumption that the common case holds, evaluate the assumption at the same time, and if it turns out false, abandon the result before it becomes visible and divert to slow, general machinery. Correctness is unchanged — nothing wrong is ever committed — but the cost of caution moves off the fast path and onto the rare one.

This only pays under conditions worth stating explicitly, because the pattern is easy to cargo-cult. The assumption must be right the great majority of the time, and you should know the actual rate from measurement rather than intuition. Discarding a partially completed operation must be genuinely possible, which constrains what the operation is allowed to touch before the verdict arrives. The recovery path may be expensive but it must be rare enough that its cost, multiplied by its frequency, stays small — a hundred-cycle recovery that fires once in a few thousand operations is invisible. And the check must actually run concurrently with the work; if it merely runs in a different order, you have gained nothing.

The same reasoning appears at every level of a system once you look for it: caching a call's resolved destination at the call site and re-validating cheaply on each use rather than resolving from scratch; recording only the exceptional cross-references and letting the ordinary ones proceed unrecorded; trapping when the assumption breaks instead of branching every time in case it might. The unifying move is to let the frequency distribution of real inputs — not the space of possible inputs — decide which path is straight and which is a detour. A programmer who thinks this way instruments before optimizing, because the whole scheme collapses if the assumed case turns out to be the minority one.

**Source:** [The Design and Evaluation of a High-Performance Smalltalk System](../works/design-and-evaluation-of-a-high-performance-smalltalk-system.md) — the type-checking discussion in the architecture chapter, where arithmetic proceeds on the assumption of simple integer operands while the tags are inspected in the same cycle and a trap catches the mismatch, plus the measured trap rates in the appendix that justify the bet.
