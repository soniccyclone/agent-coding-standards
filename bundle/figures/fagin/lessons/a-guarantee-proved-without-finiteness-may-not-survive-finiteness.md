---
type: lesson
title: "A guarantee proved without a finiteness assumption may not survive one"
figure: fagin
works: [horn-clauses-and-database-dependencies]
axes: [verifiability, hardware-affinity]
subdomains: [foundations-of-computation, algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# A guarantee proved without a finiteness assumption may not survive one

**Lesson:** Fagin proves that the canonical structure he wants always exists, and then spends a separate section undoing the comfort of that result. The construction combines a family of witnesses, one for each rule that fails, and when there are infinitely many such rules the object it produces is not merely infinite but uncountable. So he asks the question that actually matters for anything running on a machine: does a finite one exist? The answer is conditional. It does when the collection of rule shapes under consideration is itself finite, and he exhibits a case where dropping that restriction kills it, using a sequence of rules about longer and longer connecting paths. Any finite structure whatsoever violates one of them, so no finite structure can be free of accidental constraints.

The deeper point is that unrestricted entailment and entailment restricted to finite structures are genuinely different relations, not the same relation viewed at different scales. He cites a set of four rules that entail a fifth over arbitrary structures while the entailment fails over finite ones, and notes that both versions of the decision problem are undecidable for the broader class. A theorem proved in the unrestricted setting therefore tells you nothing automatically about the setting your program inhabits. The reasoning has to be redone, and sometimes it comes out the other way.

The reason this generalizes past logic is that the unbounded case is frequently the easier one to reason about, so it is where theory naturally settles, and every real implementation lives in the bounded case. Fagin's own earlier work makes the same point from the other side: once you cap the size of the value sets involved, a definition that looked clean immediately produces combinatorial problems that the uncapped definition never had to face. Bounds are not a detail you can add at the end. They change which statements are true.

The habit worth taking is to notice which of your guarantees quietly assume the absence of a limit, and to re-derive them under the limit you actually have. Correctness arguments that assume unbounded integers, unbounded queues, unbounded retries, or arbitrarily many distinct identifiers all belong to this family. An argument that works because a resource is inexhaustible is not a weaker version of the real argument. It is an argument about a different system, and the gap between them is where production failures live.

**Source:** [Horn Clauses and Database Dependencies](../works/horn-clauses-and-database-dependencies.md) — the section on finite canonical structures, including the theorem's finiteness hypothesis, the path-length counterexample showing the hypothesis cannot be dropped, and the cited divergence between unrestricted and finite entailment.
