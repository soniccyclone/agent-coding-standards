---
type: figure
title: Trygve Reenskaug
description: b. 1930, University of Oslo. Invented Model-View-Controller while at PARC; decades-long re-argument (via DCI) of what MVC was supposed to mean.
status: accepted
layer: implementation-mapping
subdomains: [programming-environments-and-object-systems]
tags: [figure, accepted]
---

# Trygve Reenskaug

**Dates:** b. 1930. Norwegian computer scientist, professor at University of Oslo; visiting scientist at Xerox PARC in 1978-79.

## Why a candidate
Invented Model-View-Controller while embedded in the Smalltalk group at PARC, explicitly designing it as a way to let end users *directly manipulate* a live model through interchangeable views/editors — later spent decades (through DCI) explicitly re-arguing that mainstream class-based OO had drifted from the original "objects as mental models for interaction" vision.

## Top 10 most influential works
Nearly entire bibliography self-archived at his own University of Oslo page:
1. "Thing-Model-View-Editor: An Example from a Planning System" (1979) — `public` (folk.universitetetioslo.no/trygver)
2. "Models-Views-Controllers" (1979) — `public` (same host)
3. "The Model-View-Controller (MVC): Its Past and Present" (2003, JAOO) — `public` (self-archived)
4. "The Data, Context, and Interaction Paradigm" (2009, with Coplien, SPLASH) — `paywalled` (self-archived versions on his site)
5. *Working With Objects: The OOram Software Engineering Method* (1996, with collaborators) — `paywalled`
6. DCI tutorial/overview materials (SPLASH '12, with Coplien) — `public` (self-archived slides, artima.com/DCI)

## Lessons
Across fifty years and three vocabularies — editors and views at PARC, roles and collaborations in OOram, data and context and interaction in DCI — Reenskaug keeps making one argument with unusual stubbornness: a notation that can only describe one participant at a time cannot describe what a system does, and everything downstream of that gap is a symptom. The lessons therefore cluster around what is missing rather than what is present. Communication between parts deserves a first-class construct, because what a language has no word for gets encoded implicitly and inconsistently; local correctness does not compose when what counts as correct depends on the caller's purpose; two orthogonal decompositions forced through one mechanism both come out wrong; and a requirement nobody can point at in the code cannot be reviewed, which is why emergent behavior is a doctrine with a cost rather than an achievement. His positive proposals are all about where things go and who is allowed to see them: sort behavior by what it drags into scope rather than by the noun it mentions, keep state whose meaning expires with an operation out of the object's permanent structure, put permission on the relationship rather than the interface, give a legitimate mismatch between two structures its own named layer, and treat entities and collaborations as the same thing viewed from different altitudes. Running underneath is a hard-headed methodological streak: a model answers a question and cannot be judged without one, hierarchy is a convenience of thought rather than a feature of the world, composition earns the name reuse only when it preserves what you already verified, and a discipline is worth precisely the working programs it forbids. He is equally clear that structure nobody can see does not exist — comprehensibility has to be designed in from the start rather than documented in later, roles are the invariant while the number of objects carrying them is a sizing decision, and the browser that displays a decomposition is part of the language that expresses it.
