---
type: lesson
title: "Fix what is not allowed to move, then build motion out of ordinary operations instead of a migration feature"
figure: cardelli
works: [a-language-with-distributed-scope]
axes: [expressiveness, primitive-count, parallelizability]
subdomains: [distributed-systems-and-concurrency, programming-environments-and-object-systems]
tags: [lesson]
---
# Fix what is not allowed to move, then build motion out of ordinary operations instead of a migration feature

**Lesson:** Once things can be in more than one place, the temptation is to make everything mobile and then fight the consequences: two copies of state that both think they are authoritative, a reconciliation story, and a migration subsystem with its own failure modes. A better sequence starts from a prohibition. Decide which entity is not allowed to move, on the grounds that duplicating it would duplicate authority, and let everything else move freely. Here state-bearing objects are pinned to the site that created them while references to them travel without restriction, so the identity question never arises: there is one place where the state lives and any number of places that can name it.

The prohibition then has to be paid for, and the interesting part is that it can be paid in the language rather than in the runtime. Relocation is expressible as a copy at the destination followed by turning the original into a forwarder, both of which are operations that exist for their own reasons, so migration is a short program rather than a primitive. That has three consequences worth generalizing. The atomicity requirement, that no operation observe the half-migrated state, is met by the mutual exclusion facility that was already there, rather than by a bespoke protocol. The forwarding step is the local-surrogate idea from distributed systems lifted into the language, so redirection becomes something programs can decide about instead of something the transport layer does invisibly. And because relocation is a program, variants are easy: leave a forwarding chain, or additionally re-register under the old public name so that new clients skip the indirection entirely.

The generalizable move is to separate the immobility decision, which is about where authority lives, from the mobility mechanism, which is about how references and copies are managed, and then to check whether the mechanism can be assembled from operations that already earn their place. A migration feature invented as a unit tends to bundle both decisions and to hide the authority question inside the implementation, which is where duplicated-state bugs live.

**Source:** [A Language with Distributed Scope](../works/a-language-with-distributed-scope.md) — the language overview's decision that objects are site-local and never moved automatically while references travel freely, and the object migration example, which codes relocation from cloning and redirection, relies on the existing serialization facility for atomicity, and shows the name-server variant that avoids indirection chains.
