---
type: lesson
title: "As a system's defects thin out, the survivors are almost all synchronization, so design for concurrency at the start or not at all"
figure: cutler
works: [oral-history-of-david-cutler, decwest-sdt-agenda-prism-vs-mips]
axes: [parallelizability, verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# As a system's defects thin out, the survivors are almost all synchronization, so design for concurrency at the start or not at all

**Lesson:** Defects are not drawn from a uniform pool. The ones that fall out easily are errors of control flow and arithmetic, findable by inspection and by any test that happens to touch the path. What remains once those are gone is a qualitatively harder population: missing memory barriers, locks held over the wrong region, orderings between code paths that are usually but not always safe. So the difficulty of the remaining work rises as the count falls, and a project's residual risk is concentrated almost entirely in its concurrency structure. A programmer who internalizes this stops reading a shrinking defect count as proportional progress and starts treating the endgame of a system as a synchronization review rather than a cleanup.

This is the argument for making a system concurrent from its first design rather than parallelizing it later. Retrofitting concurrency means revisiting every invariant in a codebase that was written under the assumption of a single thread of control, and doing so without the benefit of the original author's reasoning about what was protecting what. Deciding up front that multiple processors are the normal case forces every component to state its synchronization discipline while its author still has the whole picture. The cost of that decision is real and shows up as schedule, which is worth naming honestly, but it is paid once instead of being paid again on every component in an unbounded sequence of later passes.

Because these are the hard bugs, the mechanisms the machine provides for making state changes atomic are not incidental conveniences but the foundation the whole discipline rests on. An architecture that offers no interlocked read-modify-write, no way for one processor to identify itself, no way for one processor to interrupt another, and no stated rules about when a write becomes visible or when caches agree, has not left concurrency to software; it has made correct concurrency unstateable. Every synchronization argument you would like to make has to be replaced by an argument about a specific implementation's timing, which is exactly the class of reasoning that does not survive the next chip.

**Source:** [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — the exchange on how to get fewer and easier defects, where he identifies synchronization rather than code flow as the hard residue, alongside his account of committing to multiprocessor support from the first day of the kernel's design. Also [DECwest/SDT Agenda: PRISM vs. MIPS](../works/decwest-sdt-agenda-prism-vs-mips.md) — the architectural-problems slides, which treat absent interlocked instructions, absent processor identification, absent interprocessor interrupts, and undefined data-sharing and cache-coherency rules as first-order disqualifiers.
