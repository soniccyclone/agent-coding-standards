---
type: lesson
title: "Refuse privileged tiers: make one mechanism cover everything, and accept the implementation bill on the expectation that technique will pay it down"
figure: goldberg
works: [smalltalk-80-the-language-and-its-implementation]
axes: [primitive-count, expressiveness, hardware-affinity]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Refuse privileged tiers: make one mechanism cover everything, and accept the implementation bill on the expectation that technique will pay it down

**Lesson:** Most systems that adopt a good idea adopt it partially. They apply the new model where it is convenient and keep an older, faster, more familiar mechanism underneath for the things that would be awkward — arithmetic, control flow, the definitions of types themselves. This book argues for and demonstrates the opposite policy: one mechanism, applied without exception, all the way down and all the way up. Adding two numbers is a request to a number. Choosing between branches is a request to a truth value, answered by two different classes that each know what to do, so conditional execution needs no construct of its own. Deferred activity is an object, which is why loops and user-invented control forms are ordinary requests too. The definitions of types are objects, so is a running computation, so is the compiled form of a method. Nothing is permitted to sit outside the model and be explained by a different story.

The payoff is not elegance for its own sake, and this book is explicit about the mechanism of the payoff. Uniformity collapses the number of independent things a reader must know: if there is one rule for what happens when something is asked of something, then encountering an unfamiliar expression requires no new theory, at any scale. It also means the extension mechanism available to a user is the same one the system itself is made of — there is no second-class tier for things added later, so what a stranger can build is bounded only by what the builders could build. And it removes whole categories of special case at the boundary: the reason a construct cannot be redefined, extended, or inspected is usually that it was privileged, and nothing here is.

What makes this an argument rather than a preference is the cost accounting attached to it. The authors record that pushing uniformity into arithmetic drew resistance on efficiency grounds, that they kept it anyway, and that across successive versions implementation technique narrowed the penalty to near nothing. That is a specific and falsifiable bet: a cost imposed by a uniform model is likely to be an *implementation* cost, and implementation costs are the kind that get engineered away, while structural non-uniformity is permanent and compounds. The comparison they draw with an earlier language that used objects only at the high level and delegated arithmetic and control structures to an embedded conventional language is the counterfactual — that system got its speed immediately and its ceiling permanently.

A programmer who takes this seriously treats "we'll special-case this one for performance" as a claim requiring evidence about where the cost actually lives, and treats an exception to the model as a debt that never amortizes. The corollary is a design test: if some part of your system cannot be described by the rules the rest of it follows, you have two systems, and users will eventually discover the seam by falling into it.

**Source:** [Smalltalk-80: The Language and Its Implementation](../works/smalltalk-80-the-language-and-its-implementation.md) — the uniformity argument stated in the introductory chapters and defended again in the kernel-support and number chapters, where the efficiency objection to uniform arithmetic and its resolution across versions are discussed directly, alongside the treatment of Boolean classes that turns conditional selection into ordinary message dispatch.
