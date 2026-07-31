---
type: lesson
title: "An iteration costs what changes, not what it contains"
figure: mcmillan
works: [symbolic-model-checking-10-20-states-and-beyond]
axes: [expressiveness, hardware-affinity]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# An iteration costs what changes, not what it contains

The fixed-point loop at the heart of this method is about as plain as a loop gets: start from the empty approximation, apply the body, compare with the previous round, stop when nothing moved. The naive way to price it is iterations times the cost of the body. The paper quietly rejects both factors, and the way it does so is worth stealing.

The first correction is ordinary and everyone half-knows it. The body splits into the part that mentions the quantity being iterated and the part that does not, and the second part evaluates identically every round, so it should be evaluated once. That is loop-invariant hoisting wearing different clothes. The second correction is the one people miss: having noticed that the per-round cost is set by how much of the body depends on the iterated quantity, the authors say plainly that it is therefore worth *rewriting the specification* so that less sits inside the recursion. The dependency surface is not a property of the problem handed to you. It is a property of how you wrote the problem down, and it can be moved. Caching what happens to be invariant is a mechanical optimisation; restructuring so that more of the work becomes invariant is a design act, and it is available long before you reach for a cache.

The third correction is about the loop's control rather than its data, and it is the easiest to overlook entirely. An iterate-until-stable strategy has to ask, every single round, whether anything changed. If that comparison is expensive — a structural walk, a deep equality, a re-derivation — then a loop that converges in a few dozen rounds can spend most of its life deciding whether to keep going. The reason this method can afford the simplest possible convergence rule is that its representation is canonical, so two equal things are literally the same object and the test costs nothing. Choosing a representation with an eye on the cost of the *stopping condition*, not just the cost of the values, is what makes the naive strategy viable rather than embarrassing.

Put together, these give a three-part cost model for any iterative computation that is far more useful than a stopwatch: how many rounds, how much of each round actually varies, and how expensive it is to detect that you are done. Each is attackable separately and by different means — the first by an algebraic reformulation of the recurrence, the second by moving work out of the recursive scope, the third by a representation choice. A programmer who carries this asks which of the three a slow loop is losing to before touching any of them, because the fixes do not substitute for each other.

**Source:** [Symbolic Model Checking: 10^20 States and Beyond](../works/symbolic-model-checking-10-20-states-and-beyond.md) — the discussion immediately following the fixed-point procedure: the observation that subterms not mentioning the iterated relational variable need not be recomputed, the resulting recommendation to rewrite formulas so fixed-point subterms carry fewer free relational variables, and the remark that convergence detection is cheap because equality of the canonical representation is a constant-time test.
