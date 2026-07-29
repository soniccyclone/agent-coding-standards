---
type: lesson
title: "Of the programs that work, confine yourself to the ones you can understand — the machine will accept far worse"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Of the programs that work, confine yourself to the ones you can understand — the machine will accept far worse

**Lesson:** Consider every program a given machine could execute — every bit pattern in memory, started from every possible entry point. The count is astronomical and the machine regards all of them as legal. An infinitesimal fraction of that set does anything a person would call meaningful, and the natural conclusion is that programming means finding your way into that fraction. The sharper claim is that the meaningful set is *still* too large to be acceptable, because the behaviour of most programs in it lies beyond any human's grasp. What you should actually restrict yourself to is a small region inside the meaningful set: the programs that work *and* that someone can follow.

The consequence is a reversal of where the constraint comes from. A correctness-only discipline treats comprehensibility as a nice-to-have, something to improve once the thing works. This argument makes it a membership condition: a program you cannot follow has not qualified, however faithfully it produces the right answers, because you have no way to establish that it will keep producing them under circumstances you have not tried. The tragedy of the field, in the formulation this rests on, is that for any given problem there is essentially one right solution and an enormous number of others that also work — and nothing in the machine's behaviour distinguishes them for you.

That is also the answer to why one would ever write a description of a program beyond the program itself. Not because the code is imprecise — the code is the only fully precise artifact there is, and for a problem simple enough to yield simple code, nothing beats reading it. Higher-level descriptions become necessary exactly when the structure of the thing outgrows what a mind can hold, which means every methodology, every notation, and every diagram is aimed squarely at a human audience. The machine does not know about any of it; it is executing bit patterns. So when you judge a description technique, the only question that matters is whether it makes a person's understanding of the system more reliable, and any defence of it that appeals to what the computer needs has changed the subject.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 4's discussion of why high-level descriptions exist at all, which builds the three nested sets (all executable programs, the meaningful subset, the understandable subset) and attributes the central insight and the accompanying epigram about one correct solution among many that work to a seminar by M. A. Jackson; the surrounding argument that the audience of any manifest model is a human being rather than a computer is Reenskaug's own.
