---
type: lesson
title: "When the machine's atomic unit is narrower than your invariant, restructure the data until the invariant fits behind one reference"
figure: herlihy
works: [software-transactional-memory-for-dynamic-sized-data-structures]
axes: [hardware-affinity, verifiability, primitive-count]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---

# When the machine's atomic unit is narrower than your invariant, restructure the data until the invariant fits behind one reference

**Lesson:** A recurring shape of problem: several fields must change together or not at all, and the machine offers atomicity over exactly one word. The instinct is to reach for a protocol that makes several single-word updates look like one — a sequence of steps with a recovery procedure for every intermediate state, which is where the difficulty and most of the bugs live. There is a structurally different answer. Stop trying to update the fields and instead make the group of fields a single immutable record reachable through one pointer; then an update is the construction of a fresh record followed by one conditional pointer swap. The multi-field atomicity you needed becomes the single-word atomicity the machine actually has, not by emulation but because the invariant has been relocated into a place where a one-word change can express it.

The consequences run further than the update itself. Anyone who follows the pointer sees a self-consistent group by construction, so readers need no protocol at all — there is no intermediate state to be caught in, which is why the participant that owns the current record can go on to work against it with no further synchronization whatsoever. The cost accounting also becomes clean: a small constant number of strong synchronization operations per object touched, plus the copying, and nothing else. And a subtlety worth carrying: this pattern depends on the swapped-in identity being genuinely fresh, because a conditional swap can only tell you the pointer's value is unchanged, not that nobody moved it and moved it back. Reclaiming and reusing record identities silently breaks it. A managed environment hides that hazard by not recycling a record while anyone can still reach it, which is convenience rather than absolution — the reasoning has to be done explicitly wherever memory is reused.

The transferable question is one to ask early rather than late: what is the smallest set of facts that must change simultaneously, and can I arrange for that set to live behind a single mutable reference to immutable content? Where you can, a whole class of intermediate-state reasoning evaporates and the mapping down to the hardware becomes a single instruction. Where you cannot — because the group is too large to copy — you are back to protocols, and it is worth knowing that this is the reason, so that the choice of data representation is recognized as the thing that decided how hard the concurrency would be.

**Source:** [Software Transactional Memory for Dynamic-Sized Data Structures](../works/software-transactional-memory-for-dynamic-sized-data-structures.md) — the implementation section's introduction of an indirection record holding the three logically-atomic fields, updated by a single conditional swap of the container's one reference, plus the accompanying cost analysis and the footnote on why recycled identities would defeat the conditional swap.
