---
type: lesson
title: "Some things have no identity of their own, and saying so early makes the rules fall out"
figure: chen
works: [the-entity-relationship-model-toward-a-unified-view-of-data]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Some things have no identity of their own, and saying so early makes the rules fall out

**Lesson:** Chen draws a line through the population of things a system models: those that can be picked out by their own observable properties, and those that cannot. A person's dependent is the second kind. Two dependents may share a first name; what distinguishes them is which employee supports them. So the dependent's identity is borrowed — partly its own, partly the identity of the thing it hangs off. Chen then notes the borrowing recurses. A unit inside a division inside a firm is named by a local number plus the identity of its parent, which is itself a local number plus the identity of its parent, until the chain terminates in something self-identifying. Identity, on this view, is not a property every thing possesses; it is something a thing either has or derives, and which of the two it is a fact about the domain rather than a convenience of the schema.

The reason to mark the distinction at design time is that a great deal of behavior is determined by it, and determined mechanically. Chen works through insertion, revision, and removal and the pattern is consistent: once you have recorded that one thing's existence hangs on another's, what must happen when the second disappears is no longer a policy question. The dependent goes too, and so does anything hanging off the dependent, following the chain of dependence as far as it runs. Likewise, revising a value that some other thing's identity was built out of forces that identity to be revised everywhere it was borrowed. These are not rules a designer invents and hopes to remember to apply; they are consequences of the dependence relation, and they are the same consequences in every domain.

That is the payoff, and it is a payoff in checkability rather than in convenience. A system where dependence is written down can derive its own integrity rules and enforce them uniformly. A system where dependence lives only in the designer's head must have those rules hand-written at every site that deletes or renames something, which means they will be written inconsistently and some site will be missed. The failure is silent and looks like orphaned records nobody can account for.

A programmer who has absorbed this asks a specific question of every type they introduce: can an instance of this be identified without reference to anything else? A no is not a defect to be papered over by minting a synthetic identifier. Minting one buys uniqueness while discarding the dependence, and the dependence was the useful part — it was what told the system when the thing should stop existing. Give the thing the composite identity its situation actually has, and cascade behavior stops being something to remember.

**Source:** [The Entity-Relationship Model — Toward a Unified View of Data](../works/the-entity-relationship-model-toward-a-unified-view-of-data.md) — the treatment of entities identified only through a relationship with another entity, the recursive application of that identification until self-identifying entities are reached, and the tabulated consequences of insertion, updating, and deletion that follow from having recorded existence dependence.
