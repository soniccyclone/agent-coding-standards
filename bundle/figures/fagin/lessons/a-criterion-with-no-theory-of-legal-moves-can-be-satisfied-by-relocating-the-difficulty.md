---
type: lesson
title: "A criterion with no theory of legal moves can be satisfied by relocating the difficulty"
figure: fagin
works: [a-normal-form-for-relational-databases-based-on-domains-and-keys]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A criterion with no theory of legal moves can be satisfied by relocating the difficulty

**Lesson:** Having defined a standard for a good design, Fagin immediately turns around and breaks it twice. First: keep the structure exactly as it is and delete every constraint. The mapping from old to new is the identity, so nothing is lost in the sense the field's own definition of losslessness requires, and the result trivially meets the standard because it has no constraints left to violate. Second: encode the entire contents of the system as a single record with two columns, one of them holding everything, and let the permitted set of values for that column be the set of all valid states. Again the standard is met, this time even under the stronger demand that the mapping be reversible in both directions. He then says the obvious thing: nothing whatsoever has been gained, and the difficulty of maintaining the original constraints has simply become the difficulty of maintaining one monstrous value restriction.

The general point is that a quality metric names a destination, and a destination alone cannot rule out arriving there by throwing away the cargo. What closes the hole is a companion account of which transformations are permitted and what they cost. Fagin sketches what such an account would have to include: reversibility is necessary but nowhere near sufficient, the restrictions the transformation must respect have to be stated, the time to convert in each direction matters, and crucially the incremental cost matters, so that a single small change to the source produces a small change to the target rather than a rebuild. Without that, the metric is gameable and any process that optimizes it will find the game.

Programmers encounter this constantly and usually do not name it. Complexity is nearly conserved: a lint rule that counts branches is satisfied by hiding branches in data, a coverage target is satisfied by tests that assert nothing, a module-size limit is satisfied by files that exist only to be included, a "no logic in the template" rule is satisfied by pushing logic into names. In each case the measured quantity improved and the system did not, because the difficulty moved to somewhere the metric does not look. The habit this teaches is to pair every criterion you adopt with an explicit statement of which moves are allowed and what they cost, and to test a new criterion by first trying hard to satisfy it dishonestly. If you find a cheap degenerate solution, you have learned that the criterion is measuring a proxy, and you know which unmeasured dimension needs to be named.

**Source:** [A Normal Form for Relational Databases That Is Based on Domains and Keys](../works/a-normal-form-for-relational-databases-based-on-domains-and-keys.md) — the section on transforming a schema into the new normal form, which exhibits the constraint-stripping identity transformation and the single-record encoding, then argues that the real open problem is defining which transformations count and what their cost is.
