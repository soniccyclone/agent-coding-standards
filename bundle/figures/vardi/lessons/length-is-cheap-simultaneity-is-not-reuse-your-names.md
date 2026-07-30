---
type: lesson
title: "Length is cheap, simultaneity is not: reuse names to keep the working set narrow"
figure: vardi
works: [on-the-complexity-of-bounded-variable-queries]
axes: [hardware-affinity, cognitive-load, expressiveness]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# Length is cheap, simultaneity is not: reuse names to keep the working set narrow

**Lesson:** The naive way to describe a chain of n steps introduces a name for every intermediate point, so the description's breadth grows with its length. The same chain can be described with a small fixed set of names, reused: introduce a fresh point, rebind one of your existing names to it, and recurse. The description gets longer with n, but the number of things that must be held simultaneously does not. Since the cost of evaluation is driven by what is live at once rather than by how much text there is, this is not a stylistic preference — it is the difference between a temporary of bounded width and one whose width grows without limit.

The generalizable idea is that a program has two independent sizes. One is how much of it there is; the other is how much of it is in play at any moment. Register pressure, join width, the number of open contexts a reader must track — all are the second quantity, and it is usually the one that determines whether something is affordable. Because the two sizes look alike on the page, the second is easy to miss, and a description that grew wide when it only needed to grow long can look like an inherent cost of the problem rather than an artifact of how it was written.

So the technique to internalize is scope arithmetic: after naming something, ask when it stops being needed, and whether the next step could reuse that slot instead of demanding a new one. Deliberate rebinding is the counterintuitive part, since fresh names for everything is the habit that avoids confusion elsewhere. But a formalism (or a codebase) where names are recycled at the point their content dies has a bounded working set by construction, and bounded working sets are what make both machine evaluation and human reading tractable at scale.

**Source:** [On the Complexity of Bounded-Variable Queries](../works/on-the-complexity-of-bounded-variable-queries.md) — the section defining bounded-variable languages, which contrasts the naive path-of-length-n formula requiring n+1 variables against the equivalent formulation that reuses three by re-binding a variable inside a nested quantifier, and notes the correspondence to relational-algebra expressions whose every subexpression has bounded arity.
