---
type: lesson
title: "Prove you dominate a deliberately crippled version of yourself, then study the crippled version instead"
figure: karp
works: [an-optimal-algorithm-for-on-line-bipartite-matching]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Prove you dominate a deliberately crippled version of yourself, then study the crippled version instead

**Lesson:** The policy analyzed in this paper is hard to reason about directly, because its behavior at any moment depends on the whole tangled history of what it has already committed to. The authors get around this with a move that generalizes far beyond matching. They define a whole family of degraded variants of their policy — variants permitted to decline an opportunity for any reason at all, including no reason — and prove one blanket comparison lemma: whatever any member of that family accomplishes, the real policy accomplishes at least as much. That single lemma is then spent repeatedly. It licenses simplifying the input to a canonical worst shape, because running the real policy on the simplified input is itself just a degraded run on the original. It licenses replacing the real policy with a specially handicapped variant whose behavior has a clean characterization, and any lower bound proved for the handicapped variant transfers straight up to the real one.

The structure worth extracting is the dominance argument, and it is the opposite of how engineers usually simplify. The common move is to analyze a simplified model and hope the real system resembles it, which gives you an estimate whose error has unknown sign — the real system might be better or worse and you cannot say which. The disciplined move is to first prove the direction of the inequality: establish that the simplified thing is never better than the real thing, and only then analyze the simplified thing. Now the conclusion is not an approximation but a guarantee, because the error can only run in your favor. The comparison lemma is doing the load-bearing work, not the eventual calculation, and it is stated once in a form general enough to be reused rather than re-argued at each application.

What makes the lemma provable here is a monotonicity property: the real policy never has fewer options available than a variant that has been throwing options away, and it never passes up an option the variant took. That kind of "my state always contains yours" relationship is the general shape to look for. It shows up in engineering as a strictly conservative fallback path, a pessimistic cost model, a rate limit that is provably tighter than the real capacity, a coarser lock that admits fewer interleavings than the fine-grained one it stands in for. In each case the value comes from knowing the direction of the error, not from the model's accuracy.

The habit, then, is that whenever you catch yourself analyzing, benchmarking, or testing a simplification of what you actually ship, stop and ask which way the inequality runs and whether you can prove it. If the simplification is provably no better than the real system, every bound you establish on it is a real guarantee and you may reason about it freely. If you cannot establish the direction, you have a suggestive number and should say so out loud, because a simplified model of unknown bias is routinely presented downstream as though it were a bound.

**Source:** [An Optimal Algorithm for On-line Bipartite Matching](../works/an-optimal-algorithm-for-on-line-bipartite-matching.md) — the comparison lemma about variants allowed to decline arbitrarily, and its subsequent reuse both to reduce the analysis to a canonical worst-case input shape and to substitute a handicapped variant whose success condition has a simple description.
