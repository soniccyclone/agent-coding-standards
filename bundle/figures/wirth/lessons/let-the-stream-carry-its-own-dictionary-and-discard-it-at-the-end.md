---
type: lesson
title: "Let the stream carry its own dictionary, and discard it when the pass ends"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, hardware-affinity, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Let the stream carry its own dictionary, and discard it when the pass ends

**Lesson:** Two demands pull against each other whenever a structure containing references to things outside itself has to be written down. Self-containment says every external reference must be recorded as something globally meaningful — a name — because a number that indexes into some table elsewhere is only interpretable by a reader who already has that table, which makes the artifact a fragment rather than a document. Economy says names are the worst possible encoding to repeat: long, variable-length, and expensive to compare on every occurrence. The habit of taking one horn or the other is what produces either bloated files or files that silently depend on a context nobody wrote down.

The resolution is to notice that the two demands apply to different populations. Self-containment is a property the artifact needs once per distinct external entity; economy is a property it needs once per occurrence. So emit the name at the first occurrence, paired with a small number, and use the number for every occurrence after. The artifact still names everything it depends on, so it can be read anywhere; and the repeated part is now a fixed-width integer. The numbering is local to this artifact and needs no global registry, because its meaning is established inside the artifact by the very pairs that introduce it — a number means whatever the pair that introduced it said, and nothing outside is consulted to find out.

What makes this cheap rather than merely clever is the lifetime of the table. It is built as a byproduct of the pass that consumes the artifact and it dies when the pass ends, because nothing afterwards has any use for it: once each reference has been turned into a live pointer, the correspondence between numbers and names has no remaining reader. So the table is a local variable of the read procedure, not a data structure of the system, and it never has to be maintained, invalidated, or reconciled with anything. The general shape is worth recognising: when you find yourself wanting a persistent registry to make an encoding compact, ask whether the registry is only ever needed for the duration of one traversal. If it is, put its contents in the stream and let it be reconstructed each time — you trade a small amount of redundancy in the artifact for the disappearance of a shared mutable structure, which is almost always the better side of that trade.

The same reasoning runs in reverse when writing. Maintain the correspondence for the duration of the write, emit a pair the first time an entity is met and an index thereafter, and the writer needs one forward pass too. Symmetric single-pass reading and writing is not an accident of this scheme; it is what the scheme is for.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.8.3's description of graphics-file conversion, where pointers to fonts, libraries and classes must become position-independent, replacing every pointer by an explicit name is rejected as uneconomical in both space and speed, index/name pairs are instead interspersed within the sequence of object descriptions, the dictionaries so established are local to the Load and Store procedures, and both traverse the file exactly once while leaving it self-contained in the sense that all external quantities are represented by their names.
