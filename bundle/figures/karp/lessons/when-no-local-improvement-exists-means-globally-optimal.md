---
type: lesson
title: "Know whether your local check certifies a global property, because that decides if hill climbing is a proof or a guess"
figure: karp
works: [an-n-5-2-algorithm-for-maximum-matchings-in-bipartite-graphs, combinatorics-complexity-and-randomness]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Know whether your local check certifies a global property, because that decides if hill climbing is a proof or a guess

**Lesson:** Two procedures can look identical from the outside. Both start with a candidate answer, both repeatedly look for a small modification that improves it, both stop when no such modification can be found. The difference is whether stopping means anything. For matchings there is a theorem that no improving modification of the specific admissible kind exists exactly when the answer is already the best possible, so the loop's stopping condition is a certificate of global optimality, checkable locally. For the traveling salesman, the same shape of loop stops at something that merely cannot be improved by the moves you happened to allow, which tells you nothing about the true best answer. Karp lived on both sides of this line and described both: the local improvement heuristics he and others used for tours worked well in practice while offering no guarantee whatsoever about how good the result was.

What earns the strong version is the richness of the allowed modifications, and the way you establish it is a technique worth learning on its own. Compare your current answer against an arbitrary hypothetical better one and reason about their structural difference. If that difference must always decompose into pieces, each of which is an admissible improving modification to your current answer, then a better answer existing implies an improving move existing, so no improving move implies no better answer. The argument never needs to know what the optimum is. It also yields a bonus that the phase structure of the algorithm depends on: it bounds how short the shortest available improvement must be, given how far you currently are from the best.

The habit is to demand of every iterative refinement in your systems an explicit answer to the question of what the termination condition proves. If it proves optimality, say so and say why, because then you have a cheap runtime check for a global property and you can safely stop when it fires. If it does not, then treat the result as a candidate rather than an answer, and expect to be shipping quality that varies with the starting point and the move set. The corrosive case is the middle one, where a loop's stopping condition is quietly assumed to mean optimal because it usually produces something good, since that assumption gets built into callers downstream that never had a reason to doubt it.

**Source:** [An n^5/2 Algorithm for Maximum Matchings in Bipartite Graphs](../works/an-n-5-2-algorithm-for-maximum-matchings-in-bipartite-graphs.md) — the section deriving, from the structure of the symmetric difference between any two matchings, both the characterization of maximality by absence of an improving path and a bound on that path's length. The contrasting case, where local improvement carries no guarantee, is discussed in [Combinatorics, Complexity, and Randomness](../works/combinatorics-complexity-and-randomness.md).
