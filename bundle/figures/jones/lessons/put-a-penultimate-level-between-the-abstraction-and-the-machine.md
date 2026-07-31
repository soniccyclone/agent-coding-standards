---
type: lesson
title: "Put a penultimate level between the abstraction and the machine: target shape, reasoning notation"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Put a penultimate level between the abstraction and the machine: target shape, reasoning notation

**Lesson:** The last stretch of a design — from structures chosen for clarity down to whatever the implementation language actually offers — is the one where two hard things happen at once. The overall layout gets decided: what is one contiguous block and what is separately allocated, what is an index and what is a pointer, what is duplicated for access speed. And simultaneously the description drops out of a notation you can argue in and into one you cannot. Doing both in a single move means the layout decisions, which are the substantive ones, get made and checked in the least suitable medium available.

Split it, and split it asymmetrically. Introduce one more level whose *shape* is the target's — the same partitioning into blocks, the same indexing scheme, the same decision about which things are held indirectly — but which is still written in whatever descriptive vocabulary you have been reasoning in: collections, keyed lookups, sequences. This is the level where the layout is justified, because at this level a correspondence back up to the abstraction can be written down and its adequacy checked, and where a constraint the layout must respect can be stated as a condition on the described structure rather than as a comment. The step from there to real declarations is then genuinely mechanical, and being mechanical it does not need much argument.

The trick that makes this pay is deliberately choosing the penultimate structures with the final transition in view. The temptation is to pick whatever is most elegant to reason about and hope the mapping down is easy; that produces a level that is pleasant and then a final step that is large and unchecked. Pick instead the least abstract description that you can still reason in comfortably — one that is already committed to the shape you intend — and accept that it will look uglier than the level above. It should look uglier. Its ugliness is the layout decision becoming visible while you can still inspect it, rather than at the point where it stops being inspectable.

There is a companion move at the very bottom. If the final text can be arranged so that it reads like the level above it, with the representation detail confined to whatever naming or expansion mechanism the language gives you, then the last correspondence is checkable by looking at the two side by side. That is not a proof, but it is the difference between a final step anyone can review and a final step only its author understands.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 18's fourth development step for Earley's recognizer, which having removed the recursion turns to refining the data types and states that the overall structure of the program's data is shown at this stage still in terms of abstract objects like mappings because that makes them easy to reason about, and that the step to PL/I data types is straightforward precisely because the objects at this stage were chosen with the subsequent transition in mind; the accompanying retrieve functions relating the flattened rule vector, symbol tables and pointer-based storage back to the abstract grammar, together with the data type invariants constraining the representation and the remark that adequacy can be verified for each; and the "Program" section, where the final code uses macros so that the macro program looks very like the algorithm of the third step, with representation details hidden inside them.
