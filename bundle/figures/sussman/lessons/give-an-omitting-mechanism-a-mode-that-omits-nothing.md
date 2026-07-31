---
type: lesson
title: "Give any mechanism that works by omission a mode that omits nothing, because the diff against that mode is the only complete record of what it decided"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Give any mechanism that works by omission a mode that omits nothing, because the diff against that mode is the only complete record of what it decided

**Lesson:** There are two ways to build a mechanism that avoids unnecessary work, and they differ in what evidence they leave. One produces everything and then removes what it can prove unneeded; the removals are events, and they can be logged, counted, and reviewed. The other never produces the unneeded thing in the first place; the decisions leave no trace anywhere, because the output contains only what survived and there is nothing in it to indicate that a question was ever asked. The second style is usually the better engineering — it is cheaper, and it cannot leave debris — and it is the one that makes the mechanism opaque. You cannot audit an absence.

The recovery is cheap and worth building deliberately: give the mechanism a mode in which the condition is forced, so that it emits everything unconditionally. Run both, diff the outputs, and the difference is not an estimate of what the mechanism does. It is the exact and complete list of the decisions it made, in position, on this input. That is more information than any measurement provides. A benchmark tells you the aggregate effect and hides the distribution; the diff shows you every individual choice, including the ones that were wrong, the ones that never fire, and the pattern of where they cluster — which is where the next improvement is.

Two things follow for design. First, the forced mode is not test scaffolding to be added when something goes wrong; it should exist from the start, because its value is highest before anyone suspects a problem, when it is the only way to know whether the mechanism is doing anything at all. A conditional optimization that has quietly stopped firing produces correct output forever and is indistinguishable from one that works. Second, this is the cheapest form of the general practice of making a system able to produce its own counterfactual. Anything that decides — a cache deciding to serve, a scheduler deciding to batch, a planner deciding to skip a step — should be able to run with the decision disabled and be compared against itself, and the comparison should be a normal operation rather than an experiment someone constructs by editing code.

The habit generalizes to reviewing other people's mechanisms too. When you are handed something that claims to eliminate work, the first question is not how much it eliminates but whether you can obtain the artifact it would have produced without eliminating anything. If you cannot, the claim is untestable in detail, and the mechanism's failures will be silent by construction.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 5, Exercise 5.37, which proposes understanding the compiler's mechanism for optimizing stack usage by seeing what extra operations would be generated without it: modify the combining procedure so that it always emits the save and restore operations, compile some simple expressions, identify the unnecessary stack operations that appear, and compare that code against the code produced with the mechanism intact. Related is Exercise 5.34's instruction to compile the iterative form of a procedure and annotate the result to exhibit the essential difference from the recursive form that makes one build up stack space and the other run in constant space.
