---
type: lesson
title: "Analyse cost against the part refinement will not change, and the answer comes back as a budget the representation has to meet"
figure: reynolds
works: [the-craft-of-programming]
axes: [hardware-affinity, verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Analyse cost against the part refinement will not change, and the answer comes back as a budget the representation has to meet

**Lesson:** You do not have to wait for a concrete program to reason about its running time, and waiting is usually a mistake, because by then the decisions that determined the running time have already been made. The move is to notice when some structural feature of the computation has stopped changing — here, the shape of the call tree, which every remaining refinement will only decorate — and do the counting against that. Everything still unfixed gets left as an unknown constant. The output is not a number, it is a linear form: total cost equals so many of this kind of step times whatever one costs, plus so many of that kind times whatever one costs.

Counting the steps is its own technique, and it is not unrolling the recursion. Partition the invocations into a small number of kinds distinguished by what they do, then count each kind by a global argument rather than a local one. If a certain kind of call is exactly the kind that enlarges a set which starts empty and finishes holding everything, then there is one such call per element and you never had to think about the recursion at all. The remaining kind is then whatever is left over, obtained by counting outgoing edges. Two population counts, no induction.

The last step is the one that changes how you work. Because the constants in the linear form are still unknown, the conclusion is conditional: this is linear in the size of the input *provided* one kind of step can be made to run in constant time and the other in time proportional to a local degree. That conditional is not a caveat, it is a specification — you have derived, before choosing any data structure, the exact per-operation budget the eventual representation must come in under. Which is how you end up justified in reaching for a representation that looks strange in isolation. It is not strange; it is the cheapest thing that meets a requirement you established two levels of abstraction earlier, and without the abstract analysis you would have had no argument for paying its price.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the closing part of Section 5.4.1, which observes that further development will not change the program's calling tree and that total execution time can therefore be expressed in terms of individual call times at this stage; classifies calls as terminal or nonterminal by whether the node is already visited, argues that exactly one nonterminal call occurs per node because such a call adds a node to a set that grows from empty to the whole node set, derives the number of calls from the total out-degree, assumes unknown constants bounding a terminal call and bounding a nonterminal call plus a term proportional to out-degree, and concludes a bound of order nodes plus edges — noting that the result depends on later producing a concrete program in which a terminal call takes constant time and a nonterminal call takes time proportional to out-degree, a goal to be met by introducing an unusual data representation.
