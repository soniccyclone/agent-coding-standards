---
type: lesson
title: "Define goodness in terms of the constraints your mechanism already enforces for free"
figure: fagin
works: [a-normal-form-for-relational-databases-based-on-domains-and-keys]
axes: [primitive-count, verifiability, hardware-affinity, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Define goodness in terms of the constraints your mechanism already enforces for free

**Lesson:** Every quality criterion in the field before this one was phrased in the vocabulary of some particular family of constraints, which meant the criterion could only see defects of the kinds that family could express, and enforcing it required a mechanism that understood that family. Fagin's alternative is to pick the two notions that any storage system must already support for unrelated reasons — the permitted set of values for a column, and the identification of a record by some subset of its contents — and to declare a design good exactly when every constraint it must obey is a logical consequence of those two. The criterion never mentions decomposition, joins, or any operator. It says: if you enforce the cheap things, everything else is enforced automatically, at no additional cost.

The move worth stealing is the parameterization. Fagin points out explicitly that the definition generalizes: choose any class of constraints you consider primitive or cheap to police, and you get a corresponding notion of a well-formed design, namely that all its constraints follow from constraints in that class. The strength of the resulting criterion is inherited from the class, and a smaller class yields a stronger criterion. What makes the choice principled rather than arbitrary is that it is answerable to implementation reality: he notes that the cost measure that matters here is not instruction count or memory but page faults, and that a real theory of which constraints are cheap does not yet exist. A criterion grounded this way is simultaneously a statement about design quality and a statement about what the runtime has to do.

The consequence for a working programmer is a reordering of the question. The usual sequence is to decide what invariants the design should have and then to build machinery to check them. The better sequence is to inventory what the platform already validates without being asked — uniqueness constraints, type and range checks, foreign key relationships, whatever the storage layer or type system polices as a side effect of existing — and then to shape the design so that every invariant you care about is a consequence of those. Where you succeed, correctness costs nothing and cannot be forgotten. Where you fail, you have identified precisely the invariants that will require bespoke enforcement code, and you can decide whether they earn it.

**Source:** [A Normal Form for Relational Databases That Is Based on Domains and Keys](../works/a-normal-form-for-relational-databases-based-on-domains-and-keys.md) — the definition of the new normal form as logical consequence of domain and key constraints alone, and the later section proposing the general paradigm in which any class of easily enforced constraints induces its own normal form, with its remark on the missing complexity theory for constraint enforcement.
