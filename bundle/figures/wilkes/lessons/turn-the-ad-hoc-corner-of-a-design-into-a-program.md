---
type: lesson
title: "Find the corner of the design still being done ad hoc, and recast it as a program over a small set of primitive moves"
figure: wilkes
works: [best-way-to-design-an-automatic-calculating-machine]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Find the corner of the design still being done ad hoc, and recast it as a program over a small set of primitive moves

**Lesson:** In most systems there is one region where the surrounding discipline stops and craft takes over — the part where the designer sketches arrangements until one looks satisfactory and economical, with no method for arguing that it is right or complete. That region is the highest-value target in the whole design, and the way to attack it is not to sketch more carefully. It is to identify the smallest repertoire of elementary actions the region can be built out of, name them, and then express the region's job as a sequence over that repertoire. The craft work becomes writing sequences, which is an activity you already know how to do systematically, review, and correct.

The identification step is the real content. It requires looking at the ad hoc region and asking what the irreducible things it does to the rest of the system actually are — every distinct effect it can cause, enumerated as a closed set. Once that set exists, the region's behaviour for each of its cases is a sequence over it, alternatives inside a sequence are conditional steps, and the design's correctness question changes character: instead of asking whether a tangle of connections realizes the intended behaviour, you ask whether a written sequence does, one step at a time.

What you gain beyond tractability is a deferral you did not have before. When behaviour lives in an arrangement of connections, the specification of that behaviour has to be settled before the arrangement is built. When behaviour lives in sequences over a fixed repertoire, the repertoire and the machinery that runs sequences can be built while the specification is still undecided — and can be changed afterwards by rewriting sequences rather than rebuilding structure. The discipline that makes the hard part systematic is the same discipline that lets you postpone the decision you were least ready to make.

**Source:** [The Best Way to Design an Automatic Calculating Machine](../works/best-way-to-design-an-automatic-calculating-machine.md) — the control-proper section, which observes that this part is usually designed by drawing block diagrams until something looks workable, then decomposes every machine operation into sequences of elementary register-level steps, and notes the resulting freedom to leave the instruction set undecided until late in construction or to change it afterwards.
