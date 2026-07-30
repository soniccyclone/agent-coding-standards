---
type: lesson
title: "Simplicity is a property of the whole a user must hold, not of each part"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Simplicity is a property of the whole a user must hold, not of each part

**Lesson:** A team had separated its user-interface machinery into several frameworks along clean functional lines — input handling, coordinate transformation, scrolling, change propagation — and each one, taken alone, was reasonably simple and defensible. The observed outcome was that building a new editor had become a job for experts only. Nothing was wrong with any component. What was wrong was the arithmetic: the person doing the work has to hold all of them at once, so the cost they pay is the sum, and a sum of small numbers is not a small number.

This is the failure mode that per-component review cannot see, because every review passes. Decomposing along functional seams is exactly the advice one is given, and it genuinely reduces the complexity of each piece; what it does not reduce, and can silently increase, is the number of distinct models a user must carry simultaneously and the number of interfaces between them they must get right. Each split you make for the implementor's benefit adds a seam the consumer has to learn. So the metric has to move: measure difficulty at the point of use, by asking what a competent novice must know before their first working result, not by asking whether each module is comprehensible in isolation.

The remedy that follows is counterintuitive and worth naming, because the instinct when a system is hard to use is to simplify the parts further. Splitting again makes it worse. The move is consolidation — collapse the separate frameworks into one whose surface is a single coherent thing, absorbing the seams as internal detail. That trades implementor comfort for consumer comfort, which is the right trade when consumers outnumber implementors, and it usually costs more internal complexity than the sum of what it replaces. Paying that is the point: complexity has not vanished, it has been moved to the people who can afford it and away from the people who cannot.

The generalization is a habit of asking, of any decomposition, whose convenience produced it. Boundaries drawn to make building easier and boundaries drawn to make using easier rarely coincide, and when they conflict the second should win, because the first is paid once by a few and the second is paid repeatedly by many.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9 section 9.4, which observes that separate frameworks for the visual component functions were each reasonably simple but their sum quite formidable, making new editors a job for experts, and sets the goal of combining them into a single framework simple enough for a novice Smalltalk programmer to use with ease and confidence.
