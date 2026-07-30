---
type: lesson
title: "Find the quantity that actually blows up, then bound it with something checkable in the text"
figure: vardi
works: [on-the-complexity-of-bounded-variable-queries]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Find the quantity that actually blows up, then bound it with something checkable in the text

**Lesson:** When a system is unexpectedly expensive, the useful question is not "which class is this problem in" but "what physical quantity gets large during evaluation". For query evaluation the answer turned out to be the width of intermediate results: a naive plan can build a temporary whose number of columns grows with the length of the request, and a temporary that wide is exponentially many rows even over a small domain. Once that is identified, the cost story stops being a mystery about language power and becomes a statement about one measurable resource, and the whole gap between the cheap and expensive ways of measuring the same language is explained by it.

The second half of the move is what makes the diagnosis actionable: find a restriction on the *written form* that provably bounds the offending quantity. Capping how many distinct names a request may use caps the width of every subexpression, because a subexpression can only be about the things currently named — and unlike a promise that plans will stay narrow, this is a property anyone can check by reading the text, before anything runs. A restriction visible in the syntax is enforceable, teachable, and mechanically verifiable; a restriction stated over runtime behaviour is a hope.

That pairing — locate the blowing-up resource, then find the static property that bounds it — is the general recipe, and it also converts an engineering folk practice into a design rule. Practitioners already knew to keep temporaries small; identifying the syntactic parameter that controls it turns the folklore into an objective an optimizer can pursue and a reviewer can check. Whenever you catch yourself saying "in practice this stays small", look for the textual invariant that would make it true by construction, because that invariant is both the proof and the optimization target.

**Source:** [On the Complexity of Bounded-Variable Queries](../works/on-the-complexity-of-bounded-variable-queries.md) — the introduction, which traces the exponential gap between data complexity and combined complexity to intermediate relations whose arity grows with expression length, then proposes bounding the number of individual variables as the syntactic restriction that keeps every subexpression's arity, and hence size, polynomial; and the concluding remarks recasting variable minimization as a query-optimization methodology.
