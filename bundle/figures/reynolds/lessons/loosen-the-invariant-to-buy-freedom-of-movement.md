---
type: lesson
title: "To make a loop faster, loosen the relation it preserves so more of the state is free to move"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# To make a loop faster, loosen the relation it preserves so more of the state is free to move

**Lesson:** An invariant is not only an obligation, it is a budget. Every quantity it mentions as fixed is a quantity the loop body may not touch, and every quantity it mentions only through a variable is a quantity the body is free to change however it likes, provided the relation still holds. So when a loop is too slow, the productive question is not what cleverer instructions to write inside the body — the body's options are already pinned by what the invariant froze. The question is which frozen thing to unfreeze. Replace a constant appearing in the relation by a fresh variable, keep the relation otherwise identical, and check that it still implies the goal at exit. You have not changed the specification and you have not changed the loop's shape; you have widened the space of legal bodies, and the faster body now lives inside it.

The naive exponentiation loop shows the mechanism at its smallest. Its relation ties the accumulated result to a fixed base raised to a remaining count, which leaves the body exactly one legal move: decrease the count by one, multiply once. Introduce a variable for the base — the relation now says the accumulator times *some current* base to the remaining power equals the target — and the body may either consume the count one step at a time as before, or halve the count and square the base. The second option was not a trick discovered by staring at the code; it became sayable the moment the base stopped being a constant, and the linear algorithm became a logarithmic one for the price of one extra variable. Weakening the invariant to a strictly more general form neither weakened the result nor complicated the proof: the exit condition still forces the answer.

Read backwards, this gives a diagnostic. If a loop, a state machine, or a protocol admits only one implementation and that implementation is inefficient, the cause is usually over-specification upstream — the contract has nailed down something it never needed to nail down, and the resulting rigidity is being misread as an inherent cost of the problem. Look for the incidental constant in the invariant, the field pinned to one value in the interface, the ordering guaranteed by accident. Generalizing the contract is what creates the room for a better algorithm; the algorithm itself often follows immediately, and sometimes there is more than one candidate, in which case the choice between them turns on secondary costs rather than on order of magnitude.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the fast-exponentiation development, where generalizing the loop invariant by introducing a variable in place of the fixed base creates the freedom to halve the exponent and square, and the ensuing order-of-magnitude comparison of the resulting variants.
