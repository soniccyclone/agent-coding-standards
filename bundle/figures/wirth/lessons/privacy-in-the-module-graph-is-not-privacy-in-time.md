---
type: lesson
title: "Privacy in the module graph is not privacy in time"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Privacy in the module graph is not privacy in time

**Lesson:** Encapsulation is usually reasoned about spatially: a representation is private if no other component names it, and a private representation can therefore be changed at will. That inference holds only for representations that live and die inside one run of the system. The moment a representation is written somewhere durable, it acquires a second set of clients that the module graph cannot show you — the same program next year, a different implementation of the same abstraction, an archive restored after the code that wrote it has been replaced twice. Those clients depend on the layout exactly as strongly as a caller depends on a signature, and they cannot be found by searching for imports. So a component can simultaneously own a format outright and be unable to change it, and that is not a contradiction to be resolved but a fact to be planned around.

The planning takes a specific form: a format in this position needs a written specification even though, by the encapsulation argument, no one is entitled to read it. The specification is not there to let other modules parse the data — that would defeat the abstraction. It is there because the obligation being documented is the obligation not to change, and an obligation nobody has written down cannot be honoured by a maintainer who was not present when it was incurred. Writing it as a grammar rather than as prose is worth the extra discipline, because a grammar makes the extension points explicit: you can see which fields are fixed-width, where a count governs a repetition, and therefore exactly which changes are additive and which break every existing file.

The design consequence runs backwards into the internal representation. Since the durable form is the part you cannot revise, it deserves more care than the in-memory form it serializes, and the two should be allowed to diverge rather than being kept in step for convenience. Notice also the reason a version or kind discriminator belongs in the header of anything durable: it is the one field that lets a future reader distinguish "I do not understand this" from "I misread this", and it costs a byte at a moment when spending a byte is still possible. The general rule for any layered design is to spend disproportionate care at whichever boundary will be hardest to revise later, and durability, not visibility, is what makes a boundary hard to revise.

**Source:** [Project Oberon](../works/project-oberon.md) — section 5.4's introduction to the font file format, which states plainly that the format is completely private to the managing module while at the same time having to be ultimately stable because it is used for long-term backup and for wide-ranging data exchange, and which therefore gives the format as an explicit grammar with a leading file-identification byte and an abstraction-level discriminator ahead of the metric and raster data; together with the analogous remark in section 5.2 that the text section format obeys a set of syntactic productions given in the same notation, and that plain character files are accepted and mapped onto the general representation.
