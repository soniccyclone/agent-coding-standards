---
type: lesson
title: "Weaken the problem on purpose, then prove something exact about the weakened version"
figure: karp
works: [combinatorics-complexity-and-randomness]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Weaken the problem on purpose, then prove something exact about the weakened version

**Lesson:** When the problem you were handed is out of reach, the productive move is not to keep attacking it but to choose deliberately which requirement to drop, and then prove something airtight about the weakened problem that transfers back. Two versions of this move recur throughout Karp's account and they are worth seeing as one idea. In the first, you delete constraints until what remains is something you can actually solve, and because you only removed restrictions, the answer to the easier problem is a guaranteed bound on the answer to the hard one. That bound is not a decoration; it is the mechanism that makes searching a vast space feasible, because a sound bound on everything in a region licenses you to discard the entire region without examining it. The quality of the bound, not the cleverness of the traversal, is what determines how much you get to throw away.

In the second version you keep the constraints and weaken the demand for optimality instead, accepting an answer within a provable factor of the best. A traveling salesman with a route a few percent longer than optimal is a satisfied traveling salesman. What makes this a real discipline rather than an excuse is that the achievable factor is itself a hard, provable property of the problem, not a function of how hard you try. Some problems admit any accuracy you care to name; some can be brought to a certain error and stubbornly no further; some resist bounded error entirely; and for some, a bounded-error method would collapse the central open question of the field. Karp's account of the packing results, where a simple largest-first rule was proved never to waste more than roughly a fifth extra capacity, shows what this looks like when it goes well: a plain, cheap procedure carrying a real guarantee.

The habit is to treat the specification as one of your variables. Confronted with something intractable, ask which of exactness, generality, and completeness you actually need, drop the one you need least, and insist on a proof about whatever remains. This is what separates principled approximation from resignation. A heuristic with no bound tells you nothing about any particular run; a relaxation with a proven bound, or an approximation with a proven ratio, gives you a claim you can put in a contract. The version of this reasoning to distrust is dropping a requirement quietly and hoping, because then you have weakened the problem and gained nothing provable in exchange.

**Source:** [Combinatorics, Complexity, and Randomness](../works/combinatorics-complexity-and-randomness.md) — the account of finding lower bounds that made pruned enumeration effective on tour problems, later recognized as a known relaxation technique, together with the section on approximation algorithms with performance guarantees and the distinctions it draws among problems by how well they can be approximated.
