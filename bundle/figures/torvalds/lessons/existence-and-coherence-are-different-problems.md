---
type: lesson
title: "Existence and coherence are different problems: count references to keep a thing alive, take locks to keep it consistent"
figure: torvalds
works: [linux-kernel-coding-style]
axes: [parallelizability, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Existence and coherence are different problems: count references to keep a thing alive, take locks to keep it consistent

**Lesson:** Shared mutable state raises two questions that beginners collapse into one. The first is whether the object still exists — whether the memory you hold a pointer to is still the thing you think it is. The second is whether the object's fields are currently in a consistent state, or mid-update by somebody else. The style guide insists these are answered by different mechanisms and that substituting one for the other is a category error: a count of interested parties governs lifetime, mutual exclusion governs consistency, and most shared objects need both because both questions are live. The reason the confusion is so common is that a held lock incidentally prevents destruction, so lock-based code appears to solve lifetime too — right up to the moment a holder needs to sleep, block, or hand the object to someone else, at which point the lock is released and the incidental protection vanishes.

The payoff of separating them is concurrency. Once existence is guaranteed by a count rather than by exclusion, several parties can hold the same object simultaneously without coordinating, and any of them may sleep, wait on a device, or wander off into unrelated work without the object dissolving underneath them. Exclusion is then needed only around the actual mutations, which are usually a small fraction of the time an object is held. Conflating the two forces you to hold a lock for the entire duration of interest, which serializes readers who never needed to be serialized and makes any blocking operation while holding it either forbidden or a deadlock.

The document also supplies a decidable test, which is what makes the principle usable rather than merely true: if another execution context is able to find your object at all, and there is no count recording that fact, you have a bug — not a risk, a bug. That is a static property of the code, checkable by asking how the object becomes reachable, and it does not depend on reasoning about interleavings or on failing to observe a race in testing. The refinement mentioned for multi-class users, where a subordinate count collapses into the global one only when it reaches zero, follows the same logic one level up: distinct kinds of interest get distinct accounting rather than being flattened together.

A programmer who believes this asks, for every shared object, two separate questions with two separate answers: who guarantees this is still here, and who guarantees it is not half-updated. They stop reaching for a bigger lock when the symptom is a use-after-free, because a bigger lock is the wrong instrument, and they audit reachability rather than trying to reproduce timing.

**Source:** [Linux Kernel Coding Style](../works/linux-kernel-coding-style.md) — the data structures chapter, which separates reference counting as memory management from locking as coherence, notes that counting is what permits parallel holders across sleeps, sketches multi-level counts for users of different classes, and states the reachability-without-a-count test as an outright bug.
