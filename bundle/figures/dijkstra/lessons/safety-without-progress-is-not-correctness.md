---
type: lesson
title: "In concurrency, proving nothing bad happens is half a proof: demand progress against an adversarial schedule"
figure: dijkstra
works: [solution-of-a-problem-in-concurrent-programming-control, cooperating-sequential-processes]
axes: [verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency]
tags: [lesson]
---
# In concurrency, proving nothing bad happens is half a proof: demand progress against an adversarial schedule

**Lesson:** Every plausible-but-wrong mutual exclusion scheme fails one of two distinct obligations, and the failure modes teach the shape of the full proof. Safety (never two processes in the critical region) is the visible half; the other half is progress, and it splinters on inspection: a scheme can be safe yet serialize everyone into strict alternation, safe yet deadlock when both parties politely defer, safe yet allow two symmetric processes to dance around each other forever at exactly matched speeds. Each of those is a genuinely different bug, invisible unless the corresponding requirement was stated in advance. So the requirements come first, written to exclude failure modes, not just to describe success: no static priority, no harm from a process stopping in neutral territory, no schedule under which the decision is postponed forever.

The adversarial framing is the load-bearing part. "The bad interleaving is astronomically improbable" is a valid engineering argument between humans redialing a busy phone line; it is invalid between identical processes, which can be perfectly correlated, and it is invalid as mathematics, because a correctness claim quantifies over all schedules, not over likely ones. A solution that works with luck is a non-solution wearing a solution's clothes, and it is more dangerous than an obvious failure because testing will almost never catch it.

A programmer holding this lesson reviews concurrent code by prosecuting it: assume a scheduler that reads your code and picks the worst legal interleaving at every step, then ask what invariant blocks the double entry, and separately, what argument guarantees someone eventually gets through. Two questions, two proofs. Accepting the first as an answer to the second is the characteristic error of the field.

**Source:** [Solution of a Problem in Concurrent Programming Control](../works/solution-of-a-problem-in-concurrent-programming-control.md) — the four requirements ruling out priority, speed assumptions, stop-blocking, and eternal after-you deference, and the two-part proof, one part safety, one part guaranteed entry. Also [Cooperating Sequential Processes](../works/cooperating-sequential-processes.md) — the graded sequence of rejected mutual-exclusion attempts, each killed by a newly articulated progress requirement, culminating in the analysis of the first correct solution.
