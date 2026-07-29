---
type: lesson
title: "A predicate that flips when the system grows cannot be a primitive"
figure: curry
works: [a-theory-of-formal-deducibility]
axes: [expressiveness, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# A predicate that flips when the system grows cannot be a primitive

The most obvious way to say a thing is false is to say no proof of it exists.
Curry considers exactly that reading, names it, and then rules it out — not
because it is unclear, and not because it is hard to establish, but because it
is not stable under growth. Add facts to the system and something that had no
proof may acquire one. Every other operator he has built survives extension
untouched: what was derivable stays derivable when you add axioms. This one
does not, and that single defect disqualifies it from standing alongside the
others as a construct you can nest inside larger expressions. He is forced to
go looking for other negative notions that *are* stable, and finds several —
implying everything, or reducing to a member of a declared bad set — each of
which survives extension because each is a positive claim about what can be
derived rather than a claim about what cannot.

The test generalizes far beyond negation, and Curry applies it again where you
would not expect it. When he defines universal quantification, he is careful to
say the body must hold for an *indeterminate*, not that it holds for every term
you can currently name. Those two readings agree today and diverge tomorrow:
the second is a statement about the present inventory of terms and quietly
becomes false the moment you introduce a new one. Same shape of error, different
operator. In both cases the fault is that the predicate ranges over the absence
or the exhaustion of something, and absence is not a property of the object —
it is a property of the world at a moment.

This is the deep reason logic programming had to invent negation-as-failure as a
separate, second-class thing rather than getting real negation for free, and the
reason a closed-world query answer cannot be cached across a schema change. It
is also why a nullability check, a "no permissions match" verdict, or a "no
subscribers registered" branch behaves so badly under composition: none of them
is a fact about the value in hand, all of them are facts about a snapshot of
the environment, and every one of them can invert while nothing about the value
changed. Nest such a check inside a larger expression and the expression
inherits the instability.

A programmer who believes this runs a monotonicity check before promoting
anything to a primitive: if the system acquires more facts, more rules, more
registered plugins, more rows, can this predicate go from true to false? If yes,
it is a query, and it belongs at the edge with an explicit as-of scope — never
in the core vocabulary that other constructs compose out of. And when the useful
thing really is an absence, the fix Curry models is to replace it with the
strongest positive statement that implies it: declare the bad outcomes
explicitly and derive falsity as "leads to one of these," so that the judgment
is carried by a derivation you can exhibit and that survives every later
extension. He even keeps the unstable notion around — as a *sufficient
condition* feeding the stable one, never as the definition. That is the right
place for a closed-world observation: an input to a monotone judgment, not the
judgment itself.

**Source:** [A Theory of Formal Deducibility](../works/a-theory-of-formal-deducibility.md) — the preliminary analysis of the negation chapter, where non-extensibility is given as the fatal objection to defining falsity as absence of proof, together with the footnote in the quantifier chapter distinguishing satisfaction by an indeterminate from satisfaction by every currently available term.
