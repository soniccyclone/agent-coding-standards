---
type: lesson
title: "What you may freely rename is exactly what you do not depend on"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# What you may freely rename is exactly what you do not depend on

**Lesson:** A procedure's meaning must not depend on which names its author chose for its parameters — an apparently trivial requirement whose consequences are not trivial at all. It forces those names to be local, because if they were not, a helper's choice of parameter name could collide with a caller's and the caller's behaviour would depend on which version of the helper was in use, which destroys the black box outright.

Turn the requirement around and it becomes a diagnostic. The names you may consistently rename without changing meaning are precisely the ones the definition does not depend on. The names you may not rename are precisely its real dependencies on the outside world. That gives you a mechanical way to read off what a piece of code is coupled to: not by inspecting imports or reading documentation, but by asking which identifiers could be swapped for arbitrary fresh ones. Everything that survives that test is internal scaffolding; everything that fails it is an assumption about a shared environment.

The renaming rule also has a trap the authors point out, and it is worth internalizing because it appears wherever substitution happens. Renaming is only safe while it keeps the two categories distinct: rename a parameter to a name the body already uses freely and you *capture* it, converting a dependency on the outside world into a reference to a local value. The code still compiles, the meaning has changed, and nothing announces it. This is why consistent renaming is famously difficult to define rigorously despite sounding obvious, and why the same class of bug recurs in macro systems, template engines and any tool that splices text into a context it did not write.

The transferable practice: to find out what a component truly depends on, try to rename everything, and treat what resists as the dependency list — then check that no renaming has quietly turned an external reference into a local one.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1 section 1.1.8's treatment of local names, which argues that the meaning of a procedure must be independent of its author's choice of formal parameter names and therefore that those names must be local; distinguishes bound from free variables and defines scope; notes that a definition's meaning does depend on the names of its free variables; and gives the capture example in which renaming a parameter to `abs` would turn a free variable into a bound one and introduce a bug — with the footnote that famous logicians have made embarrassing errors formalizing consistent renaming.
