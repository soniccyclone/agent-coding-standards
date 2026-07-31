---
type: lesson
title: "Make the dispatch table total by giving its gaps the failure action"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Make the dispatch table total by giving its gaps the failure action

**Lesson:** Selecting one of many alternatives by a value is worth converting from a chain of comparisons into a single indexed lookup, since the chain's cost grows with the number of alternatives while the lookup's does not. Making that conversion sound requires noticing that the input can be outside the defined set in two different ways, and that the two want different remedies. It can fall outside the span the table covers at all, which nothing but an explicit range test can catch, and that test is unavoidable — it is the price of indexing. Or it can fall inside the span at a position where no alternative was defined, which is a different situation entirely: the position exists, it is addressable, and it can simply be made to contain the failure action.

Filling the gaps is the move worth internalizing. It costs one slot per gap and nothing at all on the paths that do match, whereas the alternative — testing membership before dispatching — taxes every dispatch, including all the common ones, to catch a case that should be rare. More importantly it makes the structure total: every index in the span has a defined outcome, so there is no state in which the dispatch reads something undefined, and the "no alternative applies" case is discovered by taking it rather than by testing for it. Sparse alternative sets bound how far this stretches, since the table is sized by the span rather than by the count, and that is the trade to check: a wide span with few alternatives is paying for a lot of failure slots.

The construction has one property worth stating plainly because it contrasts with the usual approach to unknown-yet values. The table cannot be built until every alternative's outcome is known, which is after all of them have been processed, so unlike an isolated reference to a not-yet-known position — which can be left as a gap and linked to others like it — the dispatch instruction has to be revisited once the table exists. That one revisit is unavoidable and should be recognized as such rather than engineered around; the useful discipline is to know which of your deferred decisions can be resolved in passing and which genuinely require coming back.

**Source:** [Project Oberon](../works/project-oberon.md) — the description of procedures CaseIn and CaseOut in section 12.7's account of module OCH, which states that a case statement represents a single indexed branch in contrast to a cascaded conditional, that CaseIn generates the indexed branch together with an instruction to test the index bounds, that CaseOut is called when the end of the statement is reached and the addresses of the individual cases are known so the branch table can be constructed, that a fixup of the indexed branch instruction is unavoidable, and that the address of the trap instruction is assigned to cases that remained undefined; together with the corresponding code pattern in section 12.2 showing missing cases yielding a table entry that leads to a trap.
