---
type: lesson
title: "Build in the convenient form, export in the canonical one"
figure: post
works: [formal-reductions-of-the-general-combinatorial-decision-problem]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Build in the convenient form, export in the canonical one

Post draws a distinction most people collapse: the notation you construct in and the notation your result is stated in do not have to be the same notation, and there is real leverage in keeping them apart. His permissive rule format is comfortable for definition by induction — you can write down a system that generates what you want without contorting anything. His austere rule format is uncomfortable to write in but is a single fixed shape, so anything expressed in it can be dropped into another construction as raw material. Because he has proved the two describe the same collection of generated sets, he gets to use one as a working language and the other as an interchange format, alternating freely.

That is the whole argument for a canonical form, and it is not an aesthetic argument. A construction is easy to write when the notation matches how you think about the thing being built. A construction is easy to *consume* when its output has exactly one shape, so the consumer needs no case analysis. Those are different requirements, and trying to satisfy both with one notation gives you something mediocre at each. Two notations plus a proved translation gives you both, at the cost of the translation.

The engineering pattern this licenses is everywhere once you see it: an ergonomic surface syntax that lowers to a normalized core; a rich builder API whose output is a flat serialized record; a query language with sugar that desugars to a small relational kernel. What Post insists on, and what teams routinely skip, is the equipotence proof. Without it you have not got two views of one thing, you have got two things that mostly agree, and the disagreements surface as bugs in whichever direction is less travelled. The translation being total and faithful is the load-bearing part; the notations are the easy part.

A programmer who holds this distinction stops asking "what is the right notation for this domain" and starts asking two separate questions — what do authors need to write comfortably, and what do downstream tools need to receive uniformly — then builds the bridge between the answers deliberately. The bridge is also where you put the checking: if the only path from surface to core is the translator, every downstream consumer inherits whatever invariants the translator guarantees, for free.

**Source:** [Formal Reductions of the General Combinatorial Decision Problem](../works/formal-reductions-of-the-general-combinatorial-decision-problem.md) — the introduction's corollary that the two classes of generated sets coincide, and Post's remark on alternating between the two formalisms, using the permissive one as the way to construct and the austere one as the way to name what was constructed.
