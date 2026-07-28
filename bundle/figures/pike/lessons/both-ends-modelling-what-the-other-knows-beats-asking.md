---
type: lesson
title: "Both ends modelling what the other knows beats asking"
figure: pike
works: [the-text-editor-sam]
axes: [parallelizability, cognitive-load, verifiability]
subdomains: [distributed-systems-and-concurrency, programming-environments-and-object-systems]
tags: [lesson]
---
# Both ends modelling what the other knows beats asking

**Lesson:** When two components are separated by an expensive link and either one may change the shared subject, the tempting design is a conversation: one side asks what the other has, the other answers, they agree on what to send. The cheaper design is for each side to maintain, independently and in parallel, the same explicit record of which parts of the subject the far side currently holds. Neither party queries the other about coverage, because each already knows the answer. Every message can then be trimmed against that record before it is sent — a change landing in a region the far side does not have becomes a note about sizes rather than a payload, and a change inside a region it does have travels whole.

The reason this beats negotiation is that the record does two unrelated jobs at once for the price of one. It is a routing decision — what is worth transmitting — and it is a cache — what does not need re-fetching when an old region is revisited or an obscured view redrawn. A structure invented to control a protocol turns out to be exactly the structure that avoids repeated work, and because it is derived deterministically from the same change stream on both sides, it stays consistent without acknowledgements. That also means correctness lives in one small invariant rather than in the ordering of a dialogue, which is why this kind of subset is tractable to verify formally while the chattier parts of the same protocol are not.

The generalization is that laziness needs a place to record what has been skipped. Deferring work is only safe if something remembers the shape of the hole, and that record wants to be a first-class data structure both parties keep, not an implicit consequence of message history. A programmer who believes this stops designing request/response handshakes for state synchronization and starts asking what small structure, derivable identically at both ends from the events already flowing, would make the handshake unnecessary — then checks whether that same structure also answers the caching question, because it usually does.

**Source:** [The Text Editor sam](../works/the-text-editor-sam.md) — the Communications section, on the per-file structure that both halves of the editor maintain to track which portions of a file the display side holds, and the observation about its double role as a cache.
