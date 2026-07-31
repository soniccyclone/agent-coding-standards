---
type: lesson
title: "When a requirement is impossible over everything, shrink everything"
figure: strachey
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# When a requirement is impossible over everything, shrink everything

Insist that procedures be ordinary values — storable, passable, returnable, on the same footing as a number — and you have insisted that the space of values contain the space of functions from values to values. Scott and Strachey follow that through and hit a wall that is not a matter of difficulty or taste: over arbitrary functions the requirement is flatly contradictory, because the function space is unavoidably larger than what it would have to sit inside. Two responses are available. One is to conclude that procedures cannot really be values and to accept the second-class treatment most languages of the period gave them. The other is to notice that the impossibility was proved about *all* functions, and that nobody asked for all functions.

They take the second, and the shape of the move is what generalises. Keep the requirement, restrict the universe until the requirement becomes satisfiable, then check two things. First, that the restricted class still contains everything the application needs — here the argument is that computation never asks for the functions being excluded, so nothing of value is lost. Second, and this is the part usually skipped, that every operation in the system respects the restriction. It is not enough that the value space correspond to its function space; the correspondence itself has to be of the admitted kind, and so does every operator built on top, or the contradiction returns the first time two pieces are composed. A restriction that is not closed under the operations you intend to perform is not a fix, it is a postponement.

The same paper makes the identical move earlier and more quietly. A self-referential command has no meaning among total functions — a straightforward construction shows the equation has no solution — so totality goes, and the class of admitted functions narrows again. Recurring twice in one paper is a hint that this is not a trick but a method: when a system's own requirements imply a contradiction, the negotiable thing is usually the ambient universe you assumed without thinking about it, not the requirement you actually care about.

The habit is to treat an impossibility proof as information about scope rather than as a verdict. Something you want cannot be done for all inputs, all schedules, all types, all graphs, all messages — so ask which subclass makes it possible, whether that subclass covers the real cases, and whether it is preserved by everything you plan to do. The failure mode on the other side deserves naming too: a restriction adopted because it made the argument go through, never checked for closure or coverage, which later shows up as a rule that mysteriously cannot be composed with anything.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the section on procedures, where the value space required for first-class procedures is shown to be unconstructible by a cardinality argument, resolved by admitting only continuous functions and by requiring the resulting correspondence to be continuous as well; together with the earlier recursion section, where a self-referential command's equation is shown to have no solution among total functions.
