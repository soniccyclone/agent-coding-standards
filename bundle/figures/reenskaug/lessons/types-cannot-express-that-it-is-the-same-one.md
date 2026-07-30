---
type: lesson
title: "A description in terms of kinds cannot say it was the same one throughout"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# A description in terms of kinds cannot say it was the same one throughout

**Lesson:** Describe a purchase in terms of kinds of thing and their relationships and you get something compact and apparently complete: a buyer banks with a bank, a supplier banks with a bank, a buyer purchases from a supplier. Now ask the question that actually matters for correctness — is the supplier who ships the goods the same supplier who receives the payment? The description cannot answer. Each relationship is stated between *kinds*, so "a supplier" in one relationship and "a supplier" in another are not asserted to be the same individual, and no amount of care in drawing the kinds-level picture makes them so. The property you want is about identity along a path through the structure, and identity is exactly what the kinds level abstracted away.

The fix is to describe participants rather than categories — named positions in a specific collaboration, each carrying identity, so that the same participant appearing in two relationships *is* the same one by construction. This costs compactness, since a kinds-level diagram covers many situations while a participant-level one covers a specific arrangement. What it buys is the ability to reason about behaviour at all, because most of the properties worth checking in a running system are identity properties: the same session that authenticated is the one being served, the account debited is the one that authorized, the lock released is the one acquired.

The generalizable habit is to notice which level your description is pitched at *before* trying to prove something with it, because a category-level description will fail silently rather than complain. It will happily depict a system in which the supplier who ships and the supplier who is paid are different companies, and nothing in the notation flags that as a question, let alone answers it. So when a diagram feels adequate and a correctness argument keeps slipping through your fingers, suspect the diagram is one abstraction level too high — and note that this is also why the compactness is not free: what got compressed was precisely the identity you now need.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 6's semantic view section, which contrasts the role-level semantic view with the corresponding entity-relationship diagram, notes that entities are types while roles have identity, and states that the argument about the vendor who delivers also being the vendor who is paid can be made at the role level but not the entity level — referring to this as the equivalence-of-path problem.
