---
type: lesson
title: "Before adding a mechanism, ask whether the machine already computes the predicate you need"
figure: herlihy
works: [transactional-memory-architectural-support-for-lock-free-data-structures]
axes: [hardware-affinity, primitive-count]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---

# Before adding a mechanism, ask whether the machine already computes the predicate you need

**Lesson:** The expensive part of any optimistic scheme is deciding whether someone else touched what you were working on. Proposing that as new functionality invites a new subsystem: version numbers, ownership tables, a registry of who is reading what. The move that makes the whole proposal cheap is noticing that the layer underneath is already answering exactly that question for its own reasons. A multiprocessor keeping caches consistent must already know, on every access, whether another processor holds the line and in what mode, and must already revoke a copy before a write can proceed. Detection of read-write and write-write conflict is not an extra service to be built; it is the coherence protocol's existing job, relabelled. The abstraction being asked for is therefore obtainable at close to zero marginal cost, and the entire design shrinks to naming the states and instructions that expose an answer the hardware was already producing.

The generalizable habit is to search downward for an already-maintained invariant before designing a new one upward. Whatever mechanism you are considering — a conflict detector, an invalidation feed, a staleness check, a change notification — some layer beneath you is probably tracking a closely related fact because it needs it to stay correct. Two structural tests tell you whether the reuse is real rather than wishful. Does the existing mechanism have to be right about this anyway for the system to function, so that piggybacking on it inherits its correctness instead of adding a second thing to keep in sync? And is the fact it tracks conservative in the direction you need, so that the failures are spurious rejections rather than missed conflicts? Both hold here: coherence must be exact about access rights or the machine is broken, and it may over-report sharing but cannot under-report it.

A programmer who thinks this way ends up with less machinery and better performance from the same insight, because the reused mechanism is already on the fast path and already optimized. The cost of the alternative is more than code: an independent bookkeeping structure has to be updated in step with the one below it, and every such duplication is a place where two views of the same reality drift apart. Look for the layer whose existing obligations subsume your requirement, then ask for the smallest possible window into it.

**Source:** [Transactional Memory: Architectural Support for Lock-Free Data Structures](../works/transactional-memory-architectural-support-for-lock-free-data-structures.md) — the implementation section's core observation that a protocol able to detect access conflicts thereby detects transaction conflicts for free, and the accompanying account of how transactional access rights map onto the existing shared and exclusive cache-line states and bus cycles.
