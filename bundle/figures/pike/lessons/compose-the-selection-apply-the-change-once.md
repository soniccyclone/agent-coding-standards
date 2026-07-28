---
type: lesson
title: "Compose the selection, apply the change once"
figure: pike
works: [the-text-editor-sam]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Compose the selection, apply the change once

Pipelines compose transformations: each stage receives what the previous stage produced,
so stage three is reasoning about data that no longer exists anywhere on disk. That is
powerful and it is also why long pipelines are hard to debug — a mistake in stage two
changes the meaning of everything downstream, and the only way to find it is to
reconstruct intermediate states in your head. The alternative Pike builds composes
something else entirely: each stage narrows *which part* of the unchanged subject is
under consideration, and only the final stage modifies anything.

The consequences run deeper than convenience. Because the subject never moves while the
chain is being evaluated, a stage's meaning is independent of its position in the chain's
history; you can add a qualifier in the middle and the stages after it still mean what
they meant. Refinement becomes genuinely incremental — write the crude version, watch
what it selects, bolt on another clause to exclude the cases it got wrong — and each
addition is a local edit rather than a re-derivation. The expressive gain (arbitrary
composition depth) and the verifiability gain (each clause independently checkable) come
from the same restraint: nothing writes until the end.

The habit this teaches is to look for the mutation buried in the middle of a composition
and hoist it out. Query, filter, and refine over immutable input; collect the target set;
then commit. Systems built the other way — where every stage both narrows and modifies —
force you to reason about an evolving subject and a moving cursor simultaneously, and
they make "why did this match?" unanswerable after the fact. Deferring the write is what
buys you the ability to inspect the decision before it has consequences.

**Source:** [The Text Editor sam](../works/the-text-editor-sam.md) — the discussion of
chained extract/select/reject commands and the explicit contrast drawn with shell
pipelines, where the observation is that these chains pass along a view rather than
modified data.
