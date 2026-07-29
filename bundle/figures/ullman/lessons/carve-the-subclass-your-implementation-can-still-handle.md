---
type: lesson
title: "Carve out the subclass your implementation techniques survive, and check it survives refactoring"
figure: ullman
works: [assigning-an-appropriate-meaning-to-database-logic-with-negation]
axes: [verifiability, expressiveness, primitive-count, cognitive-load]
subdomains: [databases-and-data-management, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Carve out the subclass your implementation techniques survive, and check it survives refactoring

Once a general semantics exists, the usual next move is to try to implement it in
full. Ullman documents the more productive move: work out which restricted class
of programs your best implementation techniques still apply to, and make that class
a named, first-class concept. The class in question was defined precisely so that
the query-directed optimization the field depended on — the transformation that
avoids touching data irrelevant to the question asked — would keep working, since
under the fully general semantics it would not. The restriction is not an admission
of defeat; it is the deliberate output of a design process that ran the
implementability requirement backwards into the definition of the language.

What makes such a hierarchy usable rather than a maze is the agreement property
Ullman lays out at the end: the classes nest, and where two of them both apply
they choose the same meaning. That is what lets a programmer ignore the whole
taxonomy in the common case. You write in the simplest fragment, you get the
efficient implementation, and if you later stray into a broader class the meaning
of what already worked does not shift underneath you. A hierarchy of restrictions
without that coherence guarantee would be worse than no hierarchy at all, because
every promotion between tiers would silently be a semantic change.

The sting is in the fragility Ullman then exhibits. Introduce a trivial
intermediate definition — a predicate that merely renames an existing one, the sort
of edit anyone makes for readability — and a program drops out of the simpler
admissible class even though its meaning and its data are untouched. That is a
general property of syntactic admissibility criteria, not a quirk: they are stated
over the shape of the text, so meaning-preserving edits can violate them. Anyone
who has been rejected by a borrow checker, a termination checker, a strictness
analyser or a lint rule after an innocuous extraction has met the same wall. The
practical consequence for a designer is to prefer criteria defined over structure
that refactoring preserves — grouping predicates into modules and requiring the
condition per module, rather than demanding it of the flat program — and the
consequence for a user is to recognize that "the checker refuses this" is
frequently a statement about the form of your code and not about its correctness.

**Source:** [Assigning an Appropriate Meaning to Database Logic with Negation](../works/assigning-an-appropriate-meaning-to-database-logic-with-negation.md) — the section on modularly stratified semantics, motivated by preserving the query-directed rule transformation, together with its example where adding a renaming predicate breaks local stratification but not the modular condition, and the closing figure relating the classes and their agreement on shared programs.
