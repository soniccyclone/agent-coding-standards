---
type: lesson
title: "Publish a representation you are not obliged to store"
figure: date
works: [databases-types-and-the-relational-model-the-third-manifesto, an-introduction-to-database-systems]
axes: [expressiveness, cognitive-load]
subdomains: [databases-and-data-management, programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Publish a representation you are not obliged to store

**Lesson:** Full encapsulation has a failure mode that its advocates rarely price in, and Date names it precisely: if the only way to reach a value is through operators someone anticipated, then every question nobody anticipated becomes unaskable. A type exposing a getter for one coordinate of a point and not the other does not merely make some queries slow, it makes them inexpressible, and no amount of cleverness downstream recovers the lost access. Ad hoc interrogation and access-only-through-chosen-methods are in direct tension, and a data system whose whole purpose is answering questions its designers did not foresee cannot afford to lose that argument.

His resolution is a third thing sitting between the hidden physical layout and the opaque interface: a declared representation that is part of the type's public contract, complete enough that every value of the type can be named through it and every component of it can be read and separately updated, while carrying no commitment whatsoever about how the value is actually stored. The stored form may match the published one, or may be something else entirely, converted on the way in and out by the type's implementer, who is the one party permitted to know both. Because completeness is required rather than optional, an unanticipated question is always formulable; because the published form is decoupled from the stored form, the implementer keeps full freedom to change layout.

The construction also dissolves a false choice about canonical form. A type can declare more than one representation, each complete, each with its own way of naming values and reading components; a geometric point can be published in both rectangular and angular terms with neither privileged, and whichever the machine stores is nobody's business. This matters because arguments over "the" right representation are usually arguments over which questions are convenient, and publishing several ends the argument instead of winning it. Date is careful that the published components belong to the representation and not to the type, so admitting them does not make the type structured or reintroduce visible internals; and he prefers accessors that can nest as assignment targets over the conventional get-and-set pair, since nesting keeps a deep update expressible as one statement instead of a copy-modify-write dance through temporaries.

A programmer who has taken this on stops treating "expose nothing" as the default virtue of an interface and starts asking what the complete, minimal, question-answering surface of the type is, then publishes exactly that and no layout details. The test to apply to any encapsulated type is whether an outsider could formulate a query the author never imagined; if not, the encapsulation has bought maintainability by mortgaging the type's future usefulness.

**Source:** [Databases, Types, and the Relational Model: The Third Manifesto](../works/databases-types-and-the-relational-model-the-third-manifesto.md) — the possible-representations material in the theory-of-types chapter, together with the two prescriptions that require at least one such representation to be declared and its components to be readable and updatable, whose motivating discussion is the ad hoc query failure of method-only access in object systems. Also [An Introduction to Database Systems](../works/an-introduction-to-database-systems.md), whose types chapter develops the same separation between a type and its physical representation and works the two-coordinate-systems example.
