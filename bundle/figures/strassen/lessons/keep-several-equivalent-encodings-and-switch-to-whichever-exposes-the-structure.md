---
type: lesson
title: "Keep several equivalent encodings of the same object, and switch to whichever exposes the structure you need"
figure: strassen
works: [relative-bilinear-complexity-and-matrix-multiplication]
axes: [expressiveness, cognitive-load]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Keep several equivalent encodings of the same object, and switch to whichever exposes the structure you need

**Lesson:** The instinct to settle on one canonical representation early is usually wrong when the representations are provably equivalent. Equivalent encodings are not interchangeable in practice, because each one makes a different property syntactically obvious and a different property invisible. One encoding may sit inside a family of classical structures, so every theorem already proved about that family applies without translation. Another may treat all the object's slots symmetrically, so a symmetry group acts on it and a fact proved about one slot becomes three facts for free — a symmetry the first encoding cannot even state, because it distinguishes inputs from outputs. A third may make the intended reading obvious enough to name the operations after. Establish the equivalences once, carefully, and then move between them per step according to which one makes the current argument short.

The overhead this appears to cost is smaller than it looks, and the alternative is worse. Committing to one encoding does not eliminate the others; it forces you to re-derive their advantages inside your chosen formalism, usually as unmotivated technical lemmas that would have been immediate elsewhere. The real requirement is that the translations be exact and stated up front, so a fact transported across a translation is a fact and not an analogy. Where the translation is only partial, say so explicitly and bound the damage.

That last point is the subtle discipline: a representation may be defective in some respect and still be the right one to use. An encoding whose symmetry fails to respect the structure-preserving maps is a genuine defect, but if the maps play no role in the development, the defect never touches anything. Judging a representation demands knowing which of its properties your argument actually consumes; a flaw outside that set is not a flaw for you. The corresponding failure mode is rejecting the encoding that would have made the problem easy because it is imperfect along an axis you were never going to use.

**Source:** [Relative Bilinear Complexity and Matrix Multiplication](../works/relative-bilinear-complexity-and-matrix-multiplication.md) — section 2, which sets up three equivalent categories for the same objects and explains what each buys: one extends the classical categories of algebras and modules, one carries a natural action of the symmetric group permuting the three factors, one motivates the terminology; together with the declared intention to move freely among them and the explicit dismissal of the symmetric action's failure to be functorial as irrelevant to the development.
