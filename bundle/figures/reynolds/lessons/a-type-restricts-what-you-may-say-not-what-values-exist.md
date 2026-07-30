---
type: lesson
title: "A type is a restriction on what you are allowed to say, not a description of which values exist"
figure: reynolds
works: [types-abstraction-and-parametric-polymorphism]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A type is a restriction on what you are allowed to say, not a description of which values exist

**Lesson:** Two people can build the same abstraction on incompatible foundations — one representing a compound number as a coordinate pair, the other as a magnitude and an angle with its own quotient rules — and then talk past each other for a whole term without either one uttering a falsehood, provided both confine themselves to statements that hold under either construction. That discipline is what a type is for. It is not a label announcing which set a value belongs to; it is a rule about which sentences you are permitted to form. The useful test of an abstraction boundary, then, is adversarial: could a colleague replace the representation with a different legitimate one, overnight and without telling you, and leave every claim you have written still true? Anything that fails that test was never a statement about the abstraction, only about one of its incarnations.

The consequence worth internalizing is that the discipline earns its keep through what it forbids, and the forbidden things are often perfectly meaningful at the representation level. Once a type is introduced, questions like whether it overlaps some other type, or what their common members are, must become not merely false but unaskable — even though the underlying sets certainly do have an intersection, and a different but equally valid representation would give a different one. Declaring an equality between the abstraction and its representation is likewise off limits; the honest move is to exhibit a mapping into the abstraction and argue that mapping is faithful. Interfaces that quietly permit representation-level questions have already leaked, whether or not anyone has yet exploited the leak.

This also tells you how to choose the setting in which you explain such a boundary, and the rule is: use the weakest one that supports the phenomenon. A model that equips values with more structure than the abstraction admits will license conclusions the abstraction was designed to prohibit — treat a type as a specific subset of one big universe of values and its unions and intersections snap back into existence, destroying the very opacity you were trying to model. The same caution applies to importing machinery introduced for an unrelated difficulty: the apparatus needed to handle self-reference and non-termination has no business appearing in an account of abstraction, because abstraction was practiced correctly for centuries by people who would have found partial or approximate values incomprehensible. Mechanized enforcement is what computing added; it did not invent the idea, and explanations that presuppose the mechanism mistake the enforcement for the concept.

**Source:** [Types, Abstraction, and Parametric Polymorphism](../works/types-abstraction-and-parametric-polymorphism.md) — the opening fable of the two lecturers and its two stated morals, together with the survey of prior formalizations that argues subset-of-a-universe treatments obscure abstraction precisely because they make unions and intersections well defined.
