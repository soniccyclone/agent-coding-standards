---
type: lesson
title: "An abstraction may hide data, never control flow: a construct that looks like a call must behave like one"
figure: torvalds
works: [linux-kernel-coding-style]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# An abstraction may hide data, never control flow: a construct that looks like a call must behave like one

**Lesson:** The style guide draws a hard line through the space of things a macro can do. Wrapping up a computation is fine; wrapping up a jump out of the enclosing function is condemned outright, on the explicit grounds that it breaks the model a reader builds while scanning code. That is a claim about what kind of concealment is legitimate. Readers of a program run an internal parser: they see a name followed by parentheses and commit, without conscious thought, to the belief that control returns to the next statement. An abstraction that violates that belief does not merely surprise them, it invalidates every inference they drew downstream of it, and no amount of documentation repairs the damage because the reader never stopped to consult documentation in the first place.

The same reasoning powers the neighbouring prohibitions, which look like a grab bag until you see the pattern. A construct that silently reads a variable from the caller's scope makes a hidden dependency that breaks under innocuous edits. One that can appear on the left side of an assignment is relying on a substitution property no ordinary function has, so it cannot later be converted into one. One that evaluates its argument more than once turns a harmless-looking call site into a bug the moment the argument has side effects. One that leaks an ordinary variable name into the caller's scope collides with whatever the caller happened to call things. In every case the violation is the same: the construct presents itself as a member of a familiar category and then does something no member of that category can do. The stated remedy — prefer a real function, since the compiler will inline it anyway — is the general answer, because a real function's contract is enforced rather than promised.

Why this holds more strongly than an aesthetic preference: the categories readers use to skim code are the only thing that makes large systems navigable at human speed. Nobody expands macros mentally at every call site, and nobody re-derives evaluation order per argument. Those shortcuts are what allow a person to read code faster than they could write it, and they are correct only if abstractions honour their apparent category. Data hiding is compatible with that — you can be ignorant of a structure's interior and still predict control flow perfectly. Control-flow hiding is not.

A programmer who believes this applies a category test to every abstraction they build: what will a reader assume about this from its shape alone, and is every one of those assumptions true? Anything that fails becomes either a construct whose name announces its strangeness or, better, a plain function that no longer needs the warning.

**Source:** [Linux Kernel Coding Style](../works/linux-kernel-coding-style.md) — the macros chapter, particularly its list of things to avoid: macros affecting control flow, macros depending on magic local names, macros usable as assignment targets, precedence and multiple-evaluation hazards, and local-name collisions; and its standing preference for inline functions over function-shaped macros.
