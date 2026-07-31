---
type: lesson
title: "Get full machine efficiency without machine dependence by naming the machine's parameter and computing from it"
figure: hoare
works: [notes-on-data-structuring]
axes: [hardware-affinity, expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Get full machine efficiency without machine dependence by naming the machine's parameter and computing from it

**Lesson:** Portability and peak efficiency look like opposites because of how the choice is usually posed: either you write against an abstraction that hides the machine and accept whatever the hiding costs, or you write against the machine you have and re-tune for the next one. There is a third option that gets most of both, and it is available far more often than it is taken. Find the small number of hardware quantities the efficiency actually turns on — the width of the unit the machine operates on in one step, the size of the block a device transfers, the depth of the fastest storage. Obtain each as a named value from the environment rather than writing its current number into the text. Then derive every derived size, loop bound and layout decision arithmetically from those names. The program is now shaped by the machine it runs on, exactly as a hand-tuned one is, without containing any commitment to a particular machine.

What makes this work is that the machine dependence in most tuned code is not deep. It is one number, propagated. Once the number is a name, the propagation is arithmetic the program does at startup, and the same text runs at full speed across machines whose figures differ widely. The prerequisite is that you did the derivation in the open, so the value flows through the code rather than being silently assumed in the shape of a constant — a loop bound that happens to be right for the machine you tested on is the same commitment as writing the number down, just harder to find.

Two habits make the technique pay. Do the arithmetic in a form that tolerates slack: rounding a structure up to the next whole unit, so that a set or table ends up slightly larger than asked for, is usually free and removes fiddly boundary handling from every operation, provided you have checked that the surplus is genuinely harmless. And recode the innermost loop first, before committing to the rest of the representation, because the loop is where the derived layout either pays off or does not, and it is the only part whose cost can overturn the decision. Confirming that the hot path comes out acceptable is cheap; discovering it does not after everything else is written is not.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the sieve-of-Eratosthenes example in the powerset chapter, which represents the sieve as an array of word-sized sets whose dimensions are computed from an environment enquiry giving the machine's word length, accepts a slightly oversized sieve as a harmless extension in exchange for simpler arithmetic, recodes the innermost loop first to check the representation before proceeding, and closes by noting the program works with high efficiency on machines of widely varying word lengths.
