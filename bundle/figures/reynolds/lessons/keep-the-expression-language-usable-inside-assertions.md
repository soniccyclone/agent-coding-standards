---
type: lesson
title: "Every expression you can write in the program must be legal in an assertion about it"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Every expression you can write in the program must be legal in an assertion about it

**Lesson:** Reasoning about a program means writing statements about its states, and those statements are built out of the same vocabulary the program is: the conditions, the arithmetic, the lookups. This only works if the two vocabularies are actually the same one. The moment an expression can be written in the program that cannot be written in an assertion, the correspondence is broken, and it is broken in the worst possible way — not with an error message, but with a silent hole in the region your reasoning covers. So the interchangeability of the expression language and the assertion language is not a convenience. It is the load-bearing assumption underneath the entire method, and it should be defended as such.

What breaks it is any expression whose evaluation changes the state. An assertion is a claim about a state; it has no place to put a state change. An expression that assigns while it produces a value therefore has no meaning inside an assertion at all, and once the language admits such expressions, you can no longer say "an assertion may contain any expression" — you have to say "any expression except the ones that do this," and every rule you have written down needs that exception grafted onto it. A construct that lets a statement hide inside an expression looks like a small ergonomic gain and costs you the uniformity of the whole logic.

The practical response is to define the language you *use* as a subset of the language you *have*, and to be explicit that the subset is chosen by what the proof rules can survive rather than by taste. The same discipline decides other cases in the same direction: a parameter mode that writes back through its argument is refused for the same reason, since it makes an argument position both a value and a destination. The general rule is that when a feature would force you to split "expression" into two kinds — the ones you can reason with and the ones you cannot — the feature is more expensive than it looks, and the honest accounting is to give it up rather than to give up the uniformity.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.1.8 on function procedures, where block expressions are noted to permit expressions with side effects, and the argument that beyond making programs hard to understand these invalidate the whole approach to specification and proof, which relies on the assumption that any expression writable in the programming language can also appear in an assertion, so that an expression with side effects occurring in an assertion is meaningless and the feature would undermine the rigor of the logic; followed by the decision to use neither block expressions nor call by result for function procedure parameters.
