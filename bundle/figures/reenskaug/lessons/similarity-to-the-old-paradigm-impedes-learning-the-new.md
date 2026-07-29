---
type: lesson
title: "Learn a new way of thinking in a language that forbids the old one, even if you will ship in one that permits both"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# Learn a new way of thinking in a language that forbids the old one, even if you will ship in one that permits both

**Lesson:** The obvious way to move a team onto a new paradigm is through the vehicle closest to what they already use — if they know a procedural language, adopt its object-oriented descendant, since the syntax carries over and the transition feels small. The argument here is that this reasoning is exactly backwards, and that the *similarity* is the obstacle. A hybrid language permits the programmer to keep thinking along the old track while believing the shift has happened, because nothing in the language ever forces the new concepts to be used. The familiar escape hatch is always available, and under deadline pressure it is always taken.

The recommendation that follows is deliberately uneconomical: make a clean break and write your first programs in a language that offers no fallback, even when the shipped product will be written in the hybrid. You are paying for a language you will not deploy in, to buy the one thing the deployment language cannot give you — the absence of an alternative. What is being learned is not syntax, which is cheap, but a mental model, which is expensive and which a permissive language lets you skip indefinitely.

The generalization is worth keeping for any transition where an old habit and a new one can coexist in the same tool. Ease of adoption and thoroughness of adoption pull against each other: the gentler the migration path, the more likely you arrive with the old model intact and new syntax painted over it. So when choosing how to learn something, ask what the environment makes *impossible*, not what it makes easy — and treat "this will feel familiar" as a warning about the depth of the change rather than a selling point. The corollary the same chapter draws is that once you are working in a given language you should adopt its philosophy rather than fight it, since a language is not very good at being some other language and was never meant to be.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 4's discussion of choosing a programming language, which rejects as a fallacy the common belief that a C programmer transitions more easily via C++ than via Smalltalk, argues the similarities make the paradigm shift harder by permitting old thinking, recommends a clean break even when the product will ship in the hybrid, and quotes Stroustrup on each language not being meant to be the other.
