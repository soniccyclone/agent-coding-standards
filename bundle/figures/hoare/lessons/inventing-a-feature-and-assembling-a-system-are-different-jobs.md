---
type: lesson
title: "Inventing a feature and assembling a system are different jobs, and assembly is consolidation, not invention"
figure: hoare
works: [hints-on-programming-language-design]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Inventing a feature and assembling a system are different jobs, and assembly is consolidation, not invention

**Lesson:** These are two crafts that get performed by the same person and shouldn't be. Inventing a single mechanism is a bounded, checkable activity, and it has a discipline: work on exactly one addition at a time; situate it inside an existing system you know well rather than a hypothetical clean one, so that the comparison is against reality; show it removes a specific weakness without spoiling any strength already present; demonstrate that it can be implemented simply and cheaply, not merely that it could be implemented; write the passage of the manual that would teach it, with examples, because the difficulty of that passage is a measurement; hunt specifically for the traps that cannot be caught before the thing runs; work real examples against each alternative you rejected; and if the mechanism admits a clean rule for reasoning about it, that is the strongest evidence available that it was the right shape.

Assembling a whole system from mechanisms is a different job requiring different virtues. It calls for wide familiarity with what others have built, judgment about which pieces are best, and the ability to detect combinations that are mutually inconsistent — not to mention the unglamorous obligation to reconcile leftover overlaps by ordinary engineering, decide honestly how large and complex the result should be, and carry the whole weight of implementations, manuals, teaching material, tools, libraries, and distribution. That list already exceeds what one person can do well. Adding untested ideas of one's own on top of it is the failure mode, because an untried mechanism inside a large assembly gets no honest evaluation: the errors of judgment are invisible until they are expensive, and by then the whole is committed to them. The person integrating should be consolidating known-good parts, and should have earned the right to trust them by seeing them tried elsewhere.

The same split explains the most reliable instruction for taking requests from users: hear what they ask for, keep listening past that until you understand what they are actually short of, and then find a way to supply the second thing at a small fraction of what the first would have cost. Requests arrive already shaped as mechanisms, because that is how people describe needs, and adopting the requested mechanism is how a system accumulates weight without gaining capability. Getting from the stated mechanism to the underlying lack — and finding a cheaper mechanism that covers it — is the entire measure of whether the design work is any good.

**Source:** [Hints on Programming Language Design](../works/hints-on-programming-language-design.md) — the Language Feature Design section, which separates the two design activities and gives the checklist for each, insists the integrator's task is consolidation rather than innovation, and the concluding hint about listening past what users ask for.
