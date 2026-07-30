---
type: lesson
title: "Push the caller's actual question into the computation, because a comparison is cheaper than a value"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Push the caller's actual question into the computation, because a comparison is cheaper than a value

**Lesson:** A component that computes an aggregate and a caller that only compares that aggregate against a threshold are together doing more work than the problem requires. Computing the largest value in a collection demands looking at everything, since any unexamined item could be larger. Deciding whether the largest value is at least some bound demands only finding one item that meets the bound — after which the rest of the collection is irrelevant and the scan can stop. The two tasks look almost identical from outside, and the second is often dramatically cheaper, so the productive question when something is slow is not how to speed the computation up but whether the caller ever needed the value at all.

The move is to relocate the caller's test into the computation, which changes the callee's contract from producing a value to answering a disjunction: either it reports the aggregate along with a proof that the aggregate is below the bound, or it reports that some witness at or above the bound exists, without saying which aggregate it belonged to. That second alternative is deliberately weaker, and its weakness is where the savings live. Writing such a contract takes more care than "returns the maximum", because the two branches assert different things and the argument has to work in both, but the resulting component is strictly more useful: the caller who wanted only the comparison gets it cheaply, and the caller who genuinely wanted the value can supply a bound nothing can meet.

The general habit is to look for places where a general-purpose result is being computed and then immediately narrowed. Sorting when only the top few matter; counting when only "any" or "more than n" matters; fetching a whole record when only one field is read; computing an exact distance when only a comparison against a radius is needed. In each case the narrowing predicate, moved inward, licenses an early exit or a cheaper representation that was unavailable while the interface insisted on the full answer. This is not premature optimization: it is noticing that the interface asks for more than anyone consumes, which is a specification defect that happens to also cost time.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 2.4.3's minimax program, where the straightforward approach finds each row's maximum and compares it with the incumbent, and the improvement compares each element against the incumbent during the scan so that a single element meeting the bound lets the scan be abandoned without determining the row maximum at all; the section notes that this abort is a special case of the alpha-beta heuristic for minimax over trees.
