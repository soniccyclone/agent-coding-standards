---
type: lesson
title: "Treat undefinedness as a first-class semantic outcome, and let evaluation order be part of the meaning rather than an implementation detail"
figure: mccarthy
works: [recursive-functions-of-symbolic-expressions, a-basis-for-a-mathematical-theory-of-computation]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Treat undefinedness as a first-class semantic outcome, and let evaluation order be part of the meaning rather than an implementation detail

**Lesson:** Any formalism honest enough to describe real computation has to admit that some computations do not finish, and therefore that some expressions have no value. The interesting move is what you do with that admission. If you specify a branching construct by saying its tests are examined in order and that only the selected branch is evaluated, then undefinedness is contained: an expression can name a hopeless subcomputation and still have a perfectly well-defined value, because the hopeless part is never reached. That single stipulation is what lets a function be defined by an equation mentioning itself without circularity — the base case is selected before the recursive case is ever touched, so the definition bottoms out instead of unwinding forever.

The consequence people find surprising is that logical connectives built on such a branching construct stop being commutative. Conjunction with a false left operand and a divergent right operand has a value; swap them and it has none. That asymmetry is not a defect to be patched but the correct semantics for a world where operands are computed, and it should be chosen deliberately rather than inherited by accident from whatever order the compiler happened to emit. The general principle: whenever a construct's operands may fail to terminate, the order in which they are consulted is part of what the construct *means*, and a specification that leaves it open has not specified the construct at all.

This also explains a design attitude toward notation gaps. The reason such a construct needed inventing was that existing mathematical notation could express how truth values depend on quantities but not how quantities depend on truth values, so authors dropped into English prose exactly where the symbolic language ran out. A programmer who takes that seriously reads their own fallback into commentary as evidence of a missing construct: if you have to explain in prose what your formalism cannot state, that gap is a design defect, not a writing problem. And a programmer who takes the undefinedness point seriously writes recursive definitions confident that the guard discipline, not a termination argument bolted on afterward, is what makes them well-founded — and knows which of their operators they may not reorder.

**Source:** [Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I](../works/recursive-functions-of-symbolic-expressions.md) — the section motivating conditional expressions from the inadequacy of existing notation, its rules for when such an expression's value is undefined, and the follow-on derivation of the propositional connectives with its explicit note on non-commutativity. Also [A Basis for a Mathematical Theory of Computation](../works/a-basis-for-a-mathematical-theory-of-computation.md), where the same treatment of partial functions and conditional forms is developed as the ground layer of a proof system.
