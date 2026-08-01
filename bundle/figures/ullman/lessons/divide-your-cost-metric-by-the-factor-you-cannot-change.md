---
type: lesson
title: "Divide your cost metric by the factor you cannot change"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Divide your cost metric by the factor you cannot change

**Lesson:** A performance figure that mixes what you decided with what you were handed is nearly useless for making decisions, because two designs' numbers differ for reasons that have nothing to do with either design. The repair is to factor the cost expression into the part determined by your choices and the part fixed by circumstance, then quote only the first. If the total time is the number of times you sweep the data multiplied by the volume of the data, and the volume is given to you, then the honest metric for a design is the sweep count, full stop. Everything else in the expression is a constant you and every competing design pay identically.

The gain from doing this is that the metric becomes small-integer and therefore arguable. Design decisions stop being ranked by benchmark noise and start being ranked by a number you can predict from the algorithm's structure before writing any code, which in turn makes the design conversation about the right thing: is there a formulation that folds two sweeps into one, and what does it cost in memory to do so. It also makes the trades visible in their real currency. Spending an extra sweep to shrink the working set is a legible exchange when both sides of it are counted in sweeps and bytes; it is invisible when everything is collapsed into a single wall-clock figure whose composition nobody can see.

The move has a precondition, and stating it is the part that separates a useful simplification from a misleading one. Reducing the metric to sweep count assumes the per-item work inside a sweep is genuinely dominated by the cost of the sweep itself. That assumption has an expiry: the in-memory work of expanding each unit of input into all its combinations grows fast with the size of the combinations, and there is a size beyond which it overtakes the transfer. The right treatment is to say so out loud, name the regime in which the metric holds, and then give the reasons that regime is the one you are in — you rarely need large combinations, and the pruning you do along the way shrinks each unit so the growth is fought from the other side. A simplification defended this way survives contact with a case that violates it, because the violation is recognisable. A simplification adopted silently just becomes wrong at some point nobody notices.

The general habit: before optimising, write the cost as a product, cross out every factor you cannot influence, and let what remains be the thing you report, compare and target. What you cross out is not irrelevant — it sets the absolute scale and tells you whether the problem is worth attacking at all — but it does not discriminate between your options, and a metric that does not discriminate between options cannot guide a choice.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 6's discussion of how to measure a frequent-itemset algorithm, which argues that running time is proportional to the number of passes over the basket file times the file's size, observes that the data volume is not under the algorithm designer's control, and therefore adopts pass count alone as the measure, having first named the regime in which per-basket subset generation stays cheap relative to reading the basket from disk.
