---
type: lesson
title: "If you want a change to be non-breaking, make the matching relation deliberately blind to it"
figure: steele
works: [the-java-language-specification]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# If you want a change to be non-breaking, make the matching relation deliberately blind to it

**Lesson:** Any system that pairs up declarations across a boundary — a subclass method with the supertype method it replaces, a handler with the event it serves, an implementation with the interface slot it fills — rests on some equality test between descriptions. That test silently decides which edits to either side are breaking. This specification treats the test as a design object rather than as an obvious consequence. Rather than requiring that two method descriptions be identical to be paired, it defines a directional relation that also holds when one description is what you get by discarding the newer type machinery from the other, and then defines pairing as that relation holding in either direction. The effect is stated plainly in the rationale: an author can add type parameters to an existing method and every already-written subclass keeps overriding it, so a library can adopt the feature without waiting for its subclasses, and subclass authors are not conscripted into a change they did not ask for.

The same instinct shows up as a deliberate exclusion. A modifier that constrains numeric reproducibility is declared to have no bearing whatsoever on whether one method overrides another, in either direction. That is not laziness; it is a decision that this particular property is not part of a method's identity, so changing it can never break a pairing. Elsewhere the specification is equally explicit about what the relation must remain sensitive to: because two descriptions that collapse to the same thing under the type-discarding step cannot be distinguished at run time, it forbids a type from having two members that collapse together, and derives from that the further consequence that a type cannot implement two different parameterizations of the same generic interface. So the relation is coarsened exactly as far as the intended evolution requires, and no further, with the limit set by what the runtime can actually tell apart.

The general principle is that compatibility is a property of your equality test, not a property of your good intentions. Whenever you find yourself hoping that a change "shouldn't break anything," the productive move is to locate the comparison that decides breakage and ask which fields of the description it reads. Every field it reads is a field nobody may ever change; every field it ignores is a field that is free to evolve. Choosing that set is the actual compatibility policy, and if you do not choose it deliberately you will inherit whichever set fell out of your data structures.

A programmer who thinks this way writes the comparison function before writing the migration plan. In API versioning, schema evolution, plugin registration, and cache keys, they decide explicitly which attributes are identity-bearing and which are advisory, coarsen the comparison to permit the evolution they intend, and stop coarsening at the boundary where the runtime can no longer tell two things apart — because past that point the ambiguity does not disappear, it just moves to somewhere with no diagnostic.

**Source:** [The Java Language Specification](../works/the-java-language-specification.md) — the method-signature and overriding sections of the classes chapter, where the subsignature and override-equivalence relations are defined so that an ungenerified declaration still pairs with a generified one, the numeric-strictness modifier is declared irrelevant to overriding, and same-erasure members are forbidden because the runtime cannot distinguish them.
