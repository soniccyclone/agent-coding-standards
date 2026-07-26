---
type: lesson
title: "Two declarations that look alike are not the same concept"
figure: date
works: [databases-types-and-the-relational-model-the-third-manifesto]
axes: [cognitive-load, verifiability]
subdomains: [databases-and-data-management, programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# Two declarations that look alike are not the same concept

**Lesson:** A whole generation of hybrid database products was built on an equation between a stored table and a class, and Date's dissection of that equation is a case study in how surface resemblance drives category errors. The two declarations do look nearly identical when written out, and that resemblance was treated as evidence. His first move is to note that one denotes a variable and the other denotes a type, which should have ended the discussion before any engineering began, since a container of changing values and a set of permitted values are not candidates for unification no matter how similar their syntax.

He then shows what the conflation actually costs, and the interesting part is that each cost is a specific broken guarantee rather than a general loss of purity. Declaring a field's type to be another table makes the constraint on that field time-varying, so it is not a type constraint at all: legality now depends on what happens to be stored elsewhere at the moment. Claiming one row contains another is false as stated, because what it holds is a reference, which the user must be told about, which means the conceptual picture being sold is the wrong picture. Insertion becomes either unconstrained, in which case the declared field type meant nothing, or requires supplying a whole existing row where an identifying value would have done, which is at best telling the system what it already knows and at worst a needless way to fail. Referential rules that were declarative become procedural code, and enforcing that nobody deletes outside that code becomes a new unsolved problem. Finally the equation cannot survive derivation: project a table down to one column and the result is also a table, so it should also be a class, but no operation defined on the original applies to it. That the advocates only ever had stored tables in mind, and forgot the derived ones, is diagnostic, because which tables are stored and which are derived is largely arbitrary.

Date closes with a historical aside that is really a lesson about naming. Had the field called these things data types from the start instead of adopting one term in the database world and another in the object world, a proposal to support user-defined types in a way that suggested they were not types would have been laughed at on sight. Divergent vocabulary for one concept hid a category error for years.

A programmer who has taken this in demands, before merging two abstractions that look alike, that each be classified: is it a value, a variable, a type, or an operator? Unification across those lines is a mistake regardless of how much syntax the two share. The second habit is to test any proposed identity against the derived cases, not just the primitive ones, since a claim that holds for hand-declared instances but collapses under composition was never a real identity.

**Source:** [Databases, Types, and the Relational Model: The Third Manifesto](../works/databases-types-and-the-relational-model-the-third-manifesto.md) — the first of the orthogonal proscriptions, which walks a hypothetical product's extensions toward the table-equals-class equation and then takes it apart, ending with the observation that a table containing references is no longer a relation and the conceptual integrity of the model has been spent.
