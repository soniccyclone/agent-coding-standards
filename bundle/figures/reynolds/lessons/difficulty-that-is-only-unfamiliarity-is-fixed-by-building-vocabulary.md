---
type: lesson
title: "Reasoning that feels hard is often only unfamiliar, so build the vocabulary the domain is missing"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Reasoning that feels hard is often only unfamiliar, so build the vocabulary the domain is missing

**Lesson:** When reasoning about one kind of object feels effortless and reasoning about another feels punishing, the honest first hypothesis is not that the second is intrinsically harder. Arguments about arithmetic go down easily because the concepts have been named, the laws have been stated, and everyone has absorbed them so thoroughly that they get used without acknowledgment. Arguments about indexed collections go down badly because the corresponding concepts are recent, unnamed, and not yet common property — so instead of citing a law you spell out the whole thing every time, and descriptions balloon into something nobody will read. The difficulty is a missing shared vocabulary, not a missing intellect. That reframing matters because the two diagnoses lead to opposite responses: one tells you to grind harder, the other tells you to stop and construct the vocabulary first.

Constructing it means two things, and the second is the one people skip. You need concepts and named laws about them, so that a step in an argument can be a citation rather than a derivation. And you need a notation compact enough that the descriptions stay short, because a description that is technically adequate but too long to read fails at its only job. Adequacy of a notation is not a mathematical property, it is an ergonomic one, and a notation can be complete and still useless. Judging it requires actually writing out the descriptions your real problems demand and looking at how they came out.

The most efficient place to find such a notation is in what practitioners already do informally. Programmers reasoning about ranges of an array had for years been sketching box diagrams on paper — an informal practice, ignored by the formal apparatus, and carrying real content. The productive move is not to invent a fresh syntax and ask everyone to learn it, but to take the existing sketch, give it a precise meaning, and admit it into the formal language so the picture becomes a legitimate assertion. This costs the reader nothing to learn and immediately makes long descriptions short. Look for this opportunity whenever a team maintains a diagramming or whiteboard convention alongside its real artifacts: the convention persists because it captures something the artifacts cannot say, and formalizing it is cheaper than replacing it.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the opening of Section 2.2.2, which attributes the difficulty of array assertions to unfamiliarity rather than intrinsic complexity by contrasting centuries-old arithmetic concepts used without explicit mention against array concepts still under research, notes that the existing assertion language is theoretically adequate yet leads to unreadably long assertions, and then gives precise meaning to the box-like diagrams programmers had traditionally drawn so that they can be used in assertions.
