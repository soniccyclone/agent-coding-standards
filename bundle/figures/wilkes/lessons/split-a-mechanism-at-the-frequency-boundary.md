---
type: lesson
title: "When accountability fights speed, split the mechanism at the frequency boundary rather than picking one policy"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [hardware-affinity, verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# When accountability fights speed, split the mechanism at the frequency boundary rather than picking one policy

**Lesson:** A standing tension in resource management is that speed wants operations to leave no trace while management wants a record of everything. Choosing one policy for all uses is the wrong response, because uses are not distributed evenly: some categories of the same operation happen orders of magnitude more often than others. Measure the distribution, find the boundary, and give each side its own policy — unrecorded and free for the frequent, local case, recorded and accounted for the rare case that crosses the boundary the bookkeeping exists to serve. What makes this work is that the boundary you split on is usually the same boundary the accounting is actually about, so the split costs nothing in coverage.

The naive positions are both worse for a reason worth stating. Recording everything makes the common case pay for a guarantee it does not need. Recording nothing does not even achieve the efficiency it promises: with no records at all you are committed to periodic exhaustive sweeps to work out what is still in use, and the cost of those sweeps tends to cancel the savings. The split version keeps the sweeps small — a sweep over one participant's holdings rather than over the whole system, cheap enough to run while its owner waits.

Two honest caveats belong with this. Reference counting does not eliminate the sweep, because circular structures never reach zero, so you need both mechanisms and should design accordingly rather than hoping counts suffice. And the split buys its efficiency by making addresses meaningful only locally, which forecloses things a globally meaningful naming scheme would allow — a trade that should be recorded as a trade, since a later designer with different frequencies, or a system where the frequent case is the crossing one, should reach the opposite conclusion.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's account of the compromise on capability bookkeeping: the general tension between efficiency of free copying and manageability of keeping track, the observation that keeping no records at all sees the gain negated by the cost of extensive collection, the realization that passing capabilities between domains within a process is far more frequent than between processes so the former is left unrecorded while the latter is reference counted, the note that counts cannot dispense with collection because circular chains form, and the acknowledgment that a system-wide alternative permitting global addresses might be preferable.
