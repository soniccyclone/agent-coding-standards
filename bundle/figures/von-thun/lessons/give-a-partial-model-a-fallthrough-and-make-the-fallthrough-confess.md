---
type: lesson
title: "Give a partial model a fall-through, and make the fall-through confess"
figure: von-thun
works: [a-joy-interpreter-written-in-joy]
axes: [cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Give a partial model a fall-through, and make the fall-through confess

A reimplementation of a rich system usually never gets finished, and the ordinary consequence is that it stays useless until it is. Von Thun's dispatch design avoids that trap by giving the case analysis a terminal default that punts anything unrecognised to the underlying system. The effect is that coverage becomes a dial rather than a precondition. A version handling six operators runs real programs today; a version handling sixty runs the same programs with more of their meaning determined by the model. Nothing is blocked on completeness, and completeness stops being an all-or-nothing milestone that must be reached before any value is realised.

The second half is what turns the arrangement from a convenience into an instrument. Von Thun has the default clause print the symbol it is about to delegate. Now the gap between what the model covers and what it merely borrows is not a matter of auditing source against a reference manual — it is emitted by the running system, in the order and frequency real workloads actually demand. The next thing worth implementing announces itself. Coverage work becomes demand-driven instead of alphabetical, and the honest accounting of what has not been modelled is a side effect of use rather than a document that drifts.

Note that this only works because the fall-through is loud. A silent delegation gives you the same convenience and destroys the information: the model appears to handle everything, and you lose the ability to tell modelled behaviour from borrowed behaviour — which is precisely the distinction that matters when the model is supposed to be the specification. A programmer who takes this seriously builds the escape hatch on purpose, then instruments it, and treats the log of escapes as the backlog. It applies to any incremental replacement of a legacy system, any interpreter or emulator grown by parts, any strangler-pattern migration: route the unhandled case onward so the system stays alive, and make every such route report itself so the remaining work is measured rather than estimated.

**Source:** [A Joy Interpreter Written in Joy](../works/a-joy-interpreter-written-in-joy.md) — the treatment of the case-analysis default clause, first as a way of letting an intentionally incomplete interpreter still run arbitrary programs, then revised so that the delegated symbol is written out as it passes through.
