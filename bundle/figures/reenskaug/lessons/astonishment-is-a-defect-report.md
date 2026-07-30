---
type: lesson
title: "Treat any exclamation of surprise from a user as a bug report against the design"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Treat any exclamation of surprise from a user as a bug report against the design

**Lesson:** "The system should behave as users expect" is the kind of principle everyone endorses and nobody can act on, because it offers no way to tell whether you have violated it. Sharpen it into an observable and it becomes usable: any noise of astonishment a person makes while using the thing is a warning of poor design. Not a training gap, not a documentation gap, not that particular user being unfamiliar — a defect, logged, in the design.

What makes this valuable is that it converts a subjective quality into something you can actually collect. Surprise is audible and involuntary. It happens in the moment, before anyone rationalizes it into a feature request or forgets it entirely, and it does not require the person to be able to articulate what went wrong — which is fortunate, since they usually cannot. Watching someone work and recording every flinch produces a defect list that no amount of asking them afterward would have produced. The discipline is entirely in *how you classify what you hear*: the same sound can be filed as "user needs training" or as "design is wrong," and only the second reading generates work for you.

It fits a broader stance in the same material about pushing error out of the system rather than handling it. Typing mistakes disappear entirely if a person selects something visible instead of recalling and typing its name. Illegal commands cannot be chosen wrongly if they are disabled before the menu opens rather than rejected afterward. Arbitrary internal limits — buffer sizes, maximum counts — should not exist to be exceeded, the guidance being that the only good numbers in this business are none, one, and all. Each of these removes a category of mistake instead of catching it, and where an error genuinely can still occur, it should be described in the person's own terms along with what they can do about it. Astonishment as a defect report is the same instinct applied to comprehension rather than to input.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 7's user interface design rules, adapted from lectures by Bruce Horn and published there for the first time with his permission: the Principle of Least Astonishment stating that any exclamation of astonishment from a user must be considered a warning of poor design, and the "handle errors gracefully" rule, which prefers designing error situations away (selecting rather than typing, disabling illegal commands before the menu opens, avoiding unnecessary restrictions) over reporting them.
