---
type: lesson
title: "Separate the fixed skeleton from the pluggable primitives, so one account covers a whole class of models"
figure: scott
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Separate the fixed skeleton from the pluggable primitives, so one account covers a whole class of models

**Lesson:** Even when a system has an obvious canonical realization, committing your account to that one realization is a habit worth breaking. If every realization is interchangeable, singling one out buys nothing and costs the freedom to switch; and if realizations genuinely differ — different machines, different representations, different underlying structures — then an account welded to one of them cannot say anything about the others. The discipline is to divide the concepts into two piles. One pile holds the constructs whose meaning is fixed by the framework itself: sequencing, conditionals, binding, iteration. The other holds the primitives whose interpretation is supplied from outside. A model is then just an assignment of meanings to the second pile, and the whole semantics is a function of that assignment.

The payoff is that the interesting questions become expressible and comparative. Two programs may be interchangeable under one interpretation of the primitives and distinguishable under another; that is a fact about the relationship between the programs and the world they run in, and it is a fact you can only state if the interpretation is a parameter rather than a hardwired assumption. Fixing one model in advance silently converts every such fact into either a theorem or a mystery, with no way to tell which. Notice also that the reason to generalize is not always ambition: sometimes you generalize because you do not yet know which structure is right, or because you want to run the experiment of varying it.

The trap this avoids in ordinary system design is the one where a layer's specification quietly grows to depend on incidental properties of the single implementation available when it was written. Write the layer against the operations it actually needs, keep the supplier of those operations a parameter, and what you are left with is the common structure — which is what you were trying to capture in the first place. The ad hoc details of any one instantiation do not add content to the account; they only obscure the part of it that transfers.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the argument that if all models of a theory are isomorphic you may prefer not to single one out, that restricting generality is a bad habit which misleads in more complicated situations, the split of the command language's concepts into primitive notions and fixed logical constructs, and the resulting definition of model-relative equivalence of commands.
