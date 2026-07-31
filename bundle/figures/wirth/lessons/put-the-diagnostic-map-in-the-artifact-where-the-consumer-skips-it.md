---
type: lesson
title: "Put the diagnostic map inside the artifact, in a region the consumer skips"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Put the diagnostic map inside the artifact, in a region the consumer skips

**Lesson:** When something fails at run time, what is available is machine-level: positions, offsets, numeric values. What a person needs is the authored vocabulary those correspond to. The mapping between them exists exactly once, inside the producer, at the moment of production, and is unrecoverable afterwards — so the only question is where to put it. Keeping it in a separate companion file means it can go missing, can be found in the wrong version, and requires a convention for matching it to the thing it describes. Loading it along with the artifact means every run pays memory and load time for information almost every run never uses. Both of these are avoidable by a third arrangement: put it in the same artifact, past the point where the normal consumer stops reading.

The two properties this buys are worth stating separately because they are usually traded against each other. It cannot drift, because a single object cannot be a version behind itself; matching artifact to map is not a problem that exists. And it costs the running system nothing, because the consumer is specified to ignore the region — it is not parsed, not loaded, not resident. What it costs is storage in the artifact, which is the cheapest of the three currencies in play, and one convention: the consumer must be told where its own portion ends rather than assuming it runs to the end of the object.

The content of the map is a policy decision, not a completeness exercise, and it is worth making deliberately. Include the entries that can be presented usefully with the machinery available at failure time, and leave out the ones whose rendering would require a general facility you do not want in the failure path — a post-mortem report is produced by a system that has just gone wrong, and it should depend on as little as possible. Choosing to cover the simple cases well rather than every case badly is what keeps the diagnostic path small enough to be trusted.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.8's description of object file generation, which states that after the actual object file data a part called the reference block is appended, that it is ignored by the loader but is used when traps occur during execution to generate a post-mortem dump in symbolic form, that it contains the names of variables and procedures together with their addresses obtained by a full traversal of the symbol table, and that only variables of basic unstructured type and short character arrays are included.
