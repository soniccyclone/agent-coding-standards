---
type: lesson
title: "A notation of two primitives, held constant across domains, turns comparison into perception"
figure: bachman
works: [oral-history-charles-bachman]
axes: [primitive-count, expressiveness]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A notation of two primitives, held constant across domains, turns comparison into perception

**Lesson:** Bachman's data structure diagrams reduce to two tokens: a block for a type of thing, and an arrow for a one-to-many relationship between types. Everything else — instance counts, storage layout, whether the subject is hardware or software — is deliberately absent. In the oral history he shows the notation describing a CPU as readily as a database: draw instruction cells and memory cells as blocks, reference relationships as arrows, and the architectural difference between a single-address and a three-address machine is visible at a glance, because it is literally a different number of arrows. He wanted the same treatment for operating systems, protocol interfaces, whole museum collections of computers: name each system's objects of discourse, draw their relationships, and structural sameness or difference across wildly unlike systems becomes something you see rather than something you argue about.

Why it works: a notation is an algebra, and an algebra pays off only if its primitive set is small enough to internalize completely and stable enough that every diagram is comparable with every other. Each added symbol multiplies what a reader must hold; each per-domain dialect destroys cross-domain comparison. Bachman is also candid that surface readability is part of the semantics in practice — he adopted a Japanese colleague's suggestion to shadow the blocks so that a rectangle reads as one icon rather than four lines, and he judged competing diagram products harshly for having pictures without defined meaning. A small primitive set with sharp semantics beats a rich vocabulary with fuzzy ones.

A programmer who takes this seriously reaches for one deliberately minimal modeling notation and uses it everywhere: before debating a design, draw its objects of discourse and their relationships; when two systems feel similar, diagram both in the same tokens and let the overlap or divergence show itself. And they treat a diagram whose symbols have no defined semantics as decoration, not as a model.

**Source:** [Oral History: Charles Bachman](../works/oral-history-charles-bachman.md) — the reflections section: the two-token algebra explained through the single-address versus three-address computer example, the shadow-icon anecdote, and the semantics-versus-pictures contrast with rival diagram vendors.
