---
type: lesson
title: "Define an unbounded facility as the limit of bounded ones, so no run needs semantics the bounded language lacks"
figure: hoare
works: [communicating-sequential-processes-paper]
axes: [verifiability, hardware-affinity, expressiveness]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Define an unbounded facility as the limit of bounded ones, so no run needs semantics the bounded language lacks

**Lesson:** Fixed capacities are annoying and everyone wants to remove them: declare a collection of workers without stating how many, let the count be discovered at run time, stop wasting the slots nobody used. The mistake is to treat "make it unbounded" as loosening a restriction, because it usually smuggles in a new semantic obligation. If the size can grow while the system runs, then questions the bounded version never had to answer — what state a newly created participant starts in, who is allowed to name it, what happens to a name that referred to something not yet created, whether a computation can make progress only by growing forever — arrive all at once and get answered by implementation accident rather than by definition.

The discipline that keeps the removal honest is a constraint on the meaning, not on the implementation: require that every actual execution of the unbounded program be indistinguishable from an execution of some bounded program whose limits were all fixed in advance. The unbounded construct is then defined as the limit of that family of bounded programs rather than as a new thing in its own right. This has three consequences worth having. Every property proved for the bounded family transfers, since any run you can observe is a run of a member. Nothing can be expressed that depends on actual infinity — a program whose behavior only makes sense with no ceiling at all is rejected by the criterion, which is exactly the class of programs you want rejected. And the implementation is free to allocate dynamically, since it is only obliged to match a bounded run, not to distinguish itself from one.

Generalized: when adding a dynamic version of a static feature, do not ask what the dynamic version means from scratch; ask which static family it is the limit of, and take the requirement that all its runs live inside that family as the definition. When you cannot name the family, the feature is not a relaxation of the existing one, it is a second feature wearing the first one's name, and it needs its own semantics and its own proofs. There is also a reason to spend your effort on the bounded case first even when you intend both: the bounded case is needed regardless, it is the one that maps onto machines with finite resources, and getting it exactly right is what makes the limit well defined at all.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-paper.md) — the discussion of unbounded process activation, which proposes as a good principle that any run of a program with unbounded process arrays should be identical to a run of some program with all arrays bounded in advance, and concentrates the semantics on the bounded case as the one that is necessary anyway and realistic for multiple-microprocessor implementation.
