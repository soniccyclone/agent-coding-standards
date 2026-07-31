---
type: lesson
title: "Projecting a ternary fact onto pairs loses which went with which"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Projecting a ternary fact onto pairs loses which went with which

**Lesson:** Data arrives as facts of some arity, and the tooling you want to use almost always accepts a lower one. Graph algorithms want pairs. When the underlying event involves three participants at once — someone applied a label to a document, a buyer purchased an item from a seller, a service called a method on a resource — the standard move is to project: build one pair-set for each two of the three roles, run the pairwise machinery, and treat the results as views of the same phenomenon. The projection is lossless about *participation* and silently lossy about *co-participation*. After it, you know that this person used that label and that this label appears on that document, and you can no longer recover whether that person ever put that label on that document. The three projections jointly admit combinations the original data never contained.

What makes this dangerous is that the projected structure is perfectly well formed. Nothing errors, nothing is empty, every algorithm you run on it returns a sensible answer, and the answer is about a superset of reality that includes combinations you invented by projecting. Conclusions of the form "these two are related because they both connect to a common third" are exactly the conclusions most sensitive to the loss, and they are also the conclusions most of this machinery is built to draw. So the error concentrates precisely where you are looking.

The alternative is not to refuse the projection but to keep the original arity somewhere and treat the projections as derived, disposable views. A relation with one column per role holds the ternary fact exactly; the pairwise graphs are cheap to regenerate from it and expensive to reason back from. Keeping the higher-arity form as the system of record costs storage and buys you the ability to check any conclusion the projection suggests — you can always ask the original whether a specific combination actually occurred. Where the higher-arity form is genuinely unavailable, that is worth writing down, because the analyses you can trust are then limited to ones whose claims survive the loss.

The general habit is to notice, whenever you flatten data to fit a tool, what question the flattened form can no longer answer, and to ask whether that is one of the questions you intend to ask. Arity reduction is a specific and common instance, but the pattern recurs everywhere a richer record is squeezed into a poorer schema: the flattening is usually chosen for the tool's convenience, and the discarded dimension is usually the one carrying the correlation you were hunting.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the section on graphs with several node types in the social-network chapter, which builds two separate two-party networks by deleting one node type, introduces the k-partite representation as the natural alternative, and notes that even the tripartite graph fails to record which user placed which tag on which page, so a three-column relation would be needed.
