---
type: lesson
title: "To prove something impossible, enlarge it until the impossibility is easy, then inherit the result"
figure: vardi
works: [on-the-expressive-power-of-datalog]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# To prove something impossible, enlarge it until the impossibility is easy, then inherit the result

**Lesson:** Negative results and positive results want opposite moves. To show a thing is possible you must work in the actual system, with all its awkwardness, because a program in an idealized system is not a program. To show a thing is impossible you are free to work in any system that contains yours: prove nothing in the larger system can do it, and nothing in the smaller system can either. Kolaitis and Vardi build their whole method on this. Reasoning directly about a rule-based query language is unpleasant, so they locate it inside a much larger logic — one that allows infinite conjunctions and disjunctions and is genuinely more powerful — and prove the inexpressibility results there. The awkward features of the real language stop mattering, because they are subsumed.

What makes this more than a convenience is the choice of enlargement. The bigger system is not merely bigger; it is bigger in the directions that were hard to reason about and unchanged in the direction that carries the argument. The bounded supply of names survives, and that bound is what the eventual proof technique grips. An enlargement that also relaxed the name bound would have been useless — the result would be true but vacuous, since the enlarged system could then do the thing. So the craft is to over-approximate along the axes irrelevant to your argument while holding fixed the axis your argument depends on.

This is the same shape as every sound static analysis, every conservative type system, and every abstract interpretation: reason about a superset of what can happen, and any impossibility you establish transfers down. Two disciplines make it honest. Confirm the enlargement is a genuine superset — Kolaitis and Vardi prove the containment rather than assuming it, and note it is strict. And confirm the enlargement has not become so generous that your target is now possible in it, since a negative result about an over-generous abstraction says nothing about the system you care about.

**Source:** [On the Expressive Power of Datalog: Tools and a Case Study](../works/on-the-expressive-power-of-datalog.md) — the introduction's statement of the approach, viewing Datalog variants as fragments of an infinitary logic and proving negative results in that larger setting; the theorem establishing the containment by induction on the stages of the rule operator, showing each stage is definable with a fixed number of variables; and the explicit note that the containment is strict, since the larger logic can express non-recursive queries while the rule language cannot.
