---
type: lesson
title: "Drive a complicated process from a simple shadow of it, and keep the correspondence as the invariant"
figure: vardi
works: [on-the-expressive-power-of-datalog]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Drive a complicated process from a simple shadow of it, and keep the correspondence as the invariant

**Lesson:** When a strategy over a complicated object gets too intricate to describe, do not describe it. Build a much simpler object whose decisions can be described easily, run it alongside the real one, translate each incoming event into an event for the simple object, let the simple object decide, and translate the decision back. Kolaitis and Vardi need a survival strategy on an enormous graph full of interlocking gadgets, and rather than reasoning about the graph they run a small bookkeeping game over the truth values of a Boolean formula. Every probe of the graph is read as a demand to commit to a truth value; the formula-level strategy answers it; the answer determines the graph-level move. The graph strategy is never described directly at all.

The mechanism that makes this sound is a stated correspondence, maintained at all times, between positions in the simple model and positions in the real one. The whole correctness argument reduces to two claims: the simple model never contradicts itself, and consistency in the simple model implies the property you need in the real one. Both are checkable, and neither requires holding the real object's complexity in your head. This is precisely the discipline behind writing a concrete implementation against an abstract state machine, and behind refinement proofs generally: the abstract state is the thing you reason about, the concrete moves are derived, and the mapping between them is the invariant you protect.

Two practical notes. The shadow must be small enough to reason about exhaustively — the value of this technique is entirely in the gap between the two levels, so a shadow that is merely a lightly simplified copy buys nothing. And the shadow's resource budget must be tied to the real problem's budget; here the number of probes available in the real game is exactly the number available in the bookkeeping game, which is why a strategy at one level transfers to the other. That the same paper applies the trick twice, in two unrelated arguments, with one game piloting another of a different size, is the evidence that this is a reusable structure rather than a one-off construction.

**Source:** [On the Expressive Power of Datalog: Tools and a Case Study](../works/on-the-expressive-power-of-datalog.md) — section six's proof for the two-disjoint-edges pattern, which introduces an auxiliary pebble game on Boolean formulas purely as a device for describing the survivor's moves in the graph game, sets out the four cases translating graph probes into truth-value or clause challenges, and reduces correctness to the fact that no literal ever receives both values; and the closing corollary, where a k-probe game on a transformed graph is driven by a simultaneously played 2k-probe game on the original.
