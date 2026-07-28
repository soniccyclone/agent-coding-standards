---
type: lesson
title: "If you can name the dependency, you do not need the coordination"
figure: liskov
works: [providing-high-availability-using-lazy-replication]
axes: [parallelizability, verifiability, primitive-count]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# If you can name the dependency, you do not need the coordination

**Lesson:** Total ordering is expensive because it is a global property: no participant can know its position in the order without hearing from the others, so agreement has to happen before anything can proceed. But most applications do not need a global order — they need a much smaller thing, namely that a handful of specific earlier effects are visible before a given later one. That smaller requirement is local. And a local requirement can be carried as data rather than negotiated as a protocol.

The move is to give every effect an identifier, let a request carry the set of identifiers it depends on, and let whichever site receives the request decide entirely by itself whether it has enough to proceed. If it does, it acts immediately with no consultation whatsoever. If it does not, it waits — and the waiting is for information to arrive, not for a decision to be reached, which is a fundamentally cheaper kind of waiting because the information is arriving anyway in the background. The result is that the common case costs one exchange with one peer, and background chatter among peers replaces per-request agreement among peers.

Two properties make this practical rather than theoretical, and both are worth generalizing. The dependency set must have a compact representation, or the bookkeeping swamps the savings; a per-site counter vector serves, because merging is componentwise maximum and comparison is componentwise, so a set of arbitrarily many prior effects fits in a fixed-size value. And the identifiers must be issuable without coordination, which follows from letting each site number its own effects. Conservative overapproximation is acceptable throughout: a dependency set that names more than strictly required is harmless, because the extra entries are guaranteed to already be satisfied whenever the required ones are.

A programmer who believes this treats "we need ordering here" as a prompt to identify precisely which prior effects matter, and suspects that once named, they can travel with the request instead of being enforced by a protocol. The general reframing is worth keeping: coordination is what you resort to when you cannot express the constraint as data. Expressing it as data converts a synchronous negotiation into an asynchronous propagation, and asynchronous propagation is where availability comes from — a site cut off from its peers keeps serving everything whose stated dependencies it already holds.

**Source:** [Providing High Availability Using Lazy Replication](../works/providing-high-availability-using-lazy-replication.md) — the causal-operations section, where labels of update identifiers accompany every call and a replica decides locally whether an operation is ready, with multipart timestamps supplying compact, independently generated identifiers.
