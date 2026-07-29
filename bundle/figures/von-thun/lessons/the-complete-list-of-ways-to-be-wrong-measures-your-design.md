---
type: lesson
title: "The complete list of ways to be wrong measures your design"
figure: von-thun
works: [the-prototype-implementation-of-joy]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# The complete list of ways to be wrong measures your design

The manual for von Thun's implementation contains something most language manuals cannot contain: every syntax error the system is capable of reporting, exhaustively, in about eight lines. He introduces the list by explaining why it is so short — the syntax is small, so there is very little to get wrong. Then he does the same for the runtime side, where the count is larger because there are many primitives, and there the interesting thing is not the number but the shape: every runtime failure is generated from one template pairing a requirement with the name of the primitive that wanted it, and the requirements themselves come from a shared vocabulary of a couple of dozen phrases about parameter counts, types, and non-emptiness. No primitive has a bespoke diagnostic. No failure needs prose written specially for it.

This is not a feature of the error handling; it is a readout of the design. An enumerable failure catalogue is only possible when there are few independent ways for things to combine badly, and a uniform diagnostic template is only possible when everything in the system has the same kind of contract — here, functions from a stack to a stack, so the only things that can be missing are values of a certain count and kind. Complexity in the model reappears as irregularity in the failures, unavoidably, because failures are where the model's joints show. That makes the catalogue an instrument rather than an afterthought.

Which gives a diagnostic technique that is cheap and hard to fool. Write out every distinct way your system can reject an input or refuse to proceed. If the list does not terminate, if each subsystem contributes its own error vocabulary, if diagnostics have to be authored one per feature, the system has more independent mechanisms in it than its documentation admits, and you have just measured how many. The converse is a design target worth aiming at: shrink the grammar and unify the contracts until the failure list becomes something you could print, because a user who can hold the whole failure space in their head debugs differently from one who meets a new error class every week.

**Source:** [The Prototype Implementation of Joy](../works/the-prototype-implementation-of-joy.md) — the error-messages section, which enumerates the implementation's complete set of read-time errors and then presents runtime errors as one template filled from a shared list of requirement phrases.
