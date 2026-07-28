---
type: lesson
title: "Let the width of each level be set by what you can argue, not by what you can draw"
figure: parnas
works: [the-modular-structure-of-complex-systems]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Let the width of each level be set by what you can argue, not by what you can draw

**Lesson:** When you split a responsibility into sub-responsibilities, two things
must be true and neither is checkable by inspection: the pieces must not overlap,
and together they must cover everything the parent was accountable for. Overlap
means two teams both own a decision and will diverge on it. A gap means nobody owns
it, and gaps are the expensive kind, because they are discovered only when the
missing thing is finally needed — potentially years in, after everything around the
hole has been built assuming somebody else handled it. Neither defect announces
itself; both are properties of the division, not of any piece.

The consequence is a constraint on shape that has nothing to do with taste or with
runtime structure: the number of pieces at any one split must stay small enough that
a person can construct a convincing argument for non-overlap and coverage. Not
small enough to fit on a slide, not small enough to feel tidy — small enough to
*reason about exhaustively*. Past that width the argument degrades into an assertion,
and an unargued division is a bet that the person who drew it happened to think of
everything. A wide, flat decomposition is therefore not simpler than a deeper one;
it is the same complexity with the verification step quietly removed.

This inverts a common instinct. Extra levels of nesting are usually treated as
overhead to be minimized, and flatness as a virtue. Here nesting is bought
deliberately, purely to keep each individual argument tractable, and the depth is
whatever that requirement forces. A programmer who thinks this way, when handed a
long list of sibling components, does not ask whether the list is well-named; they
ask whether anyone could demonstrate that the list is complete. If not, the fix is
to introduce intermediate groupings until each becomes arguable — and to expect
that most of the value arrives at initial design time, since the same structure that
makes coverage arguable later makes "which of these does this change touch?"
answerable.

**Source:** [The Modular Structure of Complex Systems](../works/the-modular-structure-of-complex-systems.md)
— the stated goal that branching at every non-terminal node stay narrow enough for
designers to prepare convincing non-overlap and coverage arguments, and the
conclusion's report of responsibilities landing in two places or in none when the
team worked without that structure.
