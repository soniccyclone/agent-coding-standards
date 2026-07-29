---
type: lesson
title: "Judge a safety mechanism at the level users actually care about, not the level it operates on"
figure: thompson
works: [the-unix-time-sharing-system]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Judge a safety mechanism at the level users actually care about, not the level it operates on

**Lesson:** A protective mechanism can be perfectly correct about the thing it guards and still fail completely at the thing anyone wanted guarded. Mutual exclusion over a stored object is the standard example: it can flawlessly serialize writes to that object while doing nothing about the way people actually lose work, which is by two of them independently taking private copies, editing at leisure, and writing back in sequence so that the later write silently erases the earlier one. No amount of discipline at the storage layer touches that failure, because the conflict happened entirely outside the window the mechanism was watching. The mechanism was never wrong; it was aimed at the wrong altitude.

The right test for such a mechanism is a two-sided one, and both sides matter. Is it necessary — does the failure it prevents actually occur in this system's real workload, or are you defending against a pattern that your environment does not produce? And is it sufficient — assuming the failure does occur, does having the mechanism actually stop it, or does the failure just relocate to a path the mechanism cannot see? A feature that fails either test should be refused outright rather than added in a hedged, advisory, best-effort form. Hedged versions are the worst outcome available: they cost the same implementation and documentation surface, they license everyone to reason as though the problem is handled, and they leave the real failure exactly as likely as before while making it harder to notice.

Crucially, refusing the user-visible mechanism is not the same as abandoning consistency. There are two different obligations hiding under one word. The system owes it to itself that its own bookkeeping never becomes incoherent under concurrent operations — that is non-negotiable and belongs inside the implementation, where it can be enforced unconditionally rather than depending on callers to cooperate. What the system does not necessarily owe anyone is arbitration of competing human intentions, which is a policy question that the layer holding the bytes is usually the wrong place to answer. Separating these two lets you be absolutely rigid about internal invariants while declining to ship a ceremony that only pretends to resolve the external conflict.

**Source:** [The UNIX Time-Sharing System](../works/the-unix-time-sharing-system.md) — the discussion of I/O calls, where the authors explain their decision to expose no user-level locking, arguing it on both necessity and sufficiency grounds while noting that internal interlocks still keep the file system's own structures coherent.
