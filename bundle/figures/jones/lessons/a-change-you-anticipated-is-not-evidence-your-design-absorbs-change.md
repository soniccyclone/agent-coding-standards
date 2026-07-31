---
type: lesson
title: "A change you anticipated is not evidence your design absorbs change"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A change you anticipated is not evidence your design absorbs change

**Lesson:** The usual way to demonstrate that a design tolerates change is to build it, then apply a change, then observe how little had to move. It is a fair-looking experiment and it is nearly always rigged. The person running it knew about the change before the design existed — that is why they picked it as the demonstration — and the seams the change slides through are the seams they put there for it. The result tells you the designer can anticipate a change they have already anticipated. It tells you nothing about the property being claimed, which is behaviour under changes nobody had in mind.

This matters beyond the honesty of demos, because the same self-deception operates silently during design. Every argument of the form "and if requirement X ever changes, we are fine" is evidence about X and about nothing else, and the whole value of the flexibility claim rests on the changes you did not enumerate. A design that has been decorated with parameters and hooks at all the places its author could imagine variation is not thereby flexible; it has recorded its author's imagination. Real evidence has an awkward shape: it arrives later, from outside, unchosen, and the useful data is how much of the design record survived contact with it.

So the discipline is to weight evidence by its provenance. Treat a change you invented as an exposition device — good for showing a reader how a modification would be worked through, worthless as a measurement. Treat a change that arrived from a real user, a real performance failure, or a real environment shift as the only kind that counts, and record what it actually cost: which level of the design it re-entered at, how much below that level had to be redone, and whether the existing record was good enough to reason on or had to be reconstructed first. That record accumulates into the only honest account of how change-tolerant the thing is, and it is the account nobody keeps.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 18's "Modifications" section, which reports that the original technical report developed Earley's recognizer ignoring optimizations and then simulated a change by introducing the look-ahead idea, and immediately concedes that although this made some useful points it was unfair because the design had already been thought out with that change in mind; contrasted in the same section with the later real modification, prompted by unacceptable performance on a large PL/I grammar, which was worked out and documented against the existing development record before any code was written.
