---
type: lesson
title: "A distinction that implementors apply inconsistently and users find confusing is a defect, however elegant it is"
figure: steele
works: [common-lisp-the-language-2nd-edition]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A distinction that implementors apply inconsistently and users find confusing is a defect, however elegant it is

**Lesson:** This edition of the specification is largely a record of a committee revisiting a language that had been in wide use for five years, and the most instructive thing about that record is the grounds on which it repeals things. Several repeals are not corrections of errors. The original design had drawn a careful distinction between using a type description to promise something to the compiler and using it to interrogate an object at run time; the two readings genuinely differ, and the distinction is defensible on paper. It was withdrawn anyway, on two findings offered in exactly that order: implementations had not honoured it consistently, and — flagged as the weightier of the two — users found it confusing. The same shape recurs. A theoretically clean account of what a function's type means was replaced because it turned out not to be what compiler writers could use nor what programmers expected. A whole type was deleted for having never proved useful. A binding construct was removed once it became clear its behaviour was too surprising to explain.

The principle under all of these is that a specification's correctness is not measured only against a semantic model; it is measured against what a population of implementors and programmers can reliably do. A distinction only exists if it is drawn the same way by everyone who has to draw it. If it is not, then the specification does not contain one distinction — it contains a family of divergent private interpretations, each of which quietly becomes something programs depend on. That is strictly worse than not having drawn the distinction at all, because now the divergence is invisible and blessed. Empirical evidence of confusion is therefore evidence about the design and not merely about the users, and it is the kind of evidence that can only arrive after shipping.

Notice also what survives the repeal. The specification does not pretend the underlying idea was worthless; it keeps the concept as a piece of explanatory vocabulary while removing its operational teeth, and points out that one narrow corner where the distinction still does real work has been retained. That is a more honest resolution than either defending the original design or erasing it: the concept was real, it just could not be made to bear load in the hands of ordinary users.

A designer who accepts this treats confusion reports as bug reports against the design, not against the documentation, and looks hardest at exactly the distinctions they are proudest of — because a subtle distinction that is correct and that nobody can apply is the most expensive kind of mistake, and the only way to find it is to watch a large population fail to apply it. It also implies a discipline about revision: when you remove such a distinction, say which evidence removed it, so that the next person tempted to reintroduce it has to answer the evidence rather than the argument.

**Source:** [Common Lisp the Language, 2nd Edition](../works/common-lisp-the-language-2nd-edition.md) — the type-specifier chapter's record of the vote eliminating the declaration-versus-discrimination distinction and its stated grounds, read alongside the reinterpretation of the function type specifier and the several notes deleting features for having failed in practice.
