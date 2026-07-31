---
type: lesson
title: "Split on the domain before you split into steps, or partiality gets patched into whichever step discovers it"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Split on the domain before you split into steps, or partiality gets patched into whichever step discovers it

**Lesson:** The first decomposition that comes to mind for a unit of work is nearly always a pipeline: obtain the input, compute the result, deliver it. It is a good shape and it is wrong whenever the middle stage is undefined on some of the inputs, because it has already committed to there being a result to compute and a result to deliver. The defect is not that error handling is missing; it is that the structure has no place to put it. Whatever gets added later will be added inside a stage, as an early exit or a distinguished return, and every stage downstream inherits a special value it now has to be careful about.

The correct move is to split on the domain first and pipeline second. Obtain the input, decide which case you are in, and give each case its own complete treatment. That looks like duplication and mostly is not: the cases usually differ in nearly everything they do, and where they genuinely share a step, the shared step gets factored out afterwards with a precondition that is now known to hold. What you gain is that no stage anywhere is written against a value that might not be a real result, so no stage has to defend against one — the check happened once, before anything was computed, and each branch's code operates on a domain it was written for.

The way to catch this at design time is to interrogate the first decomposition for totality before elaborating it. For each stage, ask on which inputs it is defined, and if the honest answer is "not all of them", the split you have written is at the wrong level and the domain distinction needs to move above it. Doing this early is very cheap; doing it late means restructuring a decomposition that things have already been built against, which is why the pipeline with a special value threaded through it is so common in code that nobody chose to write that way.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Appendix C.3's development of a factorial test program, which first considers refining the per-case work into reading input, computing the factorial, and writing output, rejects that shape on the grounds that it neglects the possibility that the factorial is undefined for the value read, and replaces it with a refinement that reads the value and then branches on validity, with separate treatments for the invalid and valid cases, the latter alone expanding into the compute-and-print sequence.
