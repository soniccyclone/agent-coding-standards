---
type: lesson
title: "A type is exactly its operations, and nothing about how it is stored"
figure: liskov
works: [programming-with-abstract-data-types]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# A type is exactly its operations, and nothing about how it is stored

**Lesson:** The habitual way to introduce a new kind of data is to describe its
shape: this thing is a record with these fields, that thing is an array of
those. This inverts the actual dependency. What callers use is behavior; the
shape is one of many ways to deliver that behavior, and it is chosen last. So
the honest definition of a data abstraction is the set of operations that
characterize it, full stop — the class of objects fully determined by what can
be done to them. Representation is not part of the definition; it is part of
one implementation of the definition.

The justification is an appeal to what the built-in types already do. Nobody
reasons about an integer as a bit pattern in a machine word, or treats
addition as a sequence of machine steps; the integer is used through its
arithmetic and nothing else, and this is exactly why integers are pleasant to
program with. If that pleasantness comes from behavior-only access, then it
is not a special privilege of types the language happens to ship — it is a
property any type can have, provided the language will grant a user-written
type the same treatment. Abstract data types are the generalization of a
comfort programmers already enjoy without noticing why.

Someone who thinks this way designs from the operation set outward. The first
artifact is the list of operations and what they mean in terms of each other,
because that is the whole of the specification; the storage decision is
deliberately postponed, since nothing above depends on it. It also changes
what counts as a design error. A type whose operation set does not let clients
say what they need is broken even if its data layout is perfect, and a type
whose clients must reach around the operations to get work done never really
existed as an abstraction — it was a struct with a naming convention.

**Source:** [Programming with Abstract Data Types](../works/programming-with-abstract-data-types.md) — the section analyzing what abstraction means, where a data abstraction is characterized entirely by its operations, argued by analogy with how programmers already treat the language's own built-in types.
