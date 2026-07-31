---
type: lesson
title: "Find the phase that moves data without changing the invariant, and fuse it away"
figure: wirth
works: [algorithms-and-data-structures]
axes: [hardware-affinity, cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Find the phase that moves data without changing the invariant, and fuse it away

**Lesson:** A process built as alternating stages will often contain one whose entire contribution is relocation. It reads everything and writes everything, so it accounts for a large share of the total traffic, and it establishes nothing: after it runs, the property you are trying to build up is exactly what it was before. That stage is not doing the work, it is preparing the next stage's inputs to be in the right places, and preparation of that kind is a candidate for elimination rather than for optimization. The diagnostic is precise and worth applying to any pipeline: for each stage, state what it changes about the invariant. A stage with no answer is pure overhead, however necessary it looks in the diagram.

Eliminating it means fusing it into the stage that follows or precedes — instead of producing a single combined result and then dividing it up for the next round, have the producing stage write its output directly to the several places the next round will read from. The work disappears rather than getting faster, which is the difference between removing a phase and tuning one. The price is usually a resource: you now need as many destinations as sources rather than reusing one, so the peak footprint grows even though the total traffic halves. That is the trade to evaluate, and it is a good trade far more often than not, because storage is a fixed cost you pay once and traffic is a recurring cost you pay every round.

Two further points make the technique general. First, the fusion is often expressible without extra hardware at all if you already control the addressing — two destinations can be the two ends of one region, filled toward each other, which gets you the halved traffic without the extra resource, at the cost of arithmetic that has to alternate direction. When that trick is available it is nearly free, and noticing it is a matter of asking whether "two containers" was ever a requirement or just how the diagram was drawn. Second, once the redundant stage is gone, name the surviving structure honestly: a process that used to have two phases per round now has one, and the vocabulary should change with it, because people reason about the cost of a process from the number of times it says it touches the data.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 2.4.1's observation that the splitting phases of a straight merge sort do not permute the items and are in a sense unproductive although they constitute half of all copying operations, that they can be eliminated by redistributing the merge output directly onto the two sources of the following pass, that the resulting single-phase or balanced merge is superior because only half as many copying operations are needed with a fourth tape as the price; and the same section's demonstration that a single array regarded as double-ended, with a direction increment that alternates sign and destinations that swap after each merged run, serves in place of two separate destination sequences.
