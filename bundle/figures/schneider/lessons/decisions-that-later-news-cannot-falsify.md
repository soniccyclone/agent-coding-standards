---
type: lesson
title: "Make every distributed decision rule immune to learning more, and interference disappears"
figure: schneider
works: [synchronization-in-distributed-programs]
axes: [verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Make every distributed decision rule immune to learning more, and interference disappears

A participant that decides based on incomplete knowledge is in danger only if further knowledge could reverse the decision. So insist on conditions with one property: once true, additional incoming information can never make them false. Nothing about the network needs to be assumed — not delivery speed, not relative execution rates, not fairness. A condition that only ever becomes true is safe to act on the instant it is observed, because every future observation is consistent with having acted.

The consequences run in both directions, which is why this is the right property to organize a design around rather than one nice property among several. If a condition can be invalidated by a later arrival, then whether a participant proceeds depends on when messages happen to show up — the decision is timing-dependent, and the same program will behave differently on a faster network. That failure has two faces: a participant may proceed when it should not have, and a participant may be blocked indefinitely by information that arrives in an unlucky order. Requiring immunity to further news eliminates both at once, and it is the same requirement in each case.

The deeper payoff is about interference between concurrent participants. Concurrent programs are hard precisely because one participant's actions can invalidate the facts another participant is relying on, and controlling that is most of the work of proving anything. A fact that can only become true, never become false, cannot be interfered with — there is no action available to anyone that falsifies it. Choosing decision conditions from the class of one-way facts is therefore not merely a robustness trick against message delay; it is a way of buying interference-freedom structurally, so that no per-pair reasoning about who might disturb whom is needed at all.

A programmer who has absorbed this stops asking "does this participant have the current state?" — which is unanswerable without shared memory — and asks instead "is what this participant knows enough that nothing it might yet learn changes the answer?" That question is local, checkable, and does not require the global snapshot that asynchronous systems refuse to provide. The same test applies far outside message passing: to cache validity, to feature-gate evaluation, to any decision made from a partial view of a system that is still moving.

**Source:** [Synchronization in Distributed Programs](../works/synchronization-in-distributed-programs.md) — the requirements imposed on phase transition predicates in the section developing the technique, and the discussion section's remark identifying this property as a general means of controlling interference in concurrent programs.
