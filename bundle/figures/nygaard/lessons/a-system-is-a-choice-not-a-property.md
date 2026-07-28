---
type: lesson
title: "Nothing Is Inherently A System; You Decide To See One"
figure: nygaard
works: [program-development-as-a-social-activity]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Nothing Is Inherently A System; You Decide To See One

**Lesson:** Nygaard refuses to let "system" name a feature of reality. A stretch of the world becomes a system only when somebody, for some purpose and some stretch of time, elects to regard it as a whole made of parts, picks which properties of those parts count, and picks which interactions between them count. Every one of those picks is discretionary, and a different modeller with a different purpose would carve the same territory into different components with different relevant properties, both carvings being correct.

This holds because the boundary, the component list, and the property list are not observable in the material — they are the residue of a decision about what to attend to and what to ignore. That is why arguing over whether something "really is" one system or three is unproductive, and why two competent designers can produce incompatible decompositions of the same domain without either having made a mistake. It also means a decomposition can be locally faithful and still wrong, if the properties it declared irrelevant turn out to be the ones the problem hinges on.

A programmer who takes this seriously stops treating the object model as a discovery and starts treating it as a commitment with an author and a rationale. Before defending a design they name the purpose it was selected for and the properties it deliberately drops, so both are available for challenge. They expect to hold more than one decomposition of the same domain simultaneously rather than converging prematurely on the first one, and they read a legacy model as evidence of what its authors cared about rather than as a description of the world. The cost of the discipline is real: keeping the chosen frame visible is more work than forgetting it was chosen, but the alternative is mistaking your own selection criteria for facts.

**Source:** [Program Development as a Social Activity](../works/program-development-as-a-social-activity.md) — the definitional core of the lecture, where the "system" definition is stated as a person's choice of whole-and-components and immediately contrasted with definitions broad enough to make everything a system.
