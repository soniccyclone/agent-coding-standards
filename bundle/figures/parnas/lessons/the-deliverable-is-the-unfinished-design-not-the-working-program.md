---
type: lesson
title: "The artifact worth maintaining is the unfinished design, not the working program"
figure: parnas
works: [on-the-design-and-development-of-program-families]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# The artifact worth maintaining is the unfinished design, not the working program

**Lesson:** When several variants of a system are needed, the reflex is to finish one and then cut new ones from it. The damage this does is specific rather than vague. Bringing the first variant all the way to working condition required settling questions that only that variant's circumstances posed, and every later variant inherits those settlements — not because they suit it, but because undoing them means rewriting code that already works. The inherited decisions are usually the performance-relevant ones, since they concern layout, timing, and resource assumptions tuned to a load the descendant does not have. So each generation carries deficiencies traceable to an environment it never ran in, and nobody can say which of its properties are intentional.

Deriving instead from a common ancestor removes the inheritance, but it only works if the ancestor is a real artifact. In the sequential-completion style the intermediate states are not written down precisely — which is both cause and consequence of the fact that the only thing groups exchange is finished programs. Reverse that and the precise partial design becomes the thing you actually ship to your colleagues: incomplete, but developed far enough to be built on, and specifically the document that branch points hang off. It also becomes the thing you maintain. Two live variants that diverge below the same partial design can share it as valid documentation for both, and a proposed change can be evaluated against it once for both — which is only possible because the shared part was written down rather than reconstructed by diffing two codebases.

There is a second dividend that only appears when the partial design is explicit: variants can be produced in parallel rather than in sequence. Sequential completion imposes an order for no reason other than that the parent had to exist first. With a stated common ancestor, branches that do not consume information from one another can be developed simultaneously by different people, and a newcomer can complete a branch, because completing a documented partial design is a bounded task in a way that modifying somebody else's finished program is not.

A programmer who takes this seriously changes what they consider done. The running system stops being the sole deliverable — it is one resolution of a design that is itself the durable asset — and the question "where is the description of what all our versions have in common" becomes a question with an expected answer rather than a rhetorical one.

**Source:** [On the Design and Development of Program Families](../works/on-the-design-and-development-of-program-families.md) — the account of sequential completion and the deficiencies descendants inherit from ancestors, the section on representing intermediate stages and what is offered as a contribution to others' work, and the free-space allocation walkthrough where an alternative variant is obtained by returning to the nearest common ancestor and where that stage doubles as documentation for both versions.
