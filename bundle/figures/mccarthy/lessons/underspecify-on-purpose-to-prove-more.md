---
type: lesson
title: "Specify less than you know on purpose: prove the property for the loosest thing, and every refinement inherits it"
figure: mccarthy
works: [a-basis-for-a-mathematical-theory-of-computation]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# Specify less than you know on purpose: prove the property for the loosest thing, and every refinement inherits it

**Lesson:** There is a move in reasoning about programs that looks like giving up information and is actually a way of buying reach. Instead of a function that returns one value, admit an object that returns *some* value from a permitted set — a specification so loose it is not a function at all. Then define a refinement relation: one such object refines another when every value it may return was already permitted by the other. Then notice that some properties are stable under refinement: if the loose object has the property, so does everything below it. Prove the property once, at the top, and you have proved it for every concrete implementation that stays inside the permitted set — including ones nobody has written yet.

The worked instance in the paper is small and general at the same time. Take the loosest thing that always makes a positive number smaller: it may return any smaller value at all. Show that repeatedly applying it eventually lands on zero. Observe that this eventually-terminates property survives refinement. Now *any* concrete function, however intricate, that fixes zero and strictly decreases every positive input inherits termination under iteration for free — you never have to look at how it computes, only that it stays inside the envelope. That is the entire content of a termination argument, obtained by refusing to specify the thing whose details were irrelevant.

Why this holds is the point worth carrying away: the details you suppress are exactly the ones a proof would otherwise have to carry along, and irrelevant detail in a proof is not neutral, it is cost. A specification that says more than the property needs forces every reader and every reuse to re-establish the connection between the extra commitments and the conclusion. Deliberate underspecification quarantines the conclusion from the implementation, and the refinement relation is what makes the quarantine sound rather than sloppy — it is a precise account of which implementations the proof still covers. The related notion of ambiguity as an operator, whose values are all the things satisfying a predicate, generalizes the same idea into a way of naming things by their constraints rather than their construction.

The habit this produces is a reflex to ask, of any theorem you are about to prove about a specific piece of code, how much of that code the proof actually touches — and then to restate the theorem about the weakest object the proof still applies to. It rewrites contracts in terms of what callers are permitted to rely on rather than what the current implementation happens to do, which is the same discipline that keeps a proof (and an API) alive across rewrites. It also reframes nondeterminism: an underspecified result is not a defect to be pinned down but a design choice that preserves freedom for implementers while keeping the guarantees provable.

**Source:** [A Basis for a Mathematical Theory of Computation](../works/a-basis-for-a-mathematical-theory-of-computation.md) — the section on ambiguous functions, which introduces the basic choice operator, the descendant (refinement) relation, the notion of a property being hereditary under that relation, and the termination argument derived from applying all three to the loosest decreasing function.
