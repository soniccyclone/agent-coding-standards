---
type: lesson
title: "When meaning depends on context, make the context an argument rather than a hidden table"
figure: scott
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When meaning depends on context, make the context an argument rather than a hidden table

**Lesson:** As soon as a system admits names whose meaning is assigned locally, the naive account breaks: a fragment no longer has a value, it has a value relative to the bindings in force. There are two ways to absorb that. One is to keep pretending the fragment has a value and maintain a mutable table off to the side that the interpretation consults and updates. The other is to change the type of the answer — a fragment denotes not a value but a function from binding contexts to values — and pass the context in explicitly at every step. The second costs one extra parameter threaded through every clause of the definition and buys a surprising amount.

What it buys is that scope becomes a local fact instead of a temporal one. The context is an ordinary object, so a construct that binds names is described by handing its body a context that agrees with the incoming one everywhere except at the names it binds. Nothing is mutated and nothing has to be restored afterwards, so there is no window during which the table is wrong, no discipline to remember, no interaction between the order in which pieces are examined and what they mean. Two fragments under the same context mean the same thing no matter what else the system is doing, which is exactly the property that makes local reasoning valid and makes independent evaluation of subparts safe. The mutable-table version has all the same information but arranged so that every question about it is a question about history.

The general form: whenever a component's behavior depends on ambient state that callers establish, prefer making that state a value the component receives over making it a place the component reads. The extra parameter looks like ceremony and is repeatedly the thing that lets you say what a component does without saying what happened before it ran. Note also what this buys in absences — a definition that threads its context needs no bookkeeping apparatus of its own, no symbol tables or name stacks, because those structures were never features of the thing being described, only artifacts of having refused to make the context explicit. When a design seems to require an elaborate side structure to track "where we are", check first whether "where we are" could simply be an argument.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the introduction of environments as functions from identifiers to values, the retyping of the command semantics so that a command denotes a function from environments to state transformations, the notation for an environment altered at one identifier or at a tuple of identifiers, and the observation that the environment is carried through every compound clause and modified only where identifiers are bound.
