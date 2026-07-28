---
type: lesson
title: "When you noticed the commonality decides how you should express it"
figure: liskov
works: [data-abstraction-and-hierarchy]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# When you noticed the commonality decides how you should express it

**Lesson:** Two situations look identical on a diagram and are not the same engineering problem. In one, you know several related things are coming before any of them exists, so you can name the shared idea first and let each concrete thing be introduced beneath it. In the other, the things already exist, built independently, and only later does somebody want one routine that works across them. The order in which you learned about the commonality changes which mechanism is cheap.

For the first situation a named shared parent is a good fit and costs little: it exists from the start, everything is defined relative to it, and whatever can be done once in a subtype-independent way is done there. For the second situation retrofitting a parent is a tax with no end date. Every existing participant must be edited to declare its new ancestry and rebuilt. Worse, the tax recurs: from then on, every newly invented type must be checked against every such parent, in case someone might eventually want to feed it to the shared routine — and the parent often carries no implementation at all, so it buys nothing but the permission slip.

The alternative for late-discovered commonality is to state the requirement where it is actually needed: the shared routine declares what it demands of whatever it is handed, and anything meeting the demand may be handed to it, with no taxonomy constructed and no existing type modified. What used to be a claim about ancestry becomes a claim about capability, checkable at the call site. The check moves too — instead of being made once when someone declares a type a descendant, it is made each time someone writes code that uses the shared routine, which is exactly where the assumption is being introduced.

A programmer who believes this asks "did I know about this family before or after its members existed" before drawing any hierarchy, and treats a retrofitted common ancestor as a smell rather than a cleanup. They also notice that the awkward cases — a participant missing the needed operation, using a different name for it, or using that name for something unrelated — are much easier to absorb by parameterizing the shared routine than by rearranging everyone's ancestry to accommodate it.

**Source:** [Data Abstraction and Hierarchy](../works/data-abstraction-and-hierarchy.md) — the polymorphism section, which contrasts hierarchy against what it calls the grouping approach and tallies the cost of introducing a supertype after the related types already exist.
