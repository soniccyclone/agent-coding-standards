---
type: lesson
title: "Carry an invariant richer than the proof strictly needs when the richer one mirrors what the machinery actually holds"
figure: edmonds
works: [maximum-matching-and-a-polyhedron-with-0-1-vertices]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Carry an invariant richer than the proof strictly needs when the richer one mirrors what the machinery actually holds

**Lesson:** There is a standard aesthetic that says an invariant should be the weakest statement sufficient to prove the result. Edmonds argues against it in a specific and interesting case. His characterization of optimality could be stated as the bare existence of a certifying vector; instead he states a much heavier condition, a whole nested sequence of derived structures each carrying its own weights, and he defends the choice on two grounds. It provides insight, and it corresponds naturally to the manipulations the method actually performs. Then he goes further and says the heavy version is part of the description of the algorithm, not merely a fact about it. The invariant and the data structure are the same object seen from two sides.

The value of that alignment is that maintaining the invariant and running the method become one activity. Each step of the search has an obvious effect on the sequence of derived structures, so verifying that a step preserves the conditions is a local check rather than a re-derivation, and the conditions themselves tell the implementer what state must be kept. A weaker invariant would have been easier to state and would have left the implementer to invent the bookkeeping unaided, with nothing to check the bookkeeping against. This is the practical argument for writing invariants at the altitude of the code's actual state: they stop being proof scaffolding and start being the specification of the representation.

The paper attaches a caveat that sharpens rather than weakens the point. Colleagues found that the heavy characterization can be bypassed, and that the method can be driven by a different parameterization; Edmonds reports this and observes that one parameterization may be arithmetically more convenient than the other while the same combinatorial manipulations appear essential either way. So the invariant that mirrors the machinery is not unique, and the numbers in it are partly bookkeeping. What is not negotiable is the combinatorial content underneath. A programmer taking this seriously separates the two layers deliberately: identify the structural facts the method genuinely depends on, then choose whichever concrete encoding of them is most convenient to compute with, and do not confuse a change of encoding with a change of algorithm.

**Source:** [Maximum Matching and a Polyhedron with 0,1-Vertices](../works/maximum-matching-and-a-polyhedron-with-0-1-vertices.md) — the passage introducing the heavier optimality characterization, defending it as insight-bearing and as part of the algorithm's description rather than merely necessary, and reporting the colleagues' alternative parameterization along with the judgement that the combinatorial manipulations are the same in either case.
