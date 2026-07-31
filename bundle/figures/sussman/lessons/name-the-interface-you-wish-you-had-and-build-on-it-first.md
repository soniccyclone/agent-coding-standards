---
type: lesson
title: "Name the interface you wish you had, build everything on it, and decide the representation last"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Name the interface you wish you had, build everything on it, and decide the representation last

**Lesson:** Faced with implementing arithmetic on a compound quantity, the authors do not begin with how it will be stored. They postulate a constructor and two selectors, declare that these exist, and write every operation in terms of them -- and then name what they have just done: a powerful strategy of synthesis called *wishful thinking*. The representation is chosen afterwards, once the operations built on top have shown what the interface actually needs to support.

Naming the move is what makes it teachable, because the instinct runs the other way. Representation feels like the foundation, so it feels irresponsible to build before it is settled. The inversion works because the operations are the thing that constrains the interface, and until they are written you are guessing at what the representation must serve. Writing them first turns the interface from a prediction into a derivation.

The payoff is more specific than "loose coupling," and the book demonstrates it rather than asserting it. Two genuinely different implementations -- reduce to lowest terms when constructing, or reduce when selecting -- differ in *when* work happens and therefore in which usage patterns they favour. Both satisfy the same interface, and switching between them requires changing no operation built above. The decision has been made deferrable, and it is a real decision with a real performance consequence that depends on access patterns you may not know yet.

That deferral is the thing to take. Most designs contain a handful of choices that cannot be made well early because the information arrives later. Wishful thinking is the technique that lets you keep making progress while a decision stays open, rather than either guessing and being locked in, or stalling until you know. The discipline it requires is that the postulated interface be written down concretely enough to code against -- a named constructor and named selectors, not a vague intention -- because a fictional interface you have actually programmed against is a specification, while one you have only imagined is a wish.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 sections 2.1.1 and 2.1.2, which postulate a constructor and selectors for rational numbers before saying how one is represented, name the technique wishful thinking, define all five arithmetic operations against that interface, and then show two implementations that differ in whether the common divisor is removed at construction time or at selection time -- observing that which is preferable depends on how often parts are accessed, that neither requires changing the operations above, and that data abstraction gives a way to defer the decision without losing the ability to make progress on the rest of the system.
