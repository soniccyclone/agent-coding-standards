---
type: lesson
title: "Record a restriction the abstraction does not need if the implementation wants it, and make the user decide"
figure: jones
works: [systematic-software-development-using-vdm]
axes: [expressiveness, hardware-affinity, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Record a restriction the abstraction does not need if the implementation wants it, and make the user decide

**Lesson:** Describing behaviour in the cleanest available terms sometimes makes a restriction look gratuitous. Say a collection holds distinct items and adding one that is already there is harmless, so why demand that callers not do it? The answer is that the eventual implementation is not a mathematical collection, and the restriction may buy it something real — a check it can skip, a case it need not handle, a data structure that stays simpler. There is a genuine failure mode in becoming so absorbed in the clean description that the needs of whatever will implement it are ignored entirely. Purity of description is not the objective; the objective is a description that can be both understood and built.

But the restriction is not free, and this is what makes the case interesting rather than merely permissive. Every assumption granted to the implementer is an obligation imposed on the caller, and the caller may be unable or unwilling to meet it. So the decision is not the designer's to make quietly on efficiency grounds — it is a question to put to whoever will use the thing: are you willing to guarantee this, in exchange for what it buys? Writing the restriction down is what makes the question askable. An unwritten restriction is worse than either answer, because it will be relied on by the implementation and violated by the caller.

The general habit worth extracting is to treat assumptions as a negotiated part of an interface rather than as leftovers of a design. Each one has a beneficiary, a cost, and a party who must consent. When you notice yourself about to omit an assumption because the ideal description does not require it, ask whether some implementation would want it; when you notice yourself about to add one for convenience, ask who pays. Both questions have the same shape and both are answered by writing the assumption down where the people affected can see it.

**Source:** [Systematic Software Development Using VDM](../works/systematic-software-development-using-vdm.md) — the spell-checker specification in the set-notation chapter, where the word-adding operation carries a pre-condition excluding words already present, together with the accompanying observation that this pre-condition is not necessary at the set level of description but may be important for the implementation and is therefore worth recording, that it can be a mistake to become so involved in the abstraction that the needs of the implementation are entirely ignored, and that the crucial decision is whether the user accepts the limitation.
