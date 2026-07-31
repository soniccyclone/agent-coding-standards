---
type: lesson
title: "A convenient special case quietly becomes the only shape you can imagine, so learn the general one first"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# A convenient special case quietly becomes the only shape you can imagine, so learn the general one first

**Lesson:** A restricted construct that fits its intended pattern well is not neutral equipment. It supplies a default shape for problems, and after enough use the default stops being a choice and becomes an unexamined assumption about how the solution will look. Approaching a task already expecting the main repetition to have a fixed range decided in advance is not a small bias: for a substantial class of problems, that expectation rules out every simple or efficient solution, because the natural algorithm advances different quantities on different iterations, or stops on a condition, or does not know its extent until it gets there. The construct did not cause the bad solution. It caused the good one never to be considered.

The remedy is an ordering one, and it applies to how you learn a technique as much as to how you teach it. Become fluent in the general mechanism first, on enough real problems that you have felt the shapes that do not fit any restricted form, and only then adopt the convenience. Acquired in that order, the special case is what it should be — a compact notation for a pattern you can already recognize, and which you will notice yourself trying to force. Acquired first, it becomes the boundary of the problem space.

This is a better response than either of the two positions people usually take. Banning the convenient form is an overreaction that costs real clarity where the pattern genuinely holds, and where its restrictions buy a guarantee the general form cannot offer. Reaching for it by reflex costs you the problems it does not fit. The middle position is not a compromise but a sequencing claim: the danger lies entirely in the construct arriving before the fluency, and once the fluency exists, the danger is gone and the convenience is free. The same reasoning applies to any tool narrow enough to be pleasant — a framework, a data structure, a query form — whenever it is comfortable enough that you stop noticing you have chosen it.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 4.1.6, which grants that the for statement is clearer and more concise where iteration runs over a predetermined interval, then warns that a significant number of iterations in well-written programs do not fit the pattern, that the danger is a narrowing of the programmer's viewpoint, and that the unspoken assumption that the main loop will be a for statement precludes any simple or efficient solution in cases such as the earlier partitioning program; noting that some authors avoid the construct entirely while the author is unwilling to go that far, and has deliberately postponed its introduction until the reader has seen a substantial number of programs that cannot be fitted into its mould.
