---
type: lesson
title: "Scoping a system means enumerating what cannot change, then isolating the obligation"
figure: cutler
works: [oral-history-of-david-cutler]
axes: [primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Scoping a system means enumerating what cannot change, then isolating the obligation

**Lesson:** "Build an operating system" is not a specification, and neither is any other
statement of purpose at that altitude. The specification is the pair of lists: what
capabilities the thing must have, and what constraints it is not allowed to violate. The
second list is the one that determines the design, and its most common entries are
inherited rather than chosen. An installed base of programs turns an existing interface
into something closer to a physical law than a preference: it can be extended, it can be
emulated, it cannot be repudiated. Starting over on a codebase does not release you from
it, which is why rewrites that budget for the new system and not for its inherited
obligations run long by factors rather than percentages.

The interesting design question is therefore not whether to honor compatibility but where
to put it. The failed answer smears it through the core, so that every subsystem carries
special cases for each supported legacy behavior, and the core's primitive count grows
with the number of obligations. The better answer treats each legacy interface as a
separate personality implemented above a single set of core mechanisms, so that supporting
another environment adds a module rather than complicating the kernel. This keeps the
irreducible mechanism set small and stable while the visible surface multiplies, which is
what makes the growth survivable: obligations accumulate linearly in modules instead of
combinatorially in special cases.

Doing this requires knowing the constraint at the beginning, because the mechanism set has
to be general enough to host personalities that were not the first one. A core designed
against exactly one interface cannot host a second without redesign, and by then the first
personality's assumptions are indistinguishable from the mechanisms themselves. This is
also why the difference between source compatibility and binary compatibility is worth
identifying explicitly and early. They are different obligations with very different
costs, and conflating them at scoping time guarantees discovering the difference at
implementation time.

A programmer who believes this begins a project by writing down what must keep working,
distinguishes the levels at which it must keep working, and then designs a core that
treats every one of those obligations as a client rather than as a feature.

**Source:** [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — the
insistence that a project starts with an explicit statement of capabilities and
constraints rather than an intent, illustrated by a real-time system constrained to
subset source compatibility with its predecessor, and by the later kernel whose subsystem
personalities carried several legacy environments above one mechanism set; the same
interview closes by arguing that even a from-scratch replacement for a large system cannot
discard its compatibility obligations.
