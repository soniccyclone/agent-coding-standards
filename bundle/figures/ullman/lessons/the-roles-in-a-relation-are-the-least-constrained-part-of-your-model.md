---
type: lesson
title: "The roles in a relation are the least constrained part of your model — try swapping them"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# The roles in a relation are the least constrained part of your model — try swapping them

**Lesson:** An algorithm defined over a many-to-many relation between two populations depends on the relation, not on what the two populations are called or on any intuitive reading of the connective between them. The names are documentation. Once you see that, a whole family of applications opens up that the original framing hides, because you are free to assign either population to either role, and to let the connective mean anything at all as long as it is well defined. The connective in particular is where people get stuck: they read it as containment or membership because the motivating example was containment, and then decline to model situations where the natural reading runs the other way.

The productive habit is to take a technique that works over a relation and deliberately enumerate the assignments. If the technique finds groups of one population that co-occur across many members of the other, then ask what it means to swap: the same machinery now finds groups of the other population that co-occur across many of the first. Those two questions are usually not variants of each other — they are different problems with different applications, and one of them is often something you were about to build a bespoke solution for. The classic example is that a method for finding items purchased together becomes, under the swap, a method for finding documents that share passages, which nobody would derive from the original framing.

What makes this more than a curiosity is the leverage. A technique with real engineering behind it — the memory discipline, the pruning, the pass structure — is expensive to build and expensive to tune. Getting a second and third application by reinterpreting its inputs costs nothing and inherits all of that work. The alternative, building a purpose-shaped solution per problem, means paying the same engineering repeatedly with less scrutiny each time. Reuse at the level of abstract relation is far more powerful than reuse at the level of library function, because it crosses domains rather than crossing modules.

The discipline this asks for is to write down what your algorithm actually requires, stated with the domain nouns removed. If the honest statement is "a relation between two finite sets, with the property that most members of one side relate to few members of the other," then say that, and check candidate problems against that statement rather than against the story you first heard the technique in. Domain vocabulary is a comfort that narrows what you can see.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the market-basket section of the frequent-itemsets chapter, which insists the item-basket relation is an arbitrary many-many relation whose connective need not mean "part of," and lists plagiarism detection (documents as items, sentences as baskets) and biomarker discovery as applications reached by reassigning the roles.
