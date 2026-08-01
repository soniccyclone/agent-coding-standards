---
type: lesson
title: "Give the failure handler disjoint resources, and name the one it still shares"
figure: wirth
works: [project-oberon]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Give the failure handler disjoint resources, and name the one it still shares

**Lesson:** Code that runs because something failed inherits a hostile precondition: whatever was exhausted or corrupted is still exhausted or corrupted, and any resource the handler shares with the failed computation may be the one that failed. The usable discipline is not to make the handler frugal but to make it *disjoint* — give it its own stack, its own mode, its own working store — so that the class of failure it exists to report cannot be the class of failure that stops it. A reporter that runs on the same stack that just overflowed is not a reporter; it is a second crash with worse diagnostics. Disjointness is also what lets you state the handler's correctness as a plain claim rather than a hope: given a separate stack, the stack-overflow case is handled by construction, and no reasoning about margins is required.

The second requirement is protection against the handler's own recurrence, which is a distinct hazard from resource exhaustion and needs a distinct mechanism. Any handler complex enough to be useful can itself provoke the condition it handles, and the resulting loop consumes everything and reports nothing. A single flag, set on entry and cleared on exit, converts an unbounded recursion into one lost report — a bad outcome traded for a survivable one. Note the shape of the trade: the guard does not make the handler correct, it makes its incorrectness terminate. That is usually the right thing to buy at this layer, because at the moment of failure the system's remaining obligation is to say something and stop, not to be right.

Finally, and this is the part most often skipped, the disjointness will be incomplete, and the honest move is to write down where. A reporter that must produce output touches whatever the output path allocates from, so it shares that one resource with the program it is reporting on, and there is one failure mode — exhaustion of exactly that resource — that it cannot survive. Knowing this is worth more than pretending otherwise: it tells a reader precisely which crash will produce no report, and it identifies the single change that would close the remaining hole, should someone later decide the hole matters. An unqualified claim of robustness in a failure handler is nearly always false; a qualified one, with the exception named, is checkable.

**Source:** [Project Oberon](../works/project-oberon.md) — the closing commentary of section 12.9 on the `Trap` procedure: it runs in supervisor mode on the supervisor stack and therefore functions correctly in the case of a stack overflow; a global `trapped` flag, tested and set on entry, prevents a recursive trap; and the stated assumption that the routine causes no further trap *except* if its own output operations exhaust the heap.
