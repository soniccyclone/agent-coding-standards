---
type: lesson
title: "When a program is not supposed to end, its correctness lives in the shape of the run"
figure: pnueli
works: [the-temporal-logic-of-programs]
axes: [expressiveness, verifiability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---

# When a program is not supposed to end, its correctness lives in the shape of the run

**Lesson:** The default picture of a correct program is a function: it starts, it computes, it stops, and what it left behind matches a description of what the inputs should map to. Every proof method built on that picture inherits its blind spot. An operating system, a controller, a scheduler, a server — for these, halting is the pathology, not the goal. There is no final state to characterize, so the entire functional apparatus has nothing to say about whether they work. That is not a gap at the edge of the theory; it excludes most software that runs continuously.

The move that fixes it is to relocate the object of the claim. Stop describing what a program leaves at the end and start describing how its execution develops: the properties that must hold at every point it ever reaches, and the situations that must be followed, sometime later, by other situations. "Whenever a request arrives, a response eventually follows" is a complete and demanding correctness statement about a program that never terminates, and it says nothing about a return value. Once correctness is phrased over runs rather than over endpoints, terminating programs turn out to be the easy special case — "reaches the exit with the right values" is just one such follow-from-this pattern — rather than the normal case with the rest bolted awkwardly on.

What changes in practice is what you write down before you build. A programmer who thinks this way specifies a long-running component by naming the situations that must never coexist and the responses that must not be starved, instead of writing a signature and hoping the loop around it behaves. Bugs then become statements you can express: this system can reach a state where two holders think they own the resource; this request can be postponed forever. Both are unsayable in a formalism that only knows about inputs and results, which is why systems specified that way accumulate failure modes nobody had vocabulary for.

**Source:** [The Temporal Logic of Programs](../works/the-temporal-logic-of-programs.md) — the introduction's complaint that the classical correctness tradition addressed only functional programs with a distinct beginning and end, and the section classifying specifications, where the responsiveness property of an operating-system-shaped program is given as the general form that total correctness specializes.
