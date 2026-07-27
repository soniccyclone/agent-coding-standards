---
type: lesson
title: "Weaken your rules until determinism is obvious, rather than strengthening them and proving confluence"
figure: kleene
works: [recursive-predicates-and-quantifiers]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Weaken your rules until determinism is obvious, rather than strengthening them and proving confluence

**Lesson:** A system of defining equations only computes something if, for each input, exactly one answer is derivable. Two ways exist to get there. You can write the most permissive rewriting rules you can think of — substitute anywhere, replace on either side of an equation — and then prove that all the different derivation paths converge, which is a hard theorem of the Church-Rosser kind and, for functions that may be undefined, not even a finitary argument. Or you can restrict the rules so narrowly that at each step there is no choice available at all, and uniqueness becomes a triviality you can see rather than a theorem you must earn. Restricting replacement to one side of an equation, on function applications whose arguments are already fully evaluated, does exactly that: the derivation for a given input is forced, step by step, so no two paths exist to disagree.

Notice what this costs and what it does not. It does not cost expressive power: every function definable with the permissive rules is definable with the restricted ones. It does cost convenience at the surface, and the fix for that is a translation — an equation whose left side is not in the restricted shape can be reworked into a search for a matching pair, which puts it back inside the disciplined subset. So the general pattern is: keep the core calculus deliberately weak and deterministic, and buy back the convenient notations as derived forms, rather than admitting them as primitives and paying with a confluence proof forever.

There is a genuinely surprising asymmetry worth carrying away. When comparing the weak and the strong rule set, the easy direction is showing the strong one defines nothing new. The hard direction is showing the strong one defines *everything* the weak one does — because that requires knowing the strong system is consistent, which is precisely the expensive theorem you were trying to avoid. Power in a formalism is not free even when you are only using it to establish a lower bound. And what a theory of computation actually needs from its calculus is minimal: some consistent formalism adequate to derive the values. Anything more powerful is a liability whose consistency you now owe.

The transfer to language and system design is direct. Prefer an evaluation order that is forced over one that is merely confluent; prefer a rule set where the next step is uniquely determined by the state over one where a scheduler's choices must be proved irrelevant. And be honest about which restriction you chose: the specific restriction hardly matters, only that it channels derivations into a single path. When a construct's determinism requires an argument rather than an inspection, that is a signal the primitives were chosen for the writer's convenience instead of the reasoner's.

**Source:** [Recursive Predicates and Quantifiers](../works/recursive-predicates-and-quantifiers.md) — the consistency discussion in Part II, which contrasts the easy uniqueness argument available under the restricted replacement rule with the Church-Rosser-style argument the unrestricted rule demands, shows the restricted rule loses no functions, and gives the reworking trick for equations whose left sides fall outside the permitted shape.
