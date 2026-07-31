---
type: lesson
title: "Accept the general form, then classify against a closed set"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, hardware-affinity, verifiability]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# Accept the general form, then classify against a closed set

**Lesson:** A recognizer often has to distinguish a fixed handful of reserved cases from an open-ended general case, where the reserved ones are, as text, indistinguishable from the general one until complete. The obvious approach is to teach the recognizer each reserved case directly, so that it can tell as early as possible which it is looking at. This is the expensive path: every reserved case adds branching that has to be interleaved with the general rule, the recognizer's size grows with the number of reserved cases, and adding one means editing control flow. The cheap path is to recognize the general form and only then ask, once, whether what you collected happens to be one of the reserved ones. The recognizer stays the size it would have been with no reserved cases at all, and the entire reserved set becomes a table — data that can be extended, printed, and checked without touching the recognizer.

The lookup that follows is where the reserved set's most useful property pays. That set is closed and known before anything runs, which means the structure holding it need not be a general-purpose one tuned for an unknown population. You can choose the arrangement against the actual keys, verify offline how many comparisons the worst key needs, and then state that number as a guarantee rather than an average — a small fixed bound on every lookup, including the far more common case where the answer is "none of them," which is the one that must not be slow. Building the arrangement once at start-up rather than on each use is what makes this affordable, and it is affordable precisely because the set does not change.

The general principle is worth separating from the parsing setting. Whenever a small, fixed set of special cases lives inside a larger open category, ask whether the specialness has to be detected during recognition or can be decided after it. If after, the recognizer and the special-case list become independent things that change independently, and the cost of the special cases collapses from "one branch each, forever" to "one bounded lookup, once."

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.5's account of the scanner, which explains that a sequence of letters and digits may denote either an identifier or a key word, that the determination is made by searching a table of all key words for each would-be identifier, that the table is organized as a hash table for efficiency with the hash being the sum of the characters' ordinal values plus their count modulo the table size, that at most two comparisons suffice to detect a key word, and that the table is initialized when the compiler is loaded.
