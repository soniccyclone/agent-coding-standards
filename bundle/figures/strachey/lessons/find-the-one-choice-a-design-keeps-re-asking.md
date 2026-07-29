---
type: lesson
title: "Find the one choice a design keeps re-asking"
figure: strachey
works: [the-main-features-of-cpl]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# Find the one choice a design keeps re-asking

**Lesson:** A large design will ask the same underlying question in several
places without noticing, and each place will invent its own answer, its own
keywords, and its own explanation in the manual. CPL's designers noticed that
binding a name to an expression forces exactly one decision — whether the name
gets the expression's value now, gets the expression's storage location, or gets
the expression itself to be re-evaluated at every use — and that this same
decision was being made independently at three different points in the language:
when a variable is introduced with an initial value, when a function's
non-parameter names are resolved, and when an actual argument is handed to a
routine. Instead of three unrelated feature sets, they made it one three-way
choice appearing in three positions, with the correspondence stated out loud.

This holds because the recurrence is not a coincidence — it reflects a real
question that any binding construct must answer, so the places that answer it are
instances of one thing rather than neighbours. Unifying them shrinks what has to
be learned from three vocabularies to one, and it also acts as a completeness
check: once you see the axis, you can ask whether every position on it is
available at every site, and a missing combination stands out as an oversight
rather than hiding as an unremarkable absence. The alternative accumulates
special cases whose differences are historical, and those differences are exactly
the kind a user cannot predict and must memorise.

A programmer who works this way, when adding the fourth variant of something,
stops and asks what question all four are answering. If the answer is the same
question, the right move is to name the question, enumerate its answers, and let
the four sites share the enumeration — not to add a fourth well-documented
special case. It also changes how you read an unfamiliar system: instead of
learning features one at a time, you look for the small number of recurring
decisions the features are permutations of, because that set is both far smaller
and far more predictive than the feature list.

**Source:** [The Main Features of CPL](../works/the-main-features-of-cpl.md) — the
sections on initialised definitions, on how a function definition treats the
names in its body that are not parameters, and on routine parameter modes, where
the paper explicitly points out that the three parameter-passing modes correspond
to the three kinds of initialisation.
