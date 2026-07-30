---
type: lesson
title: "An environment built to satisfy every internal audience will satisfy none of them"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# An environment built to satisfy every internal audience will satisfy none of them

**Lesson:** Organizations building software for others routinely build one internal toolchain intended to serve everyone who contributes: the people producing the low-level substrate, the people assembling components, the people configuring finished systems for customers. The author's claim is that this consolidation reliably produces something too complex to satisfy anybody, and the reason is structural rather than a matter of effort. Those groups differ in what they are responsible for, what counts as success, what they already know, and what they are trying to avoid thinking about. A single environment serving all of them must expose the union of their concerns, so every group navigates a surface most of which is addressed to somebody else.

Set against that is a claim about investment: the tools used by each internal group should be designed at least as carefully as the product shipped to the end customer. This is easy to nod at and rare to act on, because internal tooling is normally justified by whatever is cheapest to build and is measured by whether it works at all rather than by whether it fits its user. The argument for parity is that these people are the production capacity — their throughput is the organization's throughput — and an environment misfitted to its user taxes every unit of work that passes through it, indefinitely.

The two claims combine into an operational test that is more useful than either alone. For each internal group, ask whether their goals, their qualifications, their tasks, and their tools are mutually consistent, and treat a mismatch on any of the four as a defect rather than as something individuals should absorb through skill. That test has teeth in a way that "improve developer experience" does not, because it asks about a specific population and can fail. It also carries a stated constraint on the answer: what each group is required to know must remain realistic for actual people who can be hired in numbers, which rules out the tempting solution of designing for the most capable person available and letting everyone else struggle.

The general reflex is to resist consolidating tools across audiences whose responsibilities genuinely differ, even though consolidation always looks like the economical choice. Merging saves the builders' effort once and charges every user of the merged thing forever, and the charge is paid in a currency — attention spent on other people's concerns — that no one measures.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 10 section 10.1, on the layers of a value chain: production facilities for the actors on every layer should be designed at least as carefully as end user systems, the current tendency toward a common environment satisfying all needs yields solutions too complex to satisfy anybody, and the guiding principle is that the actors' qualifications must be realistic in terms of real people with goals, tasks and facilities all in harmony.
