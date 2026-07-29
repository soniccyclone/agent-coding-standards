---
type: lesson
title: "An entity at one level is a collaboration one level down"
figure: reenskaug
works: [the-dci-architecture-a-new-vision-of-object-oriented-programming]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# An entity at one level is a collaboration one level down

The things a design treats as indivisible are indivisible only relative to a chosen altitude. Reenskaug and Coplien take the tidiest example available — the account that every introductory course presents as the model of a simple entity — and point out that opened up it is not an entity at all but a standing arrangement of participants: postings, a record of them, an audit obligation, and behavior defined across the arrangement rather than owned by any one member. It looks atomic from above because its internal traffic has stabilized, and stabilized traffic is invisible traffic.

The reason this matters is that it makes the entity/collaboration distinction a viewpoint rather than a property, which in turn makes the same construct usable at every level. A collaboration whose members have settled into a fixed relationship, and which offers only a narrow face to the outside, is indistinguishable from an entity to anything above it — so it can be a participant in a larger collaboration while itself orchestrating a smaller one. You get strata without needing a different kind of building block per stratum, which is a much cheaper structure to learn and to reason about than a hierarchy of distinct concepts.

The judgment this hands you is about when to open a box. A stable collaboration should be allowed to present itself as a simple thing, and forcing its internals into view because they exist is a way of drowning every reader at every level. Conversely, when an apparently simple entity keeps growing operations that do not follow from its own nature, the honest reading is that it was a collaboration all along and the arrangement inside it has stopped being stable. Its promotion to a full participant with visible members is then recognition rather than redesign.

A programmer working this way keeps asking which altitude a given piece of reasoning belongs to, expects the answer to differ for different readers, and does not assume the decomposition that was right at the top is right all the way down. It also removes the usual excuse for a special top-level orchestration layer built out of different material than everything beneath it.

**Source:** [The DCI Architecture: A New Vision of Object-Oriented Programming](../works/the-dci-architecture-a-new-vision-of-object-oriented-programming.md) — the nested-contexts section, which reinterprets the textbook savings-account entity as a collaboration over transactions, logs, and audit trails, and shows the same construct serving as a participant above and an orchestrator below.
