---
type: lesson
title: "Define complexity as the interconnection that hides logical structure, not as the amount of stuff"
figure: wilkes
works: [best-way-to-design-an-automatic-calculating-machine]
axes: [cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Define complexity as the interconnection that hides logical structure, not as the amount of stuff

**Lesson:** Size and complexity are separate properties, and conflating them makes both unmanageable. The useful definition of complexity is the extent to which the connections between parts obscure the logical relationship among those parts. A large assembly of units wired together in an obvious pattern is not complex; a small assembly whose cross-links defeat any attempt to say what depends on what is. This matters because the two properties trade against each other: you can frequently buy a reduction in complexity by accepting an increase in quantity, and if complexity is measured in units of quantity you cannot even state the bargain, let alone take it.

The definition earns its keep by predicting two practical consequences that are otherwise easy to treat as unrelated virtues. A structure whose connections do not obscure its logic is easier to diagnose when it misbehaves, because a symptom can be localized to a part instead of to the wiring between parts. And it is easier to build, because separate people can work on separate parts without colliding — the absence of cross-connections is precisely the absence of coordination overhead between the people doing the work. Repairability and parallel construction are the same property observed from two angles, and that property is the visibility of logical relations through the interconnection.

The operational discipline this yields is to audit connections rather than count components. Ask of each link between parts whether it belongs to the logical story the design tells, or whether it exists because some local convenience needed it and it now sits there making the story untellable. The second kind is what has to be bought out, even at the cost of more total material, because it is the kind that grows the state space a reader has to hold and shrinks the number of people who can work on the thing at once.

**Source:** [The Best Way to Design an Automatic Calculating Machine](../works/best-way-to-design-an-automatic-calculating-machine.md) — the opening reliability discussion, which lists quantity, complexity and repetition as separate contributors and then defines complexity specifically in terms of cross-connections obscuring logical inter-relation, drawing out the repair and division-of-labour consequences.
