---
type: lesson
title: "Index by role: separate where a thing is defined from where it is used"
figure: naur
works: [revised-report-on-the-algorithmic-language-algol-60]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Index by role: separate where a thing is defined from where it is used

**Lesson:** A flat list of where a name appears is nearly useless, because the appearances are not doing the same work. Build the index as a partition by role instead: for each named thing, first its defining occurrence, then the places it is referred to by other definitions, then the places prose fixes its meaning. Suppress from the reference groups anything already listed as a definition, so no entry double-counts. And deliberately exclude the illustrative material — examples are for persuading a reader, not for establishing meaning, and letting them into the index would make the artifact's own account of itself unreliable.

The reason to spend the effort is that a role-partitioned index is an auditing instrument rather than a navigation aid. Because every entry is supposed to carry exactly one defining site, an entry with none is an undefined name and an entry with two is a duplicated definition — both visible by scanning a column, with no need to understand the content. Because the use-sites are enumerated separately, the blast radius of changing a definition is a finite list you can walk, not a judgement call. Because the prose-definition sites are their own group, you can check the one property a formal notation cannot enforce: that the informal commentary has actually said something about every category the grammar introduced, and has not said it in two places that might disagree. An entry with a definition and no uses anywhere is unreachable and probably wants deleting.

The generalisation is that the cross-reference structure of an artifact is part of the design, not a by-product to be generated afterward if someone has time. Whatever you are building — a specification, a schema, a module's public surface, a configuration vocabulary — decide early what the roles of an occurrence are, keep them apart, and make the invariant that ties them explicit enough to check by eye. Then note what remains outside the scheme and say so plainly: a symbol whose written form is not a word needs its own collection at the front, and the honest move is to give it one rather than to force it into an alphabetisation where nobody would look for it.

**Source:** [Revised Report on the Algorithmic Language ALGOL 60](../works/revised-report-on-the-algorithmic-language-algol-60.md) — the alphabetic index of definitions of concepts and syntactic units, and its preamble fixing the three reference groups, the rule that references already given as definitions are not repeated in the occurrence group, the exclusion of the examples from the compilation, and the separate collection of symbols not written as words.
