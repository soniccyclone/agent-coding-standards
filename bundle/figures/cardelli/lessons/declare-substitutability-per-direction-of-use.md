---
type: lesson
title: "Attach substitutability to how a slot is used, not to the thing as a whole, and read protection off the same annotation"
figure: cardelli
works: [an-imperative-object-calculus, a-semantics-of-multiple-inheritance]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Attach substitutability to how a slot is used, not to the thing as a whole, and read protection off the same annotation

**Lesson:** Asking whether one description may stand in for another is the wrong granularity of question, because the honest answer differs per slot and per direction of use. A slot that is only ever read can safely be refined, since every reader of the general version is satisfied by a more specific value. A slot that is written cannot, since a writer of the general version would install something the specific readers cannot handle. The classic unsoundness is exactly this: widen a container, store into it through the widened view, then read it back through the original and find a value that was supposed to be impossible. Once the direction of use is recorded per slot instead of guessed, both refinement and its opposite become available where each is safe, and the failing combination is rejected by construction rather than by a global ban on refinement inside mutable structures.

The elegant part is what the same annotation buys for free. A slot marked as read-only for refinement purposes is, by the same rule, a slot that cannot be written from outside, which is access control obtained as a consequence of variance rather than as a separate feature with its own syntax and its own enforcement. A component can therefore be handed out in a form that permits reading and forbids modification, while the internals, which were checked against the unrestricted description, retain the ability to modify themselves. Two apparently unrelated design concerns, flexible substitution and protection of state, are served by one mechanism, which is a strong hint that the mechanism is carved at the right joint.

The lesson for anyone designing an interface, schema, or protocol is to record for each field how it is used before arguing about whether the whole thing is compatible with a variant of itself. Compatibility is not a property of a pair of descriptions; it is a property of a pair of descriptions together with the operations that will be performed through them. Systems that lose this distinction end up either unsound or needlessly rigid, and usually both in different places.

**Source:** [An Imperative Object Calculus](../works/an-imperative-object-calculus.md) — the variance annotations introduced with the object type constructor, which permit refinement in one direction while blocking update and permit the reverse while blocking invocation, and the worked protected-cell example where subsumption into an annotated version yields external protection while internal modification survives. Also [A Semantics of Multiple Inheritance](../works/a-semantics-of-multiple-inheritance.md) — the anomaly section, where an update through a widened reference breaks and the fix is to distinguish updatable slots and require equality rather than inclusion for them.
