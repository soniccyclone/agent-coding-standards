---
type: lesson
title: "A feature's real meaning is whatever the optimizer is permitted to assume about it, not what its syntax suggests"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# A feature's real meaning is whatever the optimizer is permitted to assume about it, not what its syntax suggests

**Lesson:** When a language provides a structured mechanism for coordination and also leaves an unstructured back door open, the back door is usually judged by how easy it is to misuse. That is the wrong measure and it flatters the feature. The right question is what the translator is licensed to assume while compiling code that uses it. If updates through the back door may be deferred, reordered, or merged exactly as though nothing were shared, then the feature does not have a weak guarantee — it has no guarantee, and the text you wrote is not a description of what will happen. No amount of care at the call site recovers anything, because the discipline you are exercising is over a program that the toolchain is entitled to replace with a different one.

The general principle is that a construct's semantics is the conjunction of what it promises and what everything downstream is allowed to presume about it, and the second half is where the meaning actually lives. Programmers read syntax and infer intent; compilers, schedulers, caches and reordering hardware read the permission granted by the specification. Where those diverge, the permission wins every time, and the divergence is invisible in testing because a translator that does not yet exploit its licence produces exactly the behaviour you expected. This is why "it works today" carries so little information about shared-state code: you are not observing the semantics, you are observing one legal implementation of an under-constrained one.

Two things follow for design work. When you are writing a specification, notice that every optimization freedom you grant is subtracted from the meaning of the corresponding feature, so the freedoms and the guarantees have to be drafted together — a permission added late to help implementers silently voids user code that was correct against the earlier reading. And when you are choosing between mechanisms, prefer the one whose guarantees survive aggressive translation, even at some cost in convenience, over the one that reads more naturally and depends on the toolchain declining to do what it is allowed to do. A mechanism whose correctness rests on unexploited licence is on a timer that runs out at the next compiler release.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the Ada subsection of the discussion chapter, in the list of additional facilities: the note that tasks may access and update shared variables, and that the effect is made even more unpredictable by compilers being permitted to delay, reorder or amalgamate such updating exactly as if the variable were not shared, set against the surrounding assessment that the structured tasking features are otherwise well designed for a shared-storage multiprocessor.
