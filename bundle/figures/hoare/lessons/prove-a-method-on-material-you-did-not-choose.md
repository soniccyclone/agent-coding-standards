---
type: lesson
title: "Prove a method on material you did not choose, and expect most of what it flags not to be a bug"
figure: hoare
works: [the-verifying-compiler-a-grand-challenge-for-computing-research]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Prove a method on material you did not choose, and expect most of what it flags not to be a bug

**Lesson:** A technique demonstrated only on artifacts built to suit it has demonstrated nothing about its reach. The honest test is to point it at a large body of existing work that somebody else wrote, for their own reasons, in whatever style they liked, and to publish the result. That is uncomfortable precisely because the material was not shaped by the technique's assumptions, and the discomfort is the information: every place the method needs the artifact to be well-behaved and the artifact is not is a boundary of applicability that a curated demonstration would have concealed. Choose the corpus for being real, widely used and inconveniently large, not for being tractable.

The second half of the lesson is what to do with the output, and it is where most such efforts lose credibility. When a rigorous method is turned loose on real systems, the great majority of what it reports will not be defects. Much of it is a missing precondition nobody bothered to write down, obvious to anyone who has read the code and invisible to the tool. Some of it is a genuine anomaly that downstream code has come to depend on, so that correcting it would break working systems. Some is a real error whose triggering conditions are so rare that fixing it is not worth the change. And whole regions — the exact behavior of an interface to a person or a device — are not worth describing formally at all, because looser evidence already gives adequate assurance. Anticipating this distribution in advance is what separates a usable method from one that drowns its users in reports and is switched off within a month. Report volume is not a measure of value; it is a cost to be triaged, and the triage rules should be designed alongside the tool.

There is a standing temptation to escape all of this by discarding the existing material and starting again on ground that suits the method. Sometimes that is the right project. It is never the same project, and conflating the two lets a technique claim credit for results it only achieves under conditions it was allowed to dictate. State the rebuild as a separate undertaking with its own justification, and keep the claim about the current one scoped to the material you actually faced.

**Source:** [The Verifying Compiler: A Grand Challenge for Computing Research](../works/the-verifying-compiler-a-grand-challenge-for-computing-research.md) — the Testable criterion's insistence on demonstration against a broad selection of open-source legacy code, and the Risk-Managed section, which catalogues why proof failures on such code are usually omitted preconditions, unfixable-because-depended-upon anomalies, or errors too rare to be worth correcting, and separates the "discard legacy and start again" option out as a different grand challenge.
