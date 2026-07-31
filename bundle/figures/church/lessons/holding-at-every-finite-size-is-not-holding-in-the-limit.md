---
type: lesson
title: "Holding at every finite size is not holding in the limit, so an exhaustive check over all bounded cases can be complete and still prove the wrong thing"
figure: church
works: [introduction-to-mathematical-logic]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Holding at every finite size is not holding in the limit, so an exhaustive check over all bounded cases can be complete and still prove the wrong thing

Most of Church's solvable special cases of the decision problem work by the same device: a syntactic restriction on the formula licenses a bound, so that if the formula holds over a domain of some computable finite size, it holds over every domain, finite or not. That is a very satisfying pattern — an unbounded semantic question collapses into a finite mechanical check — and it is easy to start believing it is how the world works. Church makes a point of listing one case where it is not. That case contains formulas which are valid in every finite domain and not valid in an infinite one, and he cites a concrete example. No amount of finite checking, however exhaustive, would ever have reached the truth about them.

The structural point is that "true for each finite n" and "true in the limit" are genuinely different statements, and neither the completeness of a finite search nor the size of the numbers involved bridges them. This is not the familiar warning that you tested too few cases. It is the harder observation that testing *all* the cases of every finite size can be a complete and correct procedure whose answer is the wrong answer to the question you asked. The gap is not statistical; it is logical. Something new can only happen at infinity, and finiteness is exactly the assumption that suppresses it.

That most cases do collapse to a finite bound is what makes the exception dangerous. When a family of results all have the same shape, the shape starts functioning as a background assumption rather than a claim, and the members that violate it get read as anomalies rather than as evidence about the shape. Church's response is to state the exception by name in the same list, so the reader cannot generalize the pattern without also meeting its counterexample.

The engineering analogue is not exotic; it is the ordinary situation. A concurrency protocol verified by exhaustive model checking up to three nodes and four messages is verified for those configurations only, and the interesting failures in real distributed systems characteristically require an unbounded number of retries, an arbitrarily delayed message, or a queue that grows without bound — cases the finite model excluded by construction, not by accident. A recursive routine that terminates for every input you can construct on a test machine may not terminate. A rate limiter, cache eviction policy, or backoff scheme that behaves at every load you can generate can still have no steady state. In each case the bounded exploration is not sloppy work; it is careful work answering a different question.

What follows practically is not despair about finite testing, which is usually the only thing available and often catches everything real. It is that a bounded check should be labeled with the bound and never quietly promoted to a universal claim, and that when a universal claim is actually needed the argument has to be of a different kind — an induction, an invariant, a monotonicity argument, a proof that some measure decreases — something that reasons about all sizes at once rather than visiting them. And it is worth asking, of any system whose correctness argument is exhaustive-over-small-cases, what the unbounded version of the input actually is, and whether anything in the design changes character when that quantity is allowed to grow.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — the closing summary of the section on the decision problem in special cases, where Church observes that most of the solvable cases can be put in the form that validity in a domain of a specified finite size implies validity outright, and singles out the remaining case as an exception because it contains formulas valid in every finite domain yet not valid in an infinite one.
