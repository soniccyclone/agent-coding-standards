---
type: lesson
title: "To prove something cannot be done, count the distinctions the machine must carry"
figure: hartmanis
works: [on-the-computational-complexity-of-algorithms]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# To prove something cannot be done, count the distinctions the machine must carry

**Lesson:** There are two ways to show a resource budget is insufficient, and they are not equally usable. One is to build a pathological object that disagrees with every candidate in an enumeration — powerful, fully general, and it tells you almost nothing about any problem you actually care about. The other is to count: work out how many different pasts the machine is obliged to tell apart in order to answer correctly, work out how many different pasts its state plus its locally reachable memory can physically represent within the budget, and observe that the first number outgrows the second. When it does, no amount of ingenuity closes the gap, because the shortfall is in carrying capacity rather than in strategy.

What makes the counting argument tractable is a change in who sets the terms. When the object under study is something the machine emits on its own schedule, the analyst is a spectator. When the object is a decision about an incoming stream, the analyst chooses the stream and can therefore engineer situations where two histories must lead to different answers, forcing the machine to have distinguished them earlier. Reframing a question so that you supply the demands rather than observe the output is what converts an intractable impossibility claim into an arithmetic comparison. The first concrete impossibility result in this line of work came from exactly that reframing, not from a stronger diagonal construction.

A programmer who thinks this way handles "is this fast enough to be possible at all" differently from "how do I make this faster." Before optimizing, they ask what the computation is obliged to remember and how far that information has to travel to be used, because the answer bounds every implementation at once. The bound comes from the geometry of storage and from the number of cases that must remain separable — not from the instruction set, the language, or the compiler — which is why it survives every rewrite. This is also the honest explanation for the ceilings people keep hitting empirically: a streaming system that cannot answer a query with bounded memory is not badly written, and profiling it will never reveal the reason.

The habit generalizes beyond running time. Whenever a design claims to answer a class of questions from a summary rather than from the full history, the diagnostic is to count how many histories the summary must distinguish. If the count exceeds what the summary can encode, the design is wrong at the level of information, and the discussion about caches, indices, and clever encodings is already over.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the recognition-problem section, where the shift from generating sequences to deciding membership in a language is argued to make impossibility easier to establish, and the accompanying lower-bound argument comparing the number of input histories that must be distinguished against the machine's finite state and bounded reachable tape.
