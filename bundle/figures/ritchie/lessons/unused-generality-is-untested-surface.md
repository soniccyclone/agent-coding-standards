---
type: lesson
title: "Unused generality is untested surface, so trade it for the specific case that is actually exercised"
figure: ritchie
works: [evolution-of-the-unix-time-sharing-system]
axes: [primitive-count, verifiability, expressiveness]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Unused generality is untested surface, so trade it for the specific case that is actually exercised

**Lesson:** Before the modern way of waiting for a child process existed, the system had something strictly more powerful: a pair of calls that let any process send a one-word message to any other by identifier, with no requirement that the two be related, blocking the sender until the message was taken. Ritchie reports two uses. The command interpreter exploited it as a synchronization side effect, sending a message that was deliberately never expected to be read so that the failure of the send would signal the child's death. The initialization process used a similar convention to learn that a terminal's interpreter had finished. He can recall no third use, and the general mechanism was retired in favor of a narrower call that does only the thing anyone actually wanted.

What makes this more than a story about simplification is the bug he mentions in passing. Because the interpreter's protocol depended on a message nobody would receive, any command that decided to read messages would intercept it and cause the interpreter to behave as though the command had already exited. The general facility was, in other words, broken in a way that mattered — and the breakage was invisible precisely because the generality was unused. Nothing exercised the paths that would have exposed it. Ritchie is explicit that the defect would have been repaired had a real need appeared, which is exactly the point: the correctness of a general mechanism is only established by the variety of uses it actually receives, so unexercised generality is not capability held in reserve, it is a claim nobody has checked.

There is a second cost, subtler than the bug. The two real uses were both abuses — protocols built on error returns and conventional identifiers rather than on the mechanism's stated meaning. That is what happens when a facility is more general than its clients need: clients invent idioms in the gap, and those idioms become the actual interface, undocumented and fragile.

A programmer who believes this counts the distinct callers of every general-purpose mechanism they own. One caller means the abstraction is a disguised special case and should be renamed as one. Two callers doing something oblique to the intended semantics is a signal to replace the mechanism with what those callers were really asking for. They also refuse to justify a wide interface by imagined future clients, because a client that does not exist cannot find the bug that is waiting in the part nobody runs.

**Source:** [The Evolution of the Unix Time-sharing System](../works/evolution-of-the-unix-time-sharing-system.md) — the process-control section describing the send/receive message primitives, their two actual uses, the synchronization defect they contained, and their replacement by the less general wait.
