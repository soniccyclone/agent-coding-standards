---
type: lesson
title: "An abstraction that drops information usually only holds above a threshold"
figure: schonfinkel
works: [entscheidungsproblem-der-mathematischen-logik]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# An abstraction that drops information usually only holds above a threshold

Having shown that the components relating two distinct individuals can be struck from the formula, the authors immediately record where that erasure stops being faithful. The stripped formula and the original are equivalent with respect to validity only once the domain holds at least four things. Below that the derived conditions remain sufficient but cease to be necessary, and they exhibit formulas to prove it: one valid over a two-element domain, another over a three-element domain, neither of which satisfies the equations the general method produces. Then they say what distinguishes those escapees — in exactly those cases, the fact that the relations really take two arguments is doing essential work. The information the abstraction discarded was inert above the threshold and load-bearing below it.

Their remedy is deliberately unglamorous. For fewer than four individuals, decide by finite trial. No attempt to extend the elegant machinery downward, no reformulation to make one method cover everything; the small cases are cheap to brute-force, so brute-force them and keep the general method's statement honest by attaching its range of validity to it.

That combination is the reusable part. Any transformation that throws information away is likely to be sound only past some size, because small instances are the ones with too few elements for the discarded distinctions to be reconstructible from what remains. The pattern shows up in asymptotic reasoning that misleads at small inputs, in hash-based deduplication that behaves differently when collisions are likely rather than negligible, in statistical approximations that need a minimum sample, and in concurrency arguments that assume more participants than a two-node deployment provides. In each case the general argument is fine and its small end is a separate problem.

So an abstraction should be published with its floor, and the floor should be established by looking for counterexamples below the presumed threshold rather than by assuming continuity downward. When you find them, examine what they have in common: it will be the feature your abstraction erased, which both confirms the erasure was the cause and tells you what an extension would have to preserve. And handle the region below the floor by whatever crude method is cheapest, because the cases are small by construction — the expensive mistake is not the crude special case, it is claiming the general method covers ground it does not.

**Source:** [Zum Entscheidungsproblem der mathematischen Logik](../works/entscheidungsproblem-der-mathematischen-logik.md) — the closing part of section 4, which limits the equivalence between the original and stripped normal forms to domains of at least four individuals, gives explicit formulas valid over two- and three-element domains that fail the derived equations, attributes those exceptions to the essential two-argument character of the relations, and disposes of the small cases by finite trial.
