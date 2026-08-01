---
type: lesson
title: "Rebuild the allocation map from the authority at startup"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, databases-and-data-management]
tags: [lesson]
---
# Rebuild the allocation map from the authority at startup

**Lesson:** A store that hands out units needs to know which units are taken. The reflexive design keeps that knowledge as a persistent structure updated alongside every allocation and release, which makes it a second authority on the same question — and two authorities on one fact means a consistency obligation that must hold across every failure, including the ones that interrupt an update between the two writes. The alternative costs a pass and removes the obligation entirely: treat the structure that *uses* the units as the only authority, and derive the occupancy map by traversing it at startup. Now there is no update path to get wrong, no ordering constraint between two writes, and no state that can be stale, because the map does not survive a restart and is never asked to.

The traversal has a second effect worth naming, because it is the reason the trade is usually favourable rather than merely tidy. Anything the authority does not reference is, by construction, absent from the reconstructed map and therefore free. So the boot-time pass is simultaneously the reclamation of everything abandoned by a crash, without any journal of what was in flight and without any special-case reasoning about partial operations. A unit half-allocated when the power failed is simply unreferenced, and unreferenced is the same as free. What would otherwise be a recovery protocol becomes a property of how the map is computed.

The cost is the one to check before adopting this: the pass is proportional to the size of the authority, not to the amount in use, and it is on the critical path of every start. That is acceptable when the authority is compact relative to the store it describes, and unacceptable when it is not — which makes this a decision about the ratio between the index and the data, and one worth stating as such rather than as a general preference. The transferable rule is the ranking, not the technique: prefer derived-at-start to persisted-and-maintained whenever the derivation is affordable, because you are trading a bounded, predictable cost for the elimination of an entire class of consistency bug.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.1's account of module FileDir's initialization, which constructs the sector reservation table by recording all files registered in the directory, requiring a traversal of the whole directory and a reading of all file headers, and which the text notes can be regarded as the garbage collection process of disk sectors; together with section 14.3's observation that this is precisely why an intact directory is a prerequisite for booting at all.
