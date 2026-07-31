---
type: lesson
title: "First-class status is a checklist you can audit, not a compliment"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# First-class status is a checklist you can audit, not a compliment

**Lesson:** Languages restrict what may be done with each kind of element they contain, and the elements carrying the fewest restrictions are called first-class. The term is usually deployed as vague praise. Here it is given as an enumerable list of rights: an element may be named by a variable, passed as an argument, returned as a result, and included in a data structure. Four checkable properties, not an atmosphere.

Turning it into a checklist is what makes it useful, because you can then audit any kind of element in any system and get a specific answer rather than an impression. Take whatever your system traffics in -- functions, types, modules, queries, transactions, permissions, configurations -- and ask the four questions. The failures are informative in different ways. Something that can be passed but not returned supports callbacks and forbids factories. Something that can be named but not stored cannot be collected, and therefore cannot be dispatched over. Each missing right forecloses a specific family of designs, and the foreclosure is usually invisible to that system's users, because you cannot miss a construction you were never able to attempt.

The list also locates the cost, which the authors are explicit about. Allowing an element to be returned is what forces the implementation to keep that element's captured environment alive after the creating call has finished, and that storage obligation is the main price of the arrangement. So the rights are neither free nor independent: the return right buys the most expressive power and imposes the most on the runtime.

Held as a habit, this converts a fuzzy design conversation into an inventory. For each kind of thing in your system, write down which of the four it has. The gaps are your design's real shape, and they predict which patterns your users will find natural and which they will keep reinventing awkwardly around the missing right.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 1 section 1.3.4 on abstractions and first-class procedures, which states that languages impose restrictions on how computational elements may be manipulated, that elements with the fewest restrictions have first-class status, and enumerates the rights -- may be named by variables, passed as arguments, returned as results, included in data structures -- crediting the notion to Christopher Strachey, with the footnote that the major implementation cost is that returning procedures requires reserving storage for their free variables while they are not executing.
