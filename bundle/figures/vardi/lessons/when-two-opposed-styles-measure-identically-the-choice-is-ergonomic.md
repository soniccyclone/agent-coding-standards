---
type: lesson
title: "When two opposed styles measure identically, the choice between them is ergonomic"
figure: vardi
works: [the-complexity-of-relational-query-languages]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# When two opposed styles measure identically, the choice between them is ergonomic

**Lesson:** Two notations can look like opposites — one a set of assertions describing what should hold, the other a sequence of operations describing what to do — and turn out to define the same class of behaviours, at the same cost, rung for rung up a whole family of extensions. Strip projection from the operational one and quantifiers from the declarative one and they still coincide; add looping to one and recursion to the other and they coincide again. When the translations run both ways cheaply and without size blowup, the debate about which style is fundamental has been settled in the least glamorous way possible: neither is, and the remaining differences are about what humans find easy to write, read, and check.

That is a liberating result rather than a deflating one, because it tells you what to argue about. Once power and cost are equal, the honest grounds for preference are the ones normally dismissed as soft: which form makes an error visible, which one composes without side conditions, which one an optimizer can rearrange safely, which one a reader can skim for intent. These are real engineering criteria, and they are the only criteria left. Conversely, anyone claiming a style is more powerful owes a specific thing the other cannot express — and in the well-studied cases, that thing usually does not exist.

The rung-for-rung correspondence carries a second lesson worth more than the first. When a ladder of extensions built in one style lines up exactly with a ladder built independently in the other, the rungs are probably not artifacts of either notation; they are levels of computational difficulty that any notation must eventually meet. That is the strongest available evidence that a taxonomy is tracking reality rather than the taste of whoever drew it, and it is worth looking for whenever you find yourself trusting a classification you invented.

**Source:** [The Complexity of Relational Query Languages](../works/the-complexity-of-relational-query-languages.md) — the section on algebraic languages, where the operational algebra and its projection-free, bounded-looping and unbounded-looping variants are each shown to match a corresponding logical language in both data and expression complexity, via translations that are logspace-computable and linear in size.
