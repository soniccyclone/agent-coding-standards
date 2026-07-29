---
type: lesson
title: "Treat a well-behavedness hypothesis as a debt, and pay it by parameterizing whatever blocks the general case"
figure: curry
works: [some-additions-to-the-theory-of-combinators]
axes: [expressiveness, verifiability]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Treat a well-behavedness hypothesis as a debt, and pay it by parameterizing whatever blocks the general case

**Lesson:** When a result holds only for the well-behaved members of a class, the restriction is rarely a fact about the subject; it is usually a fact about the technique that was used. Curry's earlier theorems said that two constructions denoting the same thing are provably equal, but only for constructions that were proper in a technical sense — those that eventually resolve into a plain arrangement of arguments. He comes back and removes the qualifier, and he demonstrates that this is a real gain rather than tidying by exhibiting a pair of improper constructions whose equality the restricted theorems cannot establish: supply them with arguments and both settle to the same result, yet treating one side purely formally leaves its reduction stuck partway, so the old route to the conclusion is closed.

The technique for removing the restriction is the transferable part. Where a subterm violates the hypothesis, replace it with a fresh variable — which does satisfy the hypothesis — build a separate construction whose job is to hand the original subterm back in, apply the restricted theorem to the well-behaved version, and then compose the two facts. The obstruction becomes a parameter, the parameterized statement lands inside the theorem's existing reach, and reinstating the parameter recovers the general claim. This is why abstraction is a proof tool and not only a code-organization tool: turning a stubborn constant into an argument is often what brings a statement inside the range of a lemma you already have.

The paper also shows what such a generalization has to survive, in a detail relegated to a footnote and worth more than its placement suggests. The general case chains together many single-step transitions, and those intermediate expressions can mention symbols that appear in neither endpoint. An induction stated only over the vocabulary of the endpoints therefore does not close; the statement must be carried over the wider vocabulary, with the extra symbols later discarded, and the discarding has to be done by machinery the system already contains. Any argument about a path between two states owes the same care.

A programmer who holds this stops accepting "works for the simple case" as a boundary of nature. Faced with a lemma, invariant, optimization or refactoring that applies only when some component is well-behaved, they ask which step of the reasoning actually needs it, then abstract that component into a parameter so the good case's argument applies, and reinstate it afterwards. They are also suspicious of induction over a process whose intermediate states are richer than its endpoints, since that is where such proofs silently fail. And they insist on the concrete witness Curry supplies: a specific instance the old, narrower statement could not reach, which is the only real evidence that the generalization bought something.

**Source:** [Some Additions to the Theory of Combinators](../works/some-additions-to-the-theory-of-combinators.md) — the second amendment, which drops the properness restriction from the earlier equality theorems; the two cases of its proof, where an offending subterm is replaced by a fresh variable and reintroduced by an auxiliary construction; the worked counterexample offered as evidence of added generality; and the footnote handling intermediate expressions whose symbols occur in neither endpoint.
