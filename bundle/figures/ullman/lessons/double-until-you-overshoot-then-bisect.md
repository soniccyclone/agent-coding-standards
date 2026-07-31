---
type: lesson
title: "Double until you overshoot, then bisect — searching for an unbounded unknown"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Double until you overshoot, then bisect — searching for an unbounded unknown

**Lesson:** Searching for a value when you have no upper bound on it looks like it needs either a guess at the range or a linear scan, and both are bad — a guessed bound is wrong eventually, and a scan costs proportionally to the answer. There is a standard two-phase construction that needs neither. Phase one probes at exponentially increasing values until the test flips, which brackets the answer within a factor of two using a number of probes logarithmic in the answer itself. Phase two bisects inside that bracket. Total cost stays logarithmic in a quantity you never had to know in advance, which is the property that makes it worth internalising as a reflex rather than rediscovering per problem.

The requirement is a monotone test: some predicate that is false below the answer and true above it, or vice versa. That requirement is the thing to check, and it is often satisfiable even when the underlying quantity is fuzzy. The predicate does not have to be a clean mathematical property — it can be "did the quality measure degrade noticeably between these two settings," evaluated by running the expensive procedure twice. The construction does not care how the test is implemented, only that its answer is consistent in direction, and noticing that a vague-sounding criterion is nonetheless monotone is usually what unlocks the technique.

What you are really buying is independence from a configuration parameter. Whenever a system has a knob whose right value depends on the data, the choice is between making someone set it, guessing a default that will be wrong, and searching for it. Searching sounds expensive and is not, once you know the cost is logarithmic — which reframes an ongoing operational burden as a one-off startup cost. That trade is favourable surprisingly often: buffer sizes, worker counts, batch sizes, retry limits, and group counts are all knobs that could be discovered by a doubling search against a monotone quality test rather than configured by whoever set them up first.

The honest caveat is that when the test is itself expensive and noisy, each probe costs real work and can lie, so the bracket you land on may be wrong by a step. That is usually tolerable, since the whole premise is that the exact answer was never sharply defined. What is not tolerable is running the exponential phase with an unbounded budget against a test that never flips — the loop needs a cap and a loud failure, because a test that never flips means the predicate was not monotone and the whole construction was inapplicable.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the section of the clustering chapter on choosing the number of clusters, which runs the procedure at exponentially growing values until the cohesion measure stops changing much, then binary-searches the resulting interval, for a total cost logarithmic in the true count.
