---
type: lesson
title: "What one level cannot define, the level above defines easily"
figure: peter
works: [uber-die-mehrfache-rekursion]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# What one level cannot define, the level above defines easily

Recursion that advances along several arguments at once is genuinely stronger
than recursion along one — that is the hard result. Péter pairs it with a much
cheaper observation that reframes the whole hierarchy: if you are allowed to
recurse over functions rather than only over numbers, the multi-argument schemes
collapse back to single-argument ones. Define a higher-order object by ordinary
one-variable recursion, then read the number-valued function off it. The extra
dimensions of the recursion do not vanish; they are absorbed into the type of
the thing being defined.

So the strength gap is not a fact about recursion, it is a fact about recursion
*at a fixed type level*. Dimension of the recursion and height of the type are
two currencies for the same purchase, and there is an exchange rate between
them. This is why Péter is careful to distinguish which comparison she is
making: the celebrated result that a certain doubly-recursive function escapes
one-variable primitive recursion is a statement about the first-order layer
only, and it says nothing about what a functional-valued definition can reach.
Confuse the two and you will believe an impossibility result that is not there.

For a programmer, the immediate use is diagnostic. When a computation resists
expression in the vocabulary at hand, there are two moves: add a construct at
the current level, or lift the whole thing one level up and let the existing
constructs do the work. The second is often smaller. Building a value that is
itself a function, an interpreter, a continuation, a staged generator — each is
a way of buying back a dimension you were missing, without adding a primitive
to the language. The cost is real and worth naming: the object you are now
recursing over is harder to hold in your head and harder to inspect, so higher
type levels trade legibility for reach. But the trade exists and is
quantifiable, and knowing it exists is what keeps "not expressible" from
hardening into "impossible."

**Source:** [Über die mehrfache Rekursion](../works/uber-die-mehrfache-rekursion.md) — the early section where multiple recursion is reduced to simple recursion once definitions of functions-of-functions are admitted, together with the framing that separates first-order strength claims from claims about higher levels.
