---
type: lesson
title: "Give up the expectation that output resembles input, and whole-program optimization becomes available"
figure: backus
works: [the-fortran-automatic-coding-system, the-history-of-fortran-i-ii-and-iii]
axes: [hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Give up the expectation that output resembles input, and whole-program optimization becomes available

**Lesson:** The intuitive way to build a translator is piecewise: each construct in the input has a corresponding chunk of output, possibly with parameters filled in. That design is easy to reason about and it caps the quality of the result, because the good decisions are exactly the ones that depend on context. Abandoning the correspondence is what unlocks them. The output then contains instructions belonging to no particular input construct; branches appear that correspond to no control statement the author wrote; expressions come out rearranged past recognition; and the same loop construct compiles to nothing in one context and to several separate groups of instructions scattered around the program in another. Nothing was smuggled in — the constructs simply no longer own regions of the output.

Structurally this forces a discipline: emit nothing until the analysis that would change what you emit is complete. Information extracted from the input has to be parked in tables rather than turned into code, and much of a translator's apparent complexity is the interplay between what has been committed and what is still pending. The unit of reasoning shifts too. Once you are optimizing across constructs, the useful unit is no longer the statement but the straight-line stretch of program with one entry and one exit, related to its neighbors by which of them can precede it. That is a representation of the whole program's shape, and it is what makes global questions askable at all.

The cost side is real and worth stating plainly, because it is the same trade every layer of modern tooling makes. When output stops resembling input, you can no longer audit the machine's behavior by reading its code as a translation of yours. Correctness has to be established at the level you wrote, the tool's own errors become a separate category of problem from your errors, and even the people who built the thing were startled by what their own optimizer produced, each needing the author of a different stage to explain a different part of the result. A practitioner who accepts this stops treating a compiler's output as a paraphrase of the source and starts treating the source as the only artifact whose meaning they are entitled to reason about directly.

**Source:** [The FORTRAN Automatic Coding System](../works/the-fortran-automatic-coding-system.md) — the account of how translation is organized so that compilation is postponed until analysis is done, the observations about output instructions and transfers attributable to no source statement, and the introduction of the single-entry single-exit block with a table of its possible predecessors. Also [The History of FORTRAN I, II, and III](../works/the-history-of-fortran-i-ii-and-iii.md) — the recollection of being astonished at the transformations the finished system applied, and of needing the author of each stage to account for its share of them.
