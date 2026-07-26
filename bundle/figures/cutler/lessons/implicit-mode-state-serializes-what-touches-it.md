---
type: lesson
title: "Any behavior you put in shared implicit state serializes every operation that reads it; encode it in the operation instead"
figure: cutler
works: [decwest-sdt-agenda-prism-vs-mips]
axes: [parallelizability, expressiveness, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Any behavior you put in shared implicit state serializes every operation that reads it; encode it in the operation instead

**Lesson:** When the meaning of an operation depends on a mode held somewhere off to the side, two things follow immediately and neither is obvious from the design's surface. The operations that consult the mode can no longer be reordered or overlapped with each other, because each one's result depends on what the mode was at its own moment, so the shared cell is a serialization point whether or not anyone intended one. And every caller becomes responsible for knowing the mode's current value, saving and restoring it across boundaries, and reasoning about who else might have changed it. Both costs come from the same choice: information the operation needs was placed outside the operation.

Putting the same information into the operation itself removes both costs at once. If the rounding behavior is part of the instruction, two instructions with different behavior can be in flight together and no caller has to remember anything. If a comparison's result lands in a destination the caller names rather than in a single shared bit, several comparisons can proceed independently. If a result is delivered to a general destination rather than a dedicated holding location that must then be copied out, no pipeline hazard and no extra move are created. Each of these looks like a small local decision about where to put a value, and each of them is actually a decision about whether the operations that use it can be independent.

The generalization is a design instinct, not a hardware fact. Wherever a system offers ambient configuration that changes what subsequent calls mean — a global mode, a thread-local setting, a current-context object, an implicit precision or locale — it has created a resource that must be coordinated, and the coordination will be invisible in the code that pays for it. The alternative is to make the varying behavior an argument. This costs a little verbosity at every call site and buys back composability, the ability to reason about a call in isolation, and the freedom to run calls concurrently. Related is the mirror-image failure: state that must be shared for correctness but has no defined sharing rules, in which case there is nothing to coordinate with and the software is left inferring the rules from one implementation's timing.

**Source:** [DECwest/SDT Agenda: PRISM vs. MIPS](../works/decwest-sdt-agenda-prism-vs-mips.md) — the architectural-problems slides, which object to floating-point rounding modes being programmed through a status and control register instead of being part of the instruction, to comparison results landing in a single status bit that serializes comparisons, and to multiply and divide results being held in dedicated registers that prohibit pipelining and force extra moves.
