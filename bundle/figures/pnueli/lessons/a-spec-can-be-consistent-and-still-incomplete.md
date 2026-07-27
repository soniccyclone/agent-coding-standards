---
type: lesson
title: "A specification can be provably satisfied and still be the wrong specification"
figure: pnueli
works: [the-anchored-version-of-the-temporal-framework]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---

# A specification can be provably satisfied and still be the wrong specification

**Lesson:** Verification compares two formal objects. Discharge every proof obligation and what you have earned is a guarantee that the program agrees with the specification — nothing at all about whether the specification agrees with what anyone wanted. That second gap cannot be closed by better tooling, because one side of it is informal by nature. So the honest split is: internal consistency of a specification is a formal question and can be mechanized, while completeness of a specification is a judgement against intent and can only be supported, never decided. Recognizing which of the two you are working on prevents the most expensive kind of false confidence, the fully verified system that does the wrong thing.

Support for the judgement side comes from an unexpected direction: a taxonomy of property shapes. If you know that requirements of long-running systems tend to fall into a small number of recurring kinds — something must hold at every point, something must happen at least once, something must keep happening, something must eventually settle and stay — then you can audit a specification by asking, for each kind, whether you have said anything of that kind or can justify why it is irrelevant here. A specification with nothing that constrains what must eventually happen is not thereby wrong, but it is under suspicion, and the taxonomy is what makes the suspicion available. This is a checklist against forgetting, not a proof of completeness, and it is worth more than its modesty suggests.

The same taxonomy pays a second dividend, which is why it is worth building carefully rather than casually. Each class of property comes attached to the kind of argument that establishes it: things that must always hold yield to an induction over transitions where the induction is buried in the rule rather than in the user's work; things that must eventually happen need an explicit measure of remaining distance to the goal; things that need repeated external stimulus to progress need that measure plus an assumption about what the environment keeps doing. So classifying a requirement is simultaneously choosing the proof strategy for it. A programmer who works this way writes specifications as a list of independently statable requirements — each one addable, removable, and checkable on its own, unlike a monolithic model of intended behavior where touching one requirement means rebuilding the whole thing — and treats the classification of each requirement as part of writing it, because that classification tells them both whether the list has an obvious hole and how each item will be discharged.

**Source:** [The Anchored Version of the Temporal Framework](../works/the-anchored-version-of-the-temporal-framework.md) — the introduction's argument that formal tools can relate two formal descriptions but cannot reconcile a formal one with an informal one, dividing consistency from completeness and proposing property classification as the guard against incompleteness; the opening of the classification section on the incrementality of conjunctive specifications versus model-based ones; and the program part of the proof system, where each of safety, response, and progress gets its own complete rule.
