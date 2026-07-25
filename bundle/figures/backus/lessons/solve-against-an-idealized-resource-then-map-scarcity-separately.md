---
type: lesson
title: "Solve the problem against an unlimited resource, then treat scarcity as a separate stage"
figure: backus
works: [the-fortran-automatic-coding-system, the-history-of-fortran-i-ii-and-iii]
axes: [hardware-affinity, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Solve the problem against an unlimited resource, then treat scarcity as a separate stage

**Lesson:** A team building the loop-and-array machinery for a machine with three index registers found the combined problem intractable: generating good addressing code and deciding which of three physical registers holds what, simultaneously, resisted every attack. The move that rescued it was to stop solving the combined problem. Generate code for an imaginary machine with as many index registers as anyone wants, and let a later stage rewrite that program to fit the three real ones. Two whole passes of the system appeared that nobody had planned, and one more after that just to reconcile the formats — the cost of the decision was structural, not incidental, and it was still the right decision.

The general shape is worth extracting. When a problem couples a logical question to a resource-scarcity question, the coupling is often what makes it hard, and the two halves are frequently each tractable alone. Idealizing the resource lets the logical half be solved cleanly and completely; scarcity then becomes its own problem, with its own criteria and its own measurements, addressed by a stage that can be replaced without disturbing the first. The staging also localizes knowledge: independent groups can each own a stage, agree with their neighbors on what crosses the boundary, and invent freely inside their own. That is how the work actually got divided, and it is why the register-allocation stage could later be handed to different people entirely.

One detail from the same project guards against the wrong reading of the idea. The limit of three subscripts per array reference was not chosen to match the three physical registers. It was chosen because the number of cases the analysis had to distinguish grew exponentially in the number of subscripts. The hard limit came from the combinatorics of the reasoning, not from the hardware — which is the opposite of the usual assumption that the machine dictates the language's restrictions. A designer who takes both halves of the lesson idealizes the physical resource when it obstructs clear thinking, and separately watches for the limits imposed by their own analysis, because those are the ones that will not go away when the hardware improves.

**Source:** [The History of FORTRAN I, II, and III](../works/the-history-of-fortran-i-ii-and-iii.md) — the account of proposing an unlimited-register target once optimal register handling proved intractable, the two unanticipated stages that followed, the division of the project among autonomous groups negotiating their own interfaces, and the note that the subscript limit came from case explosion rather than the register count. Also [The FORTRAN Automatic Coding System](../works/the-fortran-automatic-coding-system.md) — the description of the stages that convert a program assuming unlimited symbolic registers into one using the machine's actual three.
