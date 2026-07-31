---
type: lesson
title: "Pick the structure whose weakness is exactly what buys the guarantee you need"
figure: scott
works: [data-types-as-lattices]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Pick the structure whose weakness is exactly what buys the guarantee you need

**Lesson:** When there is a standard, well-studied way to equip your objects with structure, the temptation is to take it because it is standard and then work around whatever it costs you. Scott does the opposite. The obvious structure on his domain is the familiar one, inherited by treating each object as a two-valued indicator and using the usual product notion of nearness; it is a good structure with famous properties. He rejects it, and the reason is not that it is wrong but that it is too strong in one specific place: it makes complementation a well-behaved operation. He wants instead a deliberately coarser notion, one that recognizes only accumulating positive evidence and never the absence of it, because under that weaker notion every well-behaved map is guaranteed to have a fixed point — and complementation, the one operation that provably cannot have one, is no longer well-behaved.

The reasoning generalizes into a design move worth naming. A universal guarantee — every X has a Y, every process terminates, every request eventually resolves — is never free; it is purchased by excluding the operations that would falsify it. So when you want such a guarantee, do not start from the richest available setting and hope. Start from the counterexample: find the single operation whose existence would refute the property you want, and then choose your notion of well-behavedness precisely so that operation falls outside it. Everything else that survives the cut comes with the guarantee attached, automatically, with no per-case argument. The cut looks like a loss of generality when you describe it and is actually where the theorem comes from.

Two further things make this cheap rather than painful. The first is that the excluded operation is usually one you did not need: an account of computation built on accumulating what is known has no business asserting what is not known, so losing complementation costs nothing you wanted. The second is that a weaker structure admits *more* well-behaved maps, not fewer — coarsening what counts as an observable distinction widens the class of things that respect it. The instinct that a restriction must shrink your working space is exactly backwards here, and it is worth checking which way it actually runs before accepting a stronger setting on the grounds that stronger must mean more.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — the opening of Section 1, where Scott sets aside the standard product topology on the powerset of the integers as a "positive-and-negative" one that makes complementation continuous, and argues for the weaker topology of positive information on the grounds that all continuous functions then possess fixed points, noting parenthetically that the equation asserting a set equals its own complement is impossible.
