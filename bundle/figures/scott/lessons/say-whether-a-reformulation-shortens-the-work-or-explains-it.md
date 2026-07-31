---
type: lesson
title: "Say whether a reformulation shortens the work or only explains it, and value both honestly"
figure: scott
works: [continuous-lattices]
axes: [cognitive-load, verifiability]
subdomains: [foundations-of-computation, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Say whether a reformulation shortens the work or only explains it, and value both honestly

**Lesson:** Recasting a result in a more abstract framework can deliver two quite different goods, and conflating them is how abstraction gets oversold. One good is economy: the new formulation makes the argument shorter, or replaces several arguments with one. The other is comprehension: the argument is the same length and the same content, but the abstract version isolates which property was doing the work and makes the result look inevitable rather than lucky. Scott is exact about which one he got when he restates his main theorem in terms of functors and limits — a full checking of the details would not make the argument appreciably simpler, the proofs are actually the same, and what the abstract version buys is that it isolates the essential idea and shows how simple it is. That is a real gain, stated without inflation.

The discipline of naming which good you got protects against both failure modes. Claiming economy you did not get produces frameworks that are adopted for a speedup that never materializes, after which the extra vocabulary is pure cost. Dismissing an abstraction because it saved no lines throws away the thing that lets the next person see why the result holds and where it will generalize. And there is a third case worth being equally blunt about: a reformulation can deliver neither. Scott has a representation theorem showing every object in his class arises from a particular construction, and reports plainly that it does not seem to be of much help in proving theorems. Recording that is more useful than presenting the theorem as though its existence were its own justification.

The test to apply, then, is not whether a restatement is elegant but what specifically it changes about the work you have to do. Does a proof get shorter? Does a class of cases collapse into one? Does a reader who follows the new version know something the old version did not tell them? If the honest answer to all three is no, the restatement is decoration, and saying so costs nothing while leaving the record accurate for whoever comes next.

**Source:** [Continuous Lattices](../works/continuous-lattices.md) — the passage after Theorem 4.4 presenting Lawvere's functorial reading of the inverse-limit argument, which states that checking the details in that form would not make the argument appreciably simpler and that the proofs are the same, while crediting the formulation with isolating the essential idea; and the remark near the end of Section 2 that the retract representation of the class provides a representation theorem of sorts but does not seem to be of much help in proving theorems.
