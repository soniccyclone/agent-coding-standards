---
type: lesson
title: "Find the independent axes of your plumbing and every rearrangement acquires a canonical form"
figure: curry
works: [grundlagen-der-kombinatorischen-logik]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Find the independent axes of your plumbing and every rearrangement acquires a canonical form

**Lesson:** The work of routing arguments to the places that consume them looks like an open-ended zoo of special cases: renumber the slots, drop one, repeat one, nest one call inside another, permute two. Curry's structural discovery is that this zoo has exactly four independent dimensions — deferring an argument past a nested application, exchanging two, using one twice, and discarding one — and that a fixed operator for each is enough to build every routing there is. That is already the interesting claim, but the sharper one comes later: not only does every rearrangement decompose into these four kinds, it decomposes in a canonical order, as discards, then duplications, then permutations, then groupings, and each of those blocks is itself uniquely determined. Two operators built any which way from the basis can be brought to this shape and compared componentwise.

Why it holds is worth sitting with, because the proof is where the design content is. Each axis is separated by a small commutation law saying how an operator of one kind slides past an operator of another kind — sometimes emerging unchanged with shifted indices, sometimes merging with its neighbour, sometimes collapsing to nothing. Given enough such laws you can push every discard leftward, every duplication next, and so on, exactly as one sorts a word in a group by relations between generators. The normal form is not stipulated; it falls out of knowing how the dimensions interact. And its payoff is decisive: uniqueness of the decomposition converts the question "do these two pieces of plumbing do the same thing" from an open search into a finite comparison.

Note also the shape of the reduction Curry chose. He does not take the smallest possible basis — he records that two operators suffice and that his four are definable from them, and declines, because with the smaller basis the elementary properties of equality become harder to establish and one of them has to be assumed outright. Fewest primitives and easiest reasoning are different objectives, and he optimizes for the second.

A programmer who thinks this way, on meeting a family of adapters, glue functions, argument-shuffling wrappers or pipeline stages, does not start cataloguing them. They look for the small set of orthogonal capabilities the family is secretly built from, then look for the rewriting laws between those capabilities, and then get a canonical form for free — which is what makes deduplication, equality checking, and optimization tractable instead of heuristic. And when someone proposes a smaller basis, they ask what it costs at the level where proofs and error messages live, rather than accepting the smaller number as self-evidently better.

**Source:** [Grundlagen der kombinatorischen Logik](../works/grundlagen-der-kombinatorischen-logik.md) — Chapter II's treatment of representation, where sequences of argument positions are decomposed into groupings, omissions, repetitions and permutations, each matched to its own family of operators, and the resulting four-block normal form is shown to exist and to be uniquely determined; the remark comparing his basis with the two-operator alternative closes Chapter I.
