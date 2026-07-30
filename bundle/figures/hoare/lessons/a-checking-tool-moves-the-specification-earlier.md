---
type: lesson
title: "A checking tool's real payoff is that it moves the specification earlier"
figure: hoare
works: [the-verifying-compiler-a-grand-challenge-for-computing-research]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A checking tool's real payoff is that it moves the specification earlier

**Lesson:** The obvious case for automating a check is that it catches things people miss. That is the smaller half. The larger effect is on when the statement being checked gets written. When the only way to exercise a claim about a component is to run the program and watch, claims get written after the code, positioned near the places failures show up, and shaped by what happened to break — they are instruments of diagnosis. Once a claim can be discharged without running anything, there is nothing stopping it from being written first, and writing it first turns the same sentence into a design decision made while the design is still cheap to change. The tool did not merely become more thorough; it moved a piece of thinking from after the fact to before it.

This is the right way to evaluate a proposed piece of automation generally: not by how much of the existing activity it absorbs, but by which activities its existence makes newly worth doing, and in what order. An organization will not start stating things it has no way to act on. Give it a way to act on them and the practice reorganizes around the new capability, often in ways nobody argued for directly. It also explains why partial capability is worth deploying — people will begin writing claims down before the machinery to prove them exists, because the claims are already useful as design artifacts and can be checked by cruder means in the meantime.

There is a second-order return worth noticing. Statements written to be checked are, from the machine's point of view, redundant: they say something the code already determines. That redundancy is what makes checking possible at all, and once it is present, the downstream tooling can consume the same statements for entirely different purposes — a compiler that knows a claim holds can rely on it to generate better code than it could infer alone. Information stated for the purpose of being verified turns out to be information stated for the purpose of being exploited. Design the annotation so it can serve both, and the cost of writing it is charged against two budgets instead of one.

**Source:** [The Verifying Compiler: A Grand Challenge for Computing Research](../works/the-verifying-compiler-a-grand-challenge-for-computing-research.md) — the Revolutionary criterion, contrasting assertions used as test oracles with assertions formulated as specifications in advance of code, the Effective criterion's expectation that users will begin checking newly inserted assertions in production before proof tools exist, and its note that compiler writers will later exploit the redundant information in verified programs for optimization.
