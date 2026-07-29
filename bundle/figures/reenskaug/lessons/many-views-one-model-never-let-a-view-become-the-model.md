---
type: lesson
title: "Many views, one model — never let a view become the model"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Many views, one model — never let a view become the model

Reenskaug describes a set of roughly ten different presentations of the same design — a prose statement of what the design is about, what arrives from outside and what results, who participates, what each may say to whom, example sequences over time, how data moves, how a participant's condition changes, what happens inside one participant when a request lands. What makes the arrangement work is a claim he states repeatedly and treats as load-bearing: these are all views of one underlying thing, not separate documents. The design exists once; what you look at is a projection chosen to answer the question in front of you.

The alternative, which is the norm, is a pile of artifacts each authoritative for its own aspect. The failure mode is not that any one of them is wrong but that they disagree, silently, at different rates, and the disagreement is discovered by whoever trusts the wrong one. Reenskaug is explicit that his views are not independent — they overlap, so the same fact appears in several — and that their mutual consistency ought to be enforced mechanically, with manual enforcement admitted as a fallback rather than recommended. Naming redundancy and then owning the consistency obligation is the whole trick; redundancy is what makes multiple views useful and also what makes them dangerous.

Two smaller points fall out. Nobody needs all the views, so a team should choose the few their problem actually rewards and ignore the rest without feeling incomplete — the availability of a projection is not an obligation to produce it. And presentation-level conveniences, such as collapsing a cluster of participants into a single symbol to keep a diagram readable, must be understood as artifacts of the picture with no counterpart in the underlying design, or they will eventually be mistaken for structure and reasoned about as if they existed.

A programmer holding this asks, of every diagram and generated document, which artifact is the single source and whether the rest are derived from it or merely correlated with it. Where they are merely correlated, the honest options are to generate them or to delete them; keeping them by discipline is a bet on attention that always eventually loses.

**Source:** [Working with Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — the concepts-and-notation section of the role modeling chapter, which enumerates the ten views, tabulates which are meaningful from which vantage point, and states that they are presentations of one model whose non-orthogonality demands consistency enforcement; together with the note that virtual clustered roles exist only in the presentation.
