---
type: lesson
title: "The leverage lives in how the data is represented; when a program resists, stop reading the logic and go look at the tables"
figure: brooks
works: [mythical-man-month]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# The leverage lives in how the data is represented; when a program resists, stop reading the logic and go look at the tables

**Lesson:** Control flow is downstream of representation. Given the shape of the data a program works over, most of its logic is determined and much of it is obvious; given the logic alone, the program remains opaque, because the choices that mattered have been hidden. This is why a program's tables and structures are the honest summary of its design and its flow of control is a derivative artifact. Reading the two in that order is a habit with immediate practical returns, both for understanding someone else's system and for finding out why your own is fighting you.

The same ordering governs where improvements come from. Careful technique and local cleverness are worth having and are worth teaching explicitly rather than leaving to instinct, but they produce increments. The substantial gains arrive as strategic changes, and while some of those are new algorithms with better asymptotics, more of them are re-representations of the same information. Once you see the data differently, cost collapses in whole regions of the program at once. Historical examples run to interpreters written for interpreters when interaction is rare and space is precious, and to compilers encoded so densely that the decoding cost is repaid many times over by never touching external storage. Each trade is only visible from the representation, never from the flow chart, and each depends on knowing which resource the actual machine makes expensive.

A programmer who has absorbed this responds to being cornered by disengaging from the code entirely and contemplating the data. It also changes what gets documented and reviewed first: the layout of what is stored, the invariants it satisfies, and why that shape was chosen, ahead of the procedure that manipulates it. And it explains why space and time can be budgeted at all. The relationship between them is smooth over a remarkably wide range, so a design's cost profile is largely a consequence of representational decisions that can be reasoned about before any of the procedures exist.

**Source:** [The Mythical Man-Month](../works/mythical-man-month.md) — the chapter on controlling program size, whose closing sections separate craftsmanship in space-time trading from the strategic re-representation that produces the large wins, and which places the essence of the activity in the choice of representation rather than in procedural cleverness.
