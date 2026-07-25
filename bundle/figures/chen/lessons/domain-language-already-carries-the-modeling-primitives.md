---
type: lesson
title: "The language people already use to describe a domain carries its structure"
figure: chen
works: [english-sentence-structure-and-entity-relationship-diagrams]
axes: [expressiveness, primitive-count]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# The language people already use to describe a domain carries its structure

**Lesson:** Chen holds a modeling notation up against the grammar of ordinary description and asks whether the joints line up. They do, and tightly. What a language marks as a thing corresponds to a category of thing in the model; an action taking an object corresponds to an association; a modifier of a thing becomes a property of that thing; a modifier of an action becomes a property of the association. The nesting works too. A noun formed from a verb corresponds to an association promoted to a thing in its own right, so that further associations can attach to it, and a subordinate clause behaves like a cluster of things and associations collapsed into a single unit at a higher level. The same handful of constructs recurses all the way down a sentence.

Two conclusions come out of this and they are worth separating. The practical one is that requirements are already written in a structured language, so the raw material for a model is there to be read rather than conjured — and reading it is more reproducible than intuiting it. The theoretical one is more interesting: the correspondence is evidence about the primitives themselves. If a modeling vocabulary of roughly that size independently matches distinctions that every natural language already draws in order to describe states of affairs, the vocabulary is probably not an arbitrary invention. It is tracking something about how descriptions of the world decompose. By the same token, a formalism demanding constructs with no counterpart in ordinary description, or lacking one for a distinction description makes constantly, is suspect on that ground alone, before any usability study.

A programmer designing a domain vocabulary can run this as a test. Say the sentences practitioners actually say, and see what the model does with them. A sentence that cannot be expressed without contortion points at a missing primitive; a construct in the model that none of their sentences need is probably surplus. There is a further signal in how practitioners talk: when they start turning a verb into a noun — when the shipping becomes a thing that clerks perform, rather than a thing that happens to products — an association has acquired its own identity and properties, and that promotion is worth catching in the model early rather than after the fields start piling up in the wrong place.

**Source:** [English Sentence Structure and Entity-Relationship Diagrams](../works/english-sentence-structure-and-entity-relationship-diagrams.md) — the eleven translation guidelines mapping parts of speech onto modeling constructs, particularly the treatment of verbal nouns as promoted associations and of clauses as recursively abstracted higher-level things.
