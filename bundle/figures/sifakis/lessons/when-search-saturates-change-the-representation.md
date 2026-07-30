---
type: lesson
title: "When an exhaustive method stalls, attack the representation before the algorithm"
figure: sifakis
works: [turing-lecture-2009]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# When an exhaustive method stalls, attack the representation before the algorithm

**Lesson:** The single largest jump in the reach of automatic verification came from leaving the search procedure essentially intact and changing how the set of states and the transition relation were written down. Explicit adjacency structures store one entry per element and therefore cost what the state space costs; a canonical compressed form for boolean functions stores the regularity instead, and the systems people actually build are extremely regular. Same fixpoint computation, many orders of magnitude more system. Before rewriting a search, ask what its data structure is forced to spend memory on that the problem does not actually vary.

Every such representation is a wager on one specific kind of structure, which means each has a hard ceiling somewhere else. The compressed boolean form depends on a variable ordering shared along all paths; finding a good one is difficult, and for some functions — the classic case being a middle output bit of a multiplier — no ordering is compact at all. That is not a bug to be engineered away but a proof that the wager loses on that class. The next advance therefore came from a different encoding entirely, unrolling behavior to a bounded depth and handing the result to a solver whose strengths lie elsewhere. Progress here looks less like refining one representation and more like accumulating a stable of them with known failure modes.

Two representations can also refuse to compose. Exploiting replicated structure and exploiting boolean regularity were shown to resist naive combination, and the way through was not to force them together but to let one reorganize dynamically in response to the other. When two optimizations fight, that is information about the shape of the problem, and the resolution is usually a new interface between them rather than a merge.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Clarke's section on major breakthroughs: symbolic model checking with decision diagrams, the ordering limitation and the multiplier counterexample, the shift to satisfiability-based bounded checking, and Emerson's note on combining symmetry with symbolic representation.
