---
type: lesson
title: "Constrain the transitions rather than the states, and schema change stops requiring migration"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Constrain the transitions rather than the states, and schema change stops requiring migration

**Lesson:** There are two things a schema can mean. It can define the set of legal states, in which case changing it invalidates data that was legal a moment ago, and the stored contents must be restructured to match — the familiar migration problem, where every schema change carries a data-rewriting project. Or it can define the set of legal *edits*: given a structure as it stands, which insertions and deletions are permitted. This author's system takes the second reading, and the consequence is that existing structures survive schema changes untouched.

The example makes the difference concrete. Tighten a cardinality so that a document must now have exactly one author, and old documents with none or with several remain valid and readable. What changes is only what you may now do: no new document can be created without an author, and the last author cannot be removed from an old one. The constraint is fully in force going forward and imposes no obligation backward. This is strictly weaker than state validity — at any moment the store may hold structures the current schema would not permit you to build — and the weakness is the entire point, since it is what buys evolution without migration.

Two justifications are given and they are of different kinds. The first is capability: no known algorithm intelligently transforms an existing structure to conform to new notions, so state-based validity does not actually deliver the automatic migration it implies — someone writes the transformation by hand, per change, and guesses at intent. Admitting that up front is more honest than a rule you cannot enforce without a human. The second is a claim about what records are for: old structures were created under the old assumptions and should stay unchanged in the archive, because rewriting them to satisfy today's rules destroys the evidence of what was true when they were made. Migration is not a neutral technical step; it is a lossy edit of history performed for the convenience of the current model.

The transferable move is to ask, of any invariant you are about to impose, whether you need it to hold of all states or only of all future changes. Transition constraints are cheaper to enforce (they are checked at exactly the moment of the operation, where the intent is present), they compose with evolution instead of fighting it, and they leave the record intact. Reserve state invariants for the properties something genuinely cannot function without — and expect that list to be much shorter than the schema you would otherwise have written.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 11 sections 11.3 and 11.3.2, which contrast the relational schema (defines all legal data structures; the database must be restructured if the schema changes) with the OOCS Schema (controls editing by defining legal insertions and deletions, so object structures survive schema changes without restructuring), give the author-cardinality example in which old documents with no or multiple authors stay valid while new ones cannot be created without an author, and state the two reasons: no known algorithm intelligently transforms an existing structure to conform to new notions, and a refusal to rewrite history since old structures were created under old assumptions and should be retained unchanged in the archives.
