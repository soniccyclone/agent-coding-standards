---
type: lesson
title: "Make hypothesis a first-class scope, so that asking what if uses the same machinery as recording what is"
figure: abrial
works: [data-semantics]
axes: [expressiveness, cognitive-load, parallelizability]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Make hypothesis a first-class scope, so that asking what if uses the same machinery as recording what is

**Lesson:** If a model of the world only ever holds what is true, it can answer questions and nothing more. Its real value appears when someone can ask what would follow from a change they have not made, which requires the model to hold several worlds at once: the shared one, and speculative variants beneath it. Abrial's construction generalizes the scoping notion from block-structured languages into a runtime object. A context is a thing you create and destroy explicitly, independent of any process, arranged in a tree beneath a shared root. Every action takes effect in some context, and its effect is visible to that context and its descendants but invisible above. Reading a value means walking up the chain, applying the assertions and retractions encountered along the way. Speculative work is therefore not simulated by copying and diffing; it is expressed in exactly the vocabulary that non-speculative work uses.

What the same mechanism buys, once built, is more than the original purpose. Because effects in a private context are unseen elsewhere, several users can work simultaneously on the shared model without interfering — isolation falls out of the scoping rule rather than being a separate feature. Because a context is independent of any process, a line of what-if reasoning can be kept alive across sessions and returned to later, so the tree of live contexts is a persistent structure and not a call stack. And because a traversal can record its intermediate findings in a context of its own, a shared graph can be walked concurrently by several traversals without any of them corrupting the others' bookkeeping, which is otherwise a nasty problem. One idea, several apparently unrelated capabilities.

The transferable thought is about where speculation belongs in a design. Most systems treat it as an application-level concern and reimplement it badly and repeatedly, as snapshot-and-restore, as undo stacks, as staging tables, as sandbox copies of production data — each of them a private, partial version of the same construct. Making layered hypothetical state a primitive of the model instead means that consistency rules, derivation, and access control automatically apply inside a hypothesis, since a hypothesis is not a special mode. The design question worth asking of any stateful system is whether it can represent a possibility as cheaply and as faithfully as it represents a fact. Systems that cannot force their users to choose between reasoning about change and preserving the truth.

**Source:** [Data Semantics](../works/data-semantics.md) — the section introducing contexts as independently created objects arranged in a hierarchy, with the rule that effects performed in an inner context are hypothetical and unseen from the outer ones, described there as giving the model imagination; its use for per-user isolation and for persisting speculative work between sessions; and the course-prerequisite example where a private context makes a shared graph traversal reentrant.
