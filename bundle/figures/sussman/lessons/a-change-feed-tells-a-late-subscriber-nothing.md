---
type: lesson
title: "A subscriber to changes learns nothing about the present, so joining must deliver a synthetic first event"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# A subscriber to changes learns nothing about the present, so joining must deliver a synthetic first event

**Lesson:** In the circuit simulator, a wire notifies its attached devices when its signal changes, and only then — a write of the value it already holds does nothing. The registration procedure therefore does something that looks gratuitous: after adding a new action to the wire's list, it immediately runs it once. The authors turn this into an exercise, because deleting that one line produces a simulator that is wrong in a way that will not show up as an error anywhere. A device attached to a wire that already carries a value never learns the value. It waits for a change that already happened.

The general fault is that a change feed carries derivatives, and a derivative alone does not determine a position. Any component that learns about the world exclusively through change notifications is correct only if it was present before the world had any state — which is true of the first component and false of every one added afterwards. The gap is invisible from inside: the subscriber is not receiving errors, it is receiving nothing, and nothing is exactly what a quiet system also produces. Late joiners in a pub/sub topic, a cache warmed only by invalidations, a UI bound to a diff stream, a replica catching up from a log with no snapshot, a watcher registered after the file was written — all the same shape.

The fix is the one the simulator uses and it is worth stating as a rule rather than a trick: subscription is not complete until the subscriber has been told the current state. Either the act of joining synthesizes an initial event, or the feed is defined to be a snapshot followed by a stream of changes, or the subscriber has some independent way to read the present. Some mechanism must bridge the gap; picking one is a design obligation of the notification system, not of each subscriber, because each subscriber solving it separately will produce as many partial solutions as there are subscribers.

There is a cost to be honest about. Delivering a synthetic event at registration means every handler must tolerate being invoked with a state that did not just change, which rules out handlers whose logic depends on a transition having occurred. That is a constraint on what a handler may assume, and it is better to impose it deliberately at the outset than to discover it when a handler that counted edges starts counting one extra. Decide which the feed carries — states or transitions — and make every participant obey the same answer.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 3 section 3.3.4's representation of wires, whose set-my-signal! runs the registered action procedures only when the new value differs from the current one, and whose accept-action-procedure! adds the given procedure to the list and then runs it once immediately; together with Exercise 3.31, which asks the reader to explain why this initialization is necessary and to trace the half-adder example to say how the system's response would differ if the registration procedure merely added the action without running it.
