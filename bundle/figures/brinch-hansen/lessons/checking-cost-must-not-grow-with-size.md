---
type: lesson
title: "Choose structures whose checking cost per part does not depend on how many parts there are"
figure: brinch-hansen
works: [operating-system-principles]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Choose structures whose checking cost per part does not depend on how many parts there are

**Lesson:** There is a crude scaling argument that decides more architecture than most style debates do. If every part of a system may interact with every other part, then convincing yourself one part is correctly connected requires examining its relationship with all the rest, and the total effort grows with the square of the part count. If instead the parts are connected only through a fixed set of constraints, so that checking one part means checking it against the constraints rather than against its peers, the per-part effort is constant and the total grows linearly. The two regimes are not degrees of tidiness. One of them has a ceiling beyond which reliable construction is impossible, and the other does not, which makes the choice between them the first architectural decision rather than a refinement of later ones.

Taking the argument seriously means designing the interface rules before designing the parts, because the whole benefit lives in the rules being uniform, small, and stated in advance. It also means treating any component whose correctness depends on knowing the behavior of many specific siblings as a defect in the structure rather than a difficult component. And since the effort in question is human effort, the constraints have to be written down precisely enough that two people check against the same thing. A group that intends a simple structure but leaves the assumptions at each boundary to verbal agreement gets neither regime: each member independently invents assumptions about the others' components, some of them wrong, and the coupling they carefully avoided in the design shows up in the code anyway.

The same reasoning explains why this discipline matters most exactly where it feels least affordable. Systems get modified for their entire lives, by people who did not build them, for reasons nobody anticipated — understanding improves and moves the goal, technology changes and moves the tools, and the builders' own limits guarantee errors along the way. Under those conditions the ability to predict the effect of a change is what reliability actually consists of, and that ability is a direct function of how much of the system a change forces you to hold in mind.

**Source:** [Operating System Principles](../works/operating-system-principles.md) — the section on abstraction and structure in the chapter on sequential processes, where the two connection regimes are compared step-for-step and the conclusion is drawn that only structures with per-component verification cost are viable at scale, followed by the argument about undocumented assumptions between members of a design group.
