---
type: lesson
title: "Earn the right to infinite objects by building them as limits of finite ones"
figure: scott
works: [logic-and-programming-languages]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Earn the right to infinite objects by building them as limits of finite ones

**Lesson:** Higher-level program features drag in genuinely infinite objects — unbounded streams, recursive definitions, procedures that take procedures — and a theory that refuses them is a theory of toy languages. But an infinite object is only usable if you can say how a finite machine gets a grip on it. The discipline that makes this work: define what it means for one element to be a finite approximation of another, show that any element is the least upper bound of its finite approximations, and then insist that every operation you admit be determined by its behavior on those approximations. The infinite object is legitimate because it is nothing more than the limit of a chain of finite ones, and manipulating it reduces to manipulating the chain.

The load-bearing condition is continuity, and it is worth seeing what it actually buys rather than treating it as a technical hypothesis. A continuous operation cannot detect the difference between an object and its own approximating chain: apply it to the limit and you get the limit of applying it to the stages. That is precisely the property a mechanically realizable operation has, since a machine only ever inspects finitely much of its input before producing any finite part of its output. So continuity is not a restriction imposed to make proofs go through; it is the mathematical name for implementability, and a construction that violates it is telling you it has no computational reading. Restricting attention to continuous functions is what keeps a wildly infinitary construction constructive.

The transferable habit is to make finiteness a derived notion instead of a structural one. Do not build your model out of finite things and then panic when the problem needs unbounded ones; build the unbounded thing and equip it with a notion of finite part, so that finite computation is recovered as the way you interact with it rather than as a limit on what can exist. This is why the approach scales to function spaces and towers of function spaces: at every level the same approximation story is available, so an object of infinite type is still something a finite process can converge on. Whenever a design forces a hard cap because the general case seemed unmanageable, ask instead what the finite approximations to the general case are, and whether every operation you need is continuous in them.

**Source:** [Logic and Programming Languages](../works/logic-and-programming-languages.md) — the truncation of an infinite Boolean sequence to its finite prefixes, the identification of the original sequence as the least upper bound of those truncations, and the argument that the construction stays constructive precisely because only continuous functions are admitted.
