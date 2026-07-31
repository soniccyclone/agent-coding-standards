---
type: lesson
title: "When the latency is waiting, widen what you are willing to accept — speed cannot help you"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [parallelizability, hardware-affinity, expressiveness]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# When the latency is waiting, widen what you are willing to accept — speed cannot help you

**Lesson:** Suppose a component's elapsed time is dominated not by the work it does but by waiting for something to become available. Two moves are on the table and only one of them addresses the problem. Making the component faster shrinks the part that was never the bottleneck. Broadening the set of arrivals it is prepared to accept changes the distribution of the wait itself: if any of several independent arrivals will do, you are waiting for the first of them rather than for a nominated one, and with independent sources of similar rate, being willing to take either of two halves the expected wait. Nothing about the machinery changed. The requirement changed, and the requirement was what was costing the time.

The same widening is simultaneously the defence against getting stuck, which is why it is worth hunting for specifically. Insisting on one particular arrival is a wager that it will come, and it is a wager lost outright when the counterparty happens to be producing the other one first — including the very ordinary case where both arrivals come from the same source, which emits them in an order you had no way to predict. Being willing to take either eliminates that failure rather than mitigating it. Design moves that improve the typical case and the worst case at once are rare enough that recognizing this one is worth a habit.

Two things to be careful about. The cost of widening acceptance is that you must genuinely be able to handle everything you offered to accept: an offer you cannot honour is worse than never making it, and a broad acceptance that immediately rejects most of what arrives has all the coupling and none of the benefit. And the opportunity is found by asking a plain question that almost nobody asks — is the thing being waited for the only acceptable next occurrence, or merely the one that got named? Where several would do, name several. The reason the question goes unasked is largely notational: most languages make waiting for one specific thing the effortless default and waiting for whichever comes first an awkward special construct, which is an argument about the notation rather than about the engineering.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the input and output section of the communication chapter, where a process may offer a choice of input channels and the choice is settled by whichever corresponding output becomes ready first; the accompanying discussion noting that an implementor is expected though not compelled to resolve the nondeterminism in favour of the first ready output, that this protects against the deadlock which follows when the other output never occurs or can occur only afterwards — as when both channels lead to one process that outputs on them in sequence — and the bus-stop illustration, in which a traveller prepared to take either of two routes waits half as long on the assumption of random arrivals, with the remark that waiting for the first of several possible events is the only way to achieve this and that buying faster computers is useless.
