---
type: lesson
title: "Treat the boundary between layers as a design variable, and decide what lives on each side last"
figure: ungar
works: [design-and-evaluation-of-a-high-performance-smalltalk-system]
axes: [hardware-affinity, primitive-count, expressiveness]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Treat the boundary between layers as a design variable, and decide what lives on each side last

**Lesson:** The standard advice is to define an interface and then implement beneath it, keeping the specification independent of the machinery that will realize it. That discipline buys portability, and it costs you the largest lever you have. When a function's placement is fixed by the interface, every inefficiency it causes must be attacked in place. When placement is negotiable, the same problem can be solved by moving the function: an operation that is awkward in the lower layer becomes a routine the upper layer supplies, a decoding step the upper layer keeps re-doing gets performed once ahead of time, a rare case gets removed from the fast machinery entirely and handled by a general handler that is allowed to be slow. None of those are optimizations within a layer. They are relocations across a boundary that most designs treat as fixed.

Two things make this a discipline rather than an excuse for layering violations. First, the direction of travel is chosen by measurement, not preference — move a function toward whichever side makes the aggregate cheaper on real workloads, and be willing to move it back. Second, relocation is only legitimate if the abstraction the user sees survives it: the whole point is that someone above the whole stack should be unable to tell where anything ended up. What you are giving up is not the interface, but the pretense that the interface can be designed without knowing what will implement it.

The cost is explicit and should be stated. A system co-designed with its implementation technology cannot be lifted onto a different one for free, and it will accumulate decisions that read as strange without the context of the technology that motivated them. That trade is worth making when the alternative is a design that meets its interface and fails its purpose — but it obliges you to record why each function landed where it did, because the reasoning is the only thing that will let a successor re-decide when the technology changes. A programmer who works this way asks, of every performance problem, not only "how do I make this faster here" but "which layer should be doing this at all."

**Source:** [The Design and Evaluation of a High-Performance Smalltalk System](../works/design-and-evaluation-of-a-high-performance-smalltalk-system.md) — the concluding chapter's statement that the key to the system's performance was willingness to migrate functionality up and down the implementation hierarchy and to view the system as a whole rather than as layers, illustrated throughout by decisions to compile rather than interpret and to replace rarely used built-in operations with software handlers.
