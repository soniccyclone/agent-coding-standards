---
type: lesson
title: "What you stored and what merely follows from it are not interchangeable"
figure: fagin
works: [on-the-semantics-of-updates-in-databases]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [databases-and-data-management, foundations-of-computation]
tags: [lesson]
---
# What you stored and what merely follows from it are not interchangeable

**Lesson:** If a body of knowledge is closed under its own inference rules, then every consequence sits in it on equal footing with everything that was put there deliberately. That looks like a simplification, and for asking questions it is one: membership and derivability collapse into a single relation. Fagin, Ullman and Vardi show that it is a disaster for changing things. Their worked case is tiny. Hold two independent beliefs; the conjunction of the two, and every other consequence, is also present in the closed version. Now learn that one of the two originals is false. In the un-closed version you retract that one belief, insert its replacement, and you are done, which is exactly what anyone would expect. In the closed version the derived combination is just as much a member as the originals were, so retracting the falsified belief is not enough and something further has to go, with no principled way to say which. Push the example slightly and the closed version has to be abandoned wholesale.

The reason is that closure destroys information you actually needed. Deliberately asserting something and merely being committed to it are different epistemic states, and the difference is precisely what tells you where to cut when a commitment turns out to be wrong. A closed representation is a projection that discards provenance, and provenance is the input to revision. The paper's design choice follows directly: it works with un-closed sets and requires an inserted statement to be present explicitly, not merely entailed, while requiring a deleted statement to be absent explicitly rather than merely unprovable. The asymmetry in those two conditions looks fussy until you notice it is what keeps the two categories of fact distinguishable at all.

The general shape recurs wherever a system caches, denormalizes, or memoizes: the derived form is fine for reads and treacherous for writes. Merging a computed value into the same store as its inputs, with no marker of which is which, produces a store you can query and cannot correct. Configuration systems that flatten a layered override chain into one effective document, ORMs that write back computed columns, build systems that check generated files into the same tree as the sources, all hit the same wall the moment someone needs to change something: the edit has no unique home. The habit worth taking is to ask, of any representation, not only what it lets you ask but what it lets you revise, and to treat any place where those diverge as a sign that a distinction was flattened too early.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — the treatment of closed versus un-closed theories, including the small propositional example showing that the same insertion behaves reasonably in the un-closed setting and forces wholesale abandonment in the closed one, and the accompanying justification of the deliberately asymmetric insertion and deletion conditions.
