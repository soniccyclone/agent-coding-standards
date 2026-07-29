---
type: lesson
title: "Map the space of meanings before arguing about notation"
figure: strachey
works: [fundamental-concepts-in-programming-languages]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# Map the space of meanings before arguing about notation

Strachey's division of labour is blunt: meaning is what you are trying to express, notation is the tax you pay to write it down. Which means that until you know what the interesting things to express are, work on how to write them is guesswork dressed as rigour. He is explicit that the pressing task in language design is to survey the field of semantic possibilities — to find where the peaks are — and that questions of convenient syntax become worth attention only once the terrain is known.

The reason this ordering matters is that syntax work is seductive precisely because it is tractable. Grammar formalisms give you a well-defined game with clean results, so a researcher can spend years mapping the boundaries of a notation while the underlying question of what the notation should be able to say goes unexamined. Strachey's complaint about the fascination with grammar limits is not that the mathematics is bad but that it explores the frontier of a technique already known to be inadequate, while the more consequential question — what constructs a language ought to be able to mean — sits untouched. Effort follows tractability rather than importance unless you consciously resist.

For a working designer this reorders the whole activity. You start by asking what values, what bindings, what forms of combination the language admits, and you write those out in whatever ugly, bracket-heavy form makes the structure visible — the applicative form of an expression rather than the familiar infix one — accepting unreadability as the price of seeing the shape. Only after the semantic inventory settles do you design surface forms, and at that point differences that felt like deep disagreements often turn out to be the same construct wearing different clothes. Conversely, when a proposed syntax cannot be explained in terms of the semantic inventory, that is not a notation problem; it is a signal that a new kind of meaning has been smuggled in and has not been analysed yet.

**Source:** [Fundamental Concepts in Programming Languages](../works/fundamental-concepts-in-programming-languages.md) — the preliminary discussion of why syntactic questions are held to be premature, and the running practice through the lectures of rewriting familiar constructs in explicit applicative form to expose their structure.
