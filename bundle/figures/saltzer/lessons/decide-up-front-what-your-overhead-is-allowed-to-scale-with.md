---
type: lesson
title: "Decide up front what your overhead is allowed to scale with"
figure: saltzer
works: [traffic-control-in-a-multiplexed-computer-system]
axes: [parallelizability, hardware-affinity, verifiability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Decide up front what your overhead is allowed to scale with

**Lesson:** Write down, before choosing any algorithm, which quantities the cost
of one housekeeping operation is permitted to depend on — and which it is not.
"Independent of the number of participants" is a design constraint of exactly the
same standing as a functional requirement, and it eliminates whole families of
otherwise attractive designs on sight: any arrangement that searches or sorts a
population at the moment of use is out, which pushes the work to the moment of
entry, where the population is not consulted. Stated that early, the constraint is
free. Discovered later, it is a rewrite, because the interfaces will have been
shaped around the assumption that scanning is available.

Two things follow from taking it seriously. First, if the per-operation cost is
constant, then the fraction of the machine spent on overhead depends only on that
constant and on how much useful work a participant does between operations — not
on the size of the installation at all. That is what makes one design serve a
three-user system and a five-thousand-terminal one, and it also tells you the real
limit: the design fails not when the system gets big but when the granularity of
work gets small relative to the constant, which is a property of the workload
rather than of the hardware. Second, the constraint moves the bottleneck somewhere
visible. Constant-cost bookkeeping still needs a moment of exclusive access to
something shared, and the fraction of time that thing is held, multiplied by the
number of parties contending for it, is a number you can compute in advance and
compare against the scale you intend to reach — and when it crosses one, the fix
is structural, splitting the contended thing so it can be held in pieces.

None of this can be believed without instrumentation, because a mis-tuned policy
counterfeits the symptoms of a resource shortage. Overhead machinery that fires
too often — evicting things that are about to be needed again, or interrupting work
so frequently that the interruption dominates the work — turns a genuine surplus
into an apparent scarcity, and any capacity measurement taken in that state is
worthless. So the design owes you two things: meters in the housekeeping paths,
and a cheap way to vary a resource so you can find where the curve bends. A
programmer who believes this ships the meter with the mechanism, rules out
self-inflicted overhead before drawing any conclusion about capacity, and keeps a
knob for the adjustment the physical system will inevitably need.

**Source:** [Traffic Control in a Multiplexed Computer System](../works/traffic-control-in-a-multiplexed-computer-system.md) — the dismissal in chapter three of any scheduling scheme whose cost grows with the number of waiting processes, and chapter five's treatment of scaling, the shared-list contention bottleneck, and the thrashing diagnostics that must precede any judgment about system balance.
