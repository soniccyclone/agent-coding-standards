---
type: lesson
title: "When the producers are autonomous, let the data carry its own structure"
figure: abiteboul
works: [web-data-management]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# When the producers are autonomous, let the data carry its own structure

**Lesson:** The received order of operations is that a type comes first and instances come afterward: declare the shape, then create values that conform. This work identifies the conditions under which that order stops being viable and describes the alternative. When data is produced by many parties who do not coordinate, the same information arrives in variant shapes and units, expected pieces are missing because a contributor was unavailable, unanticipated pieces appear because someone had more to say, and the structure of a newly encountered source is not known until you have looked at it. The alternative is to make the structure travel inside the data, so that a value describes itself and the boundary between type and instance blurs deliberately. Typing then becomes optional and partial rather than a precondition, applied where you have the leverage to demand it and skipped where you do not.

The sharpest part of the argument is a scaling observation that does not get made often enough. In this regime the description of the shape can grow to the size of the data it describes, or larger, and it can change faster than the data does. A schema is only a compression of the data's structure when the structure is regular and stable. Once the structure is irregular and churning, the schema stops being a compression and becomes a second dataset with its own maintenance burden and its own staleness, and insisting on it up front means paying that cost in exchange for a guarantee it can no longer deliver. This is the actual reason rigid models were passed over for exchange between independent parties, and it is a claim about the economics of the situation rather than a preference for looseness.

The judgment this teaches is to ask who controls the producers before choosing how much structure to mandate. Inside a boundary you own, where writers and readers ship together, declare the shape early and enforce it, since the guarantee is cheap and real. Across a boundary you do not own, expect self-describing payloads, validate the fragments you actually depend on rather than whole documents, and design readers that tolerate both absence and surplus. The failure this avoids is the common one of exporting an internal schema as an external contract and then discovering that every independent contributor either violates it or forces a revision, which converts what should have been a loose coupling into a standing negotiation.

**Source:** [Web Data Management](../works/web-data-management.md) — the opening chapter's account of semistructured data, where the distinction between type and instance is described as blurred and self-description is preferred to the notion of being schema-less, and the following section weighing whether to type at all, which lists irregularity, missing and unexpected content, unknown structure, and untyped fragments as the conditions in play, and observes that a shape description may rival or exceed the data in size and change far faster.
