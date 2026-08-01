---
type: lesson
title: "Give persistent data its own namespace, and let anonymity be the privacy mechanism"
figure: wirth
works: [project-oberon]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Give persistent data its own namespace, and let anonymity be the privacy mechanism

**Lesson:** Systems arrive with one naming hierarchy already built — the one over code, where units are named, import each other, and form a dependency order. When persistent data appears, the reflex is to hang it off that hierarchy: this data belongs to that unit, so it is reached through it. The reflex is wrong, and its wrongness follows from a simple observation about lifetimes. Code units are loaded, unloaded and replaced on one schedule; persistent objects outlive all of that, are shared by parties that import nothing in common, and are grouped by what a user considers one thing rather than by what one unit manipulates. Two populations with different lifetimes, different grouping criteria and different sharing patterns want two hierarchies, related to each other but neither subordinate to the other. Building only one and stretching it to cover both means every question about the second is answered by an accident of the first.

The second hierarchy needs a scope rule, and there is a lighter one available than an access-control field on every object. Make scope a property of the collection an object sits in rather than of the object: a collection that has a name is reachable from anywhere, and every member of it acquires a global designation for free by qualification with that name; a collection that has no name is reachable only through whatever holds it, and its members therefore cannot be designated from outside at all. Privacy is then not enforced, it is a consequence of there being nothing to say. That is a strictly stronger guarantee than a checked permission, because a check can be circumvented or forgotten while an unutterable name has no failure mode, and it costs nothing to implement — you get it by omitting the naming step rather than by adding a mechanism.

The arrangement has a further property worth extracting. Because scope follows placement, changing an object's visibility is a move between collections rather than an edit to the object, so visibility is expressible as an operation on the structure and is visible by inspecting the structure. Contrast a per-object flag, where the set of publicly reachable things exists nowhere in particular and can only be computed by examining everything. Any policy you can encode as membership becomes checkable by looking at one place; any policy you encode as an attribute becomes a survey.

The general habit: when a system grows a second population of long-lived named things, ask whether it deserves its own naming hierarchy rather than a corner of the existing one, and decide by comparing lifetimes and grouping criteria rather than by convenience. And when the new hierarchy needs a public/private distinction, try to realize it as the presence or absence of a name on a container before reaching for a per-item permission.

**Source:** [Project Oberon](../works/project-oberon.md) — appendix A.1's description of object libraries as indexed collections of persistent object instances, each either public or private to some host; public libraries being named and accessible from any authority so that a member object can be referenced invariantly by its qualified name; private libraries being anonymous and encapsulated in some higher authority, typically a document; and the statement that object libraries may refer to one another and in their entirety build a hierarchy which is in a sense dual to the system's module hierarchy.
