---
type: lesson
title: "For every result, know the smallest set of assumptions it actually consumes"
figure: hilbert
works: [grundlagen-der-geometrie]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# For every result, know the smallest set of assumptions it actually consumes

**Lesson:** Most people are satisfied when a proof works. Hilbert organizes an entire book around a harder standard: for each theorem, name exactly which assumptions the derivation used, and no more. He proves the theory of proportion and then the theory of areas while deliberately withholding the continuity axiom, so the reader can see those theories do not depend on it. He notes that all facts about congruence and rigid motion follow without ever invoking the parallel postulate. He observes that Euclid took the congruence of all right angles as an axiom when it is derivable, and that Euclid's proof about triangles of equal content leaned on an unstated principle about magnitudes — in effect an extra geometrical axiom nobody had declared. The closing discussion makes the standard explicit: the aim throughout was to determine, for each question, which limited means suffice to answer it.

The payoff is not tidiness. An assumption you did not know you were using is an assumption you cannot remove, weaken, or replace, and it silently narrows where the result can be transported. Hilbert's accounting is what makes the interesting variations possible: because he knows the area theory never touched continuity, he can exhibit a non-Archimedean geometry in which two triangles share base and height, have equal content, and yet cannot be cut into congruent pieces — a distinction invisible to anyone who had continuity switched on by default. Unstated dependencies also destroy the interpretation of a result: Euclid's hidden magnitude principle means his theorem was about a different, stronger system than he thought.

For a programmer the corresponding discipline is minimal dependency accounting at every level. When a module's correctness argument silently relies on the database being on the same host, on messages arriving in order, or on a clock being monotonic, that assumption is part of the module whether or not anyone wrote it down, and the first deployment that breaks it breaks the module for reasons nobody can trace. The practice is to write the argument for each guarantee with an explicit list of what it consumes, and then to look at that list adversarially: which item can be dropped, which is doing more work than expected, which was inherited from a neighbor rather than genuinely needed. Doing this reliably tells you which parts of the system are portable and which are welded to their current environment.

**Source:** [Grundlagen der Geometrie](../works/grundlagen-der-geometrie.md) — the layered development in which proportion and area are established while the continuity axiom is withheld, the remarks correcting Euclid's unacknowledged assumptions, and the concluding discussion of purity of method.
