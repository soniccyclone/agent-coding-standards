---
type: lesson
title: "A derivation engine hands you proofs, not facts, so anything you count over its output counts derivations"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# A derivation engine hands you proofs, not facts, so anything you count over its output counts derivations

**Lesson:** Ask a deductive system which things have some property and it will report each thing once for every distinct way it could establish that thing. Two independent routes to the same conclusion are two answers. This is not a bug and it cannot be fixed inside the engine without changing what the engine is: the engine's job is to explore derivations, and the number of derivations reaching a conclusion is a genuine, and genuinely variable, property of the rule set and the data. A result appearing four times means four routes were found, and the four are all correct.

The trap is that the output looks like a list of facts, is shaped like a list of facts, and is nearly always consumed as if it were one. Sum a column over it and the multiply-derived rows are counted multiple times. Average it and the answer is weighted by derivability. Count it and you have measured your rule set rather than your data. What makes this particularly nasty is that the arithmetic is not obviously wrong — the totals are plausible, the individual entries are all true, and nothing anywhere is invalid. The defect only shows up if someone independently knows what the answer should be.

The correction is to insert a deduplication step between deriving and aggregating, and to be explicit that this step is where facts are recovered from proofs. It is not a performance tweak or a cosmetic tidy-up; it is a semantic transition from one kind of collection to another, and the choice of which fields determine identity is a real modelling decision that has to be made deliberately. The habit worth forming is that any pipeline whose front half derives and whose back half aggregates needs a visible boundary between the two, and the boundary is where you write down what makes two answers the same answer.

The pattern extends well beyond inference engines to anything that finds results by search or traversal: a join that produces a row per matching pair, a graph walk that reaches a node by several paths, an event replay where the same underlying occurrence generated several records, a dependency resolution that reaches the same package through several parents. In each case the multiplicity is meaningful information about the structure of the search — sometimes exactly what you want to know — and is catastrophic if silently interpreted as multiplicity in the domain. Before aggregating any derived collection, ask what one row of it actually denotes.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 4 section 4.4.3, Exercise 4.65, in which querying the organizational-seniority rule returns one particular person four times and the reader is asked why, the cause being that the rule body can be satisfied through several distinct intermediate bindings; together with Exercise 4.66, where a proposed extension adds accumulation operators such as sum, average and maximum by feeding a query's stream of result frames through an extractor and then into an accumulator, and the proposer realizes on being shown the repeated result of the previous exercise that the simple accumulation scheme cannot work, with the exercise asking for a method to salvage it.
