---
type: lesson
title: "Give the axis of local variation its own artifact, and edits along the two axes stop colliding"
figure: knuth
works: [literate-programming]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Give the axis of local variation its own artifact, and edits along the two axes stop colliding

A program that has to run in many environments accumulates two kinds of change that look identical in a diff but behave nothing alike. One kind expresses what the program means and evolves with the author's understanding. The other kind expresses where the program happens to be running — a differently named library routine, a file convention, a compiler's private idea of the language — and evolves with the site, not the author. When both kinds live in the same text, they interleave, and every upstream revision forces every site to reconcile someone else's semantic work with its own local accommodations by hand.

The move this work makes is to refuse to let the second kind into the master text at all. The environment-specific adjustments are collected into a separate file of ordered replacements applied on the way in, and the master is never edited to accommodate any particular site. The payoff is stated as a symmetry, and the symmetry is the whole insight: the arrangement works when the master changes and the local file stays put, and it works when the local file changes and the master stays put. Because the two artifacts move independently, a new upstream version usually composes with an unmodified local file on the first try, since revisions to the meaning of a program rarely land on the handful of places where the environment intrudes. That empirical claim is the load-bearing part — it is what makes the separation cheap rather than a permanent merge tax.

There is a subtler consequence than convenience. Once local adjustment is a distinct artifact, it is also a distinct object of review, and the parts of the system that carry the real subtlety — the control flow, the data structure invariants — are visibly untouched by porting work. Anyone auditing an installation can read just the delta and know the extent of what was done to it, instead of having to establish by inspection that nothing important drifted. Applying the replacements is made to fail loudly when the text it expected is not there, so a master that has moved out from under a stale delta announces itself rather than silently producing a program nobody wrote.

A programmer who internalizes this looks, early in a design, for the axis along which reality will refuse to be uniform — platform, tenant, regulatory jurisdiction, hardware revision, protocol version — and gives that axis its own file, its own review, and its own lifecycle, rather than sprinkling conditionals through code whose subject is something else entirely. The test of whether the split was drawn correctly is exactly the symmetry above: if changes to one side routinely force changes to the other, the fault line was misplaced and the two artifacts are really one.

**Source:** [Literate Programming](../works/literate-programming.md) — the portability discussion, which introduces the paired source-and-change-file scheme, notes it was added only after real porting experience rather than designed in, and argues its value from the independence of the two edit directions.
