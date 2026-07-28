---
type: lesson
title: "Funnel every failure into the one outcome your program already knows how to handle"
figure: liskov
works: [guardians-and-actions]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# Funnel every failure into the one outcome your program already knows how to handle

**Lesson:** A distributed program can fail in a demoralizing number of ways: a machine loses power mid-update, a disk stops answering, a peer becomes unreachable, a message vanishes. The instinct is to enumerate them and write a response to each, which produces code where the failure handling dwarfs the work and is exercised only by disasters, meaning it is never right. The better move is to collapse the taxonomy: define one outcome that means "this attempt did not happen," arrange for every distinct failure to produce that outcome, and then the programmer writes recovery once, for one case, on a path exercised constantly.

Making that collapse honest takes real machinery, and the machinery is where the design effort belongs. The unit of work must be all-or-nothing, so a half-finished attempt leaves no trace anyone can observe. Durable state must be written only at the moment an attempt is declared complete, so a machine that dies mid-attempt necessarily comes back to the state before it. The visible cost is that a failure late in a long attempt discards more work, which is acceptable precisely when attempts are short relative to how often things break — an engineering judgment that should be made explicitly rather than by accident.

The same collapse handles restarting after a crash, if the module's state is split deliberately. Part of it is the truth, declared durable. The rest is derived — caches, indexes, whatever exists to make things fast — and is declared reconstructible, with the reconstruction written as an ordinary named part of the module. Then coming back from a crash is not a special mode: the durable part reappears as of the last completed attempt, the reconstruction runs, and the module resumes. Nobody writes crash-specific logic because there is no crash-specific state.

A programmer who believes this stops writing per-failure-mode handlers and starts asking what single outcome all their failures could be made to produce, then builds the mechanism that guarantees it. They also classify every piece of state as either the truth or a rebuildable convenience, and treat any state that is neither — durable but not authoritative, or derived but not reconstructible — as a bug waiting for the next power cut.

**Source:** [Guardians and Actions: Linguistic Support for Robust, Distributed Programs](../works/guardians-and-actions.md) — the atomicity section's treatment of hardware failure as forced crash and forced abort, and the guardian-structure section's split of state into stable and volatile with a recovery step that rebuilds the volatile part.
