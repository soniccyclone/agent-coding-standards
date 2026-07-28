---
type: lesson
title: "Let a process's position hold the state a queue would track"
figure: pike
works: [acme-a-user-interface-for-programmers]
axes: [parallelizability, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, programming-environments-and-object-systems]
tags: [lesson]
---
# Let a process's position hold the state a queue would track

A server that must hold many requests in flight has a choice about where the
progress of each request lives. The conventional answer keeps it in data: a queue
of pending requests per resource, plus code that, after anything interesting
happens, walks the queue looking for requests that can now be satisfied. This work
reports what that costs in practice from direct experience with an earlier
single-threaded window system — the queue structure fit poorly with the rest of the
program, and getting it right across every combination of partial reads, unusual
input modes, resource deletion, and multi-byte characters took painstaking effort
and still produced bugs.

The alternative taken here is to give each outstanding request its own process,
which blocks exactly where the request is waiting. The state of the request is then
implicit in where that process is in its own code, and the queue disappears along
with the scanning pass, because a process that becomes able to proceed proceeds on
its own. The comparison offered is blunt: the concurrent version is a handful of
lines against the earlier explicit machinery, and it worked correctly the first
time, which the queue-based version did not. The reasoning generalizes beyond
window systems. When the state you are tracking is essentially "how far through a
protocol is this participant," control flow is a more faithful representation of it
than a data structure, because control flow enforces the ordering for free while a
state field lets you write any transition you like.

Two supporting decisions make it practical rather than profligate. Processes are
recycled through a pool with an allocator that hands out idle ones, so the per-request
cost is amortized; and requests that can be answered immediately are answered
directly by the front-end process without waking anyone, so the machinery is only
paid for by the requests that actually block. That is the honest form of the
technique: cheap concurrency plus a fast path, not a process for its own sake. A
programmer who has absorbed this reaches for a blocked thread of control where they
would previously have written a state field and a scheduler, and reserves explicit
state machines for the cases where the state must be inspected or persisted from
outside.

**Source:** [Acme: A User Interface for Programmers](../works/acme-a-user-interface-for-programmers.md) — the implementation section on concurrency, which contrasts the per-window queues of the earlier window system with a dedicated process per outstanding file-protocol request, including the pooling of idle processes and the immediate handling of simple requests.
