---
type: lesson
title: "An impossibility result indicts one of your background assumptions, not the thing you wanted"
figure: scott
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# An impossibility result indicts one of your background assumptions, not the thing you wanted

**Lesson:** Twice in the same development a natural requirement turned out to have no solution, and both times the resolution was the same shape. Recursive definitions demand that a function equal something defined in terms of itself; among total functions such an equation can be set up so that nothing satisfies it. A design in which procedures are ordinary values demands a space that contains its own space of functions; a counting argument shows no such set exists. Neither obstruction is a verdict on recursion or on first-class procedures. Each is a verdict on an unexamined background commitment — that functions are total, that "function" means arbitrary set-theoretic map — and the productive response is to find the commitment doing the damage and weaken exactly it.

What makes this more than wishful thinking is the discipline attached to the weakening. Enlarging the value space with an element for "no answer" turns partial behavior into total behavior on a bigger space; narrowing what counts as a map to those that respect approximation cuts the function space down enough that the counting argument no longer bites. Both moves change the ambient notion rather than the requirement, and both come with an obligation: show that the weakened notion still contains everything you actually needed. That check is the whole of the argument's honesty. Restricting to approximation-respecting maps would be cheating if the operations a computation performs were not of that kind — the move is legitimate precisely because computable behavior lives comfortably inside the smaller class, so nothing of interest was thrown away to buy the existence result.

The general habit: when a proof tells you that what you want cannot exist, do not read it as a boundary on ambition. Read it as an inventory request. Enumerate the assumptions the proof consumed, find the one that is convention rather than necessity, and ask what the world looks like without it — then verify that your real cases survive the change. The failure mode on the other side is just as expensive: quietly dropping the feature, or bolting on a special case that evades the argument without addressing it, leaves the wrong assumption installed and it will block the next thing too. An obstruction you have traced to a specific replaceable assumption is a design lead, not a wall.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the demonstration that the functional equation for a recursively defined command has no solution among total state transformations, the Cantor cardinality argument against a value space isomorphic to a sum including its own function space, and the resolution by admitting an undefined element and restricting function spaces to continuous maps, justified by the claim that computability theory is content with continuous functions.
