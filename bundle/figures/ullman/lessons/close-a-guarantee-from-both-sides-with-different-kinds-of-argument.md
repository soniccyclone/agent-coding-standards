---
type: lesson
title: "Close a guarantee from both sides, with a witness above and a structural argument below"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Close a guarantee from both sides, with a witness above and a structural argument below

**Lesson:** When you claim that a procedure always achieves at least some fraction of the best possible result, you are making two separate claims that need two entirely different kinds of evidence, and confusing them is why such claims are so often either unprovable or unfalsifiable. The ceiling — the guarantee cannot be better than this — is established by exhibiting one input on which the procedure genuinely does that badly. A single concrete witness settles it, permanently, and constructing witnesses is cheap and satisfying work. The floor — the guarantee is never worse than this — cannot be established by examples at all, no matter how many. It requires an argument over the structure of every possible run.

The floor argument has a recognisable shape worth learning as a technique. You compare a run of your procedure against a hypothetical best run, and instead of tracking what your procedure did, you characterise what it must not have done. Take the items the ideal solution handled that yours did not; observe that your procedure's own rule forbids leaving such an item untouched unless something adjacent to it was already taken; conclude that each shortfall implies a corresponding success elsewhere in your own output; then count. The greedy rule that looked too simple to analyse turns out to be exactly what makes the argument go through, because a rule that never declines an available opportunity leaves a trail of forced consequences you can enumerate. Simple rules are not merely easy to implement; they are the ones whose behaviour is small enough to reason about globally.

When the two bounds meet, you are done and you know you are done, which is the practical point of doing both. When they do not meet, the gap is not an embarrassment but a work item that tells you exactly where to push: either the witness is not adversarial enough and a nastier input exists, or the structural argument is conceding more than it needs to. That is a far better position than an unbounded belief that the procedure is "usually fine."

Generalise the discipline past algorithm analysis. Any property you assert of a system — latency never exceeds, memory never grows past, this cache never misses more than — deserves the same treatment: an example demonstrating the property cannot be strengthened, and an argument from the mechanism showing it cannot be weakened. Testing alone can only ever supply the first half.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the advertising chapter's analysis of greedy maximal matching, where one adversarial edge ordering caps the ratio and a counting argument over the nodes matched in the ideal solution but not the greedy one establishes the matching floor, the two coinciding to fix the ratio exactly.
