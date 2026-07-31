---
type: lesson
title: "Find the smallest case where the hard feature is really present"
figure: schonfinkel
works: [entscheidungsproblem-der-mathematischen-logik]
axes: [cognitive-load, verifiability]
subdomains: [foundations-of-computation, formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Find the smallest case where the hard feature is really present

The paper does not attack the decision problem in general. It states that it will settle the very simplest case not already disposed of, and then spends real effort establishing which case that is. The formulas are first put in a shape where all quantifiers stand in front, which gives a classification by the pattern of that prefix. A single leading quantifier is discarded as no new problem: with one variable available, a relation can only ever be applied with all its argument places filled by the same thing, and such an expression behaves exactly like a one-place predicate. Relations do not genuinely occur, whatever the notation suggests. Two leading quantifiers is the first place they can, so that is where the frontier is.

Then the frontier is narrowed again. Of the four possible two-quantifier prefixes, three collapse to propositional checks by direct argument, leaving a single type — existential before universal — as the only real content. So a problem that presents as a broad landscape of cases is reduced by triage to one case, with the reasons the others are cheap written down rather than assumed. The generalization to longer prefixes is stated in the same terms: every prefix in which no existential precedes a universal is trivially decided, which locates the difficulty precisely at that one adjacency rather than at length or complexity in general.

The transferable part is the test they apply, not the classification they get. An input feature counts as present only if it can actually exercise the machinery you think it exercises. A multi-argument relation supplied identical arguments everywhere is not multi-argument. A cache with one key is not a cache. A concurrency bug cannot be reproduced by a test that never interleaves. A parser stress case with no nesting does not test the recursion. Time spent on configurations where the hard feature is formally allowed but structurally inert is time spent re-solving something easier, usually while believing otherwise.

So before generalizing, do the triage. Enumerate the configurations, prove which ones degenerate into cases you have already handled, and identify the minimal configuration in which the phenomenon you care about is unavoidable. That minimal case is where the work belongs, because everything below it is a disguise and everything above it will usually be reached by the same argument once the minimal case yields. The discarded cases are not wasted either — their triviality proofs are what let you claim coverage of the whole classification, not just of the interesting corner.

**Source:** [Zum Entscheidungsproblem der mathematischen Logik](../works/entscheidungsproblem-der-mathematischen-logik.md) — the end of section 1 and section 3, where prenex normal form is used to classify formulas by quantifier prefix, a single leading quantifier is dismissed because a relation applied to one variable is indistinguishable from a predicate, and three of the four two-quantifier types are shown trivially decidable, isolating the existential-before-universal type.
