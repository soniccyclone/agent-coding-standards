---
type: lesson
title: "Turn a global limit into per-owner budgets before anyone writes code"
figure: cutler
works: [oral-history-of-david-cutler]
axes: [hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Turn a global limit into per-owner budgets before anyone writes code

**Lesson:** A whole-system property such as resident footprint, worst-case latency, or
boot time has no owner by default. It is the sum of many independent decisions, each
of which looks locally reasonable, and it therefore degrades monotonically unless
someone converts it into a quantity individual engineers are accountable for. The move
this teaches is to decompose the global limit into per-component allocations up front,
hand each engineer a number, and treat a claim that the number is unreachable as a
design conversation rather than as permission to overrun.

Why it works is a cognitive-load argument as much as an engineering one. Nobody on a
team of eight can hold the total footprint of a system in their head while writing an
interrupt handler, so a global target is unenforceable in practice; a personal
allocation is a single number that fits alongside the work. The budget also inverts the
usual failure mode of nonfunctional requirements, which is that they are checked only
at the end, when every overrun is already load-bearing and the only remaining options
are to cut features or ship bloated. Checked continuously against a per-component
allocation, an overrun surfaces while it is still one person's local problem.

The second half of the discipline is making the constraint socially unavoidable. It is
not enough to record a target in a plan document; the constraint has to appear in the
channel where the work actually gets negotiated, so that no one can trade it away
quietly in a hallway conversation. Restated in modern terms, the budget belongs in the
build output and the review checklist, not in an architecture document nobody reopens.

A programmer who believes this stops treating resource consumption as an emergent
outcome to be measured afterward and starts treating it as an input to be allocated,
the same way schedule and headcount are allocated. It also changes what "the design"
means: part of designing a component is deciding how much of the machine each piece is
entitled to, which forces the hardware's real limits into the design conversation at
the point where they can still change the structure.

**Source:** [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — the
account of building a real-time system for the PDP-11 line that had to run in far less
memory than its predecessor, where the response to the constraint was to distribute it
as individual memory allowances and keep it visible on every internal communication.
