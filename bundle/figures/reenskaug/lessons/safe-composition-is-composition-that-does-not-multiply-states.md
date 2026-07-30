---
type: lesson
title: "The compositions that stay safe are exactly the ones that refuse to multiply the state space"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# The compositions that stay safe are exactly the ones that refuse to multiply the state space

**Lesson:** Combine two behaviours in an unrestricted way and the states multiply: three states in one and two in the other yields six in the result, since any state of the first can coincide with any state of the second. That growth is the mechanical reason unrestricted composition destroys your ability to reason — not merely that the parts might interfere, but that the number of situations to consider is now the product rather than the sum, and it compounds with every further composition.

The interesting observation is what the *disciplined* forms of composition look like when drawn as state machines, because they turn out to be precisely the shapes that avoid the product. One form joins the two behaviours at their starting state and nowhere else: whichever begins runs to completion before the other can start, so the combined machine is the two original machines sharing one initial state, with no cross transitions at all — a sum, not a product. The other form nests one behaviour entirely inside a single state of the other, like a subroutine call: the outer machine is unchanged except that one of its states has an inner machine running to completion within it. Again no product.

So "safe to compose" and "does not multiply the state space" are not two properties that happen to travel together — they are the same property seen from two directions, and that gives you a test far more practical than trying to trace interference by hand. Ask what the combined state space looks like. If it is a product, you have taken on the full cross-product of situations and you must re-verify the whole; if it is a sum or a nesting, the parts' reasoning survives intact and you re-verify nothing. The corresponding prohibition falls out too, and it is sharper than a general warning about coupling: an action must not modify shared data in a way that changes which state the *other* behaviour is in, because that single edge is what converts a nesting into a product and silently invalidates everything you concluded about the parts.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 6's state diagram section, which shows general synthesis producing the product of the base state diagrams, then shows the two safe constructs as joining the base diagrams at their initial state and nowhere else, or encapsulating one inside a single state of the other, and forbids an action from modifying attributes in a way that causes a state change in a different base model.
