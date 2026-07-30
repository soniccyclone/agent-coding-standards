---
type: lesson
title: "Two organizations can share one coherent system while nobody anywhere understands all of it"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Two organizations can share one coherent system while nobody anywhere understands all of it

**Lesson:** The usual assumption behind integration is that someone has to hold the whole picture — an architect, a team, a document — because otherwise how would anyone know the pieces fit? That assumption is what makes cross-organizational systems feel impossible: no single party can be given a view of both sides, so integration becomes either a political problem or an interface document nobody trusts. The claim worth taking seriously is that the assumption is false, and that the requirement can be dropped without giving up coherence.

The mechanism is to make the *shared description* the unit of integration rather than the shared understanding. A bank packages a group of its descriptions, hides everything internal, and publishes a small set of them for customers to build on. A customer imports those and derives their own descriptions from them, integrating banking with operations the bank knows nothing about. Each side designs, implements and understands its own system completely. Neither has any view of the other's internals, and neither needs one — the two worlds are joined through the published descriptions, and the resulting whole is genuinely coherent because the shared part is a real artifact both sides build from rather than a document describing what each side hopes the other does.

What makes this more than an argument for interfaces is what it implies about comprehensibility. Understanding stops being a property of the system and becomes a property of a region, with the published descriptions marking the boundaries of each region of required understanding. The design question therefore becomes how small you can make the published surface and how stable you can keep it, because those two numbers determine how much anyone has to know. And the discipline that follows is unglamorous: get the boundaries and the exported descriptions right early and keep them stable, hold the internals brief and sketchy until then, and change what you export rarely and only deliberately — because every export you add is understanding you have obliged someone else to acquire.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 6's section on modeling in the large, which describes a bank exporting models its customers import into their own systems, calls it an enormously important result that the two system worlds constitute a coherent whole while no single person or group need have an overview of the total system, and gives the accompanying advice to stabilize the architecture and exported models early and keep them lean.
