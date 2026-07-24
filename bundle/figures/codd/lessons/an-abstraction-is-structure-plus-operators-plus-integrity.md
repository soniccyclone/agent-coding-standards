---
type: lesson
title: "An abstraction is not defined until its operators and integrity rules are"
figure: codd
works: [relational-database-a-practical-foundation-for-productivity, extending-the-database-relational-model-to-capture-more-meaning, codds-12-rules]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# An abstraction is not defined until its operators and integrity rules are

**Lesson:** Codd repeatedly corrects the same category error: identifying a model with its data structures. His definition of a data model has three inseparable components (the structure types, the operators that act on any valid instance of them, and the general integrity rules that delimit legal states and state changes), and he argues that structure specified alone leaves behavior unpinned, so infinitely many interpretations remain and speculation replaces reasoning. His barb that structure without operators is anatomy without physiology names the failure mode of an entire genre of modeling proposals that drew boxes and arrows but could not say what any operation on them meant.

The claim has organizational teeth. Codd attributes the incompatibilities between the era's data-definition and data-manipulation standards to the two having been developed by separate committees, which is the same error institutionalized: if structure and operations are one definition, they cannot be designed by different owners on different schedules. He adds a further requirement that a serious model provide a concrete conceptual representation of its instances (for relations, the table), because people cannot reason about the effect of an operation without a picture of the thing operated on; a proposal with neither operators nor a representation to think with is not yet an alternative model at all, whatever its diagrams suggest. His 12-rules article repeats the triad as the thing vendors most conveniently forget, and RM/T practices it: every structural extension arrives with its operators and its insert-update-delete rules attached.

A programmer who has internalized this refuses to review a schema, type definition, or format spec in isolation, demanding the operations and the invariants as part of the same artifact; defines a new type by what may be done to it and what must remain true of it, not by its fields; and treats any spec split that separates shape from behavior as a defect in the process, not a division of labor.

**Source:** [Relational Database: A Practical Foundation for Productivity](../works/relational-database-a-practical-foundation-for-productivity.md) — Section 3's three-component definition of a data model, the conceptual-representation requirement, and the committee argument. Also [Extending the Database Relational Model to Capture More Meaning](../works/extending-the-database-relational-model-to-capture-more-meaning.md) (the anatomy-without-physiology critique of structure-heavy semantic models, and the paper's own operator-and-rule discipline) and [Codd's 12 Rules](../works/codds-12-rules.md) (the reminder that the model's structural, manipulative, and integrity parts are frequently and conveniently forgotten).
