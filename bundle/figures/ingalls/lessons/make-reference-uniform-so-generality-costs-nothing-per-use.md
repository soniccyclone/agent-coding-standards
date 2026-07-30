---
type: lesson
title: "Make reference uniform, so a variable can hold anything and no caller has to plan for what it holds"
figure: ingalls
works: [design-principles-behind-smalltalk]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Make reference uniform, so a variable can hold anything and no caller has to plan for what it holds

**Lesson:** Naming is not a convenience laid over a system, it is the mechanism that makes a distinction reusable. Carving something out of the undifferentiated background is real work — you have to say which thing, against everything else — and without a handle you pay that cost freshly every time you want to mention it again. A stable identifier is what converts one act of distinguishing into permanent access. That is the ground-level reason a system needs a notion of an identified thing at all, before any argument about types or classes: it is how a model stops being re-derived and starts being referred to.

The design consequence people miss is that the *uniformity* of the handle carries more weight than the existence of it. If every value in the system, no matter how large or how strange, is designated the same way and at the same width, then a variable is a plain slot and can hold any of them without knowing which — generality at every storage site becomes free rather than something the site's author has to arrange in advance. Conversely, a scheme where different kinds of value are referred to differently forces every container, parameter and field to commit to a kind, and that commitment then propagates outward into every procedure that touches it. The uniformity is what makes polymorphism affordable at the representation level; without it, substitutability has to be paid for again with each variable declared.

The same uniformity is what lets creation and disposal drop out of a caller's field of view entirely. Something produced by evaluating an expression can be handed on as an ordinary handle, so no intermediate procedure needs to reserve room for it, understand its extent, or know when it is finished with; the last handle disappearing is enough to make the thing itself disappear. Automatic reclamation is often argued for as a convenience, but the sharper case is that it is a *requirement* of the model rather than an amenity on top: a system claiming that its things have independent existence, while still asking programs to schedule their deaths, has not actually delivered the independence it claims. So when evaluating a design, look at whether the promise made at the top — everything here is a thing you can just refer to — is honored all the way down to how storage is designated and released, or is quietly withdrawn a level or two below the surface.

**Source:** [Design Principles Behind Smalltalk](../works/design-principles-behind-smalltalk.md) — the Objects principle and its preceding discussion of drawing distinctions and then substituting an identifier for repeating the act of distinguishing; the account of a uniform association between objects and simple identifiers letting variables of widely differing content be implemented as ordinary memory cells and letting expression results be passed around without procedures making provision for their storage; and the Storage Management principle claiming automatic reclamation is a precondition of the object model rather than an added feature.
