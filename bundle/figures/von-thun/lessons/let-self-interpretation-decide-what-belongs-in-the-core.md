---
type: lesson
title: "Let self-interpretation decide what belongs in the core"
figure: von-thun
works: [a-joy-interpreter-written-in-joy]
axes: [primitive-count, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Let self-interpretation decide what belongs in the core

Arguments about which operations belong in a language's kernel usually run on taste. Everyone agrees the core should be small; nobody can say when it is small enough, because "enough" has no referent. Von Thun closes his interpreter paper by supplying one. He strips the interpreter down to a version whose case analysis covers only the operations the interpreter's own text uses, delegating everything else to the fall-through. The result is a program that suffices to interpret itself and nothing beyond. Minimality stops being a preference and becomes a fixed point: the core is exactly the closure of the evaluator over its own requirements.

This is a sharper test than counting primitives, because it is closed under honesty. You cannot shrink the kernel by moving work into the evaluator — the evaluator's own needs are what the kernel is measured against, so any operation the evaluator relies on gets counted whether you called it primitive or not. Nor can you pad the kernel with operations nobody needs, since the self-interpretation criterion simply excludes them. The measurement is operational and checkable by running it, not by argument: either the reduced interpreter interprets its own text or it does not.

What a programmer does differently is stop asking "is this abstraction small?" and start asking "small relative to what fixed point?" Find some self-referential closure condition the design must satisfy — a bootstrap compiler that must compile itself, a configuration system that must configure its own deployment, a build system whose build is expressed in itself, a serialiser that must round-trip its own schema — and let that condition, not intuition, determine the required surface. The condition is a specification you did not have to write down, and it will usually reveal that some things you called conveniences are load-bearing while some things you called essential are not.

**Source:** [A Joy Interpreter Written in Joy](../works/a-joy-interpreter-written-in-joy.md) — the closing minimal interpreter, presented as the version whose cases are just adequate to interpret itself with everything else left to the default clause.
