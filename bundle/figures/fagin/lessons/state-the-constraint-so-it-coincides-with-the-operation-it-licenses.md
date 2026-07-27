---
type: lesson
title: "State a constraint so that it coincides exactly with the operation it licenses"
figure: fagin
works: [multivalued-dependencies-and-a-new-normal-form-for-relational-databases]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [databases-and-data-management, foundations-of-computation]
tags: [lesson]
---
# State a constraint so that it coincides exactly with the operation it licenses

**Lesson:** There are two ways to talk about splitting a data structure into parts. One is operational: under what circumstances can I break this apart and put it back together with nothing lost? The other is declarative: what invariant does this structure obey? Fagin's central theorem for the new dependency is that these are the same question. The constraint holds precisely when the structure equals the recombination of its parts. Neither side is a consequence of the other via some chain of lemmas; they are two readings of one condition, and the proof is short because there is nothing in between them to bridge.

The value of engineering that coincidence deliberately is that every question about the invariant becomes a question about the operation and vice versa, and you get to pick whichever side is easier for the task at hand. The same condition also admits a purely local reading as a rule about completion: whenever two particular records are present, two others must be too. Fagin spends a whole section moving between these readings on the explicit grounds that the concept is hard enough that one view of it is not enough. The multiple characterizations are not decoration; each one makes a different class of proof easy. The local completion form makes structural arguments mechanical, the recombination form makes design consequences obvious, and an independence reading makes the intent legible to someone modeling a domain.

The habit this teaches is to distrust a design rule whose justification is a story and to keep reformulating it until it is provably identical to the operation it is supposed to authorize. If your rule says "when this invariant holds you may safely do X," and the invariant and the safety of X are merely correlated through argument, you have two things to maintain and a gap where bugs live. When they are the same statement, there is one thing, and checking it and licensing the operation are the same act. A programmer with this instinct writes preconditions that are exactly the weakest condition under which the operation is reversible, rather than a conservative approximation that happens to work.

**Source:** [Multivalued Dependencies and a New Normal Form for Relational Databases](../works/multivalued-dependencies-and-a-new-normal-form-for-relational-databases.md) — the first theorem, establishing the dependency as a necessary and sufficient condition for lossless splitting, together with the later section devoted to alternative equivalent views of the same concept.
