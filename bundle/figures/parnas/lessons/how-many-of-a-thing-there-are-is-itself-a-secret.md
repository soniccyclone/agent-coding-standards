---
type: lesson
title: "How many of a thing there are is itself a secret, and leaking it blocks removal as hard as addition"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# How many of a thing there are is itself a secret, and leaking it blocks removal as hard as addition

Information hiding is usually applied to representations: how a thing is stored, how a computation is done. Parnas pushes it one step further in a direction most designs never consider. The presence or absence of a component, and the number of such components, is information too, and it should be concealed from everything that does not have to know. A component may be forced to know that another one exists, because it invokes it — but there is no reason for any component to know how many others exist alongside it or how many use it. Whatever data structure records those counts belongs in a module whose secret that is, behind an interface that does not expose the number.

What makes this a design rule rather than a fastidiousness is the symmetry of the damage when it is violated. Consider an early decision that some fixed number of variants will be supported, and a codebase where dozens of places quietly encode that number — tables sized to it, loops bounded by it, switch arms enumerating it. Everyone expects adding a variant to be expensive. The surprise is that removing one is expensive in exactly the same places. You can delete the variant's code easily enough, but you get none of the resource savings that motivated the removal until you go and rewrite precisely the same sites you would have rewritten to add one. Contraction is not the easy direction; a distributed cardinality assumption taxes both directions equally.

The general habit this suggests is to look at every number in a design and ask which module owns it. Counts are the most casually distributed facts in software because they feel like configuration rather than design — nobody thinks of "there are three of these" as an assumption with a lifetime. It is one, it is usually wrong eventually, and the number of code sites that mention it is a direct measure of what changing it will cost. The version of this that most improves a design is the strongest one: build so that a component cannot tell whether its siblings exist at all, and the question of how many there are stops being askable in the places where the answer would have been baked in.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — the discussion of excessive information distribution with its operating system supporting a fixed number of conversational languages and its observation that reducing that number required rewriting the same code as increasing it, together with the information hiding section's argument that presence, absence and number of components should be hidden and recorded in separate hiding modules.
