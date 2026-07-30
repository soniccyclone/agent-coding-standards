---
type: lesson
title: "Rank your invariants explicitly, or automatic repair will sacrifice whichever one is cheapest to drop"
figure: vardi
works: [on-the-semantics-of-updates-in-databases]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Rank your invariants explicitly, or automatic repair will sacrifice whichever one is cheapest to drop

**Lesson:** A repair procedure that treats everything it stores as equally negotiable will, given a conflict, produce technically minimal and practically insane results — dropping a rule in order to admit a datum, because dropping one rule is a smaller change than rewriting many rows. The failure is not in the minimality criterion; it is that minimality was measured over a flat collection, and the collection was never flat in reality. Rules governing what may be true, facts a clerk edits daily, and derived summaries occupy completely different positions in a system's authority structure, and a formalism in which they are all just entries has thrown that structure away before the first repair is attempted.

The fix is to make standing an explicit, first-class annotation and to compare candidate outcomes level by level, from the most authoritative downward, only breaking ties at a lower level once the higher ones are equal. That is all it takes for repair to behave the way a competent operator would: sacrifice the most incidental thing that resolves the conflict, and never trade away a rule to accommodate a fact. What makes this worth generalizing is that it converts an argument about what the system should have done into a value the designer writes down once and can be held to. Anything that is going to be automatically resolved — merge strategies, constraint repair, cache invalidation, conflicting configuration layers, schema migration under load — needs this ranking to exist somewhere; the choice is only between stating it and having it emerge accidentally from implementation order.

There is a second dividend that is easy to miss and characteristic of a well-chosen mechanism. Once standing is explicit, permission becomes expressible in the same terms: a given actor may disturb only the levels below some threshold, and the integrity rules sit above every ordinary user's reach. Two concerns that would otherwise need separate machinery — which invariant yields under pressure, and who is allowed to touch what — turn out to be the same ordering read from opposite ends. When one abstraction absorbs a second concern that cleanly, it is usually a sign that you found the real structure rather than a convenient encoding.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — section three, which observes that under the flat framework an update violating a constraint can be satisfied by discarding the constraint, introduces tagged sentences with integrity constraints carrying the highest priority, defines smaller-change comparison as a level-by-level test proceeding from the highest priority downward, and remarks that the same tags supply an authorization mechanism by capping which levels a given user may alter.
