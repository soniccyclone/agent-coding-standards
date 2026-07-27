---
type: lesson
title: "Guarantees are not a ladder to climb: decompose one into its clauses and keep only the clause that is load-bearing"
figure: herlihy
works: [software-transactional-memory-for-dynamic-sized-data-structures]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---

# Guarantees are not a ladder to climb: decompose one into its clauses and keep only the clause that is load-bearing

**Lesson:** Progress conditions are usually presented as a ranking, with the temptation to take the strongest one you can afford. Treating them as a ranking hides the fact that a single condition bundles several distinct promises, which have wildly different prices and address wildly different fears. Unbundle them and ask which one you are actually buying protection against. The fear that motivates abandoning locks is that a participant stopped at the wrong moment freezes everyone else — a property of failures and preemption, not of contention. The additional promise that mutually interfering participants cannot spin against each other indefinitely is a separate clause, and it is the expensive one, because guaranteeing it inside the mechanism forces every participant to be able to finish anybody else's work, which is what makes strong non-blocking algorithms so hard to write that complex structures simply never get written.

Keeping the first clause and dropping the second gives you a condition that sounds feeble — a participant progresses if it gets a clear run — and yet retains exactly the protection that was wanted, since a stalled or dead participant obstructs nobody. What it buys in return is not a small constant factor. Because no one owes anyone else completion, any participant may unilaterally cancel any other at any moment, which collapses several hard problems at once: no helping machinery, no priority inversion to engineer around, and the freedom to let a high-priority participant simply flatten a low-priority one. The evidence offered is the kind that settles arguments — a balanced tree, built by translating textbook sequential code, described as the most intricate non-blocking structure anyone had managed, feasible only because the mechanism underneath had been made this simple.

The habit worth taking is to refuse to shop for guarantees by strength. Write down the failure you are actually defending against, find the weakest property that excludes it, and then look hard at what the extra clauses in the stronger property cost — not in performance first, but in what becomes unbuildable. And note the discipline that makes this honest rather than lazy: the dropped clause is not wished away. Livelock is named as unacceptable, and the obligation to prevent it is moved somewhere it can be addressed by policy and measurement rather than by proof. Weakening a guarantee is legitimate when you relocate the obligation; it is negligence when you merely stop mentioning it.

**Source:** [Software Transactional Memory for Dynamic-Sized Data Structures](../works/software-transactional-memory-for-dynamic-sized-data-structures.md) — the introduction's contrast between the adopted progress condition and the stronger ones, its enumeration of what the weakening buys (simplicity, unilateral abort, straightforward prioritization instead of inversion or helping), and the balanced-tree implementation offered as the payoff.
