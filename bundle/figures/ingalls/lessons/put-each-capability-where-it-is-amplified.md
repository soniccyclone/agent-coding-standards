---
type: lesson
title: "Put each capability at the one place where the most things inherit it, and let protocol rather than type set the reach"
figure: ingalls
works: [design-principles-behind-smalltalk]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Put each capability at the one place where the most things inherit it, and let protocol rather than type set the reach

**Lesson:** Every independent capability in a system should exist in exactly one place, and the interesting part of that rule is not the prohibition on duplication but the question it forces: which place? The answer is the most general level at which the capability is still true, because from there it propagates to everything more specific for free. Written at the right level, one definition upgrades an entire family at once; written a level too low, it has to be repeated, and each repetition is an obligation to keep several copies in agreement forever. The reason duplication is corrosive is not the wasted characters but the synchronization problem it creates — divergence between copies is silent, and the effort of preventing it never ends.

The reach of a well-placed definition is set by what it demands of its operands, not by what it was written for. A procedure that arranges things in order works on words as readily as on numbers, provided both answer the same comparison requests, and it does so without anyone having anticipated the second case. That is the mechanism worth designing toward: keep the demands a definition makes as small and as widely honored as possible, and its applicability expands on its own as new things enter the system honoring the same repertoire. Where a definition instead names concrete kinds, its reach is frozen at the moment of writing.

Two habits follow. When about to write something, look upward for the level where it is already true rather than writing it where you happen to need it — the extra minute of placement buys every future case. And when the same idea appears twice, treat that as a signal that the shared level has not been identified yet, not as a maintenance chore to be handled by keeping both copies updated. A system that is well factored in this sense hands both its users and its implementers disproportionate returns on small pieces of work, which is the practical definition of leverage.

**Source:** [Design Principles Behind Smalltalk](../works/design-principles-behind-smalltalk.md) — the Factoring principle with its reasons about location, synchronization and consistency, its identification of a factoring failure as a modularity failure, and the Leverage principle illustrated by defining a sort at a general collection level and by the same method handling text and numbers because both honor comparison protocol.
