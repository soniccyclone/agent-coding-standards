---
type: lesson
title: "Your primitives are the moves your notation cannot make silently"
figure: schonfinkel
works: [bausteine-der-mathematischen-logik]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Your primitives are the moves your notation cannot make silently

The five operators Schönfinkel introduces are not an arbitrary catalog. Each one exists because the bare act of writing application side by side lacks a structural law that ordinary notation with names had supplied for nothing. Application does not commute, so an operator is needed to swap argument order. It does not associate, so another is needed to shift nesting. An argument cannot be silently reused, so a third arranges sharing. An argument cannot be silently ignored, so a fourth arranges discarding. He says as much when introducing them, describing two of them explicitly as compensating for the missing commutative and associative laws.

That is a derivation of a primitive set, not a guess at one, and it generalizes. To find the irreducible operations of a system, list the structural rearrangements that its notation performs implicitly — the ones you never think about because the syntax absorbs them — and then remove the syntax. Each absorbed rearrangement reappears as an operator you must name. Reorder, regroup, duplicate, drop: with a naming scheme these are free, because a name mentioned twice shares and a name never mentioned is dropped. Without one, they are exactly the work left to do, and the resulting basis is small because the list of things names were doing is short.

This also explains why the basis turns out to be redundant. Schönfinkel shows that the identity, interchange, and composition operators are all definable from the constancy and sharing ones, leaving two. Sharing and discarding are the deep capabilities; permuting and regrouping fall out of them. That the redundancy is discoverable at all is a consequence of having derived the set from a principle instead of assembling it by taste — you can ask which members are consequences of which others, because each has a stated job.

Applied outside logic, the habit is to justify every element of a core by the structural obligation it discharges, and to be suspicious of any element you cannot so justify. It gives you a way to argue that an instruction set, a set of combinators, a language core, or an intermediate representation is complete rather than merely adequate so far — and it gives you the redundancy check for free, since a primitive with a stated job can be tested against the others for whether it was needed.

**Source:** [Über die Bausteine der mathematischen Logik](../works/bausteine-der-mathematischen-logik.md) — the third and fourth sections, which motivate each individual function by the notational law it substitutes for and then reduce the five of them to two.
