---
type: lesson
title: "Familiarity is something you can manufacture, so stop imitating the physical world"
figure: sutherland
works: [the-ultimate-display]
axes: [expressiveness, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Familiarity is something you can manufacture, so stop imitating the physical world

Human competence with a domain comes from repeated exposure, not from talent. We predict the arc of a thrown ball accurately because we have thrown thousands of them; we predict nothing about behavior in a non-uniform field because nobody's body has ever been in one. Sutherland's argument is that this asymmetry is an accident of which phenomena happen to be big, slow, and tangible — and that a machine that renders a model into a sense we already trust converts an unfamiliar regime into a familiar one. Intuition is not a fixed endowment you design around. It is a thing you can build for a domain that never had it.

The consequence for the programmer is the opposite of the instinct most people bring to representation work. If the point of rendering a model is to grow intuition where none exists, then loyalty to physical plausibility is a waste of the only real advantage: the model does not have to obey the rules of the world it depicts. Mass can be negative, solid things can be seen through, and quantities that have never had any appearance at all — an internal invariant, a dependency, a constraint relating two parts — can be given one. The rendering that most resembles reality is usually the one that teaches least, because reality is where the user's intuition already worked.

There is a second half to this: a model's internal richness is capped by the bandwidth of the channel back out to the person. Sutherland's insistence on force and sound alongside sight is not a wish list of gadgets, it is the recognition that a simulation you can only look at is throttled at the point of delivery. Pick output channels by what the model has to say, not by what the hardware happens to ship with.

A programmer who believes this treats every observability surface — a debugger view, a trace visualization, a type error, a dashboard — as an intuition-building instrument rather than a report. The test is not whether it is accurate or whether it looks like the domain, but whether someone who has stared at it for a week now guesses correctly about system behavior they have never directly observed. If it does not build that reflex, it is decoration.

**Source:** [The Ultimate Display](../works/the-ultimate-display.md) — the opening argument about the phenomena we predict well versus badly, and the later passage on displays being free of the rules of physical reality, including making Sketchpad's constraints visible things.
