---
type: lesson
title: "Choose one data representation general enough to hold your own programs, and the interpreter becomes an ordinary function"
figure: mccarthy
works: [recursive-functions-of-symbolic-expressions]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Choose one data representation general enough to hold your own programs, and the interpreter becomes an ordinary function

**Lesson:** Most language designs keep two universes apart: the data the program manipulates, and the program itself, which lives in a separate syntactic world reachable only through a compiler someone else wrote. Collapse that separation and something remarkable becomes cheap. If the language's ordinary data type is a recursively nested pair structure over atoms, then the text of a function is itself just such a structure, and the evaluator that runs it is not a privileged piece of machinery but a function of two arguments — an expression and an environment — written using the same handful of operations available to any user program. Universality stops being a metatheoretic result about machines and becomes a routine definition you can read on a page.

The reason this works is that the representation was chosen for its closure properties rather than its convenience for any single task. A pair whose components may themselves be pairs or atoms can encode a list, a tree, an algebraic expression, a set of variable bindings, a rule of inference, and a function definition, all without inventing a new type for each. What matters is not that the notation is pretty — the paper's own translation from readable function notation into the uniform form is admittedly clumsy — but that the encoding is total. Once every program is a datum, program transformation is data transformation, and writing tools that read, rewrite, differentiate, or reason about programs requires no separate parsing infrastructure.

A programmer who believes this treats "what is my universal representation?" as a design question that precedes every other. They pick the smallest structure closed under nesting that can carry all the shapes their domain produces, and they resist adding parallel special-purpose representations, because each one reintroduces the wall between the manipulator and the manipulated. They also expect to get an interpreter almost for free, and treat difficulty in writing the language's evaluator *in* the language as a diagnosis: it means the representation is not yet general enough to describe itself.

**Source:** [Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I](../works/recursive-functions-of-symbolic-expressions.md) — the definition of the symbolic-expression class as nested ordered pairs, the translation rules from function notation into that same class, and the definition of the universal function that evaluates any encoded function against encoded arguments.
