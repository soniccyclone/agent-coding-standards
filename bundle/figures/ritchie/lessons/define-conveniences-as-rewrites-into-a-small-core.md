---
type: lesson
title: "Define conveniences as exact rewrites into a small core, so growing the syntax does not grow the semantics"
figure: ritchie
works: [c-reference-manual]
axes: [primitive-count, cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Define conveniences as exact rewrites into a small core, so growing the syntax does not grow the semantics

A specification has two sizes, and they are independent. One is how many forms a user can write; the other is how many distinct behaviors the implementer and the reasoner must hold in their heads. The C manual keeps these apart with a discipline it applies over and over: a comfortable surface form is introduced not by describing what it does, but by stating the shorter expression it is identical to. Indexing is not given its own meaning at all — it is declared to be pointer arithmetic followed by indirection. Arrow selection is defined as indirection followed by dot selection. The counted loop is presented as a mechanical expansion into the conditional loop plus two extra statements. The loop-continuation statement is explained by exhibiting the jump it stands for. The compound assignments get one paragraph covering all eleven of them, by rewriting the whole family into ordinary assignment.

The reason this matters is that a behavior described in prose is a behavior that can drift from every other behavior described in prose. Two independently written descriptions of subscripting and of pointer arithmetic will eventually disagree at an edge — negative indices, multidimensional cases, what happens when the base is not an array — and nobody can tell which one is authoritative. A reduction cannot disagree with the thing it reduces to. It also cannot be forgotten during implementation, because the compiler front end can literally perform the rewrite and let the existing back end handle it. Every consequence of the core, including ones the author never thought about, propagates to the surface form for free: the manual can casually observe that subscripting therefore commutes, which is not a fact anyone designed, only a fact that follows.

The rewrites are honest about their cost too, which is part of the technique rather than an exception to it. Where the reduction is not exactly faithful, the manual says so at that spot — the compound assignment forms evaluate their left side only once, unlike the expansion; the arrow form relaxes the type requirement its equivalent imposes. Those two sentences are the entire price. Compare that to defining eleven operators from scratch and hoping the definitions stay consistent with assignment as assignment evolves.

A programmer who works this way separates the question "what may be written?" from the question "what does it mean?" and answers the second one as few times as possible. New affordances arrive as sugar with a stated desugaring, not as new nodes in the semantics. Reviews get sharper, because a proposal now has to exhibit its reduction, and a construct that cannot be reduced is visibly a request to enlarge the core — which is a much bigger conversation than adding notation. And the test surface shrinks: verify the core hard, verify the rewrites are the rewrites they claim, and the surface is covered.

**Source:** [C Reference Manual](../works/c-reference-manual.md) — the expressions chapter, where subscripting, member selection through pointers, and the assignment-operator family are each specified as equivalences to simpler forms, together with the statements chapter's treatment of the counted loop and the loop-continuation statement as expansions.
