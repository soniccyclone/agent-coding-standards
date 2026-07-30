---
type: lesson
title: "Describe an algorithm by the condition it maintains, not by its sequence of steps"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Describe an algorithm by the condition it maintains, not by its sequence of steps

**Lesson:** The customary way to present an algorithm is a sketch of its steps, which is opaque enough that the sketch nearly always has to be propped up with a traced example. The alternative is to state the condition its working state satisfies at every stage and let the steps follow. This is not merely a different presentation; it changes what you can see. Whole families of algorithms over the same structure become comparable, because they differ only in their maintained conditions, and a design decision that looks like a different program turns out to be a single extra clause. Two well-known approaches to ordering a collection in place differ by whether the finished portion is also known to be below everything remaining — one conjunct, and the entire character of the algorithm follows from it.

Push this and the labour redistributes in a useful direction. The condition carries the content, so the per-step obligation shrinks to something nearly trivial: make progress, don't break the condition. Anyone reading it can check the step by inspection and spend their attention on the condition, which is where the actual idea lives. Anyone modifying it knows precisely what must not change. And the choice of new variables to carry the state stops being arbitrary bookkeeping, because each one exists to make a specific weakening of the goal expressible.

One caution keeps this from becoming a licence for elegance. The condition must be phrased in terms of what the algorithm genuinely manipulates. An algorithm whose whole substance is the rearrangement of positions within a structure is not clarified by describing it in terms of the collection of values it holds, however cleaner that vocabulary looks in isolation — the mismatch shows up as reasoning that never quite connects to the code. Choose the abstraction the algorithm actually works in, and if the honest abstraction is index arithmetic then say so. Abstraction chosen for its beauty rather than its fit costs more than the mess it was meant to hide.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the sorting and searching section of the examples chapter: its argument that algorithm taxonomy is best tackled via data type invariants rather than pseudo-code sketches supported by examples, the binary-search development where the loop body's postcondition is deliberately weak because the important content sits in the invariant, the pair of in-place sorting families distinguished by one added conjunct, the suggestion that recording facts about data structures may communicate a design better than an algorithm outline, and the closing remark that using sets in the design of a partition-based sort was a mistake because the algorithm is tied to manipulation of indices.
