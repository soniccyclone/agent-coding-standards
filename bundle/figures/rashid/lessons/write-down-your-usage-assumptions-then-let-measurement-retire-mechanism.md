---
type: lesson
title: "Write your usage assumptions down as predictions, then let measurement of the running system retire mechanism"
figure: rashid
works: [from-rig-to-accent-to-mach]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Write your usage assumptions down as predictions, then let measurement of the running system retire mechanism

**Lesson:** Every implementation choice encodes a belief about how the thing will be used — how many of these will exist at once, how large they typically get, which case dominates, whether accesses are sequential or scattered. Those beliefs usually stay implicit, which has two bad consequences: they cannot be checked, and when they turn out wrong the structures built on them survive anyway, because nobody remembers which structure was justified by which belief. The discipline worth copying is to state the beliefs as explicit predictions before building, design deliberately for the cases they predict, and then instrument the system in real use so that each prediction is answered by a number rather than by opinion.

The predictions themselves are humble and specific, which is what makes them useful: how many references does a typical component hold, how deep does a queue actually get, what fraction of transfers are small and simple, how often does the copy-avoidance trick actually have to pay out by making a copy. Answers of this kind pay off twice. They validate a design choice on the axis you meant to buy — learning that most transferred data is read and never written is what turns a copy-on-write scheme from a plausible trick into a demonstrated one, because it says the expensive path is taken rarely enough not to matter. And they justify choosing the simpler structure: if collections are small and traversed in order, an elaborate multi-level indexing scheme is paying a permanent complexity cost for a lookup profile that never occurs, and the honest response is to replace it with a plain ordered list plus a memory of the last lookup.

The harder half of the discipline is deleting on the strength of the measurements. Mechanisms that were designed thoughtfully, implemented correctly, and then used for nothing — priority levels nobody differentiated, the ability to inspect a request before accepting it that was never used the way it was intended — are the most durable form of waste, because each one is defensible in isolation and none of them are anyone's problem. Observed non-use is evidence, and the successor system should be smaller in exactly those places. This is the one reliable force pushing back against a primitive set that only ever grows, and it requires having built the previous system in a way that let you see what it did.

A programmer who works like this ships instrumentation with the first version rather than after, keeps a written record of the assumptions each structure exists to serve, and treats "we have run this for years and nobody used that feature" as a mandate to remove it rather than a curiosity.

**Source:** [From RIG to Accent to Mach: The Evolution of a Network Operating System](../works/from-rig-to-accent-to-mach.md) — the implementation-issues sections, which list the usage assumptions carried over from the predecessor system, report measurements taken during real workloads against those assumptions, and then justify both the simplification of the address-map representation and the removal of message options found to be unused in the successor.
