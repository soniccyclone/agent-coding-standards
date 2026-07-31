---
type: lesson
title: "Keep the notation you design in deliberately unimplemented, so its expensive conveniences must be spent rather than tolerated"
figure: hoare
works: [notes-on-data-structuring]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Keep the notation you design in deliberately unimplemented, so its expensive conveniences must be spent rather than tolerated

**Lesson:** There is a standing temptation, once a notation for describing designs turns out to be precise enough to express algorithms, to build a translator for it and collapse two stages into one. Resist it when the notation contains operations that are cheap to think with and ruinous to execute — whole-structure copies, concatenations, set-valued expressions, anything that treats a large aggregate as a single value. Those operations earn their place in design precisely because they let you state what is happening without committing to how it is stored. Their removal, and the choice of representation that replaces them, is real design work, frequently forcing changes to both the algorithm and the data layout at once. A compiler cannot do that work; it can only pick some representation and hide the fact that the decision was ever open. Make the notation executable and the obligation to make that decision disappears from the process without the decision itself getting any better.

The second cost is subtler and hits the designer rather than the program. As soon as a notation runs, it acquires a cost model, and any competent person will learn which constructs are slow and start avoiding them — not just in code, but while thinking. The vocabulary available for forming ideas contracts to the subset that happens to compile well on this year's machines, and possibilities get pruned before they are ever articulated. A fixed implemented notation causes a related loss: users stop inventing notation of their own for the structure of the particular problem in front of them, because only what the implementation already knows about feels legitimate. Both effects are invisible from inside — you never see the design you failed to consider.

So keep two languages and know which one you are in. The design language is chosen for expressive fit with the problem and for the ease of stating and checking properties; the implementation language is chosen for proximity to the machine, and being able to predict cost from the shape and length of the text is a genuine virtue there, not a primitivism. Refinement is the deliberate passage between them, and it is where the efficiency argument is supposed to happen. The pleasant case is when the implementation language turns out to be a subset of the design language, so the passage is a restriction rather than a translation — but nothing about the method depends on that, and the absence of a compiler for your design notation is not an argument against using it.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the notations section of the introduction, which refuses to treat the monograph's notation as a programming language, gives concatenation of sequences as the example of an operation whose elimination is itself part of design, and warns about the mental block a learned efficiency ranking imposes on invention.
