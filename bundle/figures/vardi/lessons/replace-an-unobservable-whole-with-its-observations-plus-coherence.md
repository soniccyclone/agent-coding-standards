---
type: lesson
title: "A whole you only ever observe through a few narrow windows can be replaced by the windows, plus the coherence you just gave up"
figure: vardi
works: [on-the-complexity-of-bounded-variable-queries]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# A whole you only ever observe through a few narrow windows can be replaced by the windows, plus the coherence you just gave up

**Lesson:** A restriction can be leaky in a way that looks fatal and isn't. Capping how many names a formula uses bounds the width of everything built out of those names — but it does not bound the width of an object the formula merely *mentions*. So a formalism that lets you posit an auxiliary structure can still demand something astronomically large, even under a restriction designed to keep everything small. The move that rescues it is to notice that the large structure is never inspected as a whole. Every mention of it happens through the bounded supply of names, in some fixed pattern of repeated positions, and there are only as many such patterns as there are mentions in the text — a small, countable, statically visible number.

Once that is seen, the large object can be dissolved into exactly the narrow projections that get looked at. Nothing that ever mattered about it is lost, because nothing else was ever queried. This is the general principle behind materializing views instead of tables, storing derived indices instead of the join they came from, and passing a handful of extracted fields instead of a whole aggregate: the size of a thing is not the cost, the size of the part you actually touch is the cost, and the touched part is usually determined by the source text rather than by the data.

The half of the technique people skip is the invoice. A single object gives you consistency for free — two different ways of looking at it cannot disagree, because there is only one of it. Shatter it into independent projections and that guarantee evaporates; overlapping projections can now be assigned contradictory contents. So the replacement is only sound once you write down, explicitly, every agreement the original identity used to enforce. Vardi does exactly this, adding a quadratic pile of assertions tying the projections together, and the total stays polynomial. Treat that as the reusable discipline: when you decompose an aggregate into the slices your code touches, the invariants that held automatically become invariants you now own, and if you cannot enumerate them the decomposition is not yet correct.

**Source:** [On the Complexity of Bounded-Variable Queries](../works/on-the-complexity-of-bounded-variable-queries.md) — the existential-second-order section, where the bound on individual variables fails to bound the arity of the existentially quantified relations, and the lemma replacing each quantified relation by one bounded-arity predicate per equality pattern of its atomic occurrences, together with the mutual-consistency assertions needed to make the substitution faithful.
