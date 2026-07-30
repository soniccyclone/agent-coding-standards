---
type: lesson
title: "A theory of meaning is unfinished until every level from concept down to machine is bridged"
figure: scott
works: [logic-and-programming-languages]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A theory of meaning is unfinished until every level from concept down to machine is bridged

**Lesson:** Getting from a conceptual account of what a language means to something running on real hardware passes through several distinct levels of explanation, and each transition is a place the account can quietly fail. A mathematical semantics is genuinely valuable for being independent of any implementation — that independence is what lets definitions and proofs stay clean and stop being hostage to one compiler's accidents. But independence is not the same as adequacy. Until someone has shown how the abstract conceptualization is actualized, the honest status of the theory is promising rather than unified, and the outstanding work is not decoration on a finished result.

That gives a concrete standard for judging a semantic treatment, and it is a harsh one: does it push a real language through from beginning to end, or does it stop where the difficulties start? A treatment that carries a complex language all the way down to its compiler, organized so a reader can enter at any level, is evidence about whether the approach is fruitful. A treatment that handles the clean fragment and gestures at the rest is speculation, however elegant, because the parts that get skipped are exactly the ones that would have discriminated between a working theory and a plausible one. The distinction matters more than rigor per se — rigor applied only to the tractable core produces confident-looking results with no predictive content about the whole.

The same test applies to any abstraction, not just semantics. An abstraction that is beautiful at the top and never traced to its realization has not yet been shown to be about anything; the traversal down through the levels is where you learn whether the abstraction was carving reality or your own convenience. Two corollaries worth keeping. Be explicit about which parts of your problem your formalism actually covers and which it does not, since a pure core well served says nothing about the features left outside it. And keep the abstract layer and the mapping-down honest about each other: the mapping is not a lesser activity to be delegated after the interesting thinking is done, it is the experiment that tells you whether the interesting thinking was right.

**Source:** [Logic and Programming Languages](../works/logic-and-programming-languages.md) — the opening argument that higher-level features require passing through several levels of explanation from concept to simulation on a real machine, the closing admission that much remains to be done on whether abstract conceptualizations can be actualized before a unified theory exists, and the praise for a treatment that carries a complex language through to its final compiler without sidestepping difficulties.
