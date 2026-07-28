---
type: lesson
title: "Enumerate everything the meaning of code depends on, then split it by when it becomes knowable"
figure: chamberlin
works: [xquery-1.0-an-xml-query-language]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# Enumerate everything the meaning of code depends on, then split it by when it becomes knowable

Most languages leave their environment implicit: the meaning of a fragment quietly depends on which names are visible, which conversions are in force, what the current default for some unstated policy happens to be, where relative references resolve from. Treating that environment as an enumerable object — a named list of components, each with a stated type and stated rules for scope and initialization — is a large amount of unglamorous work, and it pays for itself twice. It makes the language checkable, because you can now say exactly which component a given rule consults and therefore what it means for that component to be unset. And it makes the language extensible, because adding a feature means adding a component and its initialization rule rather than adding an unwritten assumption.

The second half of the discipline is the sharper one: partition that environment by the time at which each part becomes available. One set of components is knowable before any data is seen; the rest only exist once evaluation begins. Once the split exists, the phases of processing fall out of it — an analysis phase that may consult only the first set, an evaluation phase that may consult both — and so does a precise answer to which category of mistake is catchable when. A wrong name is catchable early because names live in the early environment; a value that fails a constraint is not, because values live in the late one. The classification of failures into ones that must be caught before running, ones that must be caught while running, and ones that may legitimately surface in either phase depending on how much type information the implementation chose to track, is a consequence of the partition rather than an independent decision.

This also gives a principled place to put optional strength. An implementation that tracks more information in the early environment can move failures earlier, at the cost of rejecting some programs that would have run fine on the inputs actually supplied — which is the real trade of static typing, stated as a trade rather than as a virtue. Making that a declared, optional capability, with the same language accepted either way, is more honest than pretending one setting is universally correct.

A programmer who internalizes this stops writing functions whose behavior depends on ambient state nobody has listed, and starts writing down the list. It changes what you ask of a design under review: not "does this work" but "what does this consult, and at what moment does that thing come to exist." Configuration bugs, resolution-order bugs, and the whole family of works-on-my-machine failures are mostly cases of an environment component that exists but was never named.

**Source:** [XQuery 1.0: An XML Query Language](../works/xquery-1.0-an-xml-query-language.md) — the expression-context sections that itemize the static and dynamic environments component by component, and the processing-model section that derives the analysis and evaluation phases and the taxonomy of static, dynamic, and type errors from that division.
