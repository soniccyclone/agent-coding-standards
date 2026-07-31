---
type: lesson
title: "If you need one part of the answer, descend into one part only"
figure: wirth
works: [algorithms-and-data-structures]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# If you need one part of the answer, descend into one part only

**Lesson:** A question is often answered by computing something much larger and then reading the answer off it. Wanting the element that would occupy a particular rank, you put everything in order and index into the result. That works and it overcharges you, because the ordering of everything is a far stronger fact than the one you asked for, and you paid for all of it. The useful move is to look at the machinery of the expensive method and notice that it usually contains a step which divides the problem in two, and that the divide step by itself already tells you which half your answer lies in. Once you know that, the other half can be abandoned entirely rather than processed.

The change in cost is not a constant factor, it is a change in the series being summed. Processing both halves at every level costs a full pass per level, and there are logarithmically many levels, so the total is the familiar product. Processing one half means the second level costs half a pass, the third a quarter, and the sum of that series is bounded by twice the first pass, no matter how many levels there are. This is why "recurse into one side" is worth actively hunting for: it collapses a logarithmic factor to a constant, and it does so without any cleverness in the divide step itself, which is reused unchanged. The general rule to carry: when a divide-and-conquer method is used to answer a question about a *specific* position, region, or item rather than about all of them, check whether the conquer phase can be restricted to the part containing it.

Two cautions keep this honest. The good behaviour depends on the split being roughly even, so the same worst case that afflicts the parent method afflicts this one, and the same mitigations apply — but the consequences differ, since here a bad split costs you the entire advantage rather than a logarithmic factor. And the small-input caveat is stronger than usual: a method whose gain is an asymptotic collapse has nothing to offer below a modest threshold, where the direct approach is both faster and simpler, so the threshold belongs in the code rather than in a footnote. What you should take from the pattern is the habit of asking, of any expensive computation whose result you are about to index into, which parts of that result you never look at — and then whether the method can be told not to build them.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 2.3.4's treatment of finding the median, which notes that the obvious method is to sort the items and pick the middle one, then reuses the partitioning operation of the partition sort unchanged, keeps only the partition in which the desired rank lies, and iterates; the accompanying analysis summing the halving series to roughly twice the input size and contrasting this with the best sorting methods' higher order; and the section's closing observations that in the worst case each partitioning step reduces the candidate set by only one, and that there is hardly any advantage in the method for small numbers of elements.
