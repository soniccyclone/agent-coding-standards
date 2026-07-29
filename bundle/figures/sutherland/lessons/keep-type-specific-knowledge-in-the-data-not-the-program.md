---
type: lesson
title: "Keep type-specific knowledge in the data, and the programs stay general"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-thesis]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Keep type-specific knowledge in the data, and the programs stay general

There are two places a system can record what makes one kind of thing differ
from another: inside the procedures that manipulate things, or inside the
things themselves. Choosing the first means every procedure grows a decision
tree over the catalogue of types, and the catalogue becomes closed — adding a
kind of thing means editing every procedure that might encounter it. Choosing
the second means each kind of thing carries a small record naming the routines
that know how to draw it, size it, transform it, or measure its failure, and
the procedures above become type-blind: they walk structure, dispatch through
whatever the record names, and never learn the catalogue at all.

The reason this is worth more than it first looks is asymmetric growth. A
type-blind layer is written once and then paid for forever by every type added
afterwards, including types nobody had thought of when it was written. Sketchpad
converged on this only after the alternative was tried and hurt: with dispatch
buried in the code, extending the vocabulary of relations was close to
impossible; once the per-type knowledge had been lifted out into descriptor
records and the general routines knew nothing but "ask the record," new
relation types could be added in the time it takes to write one small
error-measuring routine. Sutherland reports adding them in minutes, in
batches, which is the signature of the change having been structural rather
than a matter of effort.

A programmer who believes this stops asking "where do I add the case for X"
and starts asking "why is there a place where cases are listed at all." The
practical discipline is to look for the switch — the enumeration of kinds — and
push the knowledge it encodes down into the values being switched on, leaving
behind a single generic path. It also makes a useful test of whether an
abstraction is real: if adding a new variant requires touching the general
machinery, the general machinery is not yet general, it is merely shared.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (PhD Thesis)](../works/sketchpad-a-man-machine-graphical-communication-system-thesis.md) — the discussion of generic blocks and the deliberate split between routines that apply to any drawing part and routines specific to one kind, in the chapter on the ring storage structure and again in the chapter on general recursive functions.
