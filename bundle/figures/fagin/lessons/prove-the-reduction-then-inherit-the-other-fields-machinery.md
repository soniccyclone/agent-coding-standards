---
type: lesson
title: "Prove the reduction, then inherit the other field's machinery outright"
figure: fagin
works: [functional-dependencies-in-a-relational-database-and-propositional-logic]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Prove the reduction, then inherit the other field's machinery outright

**Lesson:** Fagin observed that the arrow used to write data dependencies and the arrow used to write logical implication behave identically, and then did the thing that separates a real result from a suggestive remark: he proved that one set of dependency statements entails another exactly when the corresponding logical statements entail each other. That is not an analogy to reason by; it is a licence to transport questions. A designer with a schema question can restate it as a satisfiability question, answer it by whatever means is most convenient, and be guaranteed the answer is correct in the original domain. Because the target fragment of logic was already the subject of intense work on efficient decision procedures, an existing resolution algorithm becomes, without modification, an efficient algorithm for deciding whether a set of columns identifies records.

The discipline here is about what counts as having established the correspondence. Loose resemblance between two formalisms invites you to import intuitions, which is how false confidence spreads. A proved equivalence lets you import artifacts: algorithms, complexity bounds, decision procedures, tools other people built and debugged. The cost of proving the equivalence is usually a few pages; the return is every result the other field has accumulated and every result it will accumulate later. Fagin makes this second point explicitly, noting that progress in automated theorem proving will translate directly into progress on the database problem.

The corresponding habit is to notice when a problem you are struggling with is a re-encoding of a solved one, and to spend effort on the encoding rather than on a bespoke solution. This is the opposite of the reflex to write a custom solver. It requires knowing enough about neighbouring fields to recognize the shape of your problem in theirs, and enough discipline to prove the correspondence rather than assume it. The payoff is also a warning: once you have the mapping, you inherit the other field's hardness results as well as its algorithms, which tells you when to stop looking for a fast method.

**Source:** [Functional Dependencies in a Relational Database and Propositional Logic](../works/functional-dependencies-in-a-relational-database-and-propositional-logic.md) — the equivalence theorem and the following section, which reformulates the dependency-entailment problem as a clause-satisfiability problem and adapts an existing resolution procedure into a decision algorithm for schema questions.
