---
type: lesson
title: "A live body of existing code is the dominant design constraint, and the concessions it extracts are permanent"
figure: ritchie
works: [the-development-of-the-c-language]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A live body of existing code is the dominant design constraint, and the concessions it extracts are permanent

**Lesson:** Ritchie's account of C is largely an account of what an existing corpus of working programs would tolerate. He states the condition plainly: the language never arrived as a clean new thing with its own rules, it was continually adapted while programs written in the previous version had to keep running. Every awkward corner he apologizes for traces to that. The rule converting arrays to pointers when they are mentioned was chosen partly because it let almost all existing code survive a change in what an array fundamentally was. The relative precedence of the new short-circuit operators was left in a position he later judges wrong, specifically so that mechanical conversion of old conditionals would not be painful — with the lasting result that testing a masked value requires parentheses everyone forgets. Empty brackets in a parameter declaration are described as a living fossil of an earlier language's way of writing a pointer, retained for compatibility and confusing learners ever since. A decade later the standards committee faced the identical bind and reached the identical kind of compromise, keeping both the old and new forms of function declaration because forbidding the old one was not feasible.

The general shape is that compatibility is not paid once at the moment of the change. It is paid forever, in the form of surface irregularity that no later cleanup can remove, because by then the irregularity is itself something programs depend on. That does not make the concessions wrong — Ritchie defends the compromise as about as good as it could have been — but it does mean the decision should be made with the permanence in view rather than as a temporary bridge.

He also shows the escape hatch. When the language could not be tightened because old code and permissive compilers were still in circulation, the response was a separate program that read whole sets of source files and complained about legal but suspicious constructions, including the cross-file argument mismatches that separate compilation could not catch. Checking that cannot live in the language can still live beside it, and shipping it is how you raise the standard of practice without breaking the corpus.

A programmer who believes this stops treating backward compatibility as a footnote to a design and treats it as the design's principal author. Before a semantic change they ask which existing usages must keep working, what irregularity buying that will introduce, and whether they would still accept that irregularity in ten years with the original code long gone. When the answer is no, they take the break early while the corpus is small. When compatibility wins, they put the enforcement in an external checker rather than pretending the rule is enforced.

**Source:** [The Development of the C Language](../works/the-development-of-the-c-language.md) — the critique section on how evolution from a typeless predecessor left compilers tolerant of type errors, together with the specific compromises over operator precedence, empty-bracket parameters, standardized function prototypes, and the introduction of a separate whole-program checker.
