---
type: lesson
title: "A parameter you never do anything to can accept any phrase, and that is how control structures become library code"
figure: reynolds
works: [the-craft-of-programming]
axes: [primitive-count, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A parameter you never do anything to can accept any phrase, and that is how control structures become library code

**Lesson:** Ask what a component actually does to each of its parameters, not what kind of thing you imagined putting there. If a parameter is only ever *invoked* — never applied to arguments, never inspected, never taken apart — then the only requirement on whatever is substituted for it is that the substitution leave the surrounding text well formed. And that requirement is met by an entire syntactic category, not just by the named things you had in mind. A parameter position you thought accepted "a procedure with no arguments" in fact accepts any statement whatsoever; the analogous position on the value side accepts any expression. Nothing was added to make this true. It fell out of noticing that the constraint you assumed was never enforced by any use.

The consequence is larger than a convenience. Once a parameter position admits arbitrary statements, a procedure can take a body and a condition and impose an execution pattern on them — and now the repetition construct your language does not provide is an ordinary declaration rather than a request to the language designers. The direction of dependency inverts: control flow stops being a fixed vocabulary of built-in shapes and becomes something written in the language, by users, in the same notation as everything else. The built-in loop itself is then explicable as one particular such procedure, which is the strongest possible evidence that it never needed to be primitive.

Two things make this pay rather than merely amuse. First, the position has to be *classified* — written down as admitting statements, or expressions, so a checker can tell you at compile time when the wrong kind of phrase arrives; an unstated generalization is an accident waiting for a caller to discover. Second, substitution has to be the actual semantics, not an approximation of it, because the whole argument rests on "replace the identifier by the phrase and the program still means what it should." Languages that evaluate arguments before substituting them lose the property and, with it, the ability to build control abstractions out of ordinary procedures. Where you get to keep it, the language's list of primitive constructs can be much shorter than it looks.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.1.7 on procedure parameters, where the parameterless case is observed to remain syntactically correct under replacement of the formal by any statement, so the specifier establishes the phrase type statement and an actual parameter may be an arbitrary statement; the resulting repeat and iterate procedures presented as descriptions of control mechanisms with the forward reference to viewing the for statement as a call of iterate; Section 3.1.8's identical observation for the value side; and Section 3.1.9's summary that every binder establishes a phrase type which determines the admissible contexts, so that the copy rule's substitution is always type-correct.
