---
type: lesson
title: "Check how a property behaves under the operations you plan to apply to it"
figure: fagin
works: [multivalued-dependencies-and-a-new-normal-form-for-relational-databases, horn-clauses-and-database-dependencies]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# Check how a property behaves under the operations you plan to apply to it

**Lesson:** The older, narrower kind of dependency has a comfortable feature nobody had needed to remark on: whether it holds is unaffected by throwing columns away. It is true of a restricted view exactly when it is true of the full structure. Fagin's more general dependency does not behave this way. It survives restriction in one direction under stated conditions, and the converse fails outright: a restricted view can obey the constraint while the structure it came from obeys no corresponding one. Constraints of this kind are sensitive to what else is present, and that sensitivity is invisible until you deliberately test it.

The generalizable point is that a property is not just a predicate; it is a predicate plus its behavior under the operations of your system. Restriction, extension, composition, and product each either preserve a property or do not, and which ones do is part of the property's definition in practice even when the formal definition never mentions them. Fagin's response is instructive: rather than pretend the sensitivity away or restrict the concept to keep it well behaved, he names the residual case as its own kind of constraint that holds of the larger structure by virtue of holding in a projection of it. The awkwardness gets a name and a place in the theory instead of being suppressed.

For working programmers this is the discipline behind most invariant bugs. An invariant established for a whole aggregate is quietly assumed to hold for each slice handed to a subsystem; a validation that passes on a full record is assumed to pass on the subset that gets serialized; a property proved of a module is assumed to survive composition. Each of those is a closure claim, and each needs to be either proved or explicitly denied. The practical move is to ask, for every invariant you rely on, which operations in the system are allowed to move data across it, and to check preservation for each one rather than for the generic case.

**Source:** [Multivalued Dependencies and a New Normal Form for Relational Databases](../works/multivalued-dependencies-and-a-new-normal-form-for-relational-databases.md) — the closing section on dependencies that hold in projections, including the theorem on downward inheritance, the counterexample showing there is no converse, and the contrast drawn with the context-insensitivity of the older dependency notion. The same lesson recurs in [Horn Clauses and Database Dependencies](../works/horn-clauses-and-database-dependencies.md), whose section on restricted views shows that the older constraint language is not closed under column removal while the general one is, illustrated by a schema whose four-column view obeys an invariant no constraint of the older kind can state.
