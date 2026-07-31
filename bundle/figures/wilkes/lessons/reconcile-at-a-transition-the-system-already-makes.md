---
type: lesson
title: "Hang deferred reconciliation on a transition the system already makes, and carry the smallest per-entry state that makes deferring safe"
figure: wilkes
works: [slave-memories-and-dynamic-storage-allocation]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Hang deferred reconciliation on a transition the system already makes, and carry the smallest per-entry state that makes deferring safe

**Lesson:** Once a fast copy is allowed to absorb writes, the slow authority is owed a reconciliation, and the tempting move is to invent a schedule for paying it: a timer, a background sweep, a dirty-count threshold. Look instead for the transition the surrounding system already performs — ownership of the resource changing hands, a request completing, a tenant's turn ending — and attach the reconciliation to that. Such a moment is not merely a convenient trigger. It is the point at which the system already knows the outgoing state is finished with, which is exactly what makes the correctness argument short: there is no window to reason about, because nothing else can still be depending on the departing occupant. An invented schedule has the opposite property. It has to be correct at every instant, so it obliges you to reason about every interleaving between the flush and everybody else.

Pair the trigger with the smallest per-entry bookkeeping that makes deferral safe, and be strict about what counts as necessary. Two distinctions usually suffice: whether the slot holds something belonging to the current claimant, and whether what it holds has diverged from the authority. The first decides whether the fast path may answer at all; the second decides whether anything is owed on the way out. With both in place, the reconciliation sweep costs work proportional to what actually changed rather than to the capacity of the store, since absent and unmodified entries are dismissed by inspection. This is worth being disciplined about because anything added here is multiplied by the number of entries — asking for the minimum sufficient set of distinctions is arithmetic on a hot structure, not fastidiousness.

The pattern travels: write-back buffers, dirty-page tracking, saving a document when it closes rather than every few seconds, committing at a request boundary, refreshing a replica when its lease changes hands. The reliable sign that you have missed it is a flush policy with a tunable interval and a standing argument about what the interval should be. That argument exists because the design could not find an event already meaning "done with this," and is substituting a guess about elapsed time for a fact about control flow. When no such event genuinely exists, manufacture one and give it a name in the code rather than approximating it — a named boundary can be reasoned about and reviewed, and a timer can only be tuned.

**Source:** [Slave Memories and Dynamic Storage Allocation](../works/slave-memories-and-dynamic-storage-allocation.md) — the large-slave scheme's use of two tag bits, one recording that a word is resident and one recording that it has been altered since arriving, together with the writeback arrangement in which the scan of the fast memory is set off by the supervisor changing the base register to activate a different program, and skips every register whose bits show it holds nothing or holds an unaltered copy.
