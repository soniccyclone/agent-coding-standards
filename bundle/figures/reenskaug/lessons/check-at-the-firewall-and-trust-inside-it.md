---
type: lesson
title: "Draw a boundary, distrust everything crossing it, and trust everything inside"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Draw a boundary, distrust everything crossing it, and trust everything inside

**Lesson:** Defensive programming taken to its logical end produces a system where every component validates every input from every other component, and the result is worse than the disease: parts that spend most of their effort checking each other, with the actual work buried under mutual suspicion. Encapsulation makes this easy to do — each part *can* protect itself from all possible abuse — and the fact that it is easy and locally justifiable at every step is exactly why it happens.

The alternative is to stop treating trust as a property of individual components and make it a property of *regions*. Draw a boundary around a group of parts that collaborate on one concern. Messages crossing that boundary get checked carefully, because they come from somewhere you do not control and cannot reason about. Messages travelling within the boundary are assumed sound, because everything inside was designed together and can be reasoned about as a unit. Validation becomes a perimeter activity rather than a per-component reflex, and the cost shows up once per boundary instead of once per interaction.

What makes this actionable rather than vague is that the regions are not arbitrary — a good boundary is whatever unit you already reason about as a coherent whole, which usually means the same grouping your descriptions use. That alignment is the point: it means the trust boundary and the comprehension boundary are the same line, so a reader who understands one region understands what it assumes. The transferable habit is to answer "where does validation go?" with "at the edges of the regions I reason about," and to treat a component checking its neighbour *inside* a region as a signal that the region was drawn wrong — the parts either belong together and can trust each other, or they do not belong together.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 4's implementation-process guidelines, specifically the "make it fail-safe" item, which warns that carrying self-protection too far yields objects that spend their time checking each other and proposes fire-wall boundaries where crossing messages are treated with suspicion and internal ones assumed to be in order.
