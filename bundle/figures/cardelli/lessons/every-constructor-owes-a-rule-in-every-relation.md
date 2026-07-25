---
type: lesson
title: "Make a relaxation orthogonal: every way of building a thing owes an answer in every relation you care about"
figure: cardelli
works: [structural-subtyping-and-the-notion-of-power-type, a-semantics-of-multiple-inheritance]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Make a relaxation orthogonal: every way of building a thing owes an answer in every relation you care about

**Lesson:** Systems acquire flexibility the wrong way by default. A rule turns out to be too strict in one place, so an exception is added there; the same strictness bites elsewhere, so a differently shaped exception is added there. After a few rounds the system has several unrelated notions of "close enough", each valid for one family of constructs, and nobody can say what the general principle is because there is not one. The alternative discipline is to treat the flexibility as a first-class relation and to require, for every construct in the system, both the rules for building and using it and the rule saying when one instance of it may stand in for another. Products, sums, functions, hidden representations, and interfaces all owe an answer, including the awkward ones, and a construct without an answer is an admission of incompleteness rather than a place where the relation politely does not apply.

The reason this is worth the effort is that uniformity is what makes the relation composable. If flexibility only exists at the leaves, it stops at the first level of nesting, and a design that wanted to accept a refined component inside a container inside a function argument has to open-code the accommodation at each level. When every constructor carries its rule, refinement propagates through arbitrary nestings and the higher-order cases work without anybody having thought about them specifically. The obligation to answer everywhere also acts as a design check: constructs whose rule turns out to be strange, restrictive, or reversed are precisely the ones where the intuitive account was wrong, and being forced to write the rule down is what surfaces that.

There is a further gain in economy. Once the relation is uniform it can be given its own vocabulary, so that "a refinement of this" becomes a thing you can quantify over and abstract on, which folds the flexibility into the same abstraction machinery as everything else instead of leaving it as a special power of the checker. A designer who works this way keeps a matrix in mind: constructs down one side, relations across the top, no blank cells accepted without comment.

**Source:** [Structural Subtyping and the Notion of Power Type](../works/structural-subtyping-and-the-notion-of-power-type.md) — the stated purpose of making the relation orthogonal to all type constructions rather than a set of local relaxations, the per-constructor groups of formation, introduction, elimination, and refinement rules, and the operator that turns "refinement of" into an ordinary type. Also [A Semantics of Multiple Inheritance](../works/a-semantics-of-multiple-inheritance.md) — the extension of the relation from objects to sums and to higher-order function types, and the observation that it then works at higher order without further machinery.
