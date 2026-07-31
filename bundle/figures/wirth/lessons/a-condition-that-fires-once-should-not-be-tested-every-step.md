---
type: lesson
title: "A condition that fires once should not be tested on every step"
figure: wirth
works: [algorithms-and-data-structures]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A condition that fires once should not be tested on every step

**Lesson:** A loop guard is usually assembled from every reason the loop might stop, and the assembly is done without asking how often each reason actually fires. That is where the waste hides. A test that can succeed at most once in the whole execution — the one that detects the answer and terminates — is being evaluated on every iteration to earn its single success, while a test that must be evaluated anyway carries no such asymmetry. Once you notice the asymmetry, two cheap moves follow. If the guard is a conjunction, order it so the rarely-decisive test is evaluated last, because the common path then stops before reaching it. And if the rare test can be removed from the guard altogether and asked once after the loop, ask whether removing it is a net win.

The second move looks like a mistake, because removing the early exit means the loop keeps running after the answer is already determined, and doing avoidable work is exactly what optimization is supposed to eliminate. Do the arithmetic instead of trusting the reflex. The saving is a simplification of every step; the loss is the steps taken after the answer was known. When the number of steps is small and bounded — logarithmic in the size, say — the loss is a handful of iterations and the saving applies to all of them, so the exchange is favourable and often decisively so. When the number of steps is large and the exit typically fires early, the exchange is a disaster. The point is not that early exits are bad; it is that "stop as soon as you know" is a wish rather than an argument, and the argument is a comparison between a once-only saving and a per-step cost.

There is a second dividend that usually outweighs the first. A guard with one term rather than two has no evaluation-order dependency, no term whose meaning depends on another term having already been checked, and a correspondingly shorter invariant — which means the loop's correctness argument shrinks along with its body. That makes the simplified version not just faster but more likely to be right, and it is worth reaching for even where the timing argument is a wash. The habit to build: for every term in a loop condition, write down how many times it can decide the outcome. Terms that can decide it once belong outside the loop, or at the end of the conjunction, or in the data — never silently in the hot position.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 1.8.2's remark that efficiency improves by interchanging the two if-clauses so that equality is tested second because it occurs only once and causes termination, and the section's subsequent development of the faster binary search, which abandons the naive wish to terminate as soon as a match is established on the reasoning that the gain in efficiency at every step is greater than the loss incurred by comparing a few extra elements given that the number of steps is at most logarithmic; together with the resulting single-term loop condition and its shorter invariant, and the accompanying note that one extra equality test after the loop is then required.
