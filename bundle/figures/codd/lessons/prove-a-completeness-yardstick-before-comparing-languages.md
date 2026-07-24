---
type: lesson
title: "Prove a completeness yardstick before comparing languages"
figure: codd
works: [relational-completeness-of-data-base-sublanguages]
axes: [verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# Prove a completeness yardstick before comparing languages

**Lesson:** "Powerful enough" is not a property anyone can verify, so before a wave of query languages arrived, Codd manufactured a property that is: define the class of everything expressible in one formalism, prove a second, independently motivated formalism reaches exactly the same class, and declare that class the bar a candidate language must clear. The proof is what does the work. Because the algebra and the calculus were shown equivalent by an explicit reduction algorithm, anyone comparing a new language needs only to compare it against whichever of the two formalisms it structurally resembles, and the equivalence carries the result over to the other. Capability arguments become finite checks (is there an operation of the algebra this language cannot define?) instead of taste.

The deeper habit here is anchoring an engineering standard in a theorem rather than in a feature list. A feature list is negotiable and vendors will negotiate it; an equivalence class is not. It also sets a floor rather than a ceiling: Codd is explicit that practical languages need augmentation (counting, summation, library functions), but augmentations are then judged as additions above a provable baseline instead of substitutes for it.

A programmer who thinks this way responds to "is this DSL/API/protocol expressive enough" by first constructing the reference class of things that must be sayable, ideally via two independent characterizations that provably coincide, and only then evaluating designs. When two characterizations of the same power exist, the choice between them becomes an engineering question about secondary virtues, which is exactly where Codd took it next.

**Source:** [Relational Completeness of Data Base Sublanguages](../works/relational-completeness-of-data-base-sublanguages.md) — the definition of relational completeness in Section 3.4 and the reduction algorithm of Section 4 that establishes the algebra reaches the calculus's power, plus the introduction's framing of the algebra as a yardstick applied via a two-sided comparison scheme.
