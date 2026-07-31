---
type: lesson
title: "An idle participant that polls is competing with the one making progress"
figure: wirth
works: [algorithms-and-data-structures]
axes: [parallelizability, hardware-affinity, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# An idle participant that polls is competing with the one making progress

**Lesson:** Expressing "wait until this becomes true" as a loop that re-reads the condition looks like the cheapest possible construction: it adds no mechanism, it is obviously correct, and the waiting party is doing nothing useful anyway so its time appears to be free. It is not free, and the reason is worth internalizing because it generalizes far past this example. The condition being tested lives somewhere, and reading it consumes the very resource the other party needs in order to make it true. Two activities on separate engines still share one store, and only one of them can touch it at a time; the one that is doing nothing is therefore slowing down the one that is doing the work, and it does so most aggressively precisely when the wait is longest. The construction whose cost you did not account for is antagonistic to the outcome you are waiting for.

The general shape of the error is accounting for a participant's cost only in terms of what it accomplishes. An activity that accomplishes nothing can still consume a contended resource, and contention is where the interesting costs in a concurrent system live. Whenever a design has one party observing another's state in a loop — a spin, a poll of a status field, a retry against a service — ask what the observation costs the observed party, not what it costs the observer. If the answer is "a share of the thing that is the bottleneck," the loop is not merely wasteful but actively counterproductive, and no amount of tuning the interval fixes the structure, it only moves the point on the curve.

The repair is to stop expressing the wait as an operation the waiter performs and start expressing it as a fact the waiter asserts: name the condition, let the waiter declare that it needs the condition, and let whoever establishes the condition announce it. This is more machinery, and the machinery earns itself twice. It removes the contention, because a waiter that is not running consumes nothing. And it makes the reasoning local: the condition becomes a postcondition of the wait and a precondition of the announcement, which are two statements you can check separately at the two places they occur, instead of a global argument about a loop that reads a variable somebody else writes. Hiding the mechanism behind that pair of operations is what lets the correctness argument shrink to something a reader can hold.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 1.7.2's initial replacement of the buffer guards by repeat-until loops on the element counter, and section 1.7.3's rejection of that solution on the grounds that the idling process, by constantly polling the counter, hinders its partner because the store can be accessed by only one process at a time, together with the resulting postulate of a signal facility whose wait and send operations hide the synchronization and stand in the relation of postcondition to established precondition.
