---
type: lesson
title: "A whole execution can be reified as one static constraint object, and then attacked with tools that cannot touch running programs"
figure: cook
works: [the-complexity-of-theorem-proving-procedures, the-p-versus-np-problem]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# A whole execution can be reified as one static constraint object, and then attacked with tools that cannot touch running programs

**Lesson:** Behavior over time resists analysis because time is a dimension you have to traverse. The trick that dissolves this is to index by time instead of stepping through it: introduce one unknown per observable fact per instant — what this cell holds at that moment, which state the control is in, where attention is focused — and then write down the conditions that make an assignment to all those unknowns describe a genuine run. Uniqueness conditions say the machine is in exactly one state and each location holds exactly one value; the transition rule becomes a family of local constraints tying consecutive instants; the starting configuration and the desired outcome become boundary conditions. Executing the program is now the same thing as finding a consistent assignment. Nothing dynamic remains.

Two properties make the encoding worth something rather than merely clever. It is faithful in both directions, so a solution to the constraint object is a run and a run is a solution, which means the translation loses no information and can be used as an equivalence rather than an approximation. And it is cheap: the number of unknowns grows with the product of the space and time budgets, so as long as those budgets are modest the encoding is modest, and the whole reduction stays within the resource class you are reasoning about. Faithfulness without cheapness is a curiosity; cheapness without faithfulness is a bug generator. Both together turn a question about machines into a question about formulas, where an entirely different body of technique applies.

The generalization is what matters for practice. Any time a property is stated over the history of a system, look for a static object whose consistency is exactly that property, and then bring a solver to it. This is the ancestral form of bounded model checking, symbolic test generation, constraint-based scheduling, and type inference by constraint accumulation. The cost you accept is that the static object's size scales with the horizon you unroll, which is why the technique is powerful for bounded questions and useless for unbounded ones. Knowing that boundary is part of knowing the technique.

A programmer who has absorbed this stops treating "simulate it and watch" as the only way to learn what a system does. The alternative reflex is to ask what the invariants of an arbitrary run look like written down all at once, because a system whose runs you can characterize declaratively is a system you can ask questions of, rather than merely observe.

**Source:** [The Complexity of Theorem Proving Procedures](../works/the-complexity-of-theorem-proving-procedures.md) — the proof of the first theorem, which builds from an input a formula whose propositional letters denote tape contents, control state, and head position at each step, and whose conjuncts enforce uniqueness, initialization, correct stepping, and acceptance. Also [The P versus NP Problem](../works/the-p-versus-np-problem.md) — the section recapitulating that construction in modern terms, where the unknowns stand for the missing certificate and satisfiability of the produced formula coincides with acceptance.
