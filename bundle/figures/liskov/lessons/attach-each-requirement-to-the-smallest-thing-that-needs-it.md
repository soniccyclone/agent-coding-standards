---
type: lesson
title: "Attach each requirement to the smallest thing that actually needs it"
figure: liskov
works: [clu-reference-manual]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Attach each requirement to the smallest thing that actually needs it

**Lesson:** Generic code has to state what it assumes about the things it is given, and the lazy way to state it is at the top: this whole component requires its parameter to support comparison, equality, duplication, ordering — whatever any part of it might use. That is easy to write and needlessly exclusionary, because most callers only ever touch the parts that need none of it. The stricter and more useful discipline is to attach each requirement at the exact granularity where it is used: the container itself demands nothing of its element type, and only the specific operation that compares elements demands that elements be comparable.

The consequence is that the generic thing exists for every possible argument while some of its operations exist only for some arguments. A collection of anything at all is legal; a collection whose contents can be compared is available exactly when the contents can be compared. Nobody is turned away at the door for a capability they were never going to invoke. This is a real gain in reach, and it costs only the discipline of writing the requirement next to its use rather than in one convenient list.

The requirement also has to cut in both directions to be worth anything. Declaring what the argument must supply simultaneously declares the only things the generic code is permitted to use — it may not quietly reach for some other capability the argument happens to have. Without that second half, the declaration is documentation rather than a contract, and drifts immediately: the code grows a new assumption, the declaration does not, and callers discover the mismatch at runtime. Stating the requirement as capabilities the argument must have, rather than as an identity the argument must be, is what keeps this checkable in advance while leaving callers free to satisfy it however they like.

A programmer who believes this looks at every "this component requires..." and asks which specific entry point actually requires it, then pushes the requirement down to that entry point. They also treat a declared requirement as a ceiling on their own code, not just a floor for their callers, and expect the tooling to enforce both directions — otherwise the requirement is a comment.

**Source:** [CLU Reference Manual](../works/clu-reference-manual.md) — the parameterized-modules section, whose where clauses state required operations per module and per routine, restrict the module to using only those operations, and yield the case where a container type exists for every element type while a particular operation of it exists only for element types supplying the needed operation.
