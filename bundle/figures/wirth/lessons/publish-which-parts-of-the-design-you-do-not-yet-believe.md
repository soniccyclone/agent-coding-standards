---
type: lesson
title: "Publish which parts of the design you do not yet believe, and name them individually"
figure: wirth
works: [modula-2]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Publish which parts of the design you do not yet believe, and name them individually

**Lesson:** Stability is not a property of a document, it is a property of each region of a design, and the two are constantly confused to everyone's cost. A definition published as a single artifact invites its readers to treat every part of it as equally settled, which is false in every real case: some parts have been used long enough to have earned confidence, and others were written last month to fill a hole and have not yet met a serious application. The honest move is to say so inside the definition itself — to state that the design may be extended or changed where the issues are as yet unresolved, and then, crucially, to enumerate which areas those are by name rather than leaving the disclaimer general. A general disclaimer conveys nothing and is ignored; a list of three specific areas is actionable information, and it is the only form in which the warning can actually be used.

The value falls out in both directions. For the people building on top, the list tells them exactly where to keep their dependence shallow and where they may commit deeply, so the cost of a later change lands on the party who chose to accept it with knowledge. For the designer, writing the list is a diagnostic: the areas you cannot bring yourself to declare stable are precisely the areas where the design work is unfinished, and being unable to name any of them is a signal not of maturity but of insufficient self-examination. Expect the named areas to be the ones concerned with how components are described to each other, how names cross boundaries, and how the low-level escape hatches are shaped — the parts that touch the outside world's variability rather than the parts that are internal to the calculus. Those are where use, not reflection, produces the missing insight, which is exactly why they resist being settled at the desk.

The rule this generalizes to is that a claim of stability should be made at the granularity at which it is actually true, and made explicitly. Silence is read as a promise. If you have a versioning story, an interface, or a schema in which some parts are conjectural, say which parts, in the same document, at the same level of prominence as the rest — not in a changelog and not in a mailing-list thread. And treat the reservation as a debt with an owner: it is a statement that experience is required before the design can be closed, which means somebody has to go get the experience rather than waiting for the uncertainty to resolve itself.

**Source:** [MODULA-2](../works/modula-2.md) — the introduction's explicit reservation of the right to extend or even change the language where issues are as yet unresolved and experience in use may provide new insight, together with its naming of the three specific domains where this applies: definition modules, export of names, and low-level facilities.
