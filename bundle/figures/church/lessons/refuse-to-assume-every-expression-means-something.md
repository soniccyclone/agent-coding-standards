---
type: lesson
title: "You can dissolve a bad case by declining to assume it means anything, instead of forbidding anyone to write it"
figure: church
works: [a-set-of-postulates-for-the-foundation-of-logic]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# You can dissolve a bad case by declining to assume it means anything, instead of forbidding anyone to write it

Confronted with the self-application that generates the Russell paradox, Church takes a route most treatments do not. He grants that the offending expression can be built in his system, works out that its truth would follow from its falsehood and vice versa, and then declines to draw a contradiction from that. His reason is that nothing in his assumptions says the predicate in question has a truth value at every argument; the troublesome expression may simply be a meaningless arrangement of symbols. The paradox needs one more ingredient than the construction — it needs the premise that the construction denotes something — and he refuses to supply it.

This turns partiality into a first-class object rather than an embarrassment. Earlier in the paper he defines what it is for a predicate to be significant at an argument, builds a canonical operation that extends a predicate's region of significance as far as it can go while preserving what it says where it was already true, and proves that for some predicates this extension genuinely covers more arguments than the original did. Definedness becomes a property with structure, something to measure and maximize, instead of a precondition assumed everywhere and quietly violated at the edges.

Then he closes the loop, and this is the sharpest observation in the paper: the classical principle that a contradiction refutes its hypothesis, and the assumption that every predicate has a totally-defined equivalent, are from a certain angle the same commitment. Two things that look unrelated — a rule of inference and an assumption about domains of definition — turn out to be one purchase. That means you cannot keep the convenient reasoning principle while allowing genuinely partial predicates; the choice is single. Finding such hidden identities between assumptions is what tells you which design choices are actually available and which are the same choice wearing two names.

Setting this against Church's later work makes the trade visible from both sides. The type-theoretic route makes the bad expression unconstructible and keeps ordinary classical reasoning; this route keeps the expression constructible and pays by weakening the logic. A programmer who has both routes in hand asks which cost the situation can bear: forbid the state and accept the encoding contortions, or admit that some expressions have no value and give up the reasoning that assumed they all did. The failure is choosing neither — permitting the construction while continuing to reason as though everything is total, which is where the contradiction actually comes from.

**Source:** [A Set of Postulates for the Foundation of Logic](../works/a-set-of-postulates-for-the-foundation-of-logic.md) — the section on completion of a propositional function, which develops significance and its maximal extension, and the section on the Russell paradox, which declines to infer a contradiction and identifies reductio ad absurdum with the assumption of total significance.
