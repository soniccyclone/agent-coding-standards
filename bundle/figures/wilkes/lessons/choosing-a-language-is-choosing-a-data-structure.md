---
type: lesson
title: "Choose the representation the problem needs first, and treat a notation as a commitment to a representation"
figure: wilkes
works: [computers-then-and-now]
axes: [expressiveness, primitive-count, hardware-affinity]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Choose the representation the problem needs first, and treat a notation as a commitment to a representation

**Lesson:** Debates about notation usually proceed as if the choice of language were separable from the choice of how data is held, but it rarely is: adopting a language means adopting its representations, and if those do not fit the material you are working on there is no amount of good syntax that recovers the loss. The logically prior question is therefore which representation the problem actually demands, with the notation for manipulating it chosen or assembled afterwards. Reversing the usual order matters most exactly when it is hardest to do, because a language whose representations are unalterable is at its most attractive precisely when you have not yet worked out what shape your data has.

This also gives a sharper meaning to the level of a language than distance from the machine does. Take the distinguishing property to be how much latitude the programmer has over representation: a language that fixes it is high-level in this sense, and one that leaves it open is low-level. Defined that way, the choice between levels becomes an actual engineering decision rather than a statement of sophistication, and it becomes unsurprising that some kinds of work should move toward more latitude rather than less — a direction that looks like regression under the distance-from-hardware reading and looks like fitting the tool to the problem under this one.

The strongest consequence is about unification. When repeated attempts to build one preferred notation covering two kinds of work keep disappointing, the reason may not be insufficient design effort — it may be that the two kinds of work require different representations for efficient realization, and that no notation can be neutral about representation. If so, the divergence is fundamental and the right response is to stop trying to span it, because the all-purpose tool cannot exist. Recognizing which unifications are impossible is worth more than another attempt at one, and the test for impossibility is a conflict in representation rather than a conflict in surface form.

**Source:** [Computers Then and Now](../works/computers-then-and-now.md) — the higher-syntax section's argument that choosing a programming language is equivalent to choosing a data structure, its redefinition of high- and low-level in terms of whether representation is fixed or open, and the closing argument that the differing representational needs of arithmetic and symbol manipulation make the omnibus language a quest worth abandoning.
