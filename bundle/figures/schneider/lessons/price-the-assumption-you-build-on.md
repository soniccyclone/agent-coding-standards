---
type: lesson
title: "An assumption is a debt: you don't know what a design costs until someone builds the thing it assumes"
figure: schneider
works: [byzantine-generals-in-action-implementing-fail-stop-processors]
axes: [verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# An assumption is a debt: you don't know what a design costs until someone builds the thing it assumes

A large body of protocols can accumulate on top of an assumed component model without anyone having checked what that model costs to provide. The assumption feels free because it appears in the premises rather than in the design — and every protocol built on it inherits an unpriced liability. Two designs cannot be honestly compared while one of them is quietly charging part of its cost to an assumption. The only way to settle the comparison is to actually construct the assumed component out of the materials that really exist, and count.

Doing that construction produces an uncomfortable and useful result: the idealized component that made the protocols simple can be so expensive to build that a protocol assuming far less about component behavior wins outright. That is not a refutation of the abstraction — it is the first honest accounting of it. Until the construction exists, the field is comparing a design that pays its bills against a design that has an off-balance-sheet entry, and the comparison always favors the second one for no real reason.

The sharper half of the discipline is recognizing assumption-substitution for what it is. A design that avoids assuming "each participant can tell when another has failed" by using timeouts instead has not removed an assumption; it has traded it for an assumption about clocks, and if that clock assumption fails, two participants can disagree about whether a third is dead — which is worse than the problem being avoided. A design that avoids assuming durable shared storage by replicating state across participants has not removed the assumption either; it has written a partial implementation of exactly that storage and left it unnamed. Assumptions rarely get deleted. They get moved somewhere less conspicuous, and the design's honesty depends on whether anyone chases them there.

A programmer who works this way treats the premises section of any design as a cost estimate rather than as background. Read what the design assumes about its substrate; ask what it would take to actually supply that, on real hardware, including the failure cases; and ask whether the alternative design that assumes less is really assuming less or merely assuming differently. The habit converts vague architectural preference into a comparison with numbers on both sides, and it regularly reverses the answer.

**Source:** [Byzantine Generals in Action: Implementing Fail-Stop Processors](../works/byzantine-generals-in-action-implementing-fail-stop-processors.md) — the introduction's argument for why the idealized processor model deserves an implementation attempt at all, including its observations that timeout-based failure detection and peer-replicated state are substitutions for the assumed properties rather than escapes from them.
