---
type: lesson
title: "Cut a system along anticipated change, not along the order in which work happens"
figure: parnas
works: [on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Cut a system along anticipated change, not along the order in which work happens

**Lesson:** The default instinct when facing a system is to name its stages — take input, transform, order, emit — and make each stage a component. That instinct comes from having learned to sketch control flow before writing anything, and it produces a partitioning whose boundaries coincide with moments in time. The trouble is that time-of-execution is not a stable property of a system. What is stable, or at least predictably unstable, is the set of judgment calls the designer had to make: how data is laid out, whether a derived structure is materialized or recomputed, whether an ordering is established eagerly or lazily, what the external formats are. Boundaries drawn around stages leave those judgment calls smeared across every component, because a representation chosen in one stage must be understood by all the later ones. Boundaries drawn around the judgment calls themselves leave each one confined.

The reason this works is asymmetric information cost. A component that knows only the names and argument shapes of what it calls can survive any revision on the other side of that line; a component that knows a layout, a packing convention, or a completion guarantee is coupled to the reasoning that produced it and dies with it. So the design activity that matters is not drawing the diagram — it is producing the list of decisions that are questionable or likely to move, and then arranging that each one has exactly one keeper. Note that this makes decomposition an act of prediction. You are betting on which parts of the problem statement will shift, and the structure is the record of that bet.

Two consequences follow that programmers usually resist. First, the resulting components will not line up with phases, so a reader cannot narrate the system as a sequence — one component may be active throughout, another may not correspond to any identifiable moment at all because it may compute on demand rather than in a pass. Second, because you have moved the boundaries off the natural seams of the runtime, you can no longer let the runtime's convenience dictate them. The programmer who believes this stops asking "what does this system do, in what order" as the opening design question and starts asking "what did I have to decide here, and which of those decisions do I not trust to stay put."

Independent development follows from the same move: when the agreements between groups are complex shared layouts, those agreements must be negotiated jointly and settled before anyone can start, so the shared design work dominates. When the agreements are just call signatures, they are cheap to settle and parallel work begins almost immediately. Interface complexity, not component count, is what determines how much of a project can proceed in parallel.

**Source:** [On the Criteria To Be Used in Decomposing Systems into Modules](../works/on-the-criteria-to-be-used-in-decomposing-systems-into-modules.md) — the side-by-side comparison of the two decompositions of the same index-building program, the enumeration of five candidate changes and how far each propagates in each scheme, and the section naming the criteria used to arrive at each.
