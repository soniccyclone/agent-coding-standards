---
type: lesson
title: "A system you are forced to inhabit corrects itself; one built to a requirements list does not"
figure: thompson
works: [the-unix-time-sharing-system]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# A system you are forced to inhabit corrects itself; one built to a requirements list does not

**Lesson:** The usual theory of software quality is that you elicit requirements from someone else, satisfy them, and are done. Thompson and Ritchie report the opposite causation for their own system: its success followed from having had no external objectives to satisfy, and instead from the fact that its builders were its only users and its own maintenance host. Requirements imposed from outside terminate the feedback loop at delivery. Building an environment you personally have to work in every day means every rough edge is charged to you at full price, immediately and repeatedly, which is a far more reliable signal than any specification review.

The mechanism has two parts, and both matter. First, the builders are the users, so functional gaps and merely irritating gaps both register — and the irritating ones are the kind no specification ever captures, because nobody writes down that a facility is unpleasant. Second, the system maintains itself: its own sources live on it, are edited with its editor, and are rebuilt with its compiler, so a defect in the tools is felt while using the tools to fix the defect. That closure converts self-interest into pressure that arrives early, while a design is still cheap to revise, rather than after it has hardened into something everyone routes around.

The companion observation is that harsh resource limits acted as a design collaborator rather than an obstacle. Being unable to spend memory forced choices between expressive power and bulk to be made explicitly and repeatedly, and the authors credit that constraint with the economy of the result. A designer with unlimited budget never has to decide what is actually essential and so never finds out.

A programmer who takes this seriously changes what they build first and how they judge it. They put themselves inside the artifact — using their own library in real work, running their own tool on their own repository — before broadening it, and they treat "I never actually use this" as damning evidence rather than a neutral fact. They are suspicious of a component whose builders touch it only through tests. And when a limit bites, they read it as information about what the design should not contain rather than as a problem to be spent away.

**Source:** [The UNIX Time-Sharing System](../works/the-unix-time-sharing-system.md) — the perspective section near the end, which recounts the system's origin as one person's dissatisfaction with the facilities available to him and then names the three retrospective design influences: programmers building for their own convenience, severe size limits, and the system's self-maintenance forcing its designers to feel its defects.
