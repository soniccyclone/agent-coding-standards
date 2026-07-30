---
type: lesson
title: "When a definition resists you, derive it from the theorems it has to support and prove your results parametric in it"
figure: reynolds
works: [types-abstraction-and-parametric-polymorphism]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# When a definition resists you, derive it from the theorems it has to support and prove your results parametric in it

**Lesson:** Some concepts are easy to point at and hard to define — "this operation behaves the same way no matter what it is applied to" is one of them. The unproductive approach is to keep polishing an intuitive definition and hope it turns out to have good properties. The productive one inverts the dependency: write down the theorems the concept has to make true, then read the definition off those obligations. Done this way, the extension of the notion to compound cases stops being a design choice at all — there is exactly one way to define it that keeps the results intact, and the definition becomes something you discover rather than something you must defend.

The sharpest tool for this is the degenerate case. Insist that your machinery, fed inputs that assert nothing, must conclude nothing new: plug in the trivial correspondence between an implementation and itself and you must get back plain equality, not some weaker approximation of it. That demand looks like a formality and behaves like a constraint solver. It forces the treatment of each type constructor, and it forces the property you were trying to define to be at least as strong as a specific condition you can now write down explicitly. Whenever you are unsure whether an elaborate definition is the right one, check what it degenerates to; a definition whose trivial case is not trivial is wrong, and one whose trivial case is forced is usually right.

The final move is to stop waiting. Having established a lower bound on the definition — anything acceptable must include at least this much — you can prove your theorems from the bound alone, and note that they will continue to hold for any stricter definition that later research settles on. The results become independent of the open question, so the open question can stay open without stalling the work. Two disciplines make this honest rather than evasive. State plainly, in the text, exactly which proposition the edifice depends on and that it is unproven; and confine the unproven part to a single identifiable claim rather than letting uncertainty diffuse through the whole development. A framework with one clearly labelled hole is usable; a framework whose soundness is unstated is not, even if it happens to be sound.

**Source:** [Types, Abstraction, and Parametric Polymorphism](../works/types-abstraction-and-parametric-polymorphism.md) — the identity extension lemma and the remark that the relational treatment of polymorphic types is essentially determined by the requirement of preserving the abstraction theorem; the derivation of a minimum strength for parametricity from that lemma together with the observation that the isomorphism results hold for any more restrictive permissible definition; and the explicit statement of the unresolved central question and its dated admission of non-success.
