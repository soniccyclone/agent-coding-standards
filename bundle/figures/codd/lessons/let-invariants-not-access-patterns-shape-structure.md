---
type: lesson
title: "Let invariants, not access patterns, shape the structure of data"
figure: codd
works: [further-normalization-of-the-data-base-relational-model, normalized-data-base-structure-a-brief-tutorial, a-relational-model-of-data-for-large-shared-data-banks]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Let invariants, not access patterns, shape the structure of data

**Lesson:** Normalization's real teaching is a design epistemology. The inputs to structuring data are the time-independent facts about the domain (which attributes determine which others), not today's queries, today's record layouts, or today's traffic; Codd states outright that the goal is a structure neutral to query statistics, because statistics change and semantics mostly do not. Functional dependencies are semantic invariants a designer can elicit and write down, and once written down they mechanically dictate how the data should be decomposed. Structure stops being a matter of taste and becomes a derivation from declared facts.

The method's demonstrations are behavioral, and that is the second teaching: a structural defect is diagnosed by exhibiting an operation that misbehaves. If updating one real-world fact requires touching a time-varying number of records, or recording a new entity is impossible until some unrelated fact exists, or deleting the last incidental association silently destroys knowledge, the schema is wrong, and it is wrong before any such operation has ever been executed. Anomalies are properties of the shape, provable from the dependencies alone. Storing each fact in exactly one place, keyed by what actually determines it, makes the bad behaviors inexpressible rather than merely avoided, and Codd's conjecture that third normal form extends the life expectancy of application programs ties the discipline back to change: growth tends to force exactly the splits normalization would have made up front.

A programmer who takes this seriously designs any stateful structure (a schema, a config format, a class's fields, a cache) by first writing down what determines what, decomposes until each fact lives where its determinant is, and evaluates proposed structures by asking which update sequences they make dangerous, not by asking which reads they make convenient. Convenience for reads is recoverable by derivation (joins, views); integrity lost to a redundant structure is not.

**Source:** [Further Normalization of the Data Base Relational Model](../works/further-normalization-of-the-data-base-relational-model.md) — the functional-dependence machinery, the anomaly demonstrations motivating second and third normal form, and the growth and restructuring section with the life-expectancy conjecture. Also [Normalized Data Base Structure: A Brief Tutorial](../works/normalized-data-base-structure-a-brief-tutorial.md) (the six objectives of normalization, including neutrality to query statistics) and [A Relational Model of Data for Large Shared Data Banks](../works/a-relational-model-of-data-for-large-shared-data-banks.md) (the original normalization procedure eliminating nonsimple domains).
