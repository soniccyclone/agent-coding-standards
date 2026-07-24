---
type: lesson
title: "Identity must outlive every description of the thing identified"
figure: codd
works: [extending-the-database-relational-model-to-capture-more-meaning]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Identity must outlive every description of the thing identified

**Lesson:** Any identifier whose value users choose is, by that fact, a value users may change, and therefore a description rather than an identity. Codd's argument for system-assigned surrogates in RM/T proceeds from three concrete failure modes of user-controlled keys: their values get renumbered by real-world events like company mergers; two datasets can denote the same entity under keys drawn from different schemes, so matching on key values misses matches of entities; and an entity's life extends before its key is issued and after it is retired, yet facts about it must be recordable throughout. The conclusion is a separation of concerns: let users keep whatever mutable, meaningful identifiers they need for their own purposes, but rest the model's notion of sameness on an identifier the system generates, never displays, and never lets anyone edit, with one guaranteed invariant: two identifiers are equal exactly when they denote the same entity.

The subtle honesty in the treatment is that identity is a claim, not a discovery. The system mints distinct surrogates because a user asserted distinctness, and Codd provides a coalescing operation for the day the assertion proves wrong and two recorded things turn out to be one. Building the merge operation into the model concedes that entity resolution is fallible and makes correction a first-class act instead of a data-repair emergency.

A programmer who accepts this never uses an email address, username, serial number, or any other meaningful attribute as a primary key or foreign-key target; keeps join-on-identifier and match-on-attributes as visibly different operations with different trust levels; and designs a merge path for the day two records prove to be one entity. The rule generalizes past databases to any system that must track things over time: whatever the user can see and change is data about the thing, and identity must be the one property no description change can touch.

**Source:** [Extending the Database Relational Model to Capture More Meaning](../works/extending-the-database-relational-model-to-capture-more-meaning.md) — Section 4's three difficulties with user-controlled keys, the surrogate and E-domain machinery with its equality guarantee, and the coalescing command for entities later found identical.
