---
type: lesson
title: "Buffering absorbs variance, never a rate deficit — past two or three, extra buffers only delay the diagnosis"
figure: hoare
works: [notes-on-data-structuring]
axes: [hardware-affinity, parallelizability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Buffering absorbs variance, never a rate deficit — past two or three, extra buffers only delay the diagnosis

**Lesson:** Interposing storage between a producer and a consumer does exactly one useful thing: it lets the two run at the same time and lets each of them be temporarily faster or slower than the other without stalling its partner. Two stages of it — one being worked on, one in flight — buys the overlap. A third smooths larger fluctuations. Beyond that the returns collapse, and the reason is structural rather than empirical. A buffer holds the accumulated difference between what has been produced and what has been consumed. If the two long-run rates match, that difference stays bounded and a small buffer contains it. If they do not match, the difference grows without limit, and no finite amount of storage changes the outcome — it only sets how long the system runs before the mismatch becomes visible.

This is why "add more buffering" is such a durable false remedy. It always appears to help at first, because the extra capacity absorbs the backlog for a while, and the interval before failure is long enough that the change gets credited. What has actually happened is that the diagnosis has been postponed and the eventual failure made worse: more memory committed, more latency between an input and its effect, and a longer stretch of history to unwind when the queue finally saturates. The discipline is to treat a buffer that keeps needing to be enlarged as a measurement rather than a component — it is telling you the rates do not match, and the fix is on one of the two sides, never in the middle.

So decide which problem you have before sizing anything. If the two sides are matched on average and merely bursty, the buffer's job is to cover the bursts, and small is right. If one side simply cannot keep up, the answer is to make it faster, make the other slower, or accept loss deliberately at a place you have chosen — and the choice of where to shed load is a design decision that deserves to be made in the open, not discovered when a queue overflows somewhere nobody was watching.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the backing-store representation section of the sequence chapter, which describes holding the block containing the active end of a sequence in main store plus one more to overlap transfer with computation, notes that further buffers smooth variations in the relative speeds of processing and transfer, and warns the designer against supposing that additional buffers help when there is a basic mismatch in those speeds — beyond double or triple buffering, filling store with more of them is not worthwhile.
