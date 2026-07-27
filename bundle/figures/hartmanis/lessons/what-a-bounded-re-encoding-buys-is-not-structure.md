---
type: lesson
title: "Anything a bounded re-encoding can buy you was never part of the structure"
figure: hartmanis
works: [on-the-computational-complexity-of-algorithms]
axes: [hardware-affinity, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Anything a bounded re-encoding can buy you was never part of the structure

**Lesson:** If you can take a machine, pack pairs of adjacent symbols into single richer symbols, absorb a fixed amount of lookahead into the control state, and thereby make it do in one step what it used to do in two, then a constant factor of speed is not a fact about the problem. It is a fact about how finely you chose to slice the representation. Iterating that trick divides the running time by any constant you like, which means a cost measure taken seriously must be defined so that constant rescaling is invisible to it. The same reasoning disposes of a whole family of apparent improvements: extra reading heads on a tape, jump instructions that teleport to a marked position, permission to emit several output digits at once. Each of these can be reproduced by another machine with bounded extra bookkeeping per step, so none of them changes which problems sit in which class.

The general discipline is to ask, of every proposed extension or optimization, whether it can be simulated by the unextended system with a bounded amount of per-step work. If it can, the extension is a convenience: it may matter enormously to a deadline, but it carries no information about the difficulty of the task and must not appear in the vocabulary you use to reason about difficulty. Building the measure this way is what makes conclusions survive the things a designer does not control, including component speed, word width, alphabet size, and the encoding chosen for input and output. A cost model that moves when the hardware generation changes was measuring the hardware.

The programmer who works this way separates two conversations that are usually conducted as one. There is the question of which growth class a design falls in, where a two-times win is noise and only a changed exponent counts as news, and there is the question of whether a specific workload fits in a specific machine before a specific deadline, where a two-times win is the whole job. Mixing them produces both kinds of error: agonizing over micro-optimizations that cannot rescue a hopeless asymptotic, and dismissing as "just a constant" the factor that decides whether the system ships. Knowing which conversation you are in is the skill.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the speed-up theorem and its corollaries, where linear rescaling of the time bound leaves the class fixed, together with the results on multihead machines and jump-style instructions that leave the classes unchanged.
