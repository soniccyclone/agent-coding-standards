---
type: lesson
title: "A restriction you can evade by restating the problem in the permitted form is not a restriction at all"
figure: church
works: [a-set-of-postulates-for-the-foundation-of-logic]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [foundations-of-computation, formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# A restriction you can evade by restating the problem in the permitted form is not a restriction at all

Church's earlier system was built on a deliberate weakening: rather than stratifying expressions the way Russell did, he would keep the language free and instead deny himself the unrestricted principle that a hypothesis leading to contradiction may be declared false. The paradoxes were supposed to die for want of that principle. This paper opens by reporting that they did not, and the reason is the interesting part. One of his postulates granted the principle back for statements of one particular syntactic shape — and, as he observes, a statement not of that shape can usually be rewritten as one of much the same force that is. The permitted shape was reachable from anywhere, so the postulate handed back nearly the full strength of the principle it was supposed to ration, and a variant of the Russell paradox came through the gap. He then derives that paradox himself, in detail, against his own published system.

The repair is instructive as engineering. He does not attempt to narrow the leaky postulate; he deletes it, and then deletes three more postulates on the grounds that they only had a point while the leaky one stood. Something else that had been carried as an assumption turns out to be derivable from the rest and goes too. What remains is smaller and he states honestly what capability was lost, along with the substitute formula that can be proved and used in most of the places the lost one was wanted. Repair by removal, followed by pruning everything whose only purpose was to serve the removed thing, followed by an explicit accounting of the resulting weakness.

The general principle is that a safety property has to be stated over the meanings a system can express, not over the forms in which it expresses them, because form is cheap to change and meaning is not. Any guard whose scope is a syntactic pattern will hold exactly until someone — with no ill intent, just looking for the natural way to say what they meant — writes the equivalent thing in a shape the guard does not cover. And the cost of the leak is not proportional to how narrow the exception looked. Church's exception was narrow and specific, and it was enough to reintroduce a contradiction into the entire system.

A programmer who has internalized this evaluates a proposed constraint by trying to route around it before adopting it: if the forbidden effect can be achieved through a permitted path, the constraint buys nothing but false confidence and the friction of complying with it. It applies directly to validation that filters known-bad forms rather than establishing the property wanted, to permission checks placed on one entry point among several, and to invariants enforced at a layer callers can bypass. It also licenses a repair style people resist: when something is unsound, deleting the offending assumption and everything that existed to serve it is usually better than adding a condition that narrows it.

**Source:** [A Set of Postulates for the Foundation of Logic](../works/a-set-of-postulates-for-the-foundation-of-logic.md) — the opening section, which derives a Russell-style contradiction from the earlier postulate list by exploiting the rewritability of statements into the shape one postulate privileged, then removes that postulate together with the ones that depended on it.
