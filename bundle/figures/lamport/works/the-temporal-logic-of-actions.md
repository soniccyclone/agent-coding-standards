---
type: work
title: "The Temporal Logic of Actions"
figure: lamport
description: Introduces TLA, a temporal logic in which both a system's specification and its implementation are written as logical formulas, so that "this implementation satisfies that spec" becomes a plain logical implication you can check. Solves an awkward problem in earlier specification formalisms where specs and implementations lived in incompatible notations. Forms the theoretical core that later gets packaged, with added syntax and tooling, as TLA+.
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
year: 1994
url: https://lamport.azurewebsites.net/pubs/lamport-actions.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# The Temporal Logic of Actions

**Venue/year:** ACM Transactions on Programming Languages and Systems 16(3), May 1994 (also SRC Research Report 79)
**Source:** https://lamport.azurewebsites.net/pubs/lamport-actions.pdf — self-archived PDF on Lamport's own site, live and directly downloadable (HTTP 200).

## Lessons
- [Put the system and its specification in one formalism, so 'implements' becomes implication](../lessons/spec-and-implementation-in-one-logic.md)
- [For describing and reasoning about systems, ordinary mathematics beats programming notation](../lessons/ordinary-math-beats-programming-notation-for-reasoning.md)
- [Split every correctness claim into safety and liveness, and never let one pay for the other](../lessons/split-correctness-into-safety-and-liveness.md)
