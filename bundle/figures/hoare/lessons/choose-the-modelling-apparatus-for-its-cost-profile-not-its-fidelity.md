---
type: lesson
title: "Choose a modelling apparatus for the cost profile of the models it yields, then write down the fidelity gap"
figure: hoare
works: [notes-on-data-structuring]
axes: [hardware-affinity, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Choose a modelling apparatus for the cost profile of the models it yields, then write down the fidelity gap

**Lesson:** The apparatus you use to describe data is always weaker than the mathematics available, and that is a design decision rather than an oversight. Combining component descriptions to form a compound one admits every combination of components, including combinations that correspond to nothing in the world being modelled — a day-and-month pairing that never occurs, a status-and-timestamp pairing that cannot arise. Mathematics has no trouble excluding those; a richer construction that carved out exactly the real cases is easy to want. What it is not is free. The restricted apparatus buys a bundle of properties that the richer one loses at once: every value has fixed, modest size that grows linearly with the description; storage can be assigned statically or from a stack with no allocator behind it; the common manipulations compile to short instruction sequences; nothing needs a pointer, so values move between levels of storage without repair; and the representation decision is usually obvious. Being able to predict all of that from the shape of the description is worth more than exactness about which combinations exist.

The price is a gap between the model and reality, and the gap has to be paid for explicitly instead of silently. When the description admits values the domain does not, say so where the description is written: state the property that every meaningful value satisfies, as rigorously as if it were checkable, and accept the obligation to keep operations from steering a variable outside it. That written property is what a reader needs in order to know which of the admitted values are real, and it is what a later reader needs before adding an operation. A design that shrugs the gap off produces the familiar failure where each individual piece of code is defensible and the combination produces a value nobody would defend.

The generalization is that expressive power in a modelling language is not free goods to be maximized. Every construct you admit has to be implementable across all its uses, and the constructs whose implementation is uniform and cheap are exactly the ones whose descriptive reach is limited. Prefer the weaker apparatus with the predictable cost profile, discharge the resulting inexactness in written invariants, and reach for the more expressive construct only where the domain genuinely demands it — knowing that you have just given up static sizing, allocator-free storage, or pointer-free transfer for that part of the design.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the opening of the Cartesian product section, which lists the five implementation properties that make elementary structures favourable, and the discussion of the date type, which admits nonexistent dates, notes the definition is therefore weaker than the general mathematical means of defining sets, places responsibility on the programmer to keep variables from taking meaningless values, and recommends rigorously specifying the properties every meaningful value possesses as documentation practice.
