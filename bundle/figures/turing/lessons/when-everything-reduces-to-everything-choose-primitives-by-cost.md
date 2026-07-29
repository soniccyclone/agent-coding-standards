---
type: lesson
title: "Once your operations can all simulate each other, the primitive set is an economic choice, not a logical one"
figure: turing
works: [proposed-electronic-calculator-ace-report]
axes: [primitive-count, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, foundations-of-computation]
tags: [lesson]
---
# Once your operations can all simulate each other, the primitive set is an economic choice, not a logical one

**Lesson:** In a system rich enough that any operation can be built out of the others by some roundabout route, theoretical adequacy stops discriminating between candidate instruction sets — every candidate is adequate. What remains is judgement about cost: how often each operation is actually wanted, how expensive it is to build into the fixed part of the machine, how painful the roundabout route is when you take it. This inverts the naive design instinct. The question is not "what operations does the work require" but "which of the required operations earn a place in the layer that cannot be changed later."

The corollary is a bias about where to put things. Anything realized in the rewritable layer can be corrected, improved, or replaced as you learn; anything built into the fixed layer commits you. So a capability that can be assembled out of cheaper pieces belongs in the assembled layer even when a dedicated mechanism would be faster, because you will discover what the mechanism should have been only by using the system. That argues both for a deliberately spare set of built-in operations and for building the fixed part out of interchangeable units, so a change of mind costs rewiring rather than redesign. It also argues against perfecting the design before first use: past a point, extra design time buys less than the same time spent running the thing and finding out where it hurts.

A programmer who thinks this way spends the budget differently. Rather than a broad instruction set, API surface, or built-in operator list, they ship a small one plus a good way to compose it, and they keep a list of the composed routines that turned out hot — because that measured list, not their prior guess, is the argument for promoting something into the fast fixed path. They also accept some deliberate awkwardness: an operation that is clumsy to express through the primitives is tolerable if it is rare, and the clumsiness is information about frequency rather than a defect. The habit to build is asking, for every proposed primitive, what it would cost to do without it and how often you would pay.

**Source:** [Proposed Electronic Calculator (Report on the ACE)](../works/proposed-electronic-calculator-ace-report.md) — the discussion of the arithmetic unit's operation list, where Turing notes the operations are inter-reducible so judgement is needed in choosing the fundamental ones, leaves division out of the hardware in favour of an iterative software routine, and the later planning chapter's argument for standard interchangeable units and for learning the right circuits by using the machine.
