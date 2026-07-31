---
type: lesson
title: "Finish every test before the first mutation, and failure needs no undo"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Finish every test before the first mutation, and failure needs no undo

**Lesson:** An operation that can fail part-way through leaves the structure it was modifying in a state nobody described. The customary answers are to write a recovery path that reverses what was done, or to journal enough to reconstruct the original. Both are real techniques and both are expensive, and a large fraction of the time neither is necessary, because the failure conditions were all knowable before anything was touched. The reason they were not checked first is usually only that the checks were written where they were discovered — interleaved with the work, each one guarding the step it happened to precede — rather than gathered.

Restructuring an operation into a phase that decides and a phase that acts is therefore worth attempting before reaching for recovery machinery. The first phase computes everything the second will need and answers one question: can this complete. It writes nothing. The second phase runs only if the answer was yes, and by construction contains no branch that can abandon the work. What you get is an operation with exactly two outcomes — fully done, or nothing happened — obtained without any code that reverses anything, and a failure path that consists of returning. The cost is that resources must be located and reserved conceptually before use, and that some work is done twice when the operation proceeds; both are usually cheap next to a correct undo.

Two conditions decide whether the split is available. Everything the second phase depends on must be determinable in the first, which is a genuine design constraint and sometimes forces a representation change — locating a free slot and enough contiguous space before writing either, rather than discovering a shortage half-way. And nothing may invalidate a decision between the phases, which is trivially true in a system that runs an operation to completion and needs a stated exclusion argument in one that does not. When both hold, prefer this to recovery; when they do not, the failure is genuinely mid-flight and you must pay for undo. Knowing which situation you are in is the point — a great deal of recovery code exists only because nobody asked whether the checks could have been hoisted.

**Source:** [Project Oberon](../works/project-oberon.md) — section 11.2's statement that insertion into a mailbox begins only if all conditions for a successful completion are satisfied, following the search for a free directory slot and the search for a sufficient number of adjacent free blocks, with the alternative routes taken when either search fails described before any writing occurs, and the writing itself then proceeding as an uninterrupted sequence: marking the blocks in the reservation table, inserting the new directory information, updating table and directory on the file, and finally writing the message with its constructed header into the message part.
