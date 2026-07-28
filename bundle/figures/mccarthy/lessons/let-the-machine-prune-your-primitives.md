---
type: lesson
title: "When the machine forecloses an option, check whether what survived is cleaner before you mourn the loss"
figure: mccarthy
works: [history-of-lisp]
axes: [hardware-affinity, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# When the machine forecloses an option, check whether what survived is cleaner before you mourn the loss

**Lesson:** Physical constraint is usually treated as damage to be routed around, but it also functions as a pruning force on a design space, and the survivors of that pruning are sometimes better than what an unconstrained designer would have picked. Lisp's core operations are a case study. The target machine's word divided naturally into four fields, and the initial proposal accordingly offered a family of field-extraction functions plus a general bit-range extractor plus a four-argument construction routine. Two of those fields were narrow and awkwardly placed, and they were eventually given up. What remained was a word holding exactly two pointers, which collapsed construction to a two-argument function and extraction to two selectors, and — the part nobody was aiming at — left a single data type, an address, which meant the language needed no declarations at all.

The same pattern repeats on storage reclamation. Reference counting was the obvious incremental scheme, and it was rejected for a brutally physical reason: there were no spare bits in the word to keep a count in, and the bits that did remain were split across the word by an intervening field. That foreclosure forced the wholesale alternative, in which memory is simply abandoned until exhaustion and then swept, and the wholesale alternative turned out to have a property the incremental one lacked: it could be postponed. Correctness of the language did not depend on it, so it could be designed later while small examples ran on a free list that never filled. A constraint eliminated the option that would have entangled reclamation with every operation.

The influence then runs backwards, which is the part that completes the thought. Once the primitives existed, later machines were built with them in mind — half-word and stack instructions specified because a language wanted them — and those machines became the preferred hardware for the field. So the relationship between an abstraction and its substrate is not a one-way projection where the abstraction pays a translation tax. A primitive basis that maps cleanly onto a mechanism will pull future mechanisms toward itself.

A programmer who thinks this way reads a hardware or platform limit as information about which of their candidate designs was load-bearing, rather than as an obstacle to be abstracted away immediately. When a constraint forces a simplification, they audit the result honestly: sometimes it is a real loss to be paid back later, and sometimes several unrelated complications vanished at once, which is the signal that the constraint found a seam the design should have had anyway.

**Source:** [History of Lisp](../works/history-of-lisp.md) — the prehistory and implementation sections, which trace the reduction of the originally proposed word-field operations down to two selectors and a binary constructor, explain why reference counting was ruled out by the available bits, and later note that subsequent machine architectures were shaped to suit the language's requirements.
