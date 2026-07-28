---
type: lesson
title: "Study the problem with the scarcity switched off"
figure: saltzer
works: [traffic-control-in-a-multiplexed-computer-system]
axes: [cognitive-load, primitive-count]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Study the problem with the scarcity switched off

**Lesson:** When a design has to serve two purposes at once — expressing what the
work actually needs, and coping with the fact that there is not enough machine to
go around — the two get welded together in the first draft and stay welded
forever. The cure is to reason first about a world with unlimited resources: give
every unit of work its own dedicated hardware, assume nothing ever has to be
evicted, and ask what communication and coordination the work *still* requires.
Whatever survives that thought experiment is the part of the design you owe to
the problem. Everything you add afterwards, you add because the machine is small,
and you can label it as such.

This ordering holds because it makes the analysis converge. Scarcity introduces
mechanisms whose only justification is other mechanisms — eviction needs a policy,
the policy needs bookkeeping, the bookkeeping itself competes for the resource
it is rationing — and if you meet all of that at once you cannot tell which
constraint any given piece of machinery is paying for. Introduced one at a time,
each mechanism arrives with a visible cause and a visible cost, and you can see
which earlier decisions it forces you to revisit. The discipline also protects
the interface: the abstraction settled in the unconstrained world is the contract,
and every later mechanism has to be judged by whether it preserves that contract
invisibly or leaks the shortage upward.

A programmer working this way writes down the resource-free version even when the
real system will never run that way, and treats it as the specification of the
interface rather than a stage of the implementation. Each subsequent layer gets
introduced with the constraint it exists to absorb stated explicitly, so nobody
later mistakes a rationing artifact for an essential feature — and when a
constraint relaxes because the hardware got bigger, the machinery that was only
there to absorb it can be identified and deleted rather than inherited forever.

**Source:** [Traffic Control in a Multiplexed Computer System](../works/traffic-control-in-a-multiplexed-computer-system.md) — the stated method of the thesis: chapter three starts from an assumed abundance of processors and memory to isolate what interprocess coordination genuinely demands, then reintroduces limited processors, and chapter four reintroduces limited memory as a separate pass.
