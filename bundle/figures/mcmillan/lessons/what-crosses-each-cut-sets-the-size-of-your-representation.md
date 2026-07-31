---
type: lesson
title: "What crosses each cut sets the size of your representation"
figure: mcmillan
works: [symbolic-model-checking-10-20-states-and-beyond]
axes: [hardware-affinity, expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# What crosses each cut sets the size of your representation

The empirical section of this paper reports a result its authors clearly found more interesting than the headline number of states: as the data path of the verified pipeline is widened, the stored form of the step relation grows *linearly*, and consequently the verification time grows as a polynomial rather than an exponential. The explanation given is one sentence long and is the entire lesson. The variables were laid out so that everything belonging to one bit position sat together, and between consecutive groups only a fixed handful of signals — the control bits, the arithmetic carry — actually needed to pass. Widening the circuit adds groups; it does not widen the seam between them.

The mechanism generalises because it is not about circuits. Any canonical representation that examines its inputs in a committed order is, in effect, a machine scanning left to right that must carry across each boundary everything about the prefix the suffix could still care about. Size is then governed by the width of that carried summary, maximised over boundaries — not by how many inputs there are, and not by how many configurations the whole thing admits. The paper makes this concrete by noting that these diagrams are just minimal recognisers for the set of satisfying assignments, which is the same statement: the states at each level are the distinct things worth remembering about a prefix.

Two operational consequences fall out, and the paper commits to both. The first is that ordering is a real engineering decision, because it *is* the choice of where the cuts go, and a good one interleaves interacting quantities while keeping non-interacting ones apart. The second is more valuable and much rarer to see stated: some functions admit no good ordering at all. Multiplication is named outright as the known negative case, and the authors extend it forward — put an operation in the pipeline that moves more than a bounded amount of information between bit positions, a multiplier or a barrel shifter, and the representation stops being manageable no matter how the variables are arranged. That is not a tuning problem, and recognising it as a structural one is what stops you spending a month on orderings.

The habit this builds is to look at any large structure you have to represent, imagine slicing it along whatever order your tooling commits to, and ask how much has to be remembered across the worst slice. It is the same quantity that decides whether a streaming computation needs bounded memory, whether a join can be pipelined instead of buffered, whether a module boundary is a genuine abstraction or a wide leaky interface with a header file in front of it. Narrow cuts are the property; everything else is a way of arranging to have them, and the arrangements are worth searching for only when you have first checked that one exists.

**Source:** [Symbolic Model Checking: 10^20 States and Beyond](../works/symbolic-model-checking-10-20-states-and-beyond.md) — the pipeline performance discussion attributing linear growth of the transition relation to bit-position variable grouping with only a constant number of signals crossing between groups, the accompanying warning about multiply and barrel-shift operations, and the earlier characterisation of the diagrams as minimal finite automata over assignments.
