---
type: lesson
title: "Record why the rules are right somewhere nothing downstream depends on"
figure: kolmogorov
works: [grundbegriffe-der-wahrscheinlichkeitsrechnung]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, foundations-of-computation]
tags: [lesson]
---
# Record why the rules are right somewhere nothing downstream depends on

**Lesson:** Kolmogorov derives his axioms from experiment — repeatable conditions, the set of outcomes one is prepared to admit, the observed ratio of occurrences settling near a number — and shows how each axiom is the natural postulate given that picture. Then he says, in a footnote at the head of that very section, that a reader interested only in the mathematics need not read it, because everything that follows rests on the axioms alone and makes no use of the discussion. That is the whole discipline in one gesture. The motivation is written down carefully, it is *not* deleted or left as folklore, and it is placed where nothing above it can reach.

Two things this buys, and both matter more than they look. First, the reasoning built on the axioms cannot be contaminated by an argument that was only ever heuristic; if the empirical account turns out to be contested — and Kolmogorov sidesteps the philosophical question of what probability *is* rather than pretending to settle it — no theorem falls. Second, the axioms stay open to interpretations the motivating story never imagined, which is precisely what happens: the same system gets used in fields with no connection to random events at all. Compare the alternative, where the motivating notion is dragged inside the definitions, as in foundations that define probability *as* a limiting frequency. There the justification becomes load-bearing, every application has to relitigate it, and the mathematics inherits whatever is unresolved about the interpretation.

The software shape of this is a rule about the import graph, not about documentation habits. Rationale has to be recorded or it is lost: the measurement that justified a data structure, the incident that justified a retry policy, the regulatory clause behind a nullable column. But recorded rationale must never become an input to the code that depends on the decision. The failure modes are recognizable — a module that branches on the *reason* rather than on the stated contract, a correctness argument that quotes last quarter's benchmark, a spec whose meaning cannot be determined without knowing which customer asked for it. State the interface as axioms, so that consumers depend only on what it promises. Put the case for those axioms in a design record, a comment block, a decision log: adjacent, findable, deliberately outside the dependency graph. And label it honestly as motivation rather than proof, so no reader mistakes the one for the other.

**Source:** [Grundbegriffe der Wahrscheinlichkeitsrechnung](../works/grundbegriffe-der-wahrscheinlichkeitsrechnung.md) — Chapter I, §2 on the relation to experimental data, and specifically its opening footnote stating that the section may be skipped because the following work uses only the axioms of §1, together with that footnote's refusal to enter the philosophical question of what probability means in the experimental world.
