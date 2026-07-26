---
type: lesson
title: "Data is a body of claims, not a pile of records"
figure: date
works: [an-introduction-to-database-systems, databases-types-and-the-relational-model-the-third-manifesto]
axes: [primitive-count, verifiability, expressiveness]
subdomains: [databases-and-data-management, foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Data is a body of claims, not a pile of records

**Lesson:** The habitual way to read a table is as an abstraction of a file. Date argues for a different reading that changes what the whole enterprise is: the heading of a table states a parameterized sentence about the world, and each row is that sentence with its blanks filled in, asserted as true. The stored collection is therefore not a container of records but the set of statements the system is currently prepared to stand behind. He pairs this with the convention that anything expressible and absent is thereby denied, so the collection is exhaustive as well as true, which is what makes a query's silence informative rather than merely uninformative.

Two consequences follow immediately and are worth more than the reframing itself. First, derived results are not second-class: applying an operator produces a new relation whose own sentence is computable from the operands' sentences, so a projection turns a parameter into an existential qualifier and a join conjoins two claims over shared parameters. Querying is not fetching, it is inference, and a view is not a saved query but a derived assertion with a statable meaning. Second, several long-running design arguments become decidable rather than aesthetic. Repeating an identical row asserts the same statement twice, and repetition does not increase truth, so duplicates are not a performance trade-off but a meaningless construct. A field with no value cannot be substituted into the sentence at all, so the row asserts nothing and the whole apparatus of extra truth values that has to be bolted on to cope with it is a consequence of a modeling mistake rather than a feature.

The same lens yields Date's account of what a data foundation minimally needs. Types supply the things one is permitted to talk about; relations supply the things one says about them. He presses that these are both necessary, since without types there is nothing to name and without relations nothing can be asserted, and jointly sufficient, since nothing further is required as a logical matter. That is a strong claim about primitive economy, and it doubles as a diagnostic: a proposal that adds a third fundamental kind of thing alongside these two should be suspected of confusing something orthogonal, or of confusing the two that already exist.

A programmer who has internalized this writes down the sentence a table is meant to assert before writing the schema, and treats any column or state that makes the sentence unsayable as a design error rather than a modeling convenience. It also reorients how they read integrity rules and views: a constraint is a claim about which statements may coexist, and a derived table is a derived claim, so both belong in the same vocabulary as queries rather than in separate mechanisms.

**Source:** [An Introduction to Database Systems](../works/an-introduction-to-database-systems.md) — the "what relations mean" section of the introductory relational chapter, with its predicate-and-proposition reading, its nouns-and-sentences analogy, and its argument that types and relations are jointly necessary and sufficient; also the properties-of-relations material in the relations chapter, where the same reading disposes of duplicate rows. Also [Databases, Types, and the Relational Model: The Third Manifesto](../works/databases-types-and-the-relational-model-the-third-manifesto.md), whose survey chapter develops the relation-variable predicate, the closed-world convention, and the propagation of meaning through derived expressions.
