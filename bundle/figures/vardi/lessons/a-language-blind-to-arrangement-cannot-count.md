---
type: lesson
title: "A language blind to arrangement cannot count, so hand it the arrangement deliberately"
figure: vardi
works: [the-complexity-of-relational-query-languages]
axes: [expressiveness, verifiability]
subdomains: [databases-and-data-management, foundations-of-computation]
tags: [lesson]
---
# A language blind to arrangement cannot count, so hand it the arrangement deliberately

**Lesson:** A declarative query language earns its independence from storage layout by refusing to let answers depend on the incidental order in which values happen to sit. That refusal is exactly what makes such a language safe to optimize and safe to reimplement, and it is also the source of a blind spot that has nothing to do with computational difficulty. Asking whether a set has an even number of elements is trivially cheap to compute — but the natural recursive query languages cannot express it, because any answer would have to enumerate the elements in some sequence, and sequence is precisely the structure the language cannot perceive. So the language's expressive power lands strictly inside a complexity class instead of matching it: there are trivially cheap questions it simply cannot phrase.

The repair is instructive because it is not a language change. If the data itself carries an ordering relation, the enumeration the language could not invent is now available as ordinary data, and a mild recursion construct becomes able to express every polynomial-time question exactly — power and cost coincide. The missing capability was never a missing operator; it was missing information. That reframing is the transferable move: when a restricted formalism cannot say something surprisingly simple, check whether the obstacle is a genuine limit on power or a piece of structure that the formalism deliberately declines to see and that you are free to supply as input.

The design lesson cuts both ways, which is why it deserves care rather than enthusiasm. Handing a layout-independent language an explicit ordering restores expressive power but reintroduces the dependence the abstraction was built to prevent: queries can now discriminate between arrangements that were meant to be interchangeable, and the freedom the implementation enjoyed to reorder, partition, and parallelize is partly given back. The right posture is to treat the ordering as a named, deliberately granted capability with a stated cost, not as a convenience quietly available everywhere — and to notice that many "the language can't do X" complaints are really requests to give up an invariant whose value is invisible until it is gone.

**Source:** [The Complexity of Relational Query Languages](../works/the-complexity-of-relational-query-languages.md) — the closing remarks of the logical-languages section, where the parity query is shown to be cheap yet inexpressible in the fixpoint language, and the exact capture of polynomial time is recovered only under the assumption that one of the database's relations is a linear order on the domain.
