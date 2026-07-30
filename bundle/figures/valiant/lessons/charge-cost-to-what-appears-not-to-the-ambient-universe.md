---
type: lesson
title: "Charge cost to what actually appears, not to the size of the surrounding universe"
figure: valiant
works: [a-theory-of-the-learnable]
axes: [cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Charge cost to what actually appears, not to the size of the surrounding universe

**Lesson:** A mechanism that lives inside a large accumulated context — thousands of available names, previously built components, inherited definitions — must not pay in proportion to that context every time it does something local. The cost of acquiring one new capability should scale with the handful of things that capability actually touches, never with the cardinality of everything in scope. Stated as a requirement up front, this is a strong constraint, and it drives real decisions about representation rather than being an optimization applied afterwards.

Two moves make it achievable. The first is representational: allow a value to leave most of the universe unspecified rather than forcing an assignment to everything. When a description can say "these few are fixed, the rest are not mentioned," the things a component does not depend on become genuinely absent from its description instead of being present with a default. Silence has to be a first-class state, distinct from any particular value, or every observation drags the whole namespace along with it. The second move is statistical: you do not need to enumerate the relevant subset, only to collect enough independent samples that the chance of an unseen relevant item showing up later falls below your tolerance. Sampling until surprises become improbable gives you an approximation of the relevant set at a cost tied to that set's size, with the ambient universe dropping out of the bound entirely.

The general shape is worth extracting. Whenever a complexity claim mentions a parameter that describes the environment rather than the task, treat it as a defect to be engineered away and ask which of these two devices removes it — a representation in which irrelevance is expressible, or an estimate that converges on the relevant part from observation. A system whose costs are indexed to its total accumulated context cannot keep accumulating context; one whose costs are indexed to what each piece of work touches can grow indefinitely.

**Source:** [A Theory of the Learnable](../works/a-theory-of-the-learnable.md) — the introduction's insistence that difficulty depend only on the variables occurring in natural examples rather than on the universe of available variables, the extension of functions to concepts in section 2 with its undetermined value, and the application of the combinatorial bound at the end of section 4 which trades the total variable count for the count of variables ever determined.
