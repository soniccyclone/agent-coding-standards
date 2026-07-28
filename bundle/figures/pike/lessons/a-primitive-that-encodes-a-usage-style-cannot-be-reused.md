---
type: lesson
title: "A primitive that encodes a usage style cannot be reused"
figure: pike
works: [plan-9-from-bell-labs]
axes: [expressiveness, parallelizability, primitive-count]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# A primitive that encodes a usage style cannot be reused

When a system needs to wait on several sources of activity at once, the obvious
move is to add a facility that waits on several sources at once. This work
argues that the obvious move is a mistake, and the critique it levels at the
familiar multiplexing call is worth internalizing in full: it works only for a
privileged subset of things you might wait on, it bakes one particular structure
of concurrent program into the most privileged layer of the system, it does not
survive being stretched across a network, it is unpleasant to implement, and it
is unpleasant to use. Each of those complaints traces back to the same root. The
facility does not provide a capability; it provides a *pattern*, and a pattern
implemented low down is a pattern everyone above must adopt.

The alternative taken here is to provide something smaller and stupider — a
symmetric meeting point where two processes exchange a value when their tags
match — and then build queueing locks, reader/writer locks, sleep and wake,
and communication channels on top of it, outside the privileged layer, in
ordinary code. Because the multiplexing is now expressed in a language rather
than legislated by the kernel, it applies uniformly to every source of events
instead of a blessed list, it composes across machines, and a program that wants
a different concurrency structure writes a different one instead of arguing with
the system. The whole supporting mechanism amounts to a few hundred lines,
because most of what would have been mechanism turned out to be policy that
belonged to the caller.

The cost is honest and should be stated: with this approach a program that wants
to overlap slow input with computation must spawn a helper process to do the
waiting. That looks like extra work compared to a single call that waits on
everything. It is extra work, and the trade is deliberate — a uniform, general,
composable structure in exchange for a little ceremony in the common case.

The transferable question is: when I add this facility, am I adding a capability
or am I standardizing a shape? Capabilities belong low, where everything can
reach them. Shapes belong high, where they can be replaced without anyone's
permission. Getting this backwards is how systems acquire facilities that cover
eighty percent of cases and block the rest.

**Source:** [Plan 9 from Bell Labs](../works/plan-9-from-bell-labs.md) — the parallel programming section, which contrasts a minimal rendezvous primitive with the enumerated failings of Unix's select and notes that the synchronization library, not the kernel, holds the concurrency structure.
