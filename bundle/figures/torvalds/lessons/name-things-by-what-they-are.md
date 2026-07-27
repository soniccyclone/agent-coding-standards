---
type: lesson
title: "Name a thing by its content, and identity, integrity, and sharing stop being three separate problems"
figure: torvalds
works: [git-version-control-system]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Name a thing by its content, and identity, integrity, and sharing stop being three separate problems

**Lesson:** Most storage designs assign names independently of what is stored: a path, a revision number, an auto-incrementing key. Every such design then has to solve three further problems separately — how to know a stored item hasn't been corrupted or tampered with, how to notice that two items are the same so as not to store both, and how to talk about a whole structure by referring to one place in it. Git's founding move is to refuse the separation. The name of an object is a cryptographic digest of the object, so a name is simultaneously an address, a checksum, and a proof of equality. Verification becomes a local computation with no external metadata: recompute the digest, compare it to the name you looked it up by. Deduplication becomes automatic rather than a background job, because two identical subtrees cannot occupy two names. And because a composite object holds the names of its parts, naming the root fixes every byte reachable beneath it.

The consequence the original design writing draws out is the interesting one, and it is about where trust belongs. A content-addressed store can guarantee integrity — that what you got is what was named — but it can say nothing at all about whether the named thing is *good*. Those are different properties, and conflating them is how storage systems accumulate confused authority. Keeping them apart lets the trust question be answered outside the system entirely and very cheaply: because a single name transitively fixes an entire history, one person signing one short name endorses everything under it, and nobody has to sign anything else. A system that had merged integrity into trust would have needed a signature at every level and a story about which ones count.

There is a structural payoff too. When names are derived from content, structure becomes comparable without being unpacked: two composite objects with the same name are identical, so a difference between two large structures can be computed in time proportional to the size of the difference rather than the size of the structures. That property is not an optimization bolted on later; it is a direct consequence of the naming rule, and it is why an operation that ought to be expensive in a tree-shaped store turns out to be cheap.

A programmer who believes this asks, early in any design that stores things, whether the identifier can be a function of the content rather than an independent fact that must be maintained alongside it. When the answer is yes, they take it even at the cost of losing mutability, because mutability is the thing being traded away and immutable-plus-derivable-name buys back more than it costs. They also keep integrity and trust in separate boxes, and are suspicious of any component claiming to provide both.

**Source:** [Git Version Control System](../works/git-version-control-system.md) — the object-database description in the project's earliest design notes, which lays out the object kinds, the rule that a name is the digest of the stored bytes, the argument that structural sharing and cheap structural diffing follow from that rule, and the explicit boundary between the integrity the store provides and the trust it deliberately does not.
