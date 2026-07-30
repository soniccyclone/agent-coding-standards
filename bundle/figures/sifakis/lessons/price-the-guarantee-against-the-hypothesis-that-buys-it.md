---
type: lesson
title: "Do not ask whether an approximation is good; tabulate which hypothesis buys which class of transferable answer"
figure: sifakis
works: [property-preserving-abstractions-1995]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Do not ask whether an approximation is good; tabulate which hypothesis buys which class of transferable answer

**Lesson:** The instinctive question about a simplified model is whether it is faithful enough, which is unanswerable because it has no units. The paper replaces it with a structure that does: a table whose rows are named conditions on the mapping between concrete and abstract, and whose columns are classes of question, with each cell recording whether an answer transfers and in which direction. Mimicking in one direction buys the universally quantified fragment, one way. Mimicking in both directions upgrades the same fragment to an equivalence, so a negative abstract answer is now also a negative concrete answer. Adding a non-contradiction condition on the atomic facts extends coverage to formulas containing negation. Requiring the mapping to be a total function, or to reproduce itself when composed with its converse, buys further cells. Each is a separate theorem with its own hypothesis, and nothing is claimed beyond what a hypothesis was paid for.

What this reorganizes is the design conversation. "Is the abstraction good enough?" invites a judgment call and produces arguments nobody can settle. "Which of these five conditions does our mapping satisfy, and what does the table say we may conclude?" is a mechanical lookup, and when the answer is unsatisfying it points at a specific condition to go establish rather than at a vague need for more fidelity. It also makes the cost of strength visible: the conditions get progressively harder to satisfy as you move down the table, and the strongest of them are frequently unachievable on the systems you actually have. Knowing that in advance is what stops a team from spending a quarter pursuing a two-way guarantee that their state-collapsing scheme could never have supported.

The pattern generalizes to any lossy transformation with results riding on it — a sampled dataset standing in for a population, a staging environment standing in for production, a simplified physical model, a mocked dependency. The useful artifact is not a confidence level but an explicit list of the structural properties the substitution does and does not have, paired with the inferences each property licenses. Write that list before you start drawing conclusions, and treat every conclusion you draw as a claim to be matched against a row in it. Most bad reasoning from models is not miscalculation; it is reading an answer out of a cell that no hypothesis ever filled in.

**Source:** [Property Preserving Abstractions for the Verification of Concurrent Systems](../works/property-preserving-abstractions-1995.md) — section 6.2's separation of preservation from strong preservation, and the sequence of theorems in sections 6 and 7 attaching each class of preserved mu-calculus fragment to its own hypothesis: simulation, bisimulation, consistency, totality, and the idempotence condition on the abstraction relation.
