---
type: lesson
title: "Re-read a specialized notion as a pair, and discover the general case is already built"
figure: wirth
works: [project-oberon]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# Re-read a specialized notion as a pair, and discover the general case is already built

**Lesson:** When a design meets demands it was not built for, the reflex is to add a second mechanism beside the first. Before doing that, try re-describing the mechanism you already have in more neutral terms and see how far the neutral description reaches. A component whose domain-specific name suggests a narrow purpose frequently turns out, structurally, to be nothing more than a collection of things plus a way of selecting one — and once it is described that way, the constraint that made it narrow is visible as a convention about what those things happen to be, not as a property of the machinery. The neutral re-reading is free: no code changes, and every existing artifact is already an instance.

The move worth learning is the specific one of recognizing a *pair* where you had been seeing a primitive. If each element of a sequence is really an identifier of a collection together with an index into it, then the sequence is not a sequence of the things you named it after; it is a sequence of references to arbitrary members of arbitrary collections, which is as general as a sequence of arbitrary objects. Nothing had to be added to reach that generality — it was reached by noticing what the representation was, rather than what the original problem had called it. This is the difference between a generalization that costs and one that pays: the first widens a mechanism to admit new cases, and every existing user pays for the width; the second re-reads an existing mechanism and finds the new cases were already admissible.

Two guardrails keep this honest. The re-reading only counts if the specialized behaviour survives as a *convention* rather than as an enforced rule — if the narrow case was narrow because something in the machinery checks it, the generality is imaginary and removing the check is a real change with real consequences. And a general description does not by itself deliver the general behaviour: the clients written against the old reading may still assume the old population, so the honest claim is "the representation is already general, and here is which clients would have to be revisited to exploit it", not "the system is general." Stating the reach precisely is what makes the observation usable by someone else rather than a pleasing remark.

**Source:** [Project Oberon](../works/project-oberon.md) — section 5.4's re-interpretation of a font, prompted by the observation that documents want emphasis, differing sizes, special symbols and embedded formulae, from a style in which a character set is drawn to an indexed library of graphical objects that are mostly but not necessarily glyphs; the consequent reading of text as a sequence of library-and-index pairs, with the character code serving as the index in the ordinary case; and the explicit note that this view is in principle equivalent to defining text as a sequence of arbitrary objects.
