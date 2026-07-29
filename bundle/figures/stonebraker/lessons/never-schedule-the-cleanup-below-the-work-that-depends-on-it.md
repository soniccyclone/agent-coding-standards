---
type: lesson
title: "Never schedule the cleanup below the work that depends on it"
figure: stonebraker
works: [the-implementation-of-postgres]
axes: [parallelizability, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, databases-and-data-management]
tags: [lesson]
---
# Never schedule the cleanup below the work that depends on it

Background maintenance is usually justified with the observation that it can run when the machine is idle. That is true and it is not the property that matters. The property that matters is what happens when the machine is not idle. If the foreground path is fast only because a background task keeps some structure trimmed, and that task is scheduled beneath the foreground, then rising load starves the task, the structure grows, the foreground gets slower, slower foreground work occupies more of the machine, and the task is starved harder. There is no equilibrium in that loop. It runs away, and it runs away fastest exactly when you can least afford it.

The diagnostic is to ask whether the background work maintains something the foreground's performance model assumes. Genuinely optional work — collecting statistics, precomputing something that has a fallback path — can safely be given whatever is left over, because the foreground degrades gracefully without it. Work that maintains an invariant the fast path depends on is not background work at all; it is foreground work that has been mislabeled by virtue of running in a separate thread of control. Mislabeling it is how a system acquires a load level beyond which it does not merely slow down but collapses, and that threshold will not appear in any test that ramps load and stops at the point where response times look acceptable.

What a designer does differently is treat the scheduling relationship as part of the design rather than an operational detail to be tuned later, and pick one of three honest positions: give the maintenance task a share that rises with load so that reclamation keeps pace with production, make the foreground itself pay a small increment of the maintenance cost inline so the accounting cannot drift, or admit the fast path does not actually depend on the invariant. Deferring the question to a runtime priority setting is choosing the runaway loop and hoping nobody reaches the load that triggers it.

**Source:** [The Implementation of Postgres](../works/the-implementation-of-postgres.md) — the discussion of problems in the storage design, which traces how starving the asynchronous reclamation process under sustained load inflates the live portion of storage and feeds back into worse query performance.
