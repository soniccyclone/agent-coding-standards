---
type: lesson
title: "What you call the specification is the small part; the bulk of it is structure you assumed from a diagram"
figure: emerson
works: [using-branching-time-temporal-logic-to-synthesize-synchronization-skeletons]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# What you call the specification is the small part; the bulk of it is structure you assumed from a diagram

**Lesson:** Ask someone to state the mutual exclusion problem and you get three things: where the system starts, that two participants are never simultaneously inside the protected region, and that a waiting participant eventually gets in. Write those down formally and try to derive an implementation from them, and it fails, because they are a minority of the actual content. The rest was carried by a picture: that each participant is in exactly one region at a time, that the only route out of the waiting region is inward, that a participant can always choose to start waiting, that one participant's step cannot relocate another, that somebody is always able to move. None of that was in the stated problem. All of it was assumed by every reader.

The observation generalizes beyond formal methods. The informal problem statement carries the *global* obligations, the interesting ones people argue about. The tacit part is *local* structure: the shape of each component's own state machine and the ways it may not behave. Local structure is invisible in discussion precisely because everyone shares it, which is what makes it the reliable source of misunderstanding when two people do not. Making it explicit costs a few lines and converts an unbuildable description into one from which behavior can actually be derived.

The payoff for writing it down is reuse in an unusually clean form. Once the local structure is stated, it stays fixed across a family of problems, and you generate new problems by varying only the global assertions. Swapping the eventual-entry guarantee for a priority guarantee turns the mutual exclusion specification into a readers-writers specification with no other edits. The stable part and the varying part have been separated at the right seam, which is what makes the specification an asset rather than a one-off document.

A programmer who absorbs this stops treating the requirements conversation as complete when the contentious properties are settled. The question to ask next is: what did everyone in this room already believe about the shape of each component, and would a competent stranger implementing from this document believe the same? The parts that go without saying are the parts to say.

**Source:** [Using Branching Time Temporal Logic to Synthesize Synchronization Skeletons](../works/using-branching-time-temporal-logic-to-synthesize-synchronization-skeletons.md) — the mutual exclusion example's numbered requirement list and the remark following it, which separates the handful of global behavioral assertions from the larger group of local-structure assertions that had previously been conveyed only by a figure, and notes that varying just the global ones yields the other worked problems.
