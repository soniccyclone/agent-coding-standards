---
type: lesson
title: "Bind programs to information, never to its arrangement"
figure: codd
works: [a-relational-model-of-data-for-large-shared-data-banks, derivability-redundancy-and-consistency-of-relations-stored-in-large-data-banks, relational-database-a-practical-foundation-for-productivity, codds-12-rules, recent-investigations-in-relational-data-base-systems]
axes: [cognitive-load, expressiveness]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Bind programs to information, never to its arrangement

**Lesson:** Every accidental property of a representation that a program is allowed to see becomes a dependency that will eventually break it. Codd's founding move was to enumerate the kinds of representational accident that clients of a data system could observe in his day (storage order, the presence of an index, the shape of an access path) and to demonstrate that a program written against any one of them fails when the operations staff legitimately changes it. The maintenance cost of a system is proportional to the surface area of incidental detail its clients can perceive, so the designer's first job is to shrink that surface to the pure information content and nothing else.

The discipline this demands is stronger than "add an abstraction layer." A layer that merely renames physical concepts (a pointer called a link, an address called a position) still transmits the dependency. The interface has to be defined in terms that make representational questions unaskable: if a client cannot express "the next record" or "follow this chain," it cannot come to depend on adjacency or chains. Codd later turned this into an audit checklist, requiring physical, logical, integrity, and distribution independence as separately testable properties, because each names a distinct class of change the world will impose and each must be survivable without touching client code.

The same reasoning scales up. When independent systems must exchange data, the stable thing to standardize is a neutral boundary representation stripped of pointers, hashing, and ordering; each party then owns a private translation to whatever internals it likes, and any node can change its internals without renegotiating with the others. A programmer who has internalized this lesson designs every interface, not just database schemas, by asking which of its visible properties are information and which are today's arrangement, then makes the second category invisible before anyone can write code against it.

**Source:** [A Relational Model of Data for Large Shared Data Banks](../works/a-relational-model-of-data-for-large-shared-data-banks.md) — the opening section's catalog of ordering, indexing, and access-path dependencies and the five-structure exercise showing programs failing under restructuring. Also [Derivability, Redundancy, and Consistency](../works/derivability-redundancy-and-consistency-of-relations-stored-in-large-data-banks.md) (the same motivation in its first statement), [Relational Database: A Practical Foundation for Productivity](../works/relational-database-a-practical-foundation-for-productivity.md) (the data independence objective and the maintenance-cost argument), [Codd's 12 Rules](../works/codds-12-rules.md) (rules eight through eleven as testable independence properties), and [Recent Investigations in Relational Data Base Systems](../works/recent-investigations-in-relational-data-base-systems.md) (the fourth data-exchange policy: standardize the communication form, free the nodes).
