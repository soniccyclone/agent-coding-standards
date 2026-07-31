---
type: lesson
title: "Narrowing a choice you deliberately left open inherits the whole proof for free"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Narrowing a choice you deliberately left open inherits the whole proof for free

**Lesson:** A program that permits several behaviours has been proved correct for all of them. So if you later restrict which of those behaviours may occur, every property you established still holds — you removed possibilities from a set all of whose members were acceptable, and nothing you proved could have depended on the ones you removed. This sounds like a technicality and is actually a construction technique. It means a family of algorithms can be organized as one skeleton with an unmade decision in it, plus a series of increasingly opinionated ways of making that decision, and each member of the family inherits the skeleton's entire correctness argument without a line of it being rechecked.

The concrete form is striking. Take a plain search that picks any pending item, and constrain it to pick the pending item with the smallest accumulated cost. What you now have is a different and considerably cleverer algorithm — it computes shortest distances rather than mere reachability — but everything the plain search guaranteed still holds unaltered. The only new proof obligation is about the new state you introduced to express the constraint: the numbers you are comparing, what they mean while an item is still pending, why the smallest of them is safe to finalize. All the structural reasoning — that the loop terminates, that every reachable item is eventually handled, that no item is processed twice — comes across untouched.

The practical instruction is to notice which of your design decisions are constraints rather than changes. Adding a priority order, adding a tie-break, choosing a specific traversal, pinning down an evaluation order: these narrow an existing space of permitted behaviours and cost you nothing in re-verification. Rewriting the loop, adding a case, changing what gets recorded: these move outside the space and cost you everything. Teams routinely conflate the two and re-audit the whole thing either way, or worse, audit neither. The distinction is checkable — did the new version's set of possible executions shrink, or did it acquire executions the old one did not have? — and it tells you exactly how much of your existing argument you get to keep.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.2.2, which observes that the minimum-distance program differs from the earlier reachability program only in maintaining a distance array and using it to constrain the indeterminate choice of a pending node, that constraining an indeterminacy cannot destroy the validity of assertions, and therefore that all the reachability program's assertions remain valid and only the new properties of the distance array need to be established and numbered.
