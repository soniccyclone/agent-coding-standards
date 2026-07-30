---
type: lesson
title: "Choose the intermediate representation for what it makes nameable, not just for what it can represent"
figure: sifakis
works: [cesar-1982]
axes: [expressiveness, verifiability]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Choose the intermediate representation for what it makes nameable, not just for what it can represent

**Lesson:** Faced with a design notation people are willing to write in and a mathematics you can actually reason with, the productive move is not to build a proof theory for the notation but to compile the notation into a structure that already has one. The interesting part is which structure. The obvious criterion is adequacy — can it represent the behavior — but the criterion that pays is what the target makes explicit that the source left implicit. A textual process description says nothing you can point at when you want to talk about the moment just after some action completed; a net-shaped representation has named control points, so exactly that assertion becomes a predicate you can write down and evaluate.

That is a general property of good lowering. Compilation is usually discussed as loss, and it is, but a well-chosen target also converts implicit structure into addressable structure. Here the same translation that discards unneeded data detail simultaneously surfaces the control skeleton and the invariants that come with it, and both effects are what makes the downstream analysis feasible: less to search through, and more to refer to. If your intermediate form has no name for the thing you want to assert, the assertion cannot be checked no matter how strong the checker.

The practical test to apply when introducing any internal representation is to write down the questions you expect to ask of it and see whether each question has a subject in that representation. A representation chosen only for round-trip fidelity will pass the adequacy test and fail this one, and you will discover the failure late, when the analysis you built it for cannot phrase its own preconditions.

**Source:** [Specification and Verification of Concurrent Systems in CESAR](../works/cesar-1982.md) — the general principle of the system in section 1 and the closing discussion in section 5, on translating a high-level description into a model with an existing verification theory, and on how naming control points in the net makes properties easier to express.
