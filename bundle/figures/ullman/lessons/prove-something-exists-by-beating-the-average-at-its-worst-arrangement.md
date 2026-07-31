---
type: lesson
title: "Prove something exists by beating the average, evaluated at its worst arrangement"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Prove something exists by beating the average, evaluated at its worst arrangement

**Lesson:** To establish that some structure must be present in your data, you can often skip constructing it. Count the total amount of the relevant quantity, divide by the number of slots it could be distributed among, and observe that at least one slot must hold at least the average. If that average already clears the threshold you care about, the structure exists — you have proved it without knowing where it is or how to find it. This turns an existence question into an arithmetic question over quantities you can measure in aggregate, and it works even when the search itself is expensive, because the proof and the search are now independent.

The argument only holds if you evaluate the average under the arrangement least favourable to you. Totals fix the sum of the individual contributions but not their spread, and the derived average is usually sensitive to that spread. When contributions grow superlinearly in the per-item quantity — as they do whenever you are counting subsets — concentration helps you: piling activity onto a few items inflates the total, so the total is *minimized* when everything is spread perfectly evenly. Assuming uniformity is therefore not a simplifying convenience there; it is the pessimistic case, and computing under it is what makes the conclusion a guarantee rather than a typical-case estimate. Get the direction of that convexity wrong and you have written down a heuristic while believing you have a theorem.

Two further disciplines keep the result honest. First, the approximations you make to get a closed form have a direction too. Dropping lower-order terms to turn a ratio of falling factorials into a ratio of powers is fine for intuition and can push the derived bound to the optimistic side; when the answer matters, re-check the borderline cases against the unapproximated expression, because a bound that was rounded the wrong way is a bound that does not hold. Second, the conclusion is one-sided by construction: it says at least one instance exists, nothing about how many, and nothing about where. Treat it as a licence to run a search, not as a substitute for one.

What makes this way of thinking valuable beyond the specific counting trick is that it separates *whether to look* from *how to look*. Cheap aggregate statistics you already have — average connectivity, total volume, mean fan-out — can settle in advance whether an expensive search has a guaranteed answer. Doing that arithmetic first tells you whether a null result would mean "absent from this data" or "my search was not good enough," and those are the two interpretations that a bare empty result cannot distinguish between.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the argument in the social-network chapter for why a sufficiently dense bipartite graph must contain a complete bipartite subgraph: summing each right-side node's contribution to subsets of the left side, dividing by the number of such subsets to get an average, arguing that the sum is minimized when all degrees are equal so uniform degree is the safe assumption, and the closing note that the simplified formula overstates the achievable threshold so the exact binomial expression must be checked.
