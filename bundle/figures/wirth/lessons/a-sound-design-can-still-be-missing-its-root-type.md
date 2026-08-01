---
type: lesson
title: "A sound design can still be missing its root, and the symptom is a facility you cannot write once"
figure: wirth
works: [project-oberon]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# A sound design can still be missing its root, and the symptom is a facility you cannot write once

**Lesson:** Reviews of an existing design look for errors, and when they find none they conclude the design is finished. That conclusion skips a whole category. A structure can be correct in every particular — each of its types well chosen, each of its operations right — and still be leaving most of its leverage unclaimed, because the types were introduced independently and share no declared ancestor. Nothing is broken. There is simply no place to attach anything that ought to apply to all of them. The absence is invisible to the kind of review that hunts for defects, because an absence produces no wrong behaviour; it produces work that keeps having to be done again.

That is the symptom to learn to recognize. If you find yourself writing the same facility a second and third time for kinds of thing that have nothing to do with each other — a way of writing them to a file and reading them back, a way of naming their attributes, a way of asking one of them for a copy of itself — the repetition is not telling you to write a utility library. It is telling you the types are siblings and you never said so. Give them a common ancestor and each of those facilities becomes expressible once, phrased against the ancestor, with the per-kind residue pushed down into the kinds. The gain is not proportional to the size of the ancestor. An ancestor that declares almost nothing can unlock persistence, containment, uniform naming and generic composition all at once, because what those facilities needed was never behaviour — it was a type to be about.

Two disciplines keep this from becoming a licence to root everything. First, the ancestor must be introduced for facilities you have actually failed to write, not for facilities you imagine wanting; a root invented in advance of the repetition will get the wrong obligations attached to it, and every kind will pay for members that serve nobody. Second, retrofitting a root is only cheap when the existing kinds already behave the same way and the change is one of declaration — deriving what was independent, not reworking what was different. If making the kinds derivable requires changing what they do, you are not naming a family that existed; you are inventing one, and that is a different and much larger project.

The general habit: when auditing a design that seems sound, ask separately whether it is wrong and whether it is under-exploited. Those are different questions with different evidence. Wrongness shows up as failures. Under-exploitation shows up as duplication that everyone has stopped noticing because each instance seemed locally reasonable.

**Source:** [Project Oberon](../works/project-oberon.md) — appendix A's opening retrospective on the runtime model of chapters 3, 4 and 5, judged basically flawless and sustainable while later developments revealed unused potential, the main shortcoming being the absence of a generic object type serving as an abstract root of the entire object hierarchy; and the remedy of adding a module exporting two abstract types from which previously independent types were then derived by type extension, described as a simple extension of the kernel with an amazingly beneficial effect that enabled a generic persistence mechanism, a generalized notion of text, a hierarchic component framework and a new graphical user interface.
