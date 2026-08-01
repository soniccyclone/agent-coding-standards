---
type: lesson
title: "Accepting members of unknown type obliges you in both directions"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Accepting members of unknown type obliges you in both directions

**Lesson:** When a family of components admits both leaves and containers, the containers are routinely planned as though they were leaves with a list attached. They are not, and the gap is not marginal — it is roughly an order of magnitude, consistently, and it comes from a specific place worth being able to name in advance. A leaf answers requests about itself. A container that accepts members whose types it does not know must additionally implement the whole routing discipline downward: receiving a request, deciding whether it is addressed to itself or to something inside, transforming it into the vocabulary of its members, propagating it to each, and doing so correctly for kinds of request that did not exist when it was written.

That is only the first half. The second half is the one that gets forgotten in estimates, because it runs the other way. A member of unknown type will, at some point, need something from the enclosing structure that it cannot compute itself — more room, a redraw, a change of arrangement, a resource — and it can only get it by asking upward. So the container also owes an inbound protocol: it must accept requests from its own contents, decide whether they can be honoured, possibly renegotiate with its own container, and answer. Once that exists the container is not a conduit but a mediator, sitting between two parties who each believe they are talking to something simpler than they are. Downward propagation and upward feedback are separate protocols with separate failure modes, and a container has to get both right while a leaf has neither.

The practical use of this is in estimating and in deciding. When someone proposes that a new component "can also contain others", that clause is the whole of the work, and it should be priced as a protocol implementation rather than as a field. Often the right response is to check whether it is needed at all: many families that were designed with arbitrary nesting turn out to use one or two fixed arrangements, and a small number of purpose-built containers with known member types costs a fraction of one general container, because a container that knows what it holds can compute its members' needs directly instead of negotiating with them. The general container earns its cost only when the set of things it must hold is genuinely open.

A last note about where the difficulty is not. It is not in the recursion — nesting containers inside containers adds essentially nothing once one container is correct, because the same protocol applies at every level, and a container that can hold anything can hold another container without special provision. The cost is entirely in the first one. That asymmetry is useful to know, because it means the decision worth agonizing over is whether to have general containment at all, not how deeply to allow it.

**Source:** [Project Oberon](../works/project-oberon.md) — appendix A.4's remark that the complexity of custom interface objects is essentially determined by their structure, container objects such as panels being an order of magnitude more complex than atomic ones such as buttons, lists and bar diagrams, on the grounds that container objects must be able to manage content objects of arbitrary type, so their message handlers must properly implement parental control including propagation to contents and must in addition be prepared for feedback requests by contents, instanced by a content object requesting to expand; together with the same section's note that documents are themselves such objects and may recursively contain other documents, the desktop itself being one.
