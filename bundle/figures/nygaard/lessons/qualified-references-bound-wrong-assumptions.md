---
type: lesson
title: "Constrain What A Pointer May Denote, And Check At Runtime What You Cannot Prove"
figure: nygaard
works: [simula-67-common-base-language]
axes: [verifiability, expressiveness, hardware-affinity]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Constrain What A Pointer May Denote, And Check At Runtime What You Cannot Prove

**Lesson:** Among the requirements the report sets for itself is a blunt one about debugging: the largest source of wasted effort in the languages of the day was accessing data through a reference under a mistaken belief about what it pointed at, and the language plus its compiler should refuse to carry out such an access rather than proceed. The mechanism is to make every reference variable carry a declared restriction naming the family of things it may denote, so an access through it is meaningful by construction, plus a distinguished value for "denotes nothing" that is always in range and therefore always a case the programmer must face.

The interesting part is how the design behaves where static reasoning runs out. Assigning between references whose declared restrictions sit at different levels of the same family splits into cases: one direction is always safe and simply permitted, the reverse direction is permitted but the failure it can cause becomes a defined runtime error rather than silent corruption, and a pairing whose restrictions are unrelated is rejected outright at compile time. The same three-way treatment recurs for explicit narrowing and for parameter passing. Nothing is quietly widened to make the check go away, and nothing is banned merely because it cannot be settled in advance. The report is equally candid about where safety was traded off deliberately: the reference notion is withheld from plain values, and the stated reason is machine efficiency, with an acknowledgment that a reference is in simple cases just an address.

A programmer who works this way puts the intended range of a pointer into its declaration instead of into a comment or a convention, and treats the empty case as a first-class value rather than a bug waiting to happen. When a desirable operation cannot be shown safe statically, the response is neither to forbid it nor to allow it unchecked, but to allow it with a defined failure — a runtime error at the exact point of violation beats corruption discovered three modules later. And when a safety property is given up for machine reasons, it is written down as a decision with a stated cost, so that the next reader can weigh it instead of inferring that nobody thought about it.

**Source:** [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the introduction's demand for reference security, the chapter on types and variables where object references are given a qualifying class, and the case analysis of reference assignment legality with its explicit runtime-error branch.
