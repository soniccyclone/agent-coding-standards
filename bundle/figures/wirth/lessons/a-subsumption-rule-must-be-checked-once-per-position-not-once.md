---
type: lesson
title: "A subsumption rule must be checked once per position, not once"
figure: wirth
works: [project-oberon]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A subsumption rule must be checked once per position, not once

**Lesson:** Adding a rule that a value of a more specific kind may stand wherever the general kind is expected feels like a single, simple permission. It is not one rule; it is a separate claim about every syntactic position a value can occupy, and the claims have different truth values. In a position where the value is only read, the rule is sound without qualification: whatever is actually there satisfies at least the general kind, so every read is meaningful. In a position where the value is written through a reference, the rule is unsound as stated, because a reference typed by the general kind tells you a lower bound on what is actually there, not what is actually there. Writing a general-kind-shaped value into a location that is really a different specialization leaves the target inconsistent with its own recorded identity — it now claims to be one thing and contains another, and everything downstream that trusts the identity is wrong.

The repair is a confirmation at run time that the actual kind is what the assignment assumes, inserted by the machinery rather than written by the author. That is the part worth noticing, because it is a cost with no representation in the program text. The author sees a plain assignment; the machine performs a comparison and a conditional abort. So a permission granted in the definition has quietly attached a check to a construct that had none, and the check is in the least visible possible place. This is not an argument against the permission — the permission is valuable — but it is the reason the accounting has to be done deliberately: a rule adopted because it is simple to state can be expensive in positions its statement never mentioned.

The general procedure follows directly. For any relation introduced between kinds, enumerate the positions a value can occupy — read, written, passed by value, passed by reference, extended, compared for identity, serialized — and ask separately, for each, whether the relation is sound there, and if not what it costs to make it sound. The answers will differ. Doing this before adopting the relation converts a class of surprise into a list of decisions, and the surprises are otherwise found one at a time, each one presenting as an odd special case in an implementation rather than as what it is: a consequence of a rule adopted without checking where it applies.

**Source:** [Project Oberon](../works/project-oberon.md) — the discussion opening section 12.7's treatment of module OCH, which observes that when the destination of a record assignment is indirectly referenced — a VAR-parameter or a dereferenced variable — an implicit type guard is necessary, since assigning a value of an extended type to a destination declared with the base type is acceptable only if the actual destination has the base type and not if it happens to be some other extension of it, and which remarks that this is an example of an apparently simple and basic concept producing unexpected side-effects and complications.
