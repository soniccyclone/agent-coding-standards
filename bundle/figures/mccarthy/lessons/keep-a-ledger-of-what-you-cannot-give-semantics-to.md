---
type: lesson
title: "Keep a core that obeys equational laws, and keep an explicit list of the features you have not been able to give semantics to"
figure: mccarthy
works: [history-of-lisp]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Keep a core that obeys equational laws, and keep an explicit list of the features you have not been able to give semantics to

**Lesson:** Two forces pull on any working language or library. Convenience adds features, because a real user with a real deadline needs the thing that saves them work today. Provability removes them, because every construct that fails to obey ordinary substitution of equals for equals is a construct no equational argument can pass through. McCarthy describes deliberately choosing the second force for the core once he noticed the design had become a decent mathematical object: features were pruned, partly on aesthetic grounds and partly on the working belief that compact semantics without exceptions would make correctness proofs tractable later. That bet paid off years afterwards, when the pure fragment turned out to be representable as sentences and schemata of first-order logic — a payoff he could not have demonstrated at the time he made the choice.

What makes this more than a preference for purity is that he does not pretend the impure features away. Destructive insertion and deletion sit uneasily with structure sharing and, regarded as functions, do not permit replacing equals by equals, so programs using them fall outside logical treatment. Property lists, efficient numbers, the sequential statement forms, the argument-quoting pseudo-functions, variadic argument lists: he lists them and states plainly that none of them had been given a comprehensive, clear mathematical semantics, in his language or anyone else's. That list is the honest form of technical debt for a design. It is not a list of bugs, and none of the entries is proposed for removal, because each one is there for a good reason. It is a list of places where reasoning stops and only testing remains.

The final move is the one worth stealing. He states the condition under which his own language deserves to be superseded: when someone offers a more comprehensive feature set and also supplies clear semantics for it. That is a falsifiable succession criterion, and it is stated in terms of shrinking the ledger rather than growing the feature count. Designs that only grow features are not competing on the axis that matters.

A programmer who works this way maintains the boundary consciously. There is a subset of the system in which behaviour follows from equations and can be reasoned about by rewriting, and there is the rest, which is fenced, documented as fenced, and kept out of the parts that carry correctness weight. They know which of their conveniences break substitution and can name them on request. And when they extend the system, they ask whether the extension can be given laws, treating "I cannot state what this means" as a real design objection rather than academic fussiness.

**Source:** [History of Lisp](../works/history-of-lisp.md) — the introduction's account of pruning the core for compact, exception-free semantics in anticipation of correctness proofs, the implementation section's insistence that applicative expressions obey ordinary replacement of equals by equals and its admission that side-effecting operations violate this, the enumeration of post-1.5 features accompanied by the statement that none had received clear mathematical semantics, and the closing criterion for the language's eventual obsolescence.
