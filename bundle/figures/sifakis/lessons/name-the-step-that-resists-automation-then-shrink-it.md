---
type: lesson
title: "Name the one step that cannot be automated, then shrink it and mechanize everything around it"
figure: sifakis
works: [property-preserving-abstractions-1995]
axes: [cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Name the one step that cannot be automated, then shrink it and mechanize everything around it

**Lesson:** The honest conclusion of this paper is an admission: choosing how to collapse the concrete system onto a coarse one requires understanding the program deeply and cannot be automated. That sentence would be a discouraging place for a method to end, and it is not where they end. Having isolated the judgment call, they treat it as a fixed cost to be minimized and surround it with machinery. Once the collapsing relation is supplied, computing the coarse system from the program text, checking the specification against it, and checking that the relation respects the specification's atomic facts are all mechanical, and were all implemented. The human contributes one artifact; the tool does the rest and independently validates the one thing the human provided.

Two further moves shrink the human's contribution rather than merely fencing it off. First, the specification is mined for constraints on the answer: the atomic predicates that appear in the property, together with the non-contradiction requirement those predicates must satisfy, jointly pin down the minimum the coarse domain has to be able to distinguish. The user is no longer staring at a blank page — a lower bound on the abstraction is read mechanically off the question being asked, and in their readers-writers example that bound essentially *is* the answer, two booleans recording whether the active-reader and active-writer counts are zero. Second, the compositionality theorems let the judgment be exercised per component instead of on the assembled system, and they point out this is not only cheaper to compute but easier for the person, because a small part is something a human can actually hold in mind.

The pattern to carry away is the correct response to "this part needs human insight." Not resignation, and not a doomed attempt to automate the insight. Instead: locate the irreducible decision precisely, make it as small and as local as possible, derive whatever constraints on it the problem statement already implies, mechanize everything downstream of it, and — most importantly — make the tool check the human's input rather than trust it. A method with one narrow, validated, well-supported manual step is usable by people who are not its authors. A method with a diffuse manual step, or one whose manual input is taken on faith, is a research prototype forever, no matter how strong its theorems.

**Source:** [Property Preserving Abstractions for the Verification of Concurrent Systems](../works/property-preserving-abstractions-1995.md) — the conclusion's statement that choosing abstraction relations requires deep knowledge of the concrete program and cannot be automated, followed by its observations that the predicates in the formula plus the preservation requirements for them help find the minimal necessary abstract domain, that the compositionality results make component abstractions easier for the user to find than one for the compound system, and that with the relation given, abstraction, model checking, and predicate-preservation checking are all mechanized in their symbolic tool.
