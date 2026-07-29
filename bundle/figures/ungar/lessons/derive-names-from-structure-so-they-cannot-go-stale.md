---
type: lesson
title: "Names derived from structure cannot disagree with it; names kept beside it always eventually do"
figure: ungar
works: [organizing-programs-without-classes]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Names derived from structure cannot disagree with it; names kept beside it always eventually do

There are two ways to give a thing a name. You can attach a label to it and store the label somewhere — in the thing, in a registry, in the browser's metadata — or you can define the name as the route by which the thing is reached from a known starting point. The first is cheap to set up and independently mutable, which sounds like an advantage until you notice that "independently mutable" is the same property as "able to become wrong." A stored label and the actual structure are two representations of one fact, and two representations of one fact will drift. Rename the reference, restructure the hierarchy, and the stored label is now describing a world that no longer exists, with nothing in the system to notice.

A name computed from the structure has no such failure mode, because there is only one representation. If the route changes, the name changes with it — not because anything updates it, but because the name was never a separate artifact. This also collapses three things people usually build separately into one: the name is simultaneously an identifier a human reads, an expression a program can evaluate to obtain the object, and a path a browsing tool can walk. The categorization scheme gets the same treatment: organize by making the structure itself hierarchical, and the categories are browsable without any side data structure describing which thing belongs where.

The constraint you accept in exchange is real and worth stating: a structural name must be expressible in whatever language addresses the structure, so you give up arbitrary labels. That is the whole cost. In practice it bites far less than it sounds like it will, and the same discipline permits a thing to appear under several routes at once — one object referenced from multiple categories, no special mechanism required, because multiple references are just what references do.

A programmer who internalizes this becomes suspicious of every parallel index: the manifest listing what the directory contains, the metadata table describing which module owns which symbol, the config enumerating what the code already declares. Each is a promise to keep two things in sync forever, and that promise is always eventually broken by someone who edited one side. The question to ask is not "how do we keep the index correct" but "why is the index not simply a traversal of the thing it indexes."

**Source:** [Organizing Programs Without Classes](../works/organizing-programs-without-classes.md) — the naming and categorizing discussion, particularly its closing contrast between names derived from system structure and names recorded independently of it, including the observation that the latter can silently disagree with what programs actually reference.
