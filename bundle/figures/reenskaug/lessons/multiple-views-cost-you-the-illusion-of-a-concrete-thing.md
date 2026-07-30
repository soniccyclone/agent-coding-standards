---
type: lesson
title: "Showing two views of one thing at once costs the feeling that the thing is real, and that is a choice to make deliberately"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems]
tags: [lesson]
---
# Showing two views of one thing at once costs the feeling that the thing is real, and that is a choice to make deliberately

**Lesson:** A direct-manipulation interface works by convincing someone that the information *is* an object — visible, in one place, responding to being handled. Splitting presentation from underlying information buys the ability to show several presentations of the same thing simultaneously, which is genuinely powerful. It also breaks that conviction, because a thing you can see twice at once, in two forms, is manifestly not a physical object, and the illusion of concreteness quietly stops doing its work.

What makes this more than a curiosity is that the trade is real, both directions are defensible, and the choice is yours rather than the framework's. Someone whose work already involves several representations of one underlying thing — a planner moving between a network of activities, a bar chart against time, and a form of attributes — loses nothing, because their mental model was never a single concrete object. Multiple views match how they already think. Someone whose task is well served by treating the information as one manipulable thing loses something real, and for them the illusion is worth protecting.

And it *can* be protected without giving up the underlying separation: constrain the interface to show only one presentation of each thing at a time. The capability stays available for the cases that need it while the default preserves concreteness. That is the transferable shape — a mechanism's power and the experience it produces can pull in opposite directions, and the resolution is usually not to pick one globally but to keep the mechanism and put a policy in front of it. So when you find yourself defending a capability on grounds of flexibility, it is worth asking separately what the flexibility costs the person using it, and whether a restriction at the surface could keep both.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9's discussion of Model-View-Controller, which notes that the direct-manipulation illusion of concrete information objects is broken when a user has several views of the same object simultaneously, observes that this is of no concern to the professional planner who already manipulates multiple views of the same plan manually, and points out the illusion can be retained by constraining the interface to show one view of each object at a time.
