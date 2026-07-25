---
type: lesson
title: "The parts of a system improve at different speeds, so put the seams where the rates diverge and keep spare room in every vocabulary you fix"
figure: brooks
works: [architecture-of-the-ibm-system-360]
axes: [hardware-affinity, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The parts of a system improve at different speeds, so put the seams where the rates diverge and keep spare room in every vocabulary you fix

**Lesson:** A system is assembled from several technologies, and they do not advance together. Storage, logic, connections to the outside world, and the techniques for programming all get cheaper and faster on their own schedules, which means the ratios between them — the ratios a design implicitly encodes when it decides how much work to do where — are guaranteed to be wrong later. This is the difference between designing for a moment and designing for a decade, and it is not solved by picking better numbers. It is solved by identifying the axes along which the ratios will shift and refusing to weld across them, so that each part can be replaced or rescaled without the others having to move in step.

Two habits follow. The first is timing independence: if two components must not be locked to each other's speed, then their interaction is specified in terms of completion and status rather than in terms of elapsed cycles, and each is allowed to run on its own clock. That looks like extra work at the moment the ratio happens to be convenient, and it is the only thing that survives the ratio changing. The second habit concerns any fixed vocabulary — an operation set, a code space, a field of bits whose meanings are enumerated. Such a vocabulary is a commitment to a count of primitives, and the demands that will arrive against it cannot be enumerated in advance, only extrapolated in direction. So part of the space is reserved unassigned: not because a use is known, but because the alternative is that the first genuinely new requirement has nowhere legal to live and gets encoded as a violation of the design.

This is a different discipline from generality, and easy to confuse with it. Generality means making a facility handle every case its designers can imagine, which inflates the thing now. Open-endedness means making the design able to absorb what its designers could not imagine, which costs a little unused capacity now and forecloses nothing. The extrapolation itself is the intellectual work: naming the trends that are actually running — capacities rising, several processors instead of one, new classes of attached device, new ways of programming — and then asking of each design decision whether it stays sane under those trends or quietly assumes today's proportions. A programmer who thinks this way treats an unmarked "there is exactly one of these" or "this always finishes before that" as the most expensive kind of assumption, and spends real effort finding them before they harden.

**Source:** [Architecture of the IBM System/360](../works/architecture-of-the-ibm-system-360.md) — the open-ended design section, which argues from the differing rates at which constituent technologies change to asynchronous operation among components and to reserving unused capacity in the code space for modes and operations not yet conceived, and connects the same reasoning to anticipated growth in storage capacity, multiple processors, and new device classes.
