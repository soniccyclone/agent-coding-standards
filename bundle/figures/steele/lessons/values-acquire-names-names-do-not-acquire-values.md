---
type: lesson
title: "Think of a value as acquiring names rather than a name as acquiring values"
figure: steele
works: [lambda-the-ultimate-declarative]
axes: [cognitive-load, hardware-affinity, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Think of a value as acquiring names rather than a name as acquiring values

**Lesson:** The habitual mental model of a variable is a box: a named location whose contents change over time. This work inverts the relation. What actually exists during a computation is a set of quantities; names are labels that get attached to those quantities, sometimes several at once, over regions of program text. Introducing a procedure's parameter is not creating storage and filling it — it is granting an additional name to a quantity that already exists, and simultaneously declaring how far that name reaches. Under this reading, binding is a purely declarative act with no runtime content whatsoever, which is why it can compile into no instructions at all.

Two consequences follow that are hard to reach from the box model. First, the distinction between a variable the programmer wrote and a temporary the compiler invented evaporates: both are names for intermediate quantities, and a compiler can put them in one pool and let a value live wherever is convenient, including in several places at once with no copy privileged as the real one. Whether the programmer named a subexpression or left it anonymous makes no difference to the generated code, which is exactly the property you want, and it explains on principled grounds a register-allocation technique that had been used without justification. Second, names stop being semantically load-bearing. If you could draw arrows from where a quantity is produced to where it is used, you would not need names at all; they are a textual convenience for expressing that graph, and they are gone by the time anything runs.

For a programmer the shift shows up as a different default. Introducing a name to hold an intermediate result costs nothing and should be done freely for the reader's sake, because the name is annotation on a data-flow edge rather than an allocation. Conversely, reasoning about a program by tracking "what is in this variable now" is reasoning in the wrong currency — it invites the belief that reassignment is fundamental, when most reassignment is just a second quantity wearing a name the first quantity used to wear. Genuine state, the kind where an update must be observable to someone else, is then visible as the small and separate thing it actually is, rather than being confused with ordinary naming.

**Source:** [Lambda: The Ultimate Declarative](../works/lambda-the-ultimate-declarative.md) — the section presenting variable binding as a renaming operation, including the worked example of merging user variables and compiler temporaries into shared preference classes for register assignment.
