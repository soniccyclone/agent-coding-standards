---
type: lesson
title: "A pure function's contract is an equation; a state-changing procedure's contract is a theorem you must prove"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# A pure function's contract is an equation; a state-changing procedure's contract is a theorem you must prove

**Lesson:** Look at what has to be established before a caller may rely on a component, and the two familiar kinds of component come apart sharply. For something that changes state, the useful fact about a call — that starting in such a situation it lands you in such another — is a claim about behaviour over time, and it has to be *proved* from the body; there is real work between having the code and having the fact. For something that only computes a value, the corresponding fact is that a call equals the body with the arguments put in. That is not something you prove; it is what the declaration means. The contract is an equation, available immediately, at no cost.

This is a better account of why purity pays than the usual appeals to tidiness. The saving is not that pure code is easier to read, though it is; the saving is that an entire proof obligation disappears and is replaced by a substitution you may perform whenever you like. Because the equation does not mention the state, it holds at every moment, which means it can be used inside any argument, in any order, without tracking where you are in the execution. Reasoning about a state-changing component is confined to the sequence of steps it participates in; reasoning about a value-computing one is free of that sequence entirely.

Two consequences follow for how you carve a system. First, when deciding whether some piece should change state or return a value, weigh in the verification asymmetry, not just the ergonomics: you are choosing between an obligation and an identity. Second, the boundary has to be defended, because the equation is only true if calling really does nothing but produce a value — the moment evaluation can also change something, the equation is false and everything built on it collapses. That is the same reason self-reference is refused in this setting: an equation is worthless if the left-hand side might fail to denote anything. Purity is not a style preference here; it is the precondition under which the cheap form of contract exists at all.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.3.14 on inference for function procedures, which notes that the concrete rule is simpler than the one for proper procedures because for a proper procedure the main part of the assumptions embodies a property that must be proved about the body, whereas for a function procedure the corresponding property is self-evident — that the value of any call equals the value of the body after the appropriate substitutions — and, being independent of the state, can be expressed as a static assertion of equality; together with the closing note that neither form of the rule permits recursion, for the reasons given in Section 3.2.5.
