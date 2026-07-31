---
type: lesson
title: "Publish the obligation without publishing the name"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Publish the obligation without publishing the name

**Lesson:** Hiding is usually treated as a single decision per part: either a client may know about it or it may not. That collapses two separate questions. One is what a client may refer to — what it can name, read, assign, depend on by identity. The other is what a client's own machinery must account for in order to be correct — obligations that arise from the part's existence regardless of whether anyone can name it. Denying the first does not dissolve the second. When something built on top of your representation has to be correct about a property of it, that property has to reach the builder, or the result is not encapsulation but a silent defect.

The resolution is to publish the obligation stripped of the identity. Emit an entry saying that something with a given characteristic exists at a given position, with no name attached to it. A client can then do what correctness requires — account for it, copy it, register it, traverse it — while remaining unable to refer to it, because there is nothing to refer to. This is a sharper and more useful notion of hiding than all-or-nothing: the interface is not "the set of parts clients may see" but "the minimum information that lets a client be correct," and those are different sets, with the second one usually a little larger than the first and shaped differently.

The corollary is a check worth running on any hidden representation. List the things that must be true of clients and of anything derived from your representation — a mechanism that must find every reference, a construction that must preserve every constraint, a routine that must reproduce every part when copying. For each, ask whether the information needed to satisfy it survives the hiding. Where it does not, the choice is between publishing the obligation anonymously and performing the work yourself on the client's behalf. Silently assuming that a hidden thing imposes no external obligations is the failure mode, and it is one that only appears when someone extends the thing rather than merely uses it.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.6's explanation of the HPtr specifier in a symbol file's field list, which denotes a field of pointer type whose name is not exported but which appears in the file because, when an extension of the record type is declared, the resulting type descriptor must contain the offsets of all pointer fields for the garbage collector, and pointers inherited from the base type must not be missing.
