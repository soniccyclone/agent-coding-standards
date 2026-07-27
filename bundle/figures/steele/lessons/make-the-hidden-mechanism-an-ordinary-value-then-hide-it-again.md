---
type: lesson
title: "To gain control of a hidden mechanism, rewrite it as an ordinary value you pass around — then let the notation hide it again"
figure: steele
works: [lambda-the-ultimate-imperative]
axes: [expressiveness, parallelizability, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# To gain control of a hidden mechanism, rewrite it as an ordinary value you pass around — then let the notation hide it again

**Lesson:** Every language runs on machinery its users never name. There is an invisible answer-goes-here that each expression's result is delivered to. There is an invisible chain of pending work. In some dialects there is an invisible stack of name bindings visible to callees. The technique this work develops over and over is to take one of these invisible mechanisms, make it an explicit extra argument that every procedure receives and passes along, and see what becomes possible. Once the destination of a result is an ordinary argument, an early exit is just handing the result to a different one of two available destinations rather than a new control construct. Once the set of dynamically visible bindings is an ordinary argument — a table, or even better a function you interrogate — you can have both dynamic and lexical scoping in the same language at the same time, which no choice of closure discipline can give you, because the discipline forces one answer for all free variables at once.

The reification also exposes what the implicit version concealed. When results are delivered explicitly, the order in which operations happen appears literally in the text, temporary values that had to survive across other computations acquire visible names, and the dependence on the language's argument-evaluation rule disappears altogether — the work proves the last point, and it is precisely the kind of order-independence that determines whether pieces of an expression can be evaluated in any order at all. Nothing is added by the rewrite; the information was always there, held in a mechanism nobody could point at.

The lesson is completed by its second half, which is easy to miss and matters more in practice. Having shown how to pass a context argument everywhere, the work observes that the argument carries almost no information at most call sites, and that a notation which lets you suppress exactly that kind of low-information detail is a good notation. The recommended discipline is therefore not to write in the reified style but to understand in it: reify to see the mechanism and to define what it means, and then push it back under a notation once its behavior is settled. A programmer who works this way debugs implicit machinery by temporarily making it explicit, and evaluates language and library designs by asking which mechanisms they let you name when you need to and stop mentioning when you do not.

**Source:** [Lambda: The Ultimate Imperative](../works/lambda-the-ultimate-imperative.md) — the continuations section, which converts result-delivery into an explicit parameter and then models escapes and dynamically scoped variables with it, together with the remark on judging a notation by what it lets you leave unwritten.
