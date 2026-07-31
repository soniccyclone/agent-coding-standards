---
type: lesson
title: "A family of checks is not a check until the family is bounded"
figure: schonfinkel
works: [entscheidungsproblem-der-mathematischen-logik]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# A family of checks is not a check until the family is bounded

The opening move of the decision procedure looks like the whole solution and is not. Fix the size of the domain at some finite number, and every quantifier becomes a finite spread — the universal one a conjunction over the elements, the existential one a disjunction — so the question about predicates and relations turns into a question about a propositional formula, which is settled by trying all assignments. The reduction is exact. It is also, as the authors immediately say themselves, not an answer to the problem they posed. Two objections kill it: the domain was never promised to be finite, and even restricted to finite domains there is one such propositional check per size, so no amount of checking exhausts them.

The instructive part is that they stop and name this rather than banking the reduction as progress. What they have is a schema of decision procedures indexed by a parameter, and a schema indexed by an unbounded parameter decides nothing. The gap is closed only by a separate theorem that collapses the index: if a formula holds on a domain of a particular computable size, it holds on every domain. Once that bound exists, the infinite family of checks becomes one check, and the reduction retroactively becomes a procedure. Before it, the same reduction is a correct observation with no algorithm in it.

That distinction is the whole difference between a test and a proof of correctness, and it is easy to lose. Verifying a protocol for two nodes, three nodes, four nodes; fuzzing a parser at lengths up to some cutoff; checking a state machine to a bounded depth — each is an instance of the same shape, a family of finite decisions with the parameter left free. The instances are real evidence and none of them is the general claim. The missing piece is always the same piece: an argument that beyond some computable point, nothing new can happen. That argument, not the enumeration, is where the content lives.

The practical discipline is to write down the parameter you left free before you report the result. If you cannot bound it, say that the check is bounded and stop there — a bounded check honestly labeled is useful, and the same check labeled as general is a false claim. And when you go looking for the bound, you now know exactly what shape the theorem has to have, because the parameter you failed to eliminate is its subject.

**Source:** [Zum Entscheidungsproblem der mathematischen Logik](../works/entscheidungsproblem-der-mathematischen-logik.md) — section 2, where the expansion of quantifiers over a fixed finite domain into propositional connectives is presented, immediately followed by the authors' own statement that this does not solve the problem, and then by the theorem bounding the domain size.
