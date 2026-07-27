---
type: lesson
title: "Decide what kind of program you are writing before deciding what 'correct' means for it"
figure: lehman
works: [programs-life-cycles-and-laws-of-software-evolution]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Decide what kind of program you are writing before deciding what "correct" means for it

**Lesson:** Arguments about whether proof is worth anything usually dissolve once you notice that the disputants are talking about different species of program. Sort programs by what stands in judgment over them. In one species, a formal statement of the problem is the whole arbiter: the program is a solution to a stated problem, and nothing outside that statement has standing. In a second, the problem can be stated precisely but no implementable solution can honor the statement, so the program necessarily approximates and its worth is settled by comparing its output against the world. In a third, the program takes over some part of human activity, and the only judge is human satisfaction in the setting where it runs. These are not points on a scale of difficulty; they differ in what kind of claim "this works" even is.

The consequence is that a single word — correctness — is doing three incompatible jobs. For the first species it names a relation between two artifacts, decidable in principle, and a program of that kind is always provable in principle even when a particular proof attempt is too long or plain wrong. For the other two it names a judgment about fit with an external reality that cannot be described without abstraction, so a formally impeccable program can be worthless and a formally broken one can be entirely serviceable. Deploying proof machinery against the second and third species as wholes is not rigor but a category error, and dismissing proof because it fails there is the same error read backwards.

A programmer who takes this seriously stops asking "is this verified" as a uniform question. Instead they locate the boundary in their own system where the arbiter changes, and they let the choice of technique follow the arbiter rather than fashion: proof and specification discipline where the specification really is the last word, measurement of behavior against the world where it isn't. They also stop treating a change of requirement as an error. If the judge is the world, and the world's judgment has shifted, the earlier program was not wrong; it was answering an earlier question honestly.

**Source:** [Programs, Life Cycles, and Laws of Software Evolution](../works/programs-life-cycles-and-laws-of-software-evolution.md) — the classification section that introduces the three program types and, immediately after, the section on what verification and proof mean differently for each of them.
