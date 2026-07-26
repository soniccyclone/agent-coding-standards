---
type: lesson
title: "Give each component its own resumption point, and the state machine you would have hand-encoded disappears"
figure: dahl
works: [simula-an-algol-based-simulation-language, simula-67-common-base-language]
axes: [cognitive-load, expressiveness, parallelizability]
subdomains: [programming-environments-and-object-systems, distributed-systems-and-concurrency]
tags: [lesson]
---
# Give each component its own resumption point, and the state machine you would have hand-encoded disappears

**Lesson:** Anything worth modelling as a system has parts whose lives are long and interrupted. An entity does a little, waits on something outside itself, does a little more, and the intervals between its own actions are filled with other entities acting. There are two ways to write such a part. You can shred its behavior into fragments that the scheduler calls, and carry a variable saying which fragment comes next — reconstructing, by hand, the one piece of bookkeeping every language already does perfectly. Or you can write the part's behavior as one uninterrupted sequential text and let it own a private marker into that text, so that when control comes back it resumes exactly where it stopped. The second costs one new idea and eliminates a whole category of hand-written state.

The reason this is more than a convenience is that the marker is the state. A hand-rolled step counter is a redundant, drift-prone encoding of a position that the text itself already expresses; every branch a programmer writes on that counter is a branch he wrote because he threw the position away and then needed it back. Once each component carries its own place in its own program, actions separated by arbitrary stretches of other components' activity read as a single coherent story, in the order the modeller thinks about them. The gain compounds where it matters most: the parts of a program hardest to get right are exactly the long-lived ones with interleaved lifetimes, and this is precisely where the technique removes work rather than adding it.

Notice that this is a decomposition claim, not a performance claim. Only one component runs at a time; nothing here buys parallel hardware anything directly. What it buys is that the components are described independently, with no shared control structure between them, and the description of each one no longer encodes assumptions about who else exists or in what order the whole ran. That independence is what later makes genuine parallelism a scheduling question rather than a rewrite. A programmer who has internalized this stops asking "what event will call me next" and starts asking "what is this thing's own story," and treats every explicit state variable that merely tracks progress through a sequence as evidence that the wrong tool is in hand.

**Source:** [SIMULA - an ALGOL-Based Simulation Language](../works/simula-an-algol-based-simulation-language.md) — the sequence-control discussion, which introduces per-process reactivation points, argues they let widely separated actions be strung into one logical sequence, and observes that a component can then be read as having its own local control indistinguishable from the main one while it is running. Also [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the sequencing chapter's local-sequence-control account and the two primitive transfers that suspend a component in place and resume another where it left off.
