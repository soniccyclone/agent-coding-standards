---
type: lesson
title: "Mark the extension surface in the design notation itself, and seal everything else"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Mark the extension surface in the design notation itself, and seal everything else

**Lesson:** A framework published to consumers here distinguishes its participants explicitly: one is intended to be specialized by whoever builds on it, and the others may not be modified at all. The distinction is not left to documentation or convention — it appears in the diagram, as a drawn mark on the participants that are closed, and it is intended to be enforced by the compiler or by automated analysis of the source.

Putting the policy in the notation is the part worth extracting, because extensibility policy normally lives in the worst possible place: prose in a guide, or a naming convention, or nowhere. Two things follow from moving it into the model. It becomes visible at the moment someone is reasoning about the design rather than at the moment they are writing code against it, so the question "may I subclass this?" is answered by the picture they are already looking at. And it becomes checkable, since a marked model can be compared against an implementation mechanically — which matters because this is exactly the class of constraint that erodes silently, one justified exception at a time, until the framework's author no longer knows what consumers depend on.

The justification given for sealing is worth separating from ordinary encapsulation. It is not that the internals are ugly or unstable; it is that the provider has an integrity obligation to something shared and physical — a network many parties depend on — and can only discharge it if every path to that resource runs through code the provider validated and nobody else can alter. A subclass is not a use of an interface, it is a modification of the thing itself, and one subclass overriding one method is enough to void the guarantee for everyone. So the seal is what makes the offer possible: the provider can hand out a powerful capability precisely because the capability cannot be reshaped in transit.

The complement keeps this from being merely restrictive. Exactly one participant is designated as the specialization point, and it is the one representing the consumer's own role — so consumers are given a real place to put their variation. That is the shape to aim for generally: decide deliberately which single participant carries consumer variation, mark it, seal the rest, and enforce it with a tool. A framework that seals nothing cannot make promises; one that seals everything cannot be used.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 12 section 12.7's Connection Control framework, where the ConnUser role may be specialized through synthesis while Leg and ConnPoint are immutable roles that cannot be modified in derived models, notated as role symbols with a double boundary; the class corresponding to ConnUser must be available for subclassing while the others must be immutable, with the note that these constraints could be imposed by the compiler or checked by automatically analyzing the source code; and the closing observation that frameworks help enforce the constraints needed to protect the integrity of the switching network by insisting all access goes through validated classes the Service Constituent Creator may not subclass.
