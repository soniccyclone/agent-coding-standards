---
type: lesson
title: "Replace an inner recomputation with a guess you can check, and a product of costs becomes a sum"
figure: vardi
works: [on-the-complexity-of-bounded-variable-queries]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Replace an inner recomputation with a guess you can check, and a product of costs becomes a sum

**Lesson:** Nesting is what turns an affordable loop into an unaffordable one. Each level of a nested iteration re-runs everything beneath it from scratch on every one of its own steps, so the cost is a product across levels rather than a sum, and the exponent is the nesting depth. The interesting observation is that the depth is usually not the parameter anyone is trying to bound — the individual levels are each cheap and each provably bounded — so the blow-up is an artifact of the evaluation strategy, not of the problem.

Vardi's escape is worth internalizing as a general move: find a characterization under which the answer you were about to recompute can instead be *exhibited and verified*. Once you know that membership in the answer is witnessed by any candidate satisfying a one-step local condition, an outer level no longer needs to derive the inner answer; it can accept a proposed one and check the local condition. Checking is cheap and, decisively, it does not recurse. The iteration count collapses from a product across levels to a count proportional to the number of levels, and each check is independent enough to farm out.

The price is real and should be named honestly: you have exchanged a self-contained deterministic procedure for one that only works when the right intermediate values are supplied from somewhere. That somewhere is a search, a solver, a cache, a hint file, an annotation a human writes once. It is the same trade behind loop invariants supplied instead of inferred, memoized subresults, and certificates attached to compiled artifacts — in each case the expensive derivation is moved out of the inner loop and replaced by a cheap local check. So when profiling shows the cost concentrated in re-derivation under nesting, do not try to speed up the derivation. Look for the property that makes an answer checkable, and then arrange for the answer to arrive from outside.

**Source:** [On the Complexity of Bounded-Variable Queries](../works/on-the-complexity-of-bounded-variable-queries.md) — the fixpoint-logic section, where the naive nested-loop evaluation of alternating least and greatest fixpoints costs an exponent proportional to nesting depth, and the two lemmas characterizing fixpoint membership by an under-approximating witness let the technique approximate both kinds from below, reducing the iteration count to one proportional to the alternation depth at the cost of nondeterminism.
