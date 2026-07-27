---
type: lesson
title: "Turn a relation between two structures into a property of one bigger structure"
figure: fagin
works: [on-the-semantics-of-updates-in-databases]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, databases-and-data-management]
tags: [lesson]
---
# Turn a relation between two structures into a property of one bigger structure

**Lesson:** The same manoeuvre appears twice in this paper, in settings that have nothing to do with each other, and both times it converts a problem needing new machinery into a problem the existing machinery already handles. First: a derived projection and the data it is derived from are two separate structures related by a definition, and reasoning about statements that mention one in terms of the other is awkward. So they merge the two into a single structure carrying both, and add one statement asserting that the derived part agrees everywhere with its definition. The relation between the structures is now an ordinary constraint inside one structure, and translating a statement about the derived part into a statement about the base part reduces to substitution. Second, in the closing remarks: constraints on how a system may move between states are a different species from constraints on which states are legal, and would seem to need a different formalism. So they merge consecutive states into one composite state, at which point a legality condition on the composite says exactly what a movement condition on the pair said.

The reason this keeps working is that a relation over two objects is the same information as a predicate over their pairing, and formalisms are almost never symmetric in how well they handle those two presentations. Most machinery is built for predicates over one thing: constraint checkers, satisfaction, substitution, the whole apparatus of asking whether a structure obeys a rule. Very little is built for statements straddling two structures. Enlarging the object is therefore not merely a notational convenience, it is a way of moving a problem into the region where your tools have leverage, and it costs only the enlargement itself.

Programmers meet this constantly under other names. A property relating a function's input to its output is hard to state as a check on either alone, and easy to state on a record holding both, which is what makes property-based tests and history-recording assertions work. An invariant about how a value may evolve is hard to check at any single moment, and straightforward if the previous value travels alongside the current one, which is why event logs, undo stacks, and before-and-after triggers exist. The recognition worth internalizing is that when a constraint stubbornly refuses to fit your checking mechanism, the mechanism is often fine and the state is too small. Widening what you consider a single state is usually cheaper than building a second mechanism that can talk about two.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — the construction combining a database and its view into one extended structure with a single linking sentence, and the concluding remark that constraints on legal state transitions can be handled by the identical trick of combining successive states.
