---
type: lesson
title: "Write the story of someone using the thing before you specify it, and let the story generate the requirements"
figure: kay
works: [a-personal-computer-for-children-of-all-ages]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Write the story of someone using the thing before you specify it, and let the story generate the requirements

**Lesson:** A specification written first is a list of capabilities in isolation, and it silently assumes an idealized user who wants exactly those capabilities in exactly that order. Narrating a concrete episode of use instead — particular people, a particular afternoon, a goal they actually have, the interruptions and mistakes included — surfaces the requirements no capability list produces, because the requirements you miss are the ones that only appear as friction inside a sequence. Wandering off-task while browsing and needing to get back; wanting to filter out what someone else wants you to see; two people needing to work against the same shared state at once; being reminded of an obligation you would rather have forgotten. None of these are features anyone requests up front, and all of them are decisive for whether the thing is usable.

The narrative also serves as a design constraint you cannot fudge. If the story requires a person to break stride and think about the machinery rather than the task, the design has failed a test that a requirements document could not have posed. And because the story is written before the parts exist, it is free to demand things you do not yet know how to build, which is the correct order: let the desired experience state the target, then find out what it costs. Building the parts first and asking what experience they add up to inverts that, and produces systems whose shape is an accident of what was easy.

Two disciplines keep this honest. The story must be specific enough to be falsifiable — real names, real numbers, an actual sequence of actions rather than a montage — because vagueness lets any design claim to satisfy it. And the technical section that follows has to state plainly which parts of the story rest on things that do not yet exist, and how far the reach is, so the fiction is a target with a labeled gap rather than a promise disguised as a plan.

**Source:** [A Personal Computer for Children of All Ages](../works/a-personal-computer-for-children-of-all-ages.md) — the opening narrative of two children extending a game program in a park and an adult working from an abstracted file on a plane, written before any specification, and the later engineering sections that price the parts against that story and name outright which of its assumptions are unbuilt speculation.
