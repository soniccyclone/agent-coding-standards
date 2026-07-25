---
type: lesson
title: "Match the notation to the user's mental model, not to the underlying formalism"
figure: boyce
works: [sequel-a-structured-english-query-language]
axes: [cognitive-load, expressiveness]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Match the notation to the user's mental model, not to the underlying formalism

**Lesson:** Two notations can be provably equal in power and wildly unequal in what they demand of the person writing in them. The formally natural surface for a theory — the one that falls out of the mathematics — forces the writer to manage machinery the theory needs but the human task does not: auxiliary variables, quantifier scoping, explicit terms that stitch structures together. A better surface starts from how the intended user already reasons about the data (scanning a table column for matches, reading off the adjacent values) and builds keywords and structure around that habit, then proves the result still covers the full formal power underneath. Equivalence of expressive power is the floor of the design problem, not its ceiling.

A programmer who believes this treats "which concepts must the writer hold in mind per expression?" as a first-class design metric, separate from computability or completeness. They audit a proposed notation by counting the bookkeeping ideas a newcomer must learn before writing anything (bound variables, correlation terms, scope rules) and redesign until the common case needs none of them, reserving the heavier machinery for the rare query that genuinely requires it. They also design against the observed distribution of use — most real statements in any language turn out to be simple, so the simple case should cost almost nothing — rather than optimizing the surface for the hardest expressible case.

This is not dumbing-down: the payoff is a strictly larger population of people who can state correct programs, with no loss of reach for experts. The most consequential language design of the database era came from exactly this move — keeping a complete formal core and rebuilding only its human-facing surface.

**Source:** [SEQUEL: A Structured English Query Language](../works/sequel-a-structured-english-query-language.md) — the introduction's case for a new class of non-specialist users, the discussion of what calculus-based query languages force users to manage, and the closing side-by-side comparison of the same query in predicate calculus and in keyword form.
