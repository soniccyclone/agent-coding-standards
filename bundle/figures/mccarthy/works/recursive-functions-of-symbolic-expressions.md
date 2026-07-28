---
type: work
title: "Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I"
figure: mccarthy
description: The founding paper of Lisp, defining S-expressions as a uniform representation for both data and program, and showing how a small set of primitive functions (car, cdr, cons, atom, eq, cond) plus lambda notation suffice to define eval — an interpreter for the language written in the language itself. It grew out of McCarthy's work on formalizing computation using recursive function theory rather than out of a deliberate language-design effort. A planned Part II, meant to cover further formal results, was never published.
subdomains: [programming-languages-and-semantics, foundations-of-computation]
year: 1960
url: https://www-formal.stanford.edu/jmc/recursive.pdf
extraction: complete
survey_pages: 34
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I

**Venue/year:** Communications of the ACM 3(4), April 1960, pp. 184-195.
**Source:** https://www-formal.stanford.edu/jmc/recursive.pdf — live PDF, self-archived on McCarthy's Stanford Formal Reasoning Group page (www-formal.stanford.edu/jmc/), confirmed 200 OK.

## Lessons
- [Look for the handful of operations that generate everything, then earn the rest by derivation instead of decree](../lessons/find-the-closed-basis-then-derive-everything.md)
- [Choose one data representation general enough to hold your own programs, and the interpreter becomes an ordinary function](../lessons/one-representation-for-program-and-data.md)
- [Treat undefinedness as a first-class semantic outcome, and let evaluation order be part of the meaning rather than an implementation detail](../lessons/undefinedness-belongs-in-the-semantics.md)
- [Two formalisms of identical power can still be unequal designs: judge a basis by which operations it makes elementary](../lessons/equal-power-is-not-equal-structure.md)
- [If a bookkeeping fact is derivable from the program's own structure, make the machine derive it instead of making the programmer track it](../lessons/let-the-machine-compute-what-the-machine-can-know.md)
